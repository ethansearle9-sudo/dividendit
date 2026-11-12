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
