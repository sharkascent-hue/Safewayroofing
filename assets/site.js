/* Safeway Roofing & Chimneys — site behaviour, forms and ad tracking */
(function () {
  'use strict';

  /* ------------------------------------------------------------------
     SETTINGS — fill these in before going live.
     ------------------------------------------------------------------ */
  var CFG = {
    // Quote forms are delivered by Web3Forms to the inbox linked to the access key in each form.
    formEndpoint: 'https://api.web3forms.com/submit',
    whatsapp: '353874858556',
    // Google tags. Leave blank and nothing is loaded and no cookie banner is shown.
    googleAdsId: 'AW-18591308016',
    ga4Id: '',              // e.g. 'G-XXXXXXXXXX'
    convForm: 'YmXJCKmd7b0dEPCxg6FF', // 'Submit lead form' conversion
    convCall: '',           // Ads conversion label for a tap on the phone number
    convWhatsApp: ''        // Ads conversion label for a tap on WhatsApp
  };

  var root = document.documentElement.getAttribute('data-root') || '';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---------- Google tag + consent ---------- */
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;
  var tagIds = [CFG.googleAdsId, CFG.ga4Id].filter(Boolean);
  function conv(label, extra) {
    if (CFG.googleAdsId && label) gtag('event', 'conversion', Object.assign({ send_to: CFG.googleAdsId + '/' + label, value: 1.0, currency: 'EUR' }, extra || {}));
  }
  if (tagIds.length) {
    var choice = store('sw-consent');
    var g = choice === 'yes' ? 'granted' : 'denied';
    gtag('consent', 'default', { ad_storage: g, ad_user_data: g, ad_personalization: g, analytics_storage: g });
    gtag('js', new Date());
    tagIds.forEach(function (id) { gtag('config', id); });
    var s = document.createElement('script');
    s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + tagIds[0];
    document.head.appendChild(s);
    var bar = $('#cookie');
    if (bar && !choice) bar.classList.add('show');
    $$('[data-consent]').forEach(function (b) {
      b.addEventListener('click', function () {
        var yes = b.getAttribute('data-consent') === 'yes';
        store('sw-consent', yes ? 'yes' : 'no');
        var v = yes ? 'granted' : 'denied';
        gtag('consent', 'update', { ad_storage: v, ad_user_data: v, ad_personalization: v, analytics_storage: v });
        bar.classList.remove('show');
      });
    });
  }

  /* ---------- click tracking: calls + WhatsApp ---------- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href');
    if (h.indexOf('tel:') === 0) { gtag('event', 'click_call'); conv(CFG.convCall); }
    else if (h.indexOf('wa.me') > -1) { gtag('event', 'click_whatsapp'); conv(CFG.convWhatsApp); }
  });

  /* ---------- keep ad click IDs / UTMs for the enquiry email ---------- */
  var qs = new URLSearchParams(location.search), keep = ['gclid', 'gbraid', 'wbraid', 'gad_source', 'gad_campaignid', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
  var src = {};
  try { src = JSON.parse(sessionStorage.getItem('sw-src') || '{}'); } catch (e) {}
  keep.forEach(function (k) { if (qs.get(k)) src[k] = qs.get(k); });
  try { sessionStorage.setItem('sw-src', JSON.stringify(src)); } catch (e) {}

  /* ---------- mobile menu ---------- */
  var mnav = $('#mnav');
  $$('[data-menu]').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = b.getAttribute('data-menu') === 'open';
      mnav.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
  });

  /* ---------- scroll animations ---------- */
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function mark(el, cls, d) {
    if (!el || el.closest('.hero')) return;
    el.classList.add('rv');
    if (cls) el.classList.add(cls);
    if (d) el.style.setProperty('--d', d + 's');
  }
  // two-column blocks: text slides in from its side, photo wipes in
  $$('.split').forEach(function (sp) {
    var flip = sp.classList.contains('flip');
    Array.prototype.forEach.call(sp.children, function (c, i) {
      if (c.classList.contains('media')) mark(c);
      else mark(c, (i === 0) !== flip ? 'rv-l' : 'rv-r');
    });
  });
  $$('.sec-head').forEach(function (el) { mark(el); });
  // staggered groups
  [['.grid', ''], ['.gal', 'rv-zoom'], ['.acols', ''], ['.chips', 'rv-zoom'], ['.faq', ''], ['.lp-strip ul', ''],
   ['.contact-list', 'rv-l'], ['.list2', ''], ['.filters', '']].forEach(function (g) {
    $$(g[0]).forEach(function (box) {
      if (box.closest('.hero')) return;
      Array.prototype.forEach.call(box.children, function (c, i) {
        if (c.tagName === 'SCRIPT') return;
        mark(c, g[1], Math.min(i % 8, 7) * (g[0] === '.chips' ? 0.03 : 0.09));
      });
    });
  });
  $$('.cta-band .wrap>*').forEach(function (c, i) { mark(c, i ? '' : 'rv-l', i * 0.15); });
  $$('.prose>*').forEach(function (c) { mark(c); });
  $$('.ftr .cols>*').forEach(function (c, i) { mark(c, '', i * 0.1); });
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.05 });
    $$('.rv').forEach(function (el) { io.observe(el); });
  } else { $$('.rv').forEach(function (el) { el.classList.add('in'); }); }

  // scroll progress bar + gentle hero parallax
  var bar = document.createElement('div'); bar.className = 'prog'; document.body.appendChild(bar);
  var hbg = $('.hero .hero-bg'), ticking = false;
  function onScroll() {
    var h = document.documentElement.scrollHeight - innerHeight, y = scrollY;
    bar.style.transform = 'scaleX(' + (h > 0 ? y / h : 0) + ')';
    if (hbg && !reduce && y < innerHeight * 1.2) hbg.style.translate = '0 ' + (y * 0.35) + 'px';
    ticking = false;
  }
  addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  // hero video: honour reduced motion / data saver, pause when off screen
  var vid = $('video.hero-bg');
  if (vid) {
    var lite = reduce || (navigator.connection && navigator.connection.saveData);
    if (lite) { vid.autoplay = false; vid.preload = 'none'; vid.pause(); }
    else if ('IntersectionObserver' in window) {
      // while the intro splash is up, hold the video so it doesn't compete with the animation
      var html = document.documentElement, held = /\bintro\b/.test(html.className) && !/intro-out/.test(html.className);
      if (held) {
        vid.autoplay = false; vid.pause();
        var mo = new MutationObserver(function () {
          if (/intro-out/.test(html.className) || !/\bintro\b/.test(html.className)) {
            mo.disconnect(); held = false; var pr = vid.play(); if (pr && pr.catch) pr.catch(function () {});
          }
        });
        mo.observe(html, { attributes: true, attributeFilter: ['class'] });
      }
      new IntersectionObserver(function (en) {
        en.forEach(function (x) {
          if (x.isIntersecting) { if (held) return; var pr = vid.play(); if (pr && pr.catch) pr.catch(function () {}); } else vid.pause();
        });
      }).observe(vid);
    }
  }

  /* ---------- quote forms ---------- */
  $$('form[data-quote]').forEach(function (f) {
    var msg = $('.fmsg', f), btn = $('button[type=submit]', f);
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(f), bad = false;
      ['name', 'phone'].forEach(function (n) {
        var el = f.elements[n]; if (!el) return;
        var v = (el.value || '').trim();
        var ok = n === 'phone' ? v.replace(/\D/g, '').length >= 7 : v.length > 1;
        el.closest('.fld').classList.toggle('err', !ok); if (!ok) bad = true;
      });
      if (bad) { msg.className = 'fmsg bad'; msg.textContent = 'Please add your name and a phone number we can reach you on.'; return; }
      if (d.get('botcheck')) return;
      var em = f.elements.email;
      if (em && em.value.trim() && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em.value.trim())) {
        em.closest('.fld').classList.add('err'); msg.className = 'fmsg bad'; msg.textContent = 'That email address does not look right. Fix it or leave it blank.'; return;
      }
      if (em) em.closest('.fld').classList.remove('err');
      d.set('subject', 'New quote request: ' + (d.get('service') || 'Website enquiry') + ' (' + (d.get('area') || 'area not given') + ')');
      d.delete('redirect'); d.delete('botcheck');
      d.append('page', location.pathname);
      Object.keys(src).forEach(function (k) { d.append(k, src[k]); });
      btn.disabled = true; var label = btn.innerHTML; btn.textContent = 'Sending…';
      fetch(CFG.formEndpoint, { method: 'POST', headers: { Accept: 'application/json' }, body: d })
        .then(function (r) { return r.json().then(function (j) { if (!r.ok || !j.success) throw new Error(j.message || r.status); }); })
        .then(function () {
          gtag('event', 'generate_lead', { form: f.getAttribute('data-quote') });
          try { sessionStorage.setItem('sw-lead', '1'); } catch (e) {}
          location.href = root + 'thank-you/';
        })
        .catch(function () {
          btn.disabled = false; btn.innerHTML = label;
          var t = 'Hi Safeway Roofing, I would like a quote.\nName: ' + d.get('name') + '\nPhone: ' + d.get('phone') +
            '\nArea: ' + (d.get('area') || '') + '\nService: ' + (d.get('service') || '') + '\n' + (d.get('message') || '');
          msg.className = 'fmsg bad';
          msg.innerHTML = 'Sorry, that did not send. Please call <a href="tel:+353874858556">087 485 8556</a> or <a target="_blank" rel="noopener" href="https://wa.me/' + CFG.whatsapp + '?text=' + encodeURIComponent(t) + '">send it by WhatsApp</a>.';
        });
    });
  });

  /* thank-you page: fire the Ads conversion once per sent form */
  if (document.body.hasAttribute('data-thanks')) {
    var sent = false; try { sent = sessionStorage.getItem('sw-lead') === '1'; sessionStorage.removeItem('sw-lead'); } catch (e) {}
    if (sent) conv(CFG.convForm);
  }

  /* ---------- area checker ---------- */
  var ac = $('form[data-area]');
  if (ac) {
    var areas = JSON.parse($('#area-data').textContent), out = $('.acheck-out');
    var norm = function (s) { return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9 ]/g, '').trim(); };
    ac.addEventListener('submit', function (e) {
      e.preventDefault();
      var q = norm(ac.elements.q.value); if (!q) return;
      var hit = null;
      Object.keys(areas).forEach(function (c) { areas[c].forEach(function (a) { if (!hit && (norm(a).indexOf(q) > -1 || q.indexOf(norm(a)) > -1)) hit = [a, c]; }); });
      if (!hit && /^(d(ublin)? ?\d{1,2}w?|dublin|kildare|wicklow|co\.? ?(dublin|kildare|wicklow))$/.test(q)) hit = [ac.elements.q.value.trim(), 'our area'];
      if (hit) { out.className = 'acheck-out yes'; out.textContent = 'Yes, we cover ' + hit[0] + (hit[1] === 'our area' ? '' : ' (' + hit[1] + ')') + '. Call 087 485 8556 or request a quote.'; }
      else { out.className = 'acheck-out no'; out.textContent = 'We may still cover you. We work across Dublin, Kildare and Wicklow, so ring 087 485 8556 and ask.'; }
    });
  }

  /* ---------- gallery filter + lightbox ---------- */
  $$('.filters button').forEach(function (b) {
    b.addEventListener('click', function () {
      var c = b.getAttribute('data-f');
      $$('.filters button').forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
      $$('.gal .gi').forEach(function (g) { g.hidden = !(c === 'all' || g.getAttribute('data-c') === c); });
    });
  });
  var lb = $('#lb');
  if (lb) {
    var items = [], idx = 0, img = $('img', lb), cap = $('p', lb);
    var show = function (i) {
      idx = (i + items.length) % items.length;
      img.src = items[idx].getAttribute('data-full'); img.alt = items[idx].getAttribute('data-cap') || '';
      cap.textContent = items[idx].getAttribute('data-cap') || '';
    };
    document.addEventListener('click', function (e) {
      var g = e.target.closest && e.target.closest('.gi');
      if (!g) return;
      items = $$('.gi', g.parentNode).filter(function (x) { return !x.hidden; });
      show(items.indexOf(g)); lb.classList.add('open');
    });
    var close = function () { lb.classList.remove('open'); img.src = ''; };
    $('.x', lb).addEventListener('click', close);
    $('.p', lb).addEventListener('click', function () { show(idx - 1); });
    $('.nx', lb).addEventListener('click', function () { show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(idx - 1); if (e.key === 'ArrowRight') show(idx + 1);
    });
  }

  var y = $('#yr'); if (y) y.textContent = new Date().getFullYear();
})();
