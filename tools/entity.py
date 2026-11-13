"""Entity data for Dividend IT: NAP and verified profiles.

Single source of truth. Everything here flows into the Organization and
ProfessionalService schema on every page, so adding a directory profile or a
local phone number is a one-line change here and nothing else.

NOTHING IS INVENTED. Empty values are omitted from the markup rather than
guessed, because a wrong phone number or address on a listing is worse than a
missing one: directory citations have to match exactly or they count against
you.

To activate a location, fill in `phone` and `address` for it below.
To add a profile, append its URL to PROFILES once the listing is live.
"""

LEGAL_NAME = 'Dividend IT'
SITE = 'https://dividendit.com'

# Verified profiles for sameAs. Only add a URL once the profile actually
# exists and is public — sameAs pointing at a 404 is a negative signal.
PROFILES = [
    # 'https://www.linkedin.com/company/dividend-it',
    # 'https://www.goldenpages.ie/...',
    # 'https://clutch.co/profile/dividend-it',
    # 'https://www.cloudtango.net/providers/...',
]

# Per-location NAP. country is the ISO code. Leave phone/address empty until
# the real values exist; a location with neither emits no LocalBusiness node.
LOCATIONS = {
    'it-support-dublin':        {'city': 'Dublin',     'region': 'Co. Dublin',    'country': 'IE', 'phone': '', 'street': '', 'postcode': ''},
    'it-support-limerick':      {'city': 'Limerick',   'region': 'Co. Limerick',  'country': 'IE', 'phone': '', 'street': '', 'postcode': ''},
    'it-support-galway':        {'city': 'Galway',     'region': 'Co. Galway',    'country': 'IE', 'phone': '', 'street': '', 'postcode': ''},
    'it-support-ennis-shannon': {'city': 'Ennis',      'region': 'Co. Clare',     'country': 'IE', 'phone': '', 'street': '', 'postcode': ''},
    'it-support-winchester':    {'city': 'Winchester', 'region': 'Hampshire',     'country': 'GB', 'phone': '', 'street': '', 'postcode': ''},
    'it-support-johannesburg':  {'city': 'Johannesburg', 'region': 'Gauteng',     'country': 'ZA', 'phone': '', 'street': '', 'postcode': ''},
}

# The registered/primary contact point, used on the Organization node.
PRIMARY = {'phone': '', 'email': 'ethan@dividendit.com',
           'street': '', 'city': '', 'region': '', 'postcode': '', 'country': 'IE'}


def _address(d):
    """PostalAddress with empty fields dropped. Returns None if nothing real."""
    parts = {
        'streetAddress': d.get('street', ''),
        'addressLocality': d.get('city', ''),
        'addressRegion': d.get('region', ''),
        'postalCode': d.get('postcode', ''),
        'addressCountry': d.get('country', ''),
    }
    parts = {k: v for k, v in parts.items() if v}
    # A country alone is not an address worth marking up.
    if not parts or set(parts) <= {'addressCountry'}:
        return None
    return dict({'@type': 'PostalAddress'}, **parts)


def organization():
    """The @id-able Organization node referenced by every other schema block."""
    node = {
        '@type': ['Organization', 'ProfessionalService'],
        '@id': SITE + '/#org',
        'name': LEGAL_NAME,
        'url': SITE + '/',
    }
    if PROFILES:
        node['sameAs'] = list(PROFILES)
    if PRIMARY.get('phone'):
        node['telephone'] = PRIMARY['phone']
    if PRIMARY.get('email'):
        node['email'] = PRIMARY['email']
    a = _address(PRIMARY)
    if a:
        node['address'] = a
    return node


def local_business(slug):
    """A LocalBusiness node for a location page, or None if we have no NAP.

    Google needs name + address + phone to treat a page as a local entity.
    Without them this returns None and the page keeps its Service markup only.
    """
    loc = LOCATIONS.get(slug)
    if not loc:
        return None
    # City and county alone are not NAP. Google treats a local entity as real
    # when it has a contactable address or number; a node carrying neither is
    # an incomplete citation, which is worse than no node at all.
    if not loc.get('phone') and not loc.get('street'):
        return None
    a = _address(loc)
    node = {
        '@context': 'https://schema.org',
        '@type': 'ProfessionalService',
        '@id': f'{SITE}/{slug}#local',
        'name': f'{LEGAL_NAME} — {loc["city"]}',
        'url': f'{SITE}/{slug}',
        'parentOrganization': {'@id': SITE + '/#org'},
        'areaServed': [{'@type': 'City', 'name': loc['city']}],
    }
    if a:
        node['address'] = a
    if loc.get('phone'):
        node['telephone'] = loc['phone']
    if PROFILES:
        node['sameAs'] = list(PROFILES)
    return node


def status():
    """Human-readable readiness, for the build log."""
    ready = [s for s in LOCATIONS if local_business(s)]
    return (f'entity: {len(PROFILES)} profiles, '
            f'{len(ready)}/{len(LOCATIONS)} locations with NAP'
            + (f' ({", ".join(ready)})' if ready else ''))


# The named author behind the site's content. HubSpot's AEO checklist wants a
# visible byline with visible credentials: AI systems weight identifiable,
# credentialled sources. Everything here is factual.
AUTHOR = {
    'name': 'Ethan Searle',
    'role': 'Founder, Dividend IT',
    # Currency confirmed by Ethan: the exit figure was R80 million, roughly
    # &euro;4 million. The site states it in euro, so the bio matches.
    'bio': ('Founder of Dividend IT. Previously part-owner of LanDynamix, a South African '
            'managed service provider he helped grow from €1 million to €4 million '
            'in revenue before exiting.'),
}


def author_node():
    node = {
        '@type': 'Person',
        '@id': SITE + '/#author',
        'name': AUTHOR['name'],
        'jobTitle': AUTHOR['role'],
        'description': AUTHOR['bio'],
        'worksFor': {'@id': SITE + '/#org'},
    }
    if PROFILES:
        node['sameAs'] = list(PROFILES)
    return node
