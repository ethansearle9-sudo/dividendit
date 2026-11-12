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
/*consent-v1: analytics only runs after an explicit yes (Google Consent Mode v2) */
(function(){
  var KEY = 'ddit_consent';
  function get(){ try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v){ try { localStorage.setItem(KEY, v); } catch (e) {} }
  function apply(v){
    if (typeof gtag === 'function') gtag('consent', 'update', { analytics_storage: v === 'granted' ? 'granted' : 'denied' });
  }
  var bar = document.createElement('div');
  bar.className = 'consent'; bar.setAttribute('role', 'region'); bar.setAttribute('aria-label', 'Cookie consent'); bar.hidden = true;
  bar.innerHTML = '<p>We use analytics cookies to see which pages are useful to business owners. Nothing is set unless you agree. <a href="/privacy#cookies">Privacy</a></p>' +
    '<div class="consent-actions"><button type="button" class="consent-no">Decline</button><button type="button" class="consent-yes">Accept</button></div>';
  document.body.appendChild(bar);
  function choose(v){ set(v); apply(v); bar.hidden = true; }
  bar.querySelector('.consent-yes').addEventListener('click', function(){ choose('granted'); });
  bar.querySelector('.consent-no').addEventListener('click', function(){ choose('denied'); });
  document.addEventListener('click', function(e){
    var t = e.target.closest && e.target.closest('[data-consent-open]');
    if (t) { e.preventDefault(); bar.hidden = false; bar.querySelector('.consent-yes').focus(); }
  });
  if (!get()) bar.hidden = false;
})();
