/* LotCal shared chrome: nav, footer, dots background, disclaimer popup, cookie banner.
   Each page sets <body data-page="home" data-base="" data-pop="1" data-cookie="1"> */
(function () {
  var base = document.body.getAttribute('data-base') || '';
  var page = document.body.getAttribute('data-page') || '';
  var popOn = document.body.getAttribute('data-pop') !== '0';
  var cookieOn = document.body.getAttribute('data-cookie') !== '0';

  var LOGO = '<svg viewBox="0 0 24 24" aria-hidden="true"><defs><linearGradient id="zg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f89640"/><stop offset="1" stop-color="#e26a18"/></linearGradient></defs><rect x="1" y="1" width="22" height="22" rx="6" fill="url(#zg)"/><g fill="none" stroke="#1b0d05" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="4.5" width="12" height="15" rx="2"/><rect x="8" y="7" width="8" height="3.4" rx="0.8"/></g><g fill="#1b0d05"><circle cx="8.6" cy="13.2" r="0.9"/><circle cx="12" cy="13.2" r="0.9"/><circle cx="15.4" cy="13.2" r="0.9"/><circle cx="8.6" cy="16.3" r="0.9"/><circle cx="12" cy="16.3" r="0.9"/><circle cx="15.4" cy="16.3" r="0.9"/></g></svg>';
  var MARK = '<svg viewBox="0 0 24 24" aria-hidden="true"><g fill="none" stroke="#1b0d05" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="4.5" width="12" height="15" rx="2"/><rect x="8" y="7" width="8" height="3.4" rx="0.8"/></g><g fill="#1b0d05"><circle cx="8.6" cy="13.2" r="0.9"/><circle cx="12" cy="13.2" r="0.9"/><circle cx="15.4" cy="13.2" r="0.9"/><circle cx="8.6" cy="16.3" r="0.9"/><circle cx="12" cy="16.3" r="0.9"/><circle cx="15.4" cy="16.3" r="0.9"/></g></svg>';

  var NAV = [
    ['index.html', 'Home', 'home'],
    ['about.html', 'About', 'about'],
    ['blog.html', 'Blog', 'blog'],
    ['faq.html', 'FAQ', 'faq'],
    ['contract-size.html', 'Contract Size', 'contract-size'],
    ['contact.html', 'Contact', 'contact']
  ];

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }

  function buildNav() {
    var links = NAV.map(function (n) {
      return '<a href="' + base + n[0] + '"' + (page === n[2] ? ' class="active"' : '') + '>' + n[1] + '</a>';
    }).join('');
    var h = el('header', 'nav');
    h.innerHTML =
      '<a class="brand" href="' + base + 'index.html" aria-label="LotCal home">' +
        '<span class="brand-ico">' + LOGO + '</span><span>LotCal</span></a>' +
      '<button class="nav-toggle" type="button" aria-label="Toggle menu" aria-expanded="false">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>' +
      '</button>' +
      '<nav class="menu" aria-label="Main">' + links + '</nav>';
    var toggle = h.querySelector('.nav-toggle');
    var menu = h.querySelector('.menu');
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { menu.classList.remove('open'); });
    });
    var stack = document.querySelector('.stack');
    stack.insertBefore(h, stack.firstChild);
  }

  function buildFooter() {
    var f = el('footer');
    f.innerHTML =
      '<div>' +
        '<a class="f-brand" href="' + base + 'index.html" aria-label="LotCal"><span class="f-mark">' + MARK + '</span>LotCal</a>' +
        '<p class="f-tag">LotCal is a free educational leverage calculator for forex, metals and crypto futures. It shows the leverage you need for a position and your P&amp;L per $1 price move. Calculations are theoretical estimates &mdash; always verify contract sizes and prices with your broker before trading.</p>' +
        '<nav class="f-cols" aria-label="Site">' +
          '<div class="f-col"><p class="f-h">Site</p>' +
            '<a href="' + base + 'index.html">Home</a>' +
            '<a href="' + base + 'about.html">About</a>' +
            '<a href="' + base + 'blog.html">Blog</a>' +
            '<a href="' + base + 'faq.html">FAQ</a>' +
            '<a href="' + base + 'contract-size.html">Contract Size Guide</a>' +
            '<a href="' + base + 'how-it-works.html">How It Works</a>' +
          '</div>' +
          '<div class="f-col"><p class="f-h">Legal</p>' +
            '<a href="' + base + 'terms.html">Terms of Use</a>' +
            '<a href="' + base + 'privacy.html">Privacy Policy</a>' +
            '<a href="' + base + 'disclaimer.html">Disclaimer</a>' +
            '<a href="' + base + 'cookies.html">Cookie Policy</a>' +
            '<a href="' + base + 'contact.html">Contact</a>' +
          '</div>' +
        '</nav>' +
        '<p class="f-copy">&copy; LotCal 2026 &middot; Forex &amp; Crypto Leverage Calculator</p>' +
        '<p class="f-made">Made by <strong>Anas Shaikh</strong> <span class="bh" aria-hidden="true">&#9829;</span></p>' +
      '</div>';
    document.querySelector('.content').appendChild(f);
  }

  function buildDots() {
    var wrap = document.querySelector('.wrap');
    var cv = document.createElement('canvas');
    cv.id = 'dots';
    cv.setAttribute('aria-hidden', 'true');
    wrap.insertBefore(cv, wrap.firstChild);
    runDots(cv);
  }

  function runDots(cv) {
    var ctx = cv.getContext('2d');
    var calm = matchMedia('(prefers-reduced-motion:reduce)').matches;
    var W = 0, H = 0, dpr = 1, step = 0, cols = 0, rows = 0, seed = [];
    var mx = -9999, my = -9999, tmx = -9999, tmy = -9999;
    var hash = function (i, j) { var h = Math.sin(i * 127.1 + j * 311.7) * 43758.5453; return h - Math.floor(h); };
    function size() {
      dpr = Math.min(devicePixelRatio || 1, 2); W = cv.clientWidth; H = cv.clientHeight;
      cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      step = Math.max(14, Math.min(W / 1600, H / 940) * 20.5); cols = Math.ceil(W / step) + 1; rows = Math.ceil(H / step) + 1;
      seed = []; for (var j = 0; j < rows; j++) for (var i = 0; i < cols; i++) seed.push([hash(i, j), hash(i + 71, j + 13), hash(i + 9, j + 97)]);
    }
    addEventListener('resize', size); size();
    addEventListener('pointermove', function (e) { var r = cv.getBoundingClientRect(); tmx = e.clientX - r.left; tmy = e.clientY - r.top; });
    document.addEventListener('pointerleave', function () { tmx = tmy = -9999; });
    var C0 = [226, 106, 24], C1 = [248, 150, 64], C2 = [255, 214, 170];
    var mix = function (a, b, t) { return a.map(function (v, k) { return Math.round(v + (b[k] - v) * t); }); };
    function draw(t) {
      ctx.clearRect(0, 0, W, H);
      mx += (tmx - mx) * .12; my += (tmy - my) * .12;
      var top = H * .1, full = H * .36, R = step * .37;
      for (var j = 0; j < rows; j++) {
        var y = j * step + step * .5; if (y < top - step * 2) continue;
        var v = Math.min(1, Math.max(0, (y - top) / (full - top)));
        var col = v < .55 ? mix(C0, C1, v / .55) : mix(C1, C2, (v - .55) / .45 * .85 + Math.max(0, (y - H * .9) / (H * .1)) * .15);
        ctx.fillStyle = 'rgb(' + col[0] + ',' + col[1] + ',' + col[2] + ')';
        for (var i = 0; i < cols; i++) {
          var x = i * step + step * .5, s0 = seed[j * cols + i], a = s0[0], b = s0[1], c = s0[2];
          var wave = calm ? .7 : .5 + .5 * Math.sin(t * (1.6 + b * 2.6) + a * 6.283 + Math.sin(t * .7 + i * .21 + j * .13) * 1.4);
          var keep = Math.min(1, v * 1.6 + .12) - (a * .6);
          if (keep <= 0 && c > .08) continue;
          var s = (.42 + .58 * Math.pow(wave, 1.3)) * Math.min(1, .5 + v * .6) * (keep > 0 ? 1 : .8);
          var dx = x - mx, dy = y - my, d2 = dx * dx + dy * dy, hov = Math.exp(-d2 / (step * step * 22));
          s = Math.min(1.05, s + hov * .7);
          var r = R * s; if (r < .6) continue;
          ctx.beginPath(); ctx.arc(x, y, r, 0, 6.2832); ctx.fill();
        }
      }
    }
    function loop(ms) { draw(ms / 1000); requestAnimationFrame(loop); }
    requestAnimationFrame(loop);
  }

  function buildPopups() {
    var disc = el('aside');
    disc.id = 'disc-pop';
    disc.setAttribute('role', 'dialog');
    disc.setAttribute('aria-label', 'Disclaimer');
    disc.setAttribute('aria-live', 'polite');
    disc.innerHTML =
      '<p class="pop-t">Disclaimer</p>' +
      '<p class="pop-b">LotCal is an educational calculator &mdash; not financial advice, not a trade recommendation. Leverage trading carries a high risk of losing your entire margin. Calculations are theoretical estimates; verify contract sizes and prices with your broker.</p>' +
      '<div class="pop-a"><a href="' + base + 'disclaimer.html">Read full disclaimer</a><button id="disc-ok" class="pop-btn" type="button">I understand</button></div>';
    disc.hidden = true;

    var ck = el('aside');
    ck.id = 'cookie-pop';
    ck.setAttribute('role', 'dialog');
    ck.setAttribute('aria-label', 'Cookie consent');
    ck.innerHTML =
      '<p class="pop-t">Cookies</p>' +
      '<p class="pop-b">We use essential cookies to make this site work, and (with your consent) analytics and advertising cookies that help us understand traffic and keep LotCal free. You can accept or reject non-essential cookies. See the Cookie Policy for details.</p>' +
      '<div class="pop-a"><a href="' + base + 'cookies.html">Cookie Policy</a>' +
      '<span style="display:flex;gap:8px;flex-wrap:wrap"><button id="cookie-essential" class="pop-btn ghost" type="button">Only essential</button>' +
      '<button id="cookie-all" class="pop-btn" type="button">Accept all</button></span></div>';
    ck.hidden = true;

    document.body.appendChild(disc);
    document.body.appendChild(ck);

    function showDisc() { if (popOn) disc.hidden = false; }
    function showCookie() { if (cookieOn) ck.hidden = false; }

    if (cookieOn) {
      showCookie();
      document.getElementById('cookie-all').addEventListener('click', function () {
        localStorage.setItem('lotcal_cookie', 'all'); ck.hidden = true; showDisc();
      });
      document.getElementById('cookie-essential').addEventListener('click', function () {
        localStorage.setItem('lotcal_cookie', 'essential'); ck.hidden = true; showDisc();
      });
    } else {
      showDisc();
    }

    document.getElementById('disc-ok').addEventListener('click', function () {
      localStorage.setItem('lotcal_disc', '1'); disc.hidden = true;
    });
  }

  buildDots();
  buildNav();
  buildFooter();
  buildPopups();
})();
