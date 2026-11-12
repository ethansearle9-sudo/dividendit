"""Real publish and update dates per page, taken from git history.

HubSpot's AEO checklist wants a visible publish date and a visible last-updated
date on every page. Those have to be true, so they come from the repository
rather than being made up: first commit that introduced the file is the publish
date, most recent commit that touched it is the update date.

A page that has never been committed (new this build) gets today's date for
both, which is also true.
"""
import subprocess, datetime, functools, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


@functools.lru_cache(maxsize=1)
def _git_dates():
    """{slug: (published_iso, modified_iso)} for every tracked html file."""
    out = {}
    try:
        files = subprocess.run(
            ['git', 'ls-files', '*.html'], cwd=ROOT,
            capture_output=True, text=True, timeout=30).stdout.split()
    except Exception:
        return out
    for f in files:
        try:
            log = subprocess.run(
                ['git', 'log', '--follow', '--format=%aI', '--', f],
                cwd=ROOT, capture_output=True, text=True, timeout=30).stdout.split()
        except Exception:
            continue
        if not log:
            continue
        # git log is newest-first
        out[pathlib.Path(f).stem] = (log[-1][:10], log[0][:10])
    return out


def for_slug(slug):
    """(published, modified) as YYYY-MM-DD. Today/today for an uncommitted page."""
    today = datetime.date.today().isoformat()
    return _git_dates().get(slug, (today, today))


def pretty(iso):
    """1 March 2026 — a date a reader can actually read."""
    d = datetime.date.fromisoformat(iso)
    return f'{d.day} {d.strftime("%B %Y")}'
