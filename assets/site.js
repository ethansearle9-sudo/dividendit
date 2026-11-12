/* Dividend IT site shell: nav behaviour. Shared by every page. */
(function(){
  /* Clean up nav-closing on page restore (back/forward cache) */
  window.addEventListener('pageshow', function(){
    document.querySelectorAll('.nav-dd.nav-closing').forEach(function(el){
      el.classList.remove('nav-closing');
    });
  });
  /* Close mega menu when a link inside it is clicked */
  document.querySelectorAll('.nav-mega-menu a').forEach(function(a){
    a.addEventListener('click', function(){
      var dd = this.closest('.nav-dd');
      if(dd){
        dd.classList.add('nav-closing');
        setTimeout(function(){ dd.classList.remove('nav-closing'); }, 800);
      }
    });
  });
  /* Hamburger toggle */
  var toggle = document.querySelector('.nav-toggle');
  var links  = document.querySelector('.nav-links');
  if(toggle) toggle.addEventListener('click', function(){
    toggle.classList.toggle('open');
    links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', links.classList.contains('open'));
  });
})();
/* dd-convtrack-v1 — conversion tracking, delegated.
   Every Calendly and mailto link on the site fires an event, including links
   added later. Links that already carry an inline trackEvent handler keep it
   (their hand-written `location` label is better) and are skipped here, so
   nothing is counted twice. */
(function(){
  function clean(t){ return (t || '').replace(/\s+/g, ' ').trim().slice(0, 48); }
  function label(el){
    /* A readable location in GA4, so a click can be traced to a place on the page. */
    if (el.closest('nav, .nav-links, .nav-cta, header')) return 'nav';
    if (el.closest('footer')) return 'footer';
    var s = el.closest('section, .cta-band, .xlinks, .blk');
    if (s) {
      if (s.id) return s.id;
      var c = (s.className || '').toString().trim().split(/\s+/)[0];
      var h = s.querySelector('h1, h2, h3');
      if (h && clean(h.textContent)) return (c ? c + ':' : '') + clean(h.textContent);
      if (c) return c;
    }
    /* No section wrapper: use the nearest heading above the link. */
    var all = Array.prototype.slice.call(document.querySelectorAll('h1,h2,h3,a'));
    var i = all.indexOf(el);
    for (var j = i - 1; j >= 0; j--) {
      if (/^H[123]$/.test(all[j].tagName) && clean(all[j].textContent)) return clean(all[j].textContent);
    }
    return 'body';
  }
  function pageId(){
    var p = location.pathname.replace(/\.html$/, '').replace(/^\//, '');
    return p === '' ? 'home' : p;
  }
  document.addEventListener('click', function(e){
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    /* Already instrumented inline — leave it alone, don't double-count. */
    var inline = a.getAttribute('onclick') || '';
    try {
      if (href.indexOf('calendly.com') !== -1) {
        if (inline.indexOf('book_call_click') !== -1) return;
        gtag('event', 'book_call_click', {
          page_id: pageId(),
          location: label(a),
          button_label: (a.textContent || '').trim().slice(0, 48)
        });
      } else if (href.slice(0, 7) === 'mailto:') {
        if (inline.indexOf('trackEvent') !== -1) return;
        gtag('event', 'email_click', {
          page_id: pageId(),
          location: label(a)
        });
      }
    } catch (err) {}
  }, true);
})();
/*dd-drill-v1*/
(function(){
  function isMobile(){ return window.innerWidth <= 960; }
  /* Hamburger: rebind cleanly */
  var oldT = document.querySelector('.nav-toggle');
  if (oldT) {
    var t = oldT.cloneNode(true); oldT.replaceWith(t);
    var links = document.querySelector('.nav-links');
    t.addEventListener('click', function(){
      var open = links.classList.toggle('open');
      t.classList.toggle('open', open);
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  /* Level 1: dropdown triggers */
  document.querySelectorAll('.nav-dd-trigger').forEach(function(old){
    var el = old.cloneNode(true); old.replaceWith(el);
    el.addEventListener('click', function(e){
      if (!isMobile()) return;
      e.preventDefault();
      var dd = el.parentElement;
      var was = dd.classList.contains('open');
      document.querySelectorAll('.nav-dd.open').forEach(function(d){ d.classList.remove('open'); });
      if (!was) dd.classList.add('open');
    });
  });
  /* Level 2: mega column headings drill down on mobile */
  document.querySelectorAll('.nav-mega-col > .nav-mega-label').forEach(function(old){
    var el = old.cloneNode(true); old.replaceWith(el);
    el.addEventListener('click', function(e){
      if (!isMobile()) return;
      e.preventDefault();
      el.parentElement.classList.toggle('open');
    });
  });
})();
