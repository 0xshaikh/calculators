#!/usr/bin/env python3
# LotCal static page generator — writes all content pages with the shared chrome.
import os
os.chdir('/home/ubuntu/calculators-site')

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#050302">
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{ogdesc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://0xshaikh.github.io/calculators/{file}">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E%3Cstop offset='0' stop-color='%23f89640'/%3E%3Cstop offset='1' stop-color='%23e26a18'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect x='1' y='1' width='22' height='22' rx='6' fill='url(%23g)'/%3E%3Cg fill='none' stroke='%231b0d05' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='6' y='4.5' width='12' height='15' rx='2'/%3E%3Crect x='8' y='7' width='8' height='3.4' rx='0.8'/%3E%3C/g%3E%3Cg fill='%231b0d05'%3E%3Ccircle cx='8.6' cy='13.2' r='0.9'/%3E%3Ccircle cx='12' cy='13.2' r='0.9'/%3E%3Ccircle cx='15.4' cy='13.2' r='0.9'/%3E%3Ccircle cx='8.6' cy='16.3' r='0.9'/%3E%3Ccircle cx='12' cy='16.3' r='0.9'/%3E%3Ccircle cx='15.4' cy='16.3' r='0.9'/%3E%3C/g%3E%3C/svg%3E">
<link rel="stylesheet" href="{css}">
</head>
<body data-page="{page}" data-base="{base}" data-pop="{pop}" data-cookie="1">
<main class="wrap">
  <div class="content">
    <div class="stack{narrow}">
{body}
    </div>
  </div>
</main>
<script src="{cssjs}site.js"></script>
</body>
</html>
"""

def page(fname, title, desc, ogdesc, body, pageid, base='', css='site.css', narrow=' narrow', pop='1'):
    h = HEAD.format(file=fname, title=title, desc=desc, ogdesc=ogdesc, page=pageid, base=base, css=css, cssjs=base, narrow=narrow, body=body, pop=pop)
    with open(fname, 'w') as f:
        f.write(h)
    print('wrote', fname, len(body.split()), 'words-ish body')

# ============ ABOUT ============
about_body = """
<p class="eyebrow">About</p>
<h1>What is LotCal?</h1>
<p class="lede">A free, honest leverage calculator for people who trade forex, metals and crypto futures — built because I kept getting the arithmetic wrong.</p>
<div class="card">
  <div class="prose">
    <h2>LotCal kya hai</h2>
    <p>LotCal is a small, free, open calculator that answers one question I asked myself far too often: <strong>&ldquo;if I open this lot size on this pair with this account, what leverage am I actually using &mdash; and how much do I win or lose per $1 of price movement?&rdquo;</strong> You enter your balance, pick a pair, type a lot size and a price, and it tells you the position value, the quantity in oz / BTC / EUR, the required leverage, and the live P&amp;L per $1 move in green and red.</p>

    <h2>Why I built it</h2>
    <p>I trade futures and I kept guessing. &ldquo;Is 0.01 lot of gold a dollar a point? Two?&rdquo; I&rsquo;d do the mental math, get it wrong more often than I&rsquo;d like, and find out the real number after the trade was already open. LotCal is the check I wanted before clicking buy or sell. I made it public because the same confusion is everywhere &mdash; and because a tool that removes guesswork before a trade is worth sharing.</p>

    <h2>Who&rsquo;s behind it</h2>
    <p>I&rsquo;m <strong>Anas Shaikh</strong>. I&rsquo;m self-taught, curious about markets and automation, and I build small tools that answer real questions. LotCal is one of them. It&rsquo;s not a company and it&rsquo;s not a signal service &mdash; it&rsquo;s one person&rsquo;s calculator, published for anyone who wants to size a position before risking money.</p>

    <h2>How it works</h2>
    <p>LotCal uses the standard futures formula: <code>position value = lot size &times; contract size &times; price</code>, and <code>leverage = position value &divide; balance</code>. Contract sizes are common broker defaults &mdash; 1 lot of gold = 100 oz, 1 lot of EURUSD = 100,000 units, 1 lot of BTC = 1 BTC. Prices are reference snapshots, so replace them with your broker&rsquo;s live quote. It is deliberately conservative: it assumes your whole balance is available as initial margin, so the leverage you see is the maximum, not a promise.</p>

    <h2>What it is not</h2>
    <p>LotCal is <strong>not financial advice</strong>, not a recommendation, and not a broker. It does not execute trades, hold funds, or know your broker&rsquo;s margin tiers, fees or liquidation rules. It just does the arithmetic honestly and leaves the judgement to you.</p>
  </div>
</div>
"""
page('about.html', 'About — LotCal', 'LotCal is a free, honest leverage calculator for forex, metals and crypto futures, built by Anas Shaikh. Learn why it exists and how it works.', 'What LotCal is, why it was built, and how it calculates leverage and P&L.', about_body, 'about')

# ============ CONTACT ============
contact_body = """
<p class="eyebrow">Contact</p>
<h1>Get in touch</h1>
<p class="lede">A real person reads these. No bot, no canned replies.</p>
<div class="card">
  <div class="prose">
    <h2>Email</h2>
    <p>Write to <a href="mailto:node9555@gmail.com">node9555@gmail.com</a>. That&rsquo;s the only contact channel LotCal uses &mdash; there&rsquo;s no sign-up, no account and no form that silently drops your message.</p>

    <h2>How fast will I reply?</h2>
    <p>Usually within <strong>24&ndash;48 hours</strong> on working days. If it&rsquo;s urgent (a broken calculator, a wrong contract size), put &ldquo;LotCal&rdquo; in the subject line and I&rsquo;ll get to it first.</p>

    <h2>What to include</h2>
    <ul>
      <li>Which page or calculator you&rsquo;re using</li>
      <li>The pair, lot size and balance you entered</li>
      <li>A screenshot if something looks wrong</li>
      <li>For data requests (see the <a href="privacy.html">Privacy Policy</a>), say exactly what you want deleted</li>
    </ul>

    <h2>Email me now</h2>
    <p><a class="btnline" href="mailto:node9555@gmail.com?subject=LotCal%20%2D%20Message">Email LotCal &rarr;</a></p>
    <p style="margin-top:calc(14*var(--u))"><em>I can&rsquo;t help with trade decisions, account issues or broker problems &mdash; that&rsquo;s between you and your broker. For anything about the site itself, I&rsquo;m happy to help.</em></p>
  </div>
</div>
"""
page('contact.html', 'Contact — LotCal', 'Contact LotCal: email node9555@gmail.com, reply within 24–48 hours on working days.', 'Email LotCal directly — real email, real reply, no fake form.', contact_body, 'contact')

# ============ PRIVACY ============
privacy_body = """
<p class="eyebrow">Legal</p>
<h1>Privacy Policy</h1>
<p class="lede">Last updated: November 2026. LotCal is a static website — it collects as little as it possibly can.</p>
<div class="card">
  <div class="prose">
    <h2>1. What data we collect</h2>
    <p>LotCal is a static site with no accounts and no sign-up. We do not ask for your name, email or any personal details to use the calculator. The only things that may be collected are:</p>
    <ul>
      <li><strong>Essential cookies / local storage</strong> — used to remember your cookie choice and whether you&rsquo;ve seen the disclaimer. These are necessary for the site to work and cannot be switched off.</li>
      <li><strong>Analytics cookies</strong> — only if you accept them. These help us understand which pages are visited and how the calculator is used, so we can improve it. If you reject them, none are set.</li>
      <li><strong>Advertising cookies</strong> — only if you accept them. Third-party ad networks may set them to show you relevant ads (see below).</li>
      <li><strong>IP address and technical data</strong> — your IP and browser details are seen by the hosting provider and any third-party analytics or ad network you consent to, in the ordinary course of serving a web page. We do not store or look at them ourselves.</li>
    </ul>

    <h2>2. Google AdSense and third-party ads</h2>
    <p>LotCal may display advertising served by <strong>Google AdSense</strong> and other third-party ad networks. Google and its partners may use advertising cookies (including the DoubleClick cookie) to serve ads based on your visits to this and other websites.</p>
    <p>Google&rsquo;s use of advertising cookies enables it and its partners to serve ads based on your prior visits to LotCal and elsewhere. Third-party vendors and ad networks may also set their own cookies to show you personalised ads.</p>

    <h2>3. Cookies for personalised ads and how to opt out</h2>
    <p>Google may use the <strong>&ldquo;cookies for personalised ads&rdquo;</strong> mechanism. You can opt out of personalised advertising by:</p>
    <ul>
      <li>Visiting <strong>Google&rsquo;s Ads Settings</strong> at <a href="https://adssettings.google.com" rel="nofollow noopener" target="_blank">adssettings.google.com</a>, and</li>
      <li>Visiting <strong>www.aboutads.info</strong> to opt out of some third-party vendors&rsquo; use of cookies for personalised advertising.</li>
    </ul>
    <p>You can also block cookies entirely in your browser, or use the cookie banner on this site to accept only essential cookies. Opting out of personalised ads does not stop ads from appearing — it just makes them less targeted.</p>

    <h2>4. Your choices</h2>
    <p>Use the cookie banner on any page to accept or reject non-essential cookies at any time, or clear your cookies in your browser settings. Essential local storage items (<code>lotcal_cookie</code>, <code>lotcal_disc</code>) are used only for the site to remember your preferences.</p>

    <h2>5. Data deletion</h2>
    <p>Because we store no personal data on a server, there is usually nothing for us to delete. If you want us to remove anything you&rsquo;ve sent us by email, or to confirm what we hold, email <a href="mailto:node9555@gmail.com">node9555@gmail.com</a> with the subject <strong>&ldquo;LotCal data request&rdquo;</strong>. We&rsquo;ll confirm within 30 days.</p>

    <h2>6. GDPR — visitors in the EU, UK and Switzerland</h2>
    <p>If you are in the European Economic Area, the United Kingdom or Switzerland, the EU General Data Protection Regulation (GDPR) and UK GDPR apply to any personal data we process:</p>
    <ul>
      <li><strong>Legal basis:</strong> essential cookies are processed on the basis of legitimate interest (making the site work); analytics and advertising cookies are processed only on the basis of your <strong>consent</strong>, which you give or withhold through the cookie banner.</li>
      <li><strong>Your rights:</strong> you have the right to access, correct, erase, restrict and object to processing of your personal data, and the right to data portability. You can withdraw consent at any time by clearing your cookies or rejecting non-essential cookies in the banner.</li>
      <li><strong>Complaints:</strong> you may lodge a complaint with your local supervisory authority if you believe your data is handled unlawfully.</li>
      <li><strong>Contact:</strong> for any GDPR request, email <a href="mailto:node9555@gmail.com">node9555@gmail.com</a> with the subject <strong>&ldquo;GDPR request&rdquo;</strong>.</li>
    </ul>
    <p>Data is not transferred outside these regions knowingly; if it is (for example, via a third-party ad server), it is on the basis of the consent you give or standard contractual safeguards.</p>

    <h2>7. Children</h2>
    <p>LotCal is a trading-education tool and is not directed at children under 16. We do not knowingly collect data from them.</p>

    <h2>8. Changes</h2>
    <p>If this policy changes, we&rsquo;ll update this page and the date above. Significant changes will be flagged on the site.</p>

    <h2>9. Contact</h2>
    <p>Questions about privacy: <a href="mailto:node9555@gmail.com">node9555@gmail.com</a>.</p>
  </div>
</div>
"""
page('privacy.html', 'Privacy Policy — LotCal', 'How LotCal handles data: essential and consent-based cookies, Google AdSense, personalised ads opt-out, data deletion, and GDPR rights for EU, UK and Switzerland visitors.', 'LotCal Privacy Policy — what data is collected, AdSense and third-party ads, personalised-ads opt-out, and GDPR rights.', privacy_body, 'privacy')

# ============ TERMS ============
terms_body = """
<p class="eyebrow">Legal</p>
<h1>Terms of Use</h1>
<p class="lede">Last updated: November 2026. By using LotCal you agree to these terms.</p>
<div class="card">
  <div class="prose">
    <h2>1. Acceptance</h2>
    <p>By accessing or using LotCal you accept these Terms of Use. If you do not agree, do not use the site.</p>

    <h2>2. What LotCal is</h2>
    <p>LotCal is a free educational calculator for forex, metals and crypto futures. It computes position value, quantity, required leverage and P&amp;L per $1 price move from values you enter. It is <strong>not</strong> financial advice, investment advice, or a recommendation to buy or sell any instrument, and it is not a brokerage or trading platform.</p>

    <h2>3. Your use</h2>
    <p>You agree to use LotCal only for lawful purposes. You may not:</p>
    <ul>
      <li>Scrape, copy or republish the site&rsquo;s content without permission;</li>
      <li>Attempt to disrupt, overload or exploit the site;</li>
      <li>Use the site to misrepresent yourself or the results.</li>
    </ul>

    <h2>4. No warranty</h2>
    <p>LotCal is provided &ldquo;as is&rdquo; and &ldquo;as available&rdquo;, without warranties of any kind, express or implied, including accuracy, fitness for a particular purpose or non-infringement. Contract sizes are common broker defaults; prices are reference snapshots; the leverage shown assumes your entire balance is available as initial margin and may not match your broker&rsquo;s actual margin requirements, leverage tiers, fees, spread or liquidation rules. You are responsible for verifying every value with your broker before trading.</p>

    <h2>5. Limitation of liability</h2>
    <p>To the maximum extent permitted by law, LotCal and its owner are not liable for any direct, indirect, incidental or consequential loss arising from your use of, or reliance on, the site or its calculations. Trading leveraged products carries a high risk of losing capital, and losses may exceed your deposit. Nothing here limits rights you have under mandatory consumer protection law where you live.</p>

    <h2>6. Intellectual property</h2>
    <p>The LotCal name, logo, design and written content are owned by the site owner unless stated otherwise. You may view and share links to the site freely; you may not reproduce the content commercially without permission. Third-party names and marks (e.g. XAUUSD, BTCUSD, Google AdSense) belong to their respective owners and are used for identification only.</p>

    <h2>7. Third-party links and ads</h2>
    <p>The site may contain links to third-party sites and display third-party advertising. We do not control and are not responsible for third-party content, ads or privacy practices. An affiliate relationship, if any, will be disclosed.</p>

    <h2>8. Changes to the site and these terms</h2>
    <p>We may change, suspend or discontinue any part of LotCal at any time, and may update these terms. The latest version is always on this page; continued use after a change means you accept it. We&rsquo;ll update the date above when we do.</p>

    <h2>9. Governing law</h2>
    <p>These terms are governed by the laws of the site owner&rsquo;s country of residence, without regard to conflict-of-law rules. Mandatory consumer laws of your country of residence are not affected.</p>

    <h2>10. Contact</h2>
    <p>Questions about these terms: <a href="mailto:node9555@gmail.com">node9555@gmail.com</a>.</p>
  </div>
</div>
"""
page('terms.html', 'Terms of Use — LotCal', 'LotCal Terms of Use: acceptance, permitted use, no warranty, limitation of liability, intellectual property and changes to the site.', 'Terms of Use for LotCal — the conditions for using the site.', terms_body, 'terms')

# ============ COOKIES ============
cookies_body = """
<p class="eyebrow">Legal</p>
<h1>Cookie Policy</h1>
<p class="lede">Last updated: November 2026. This explains the cookies and local storage LotCal uses, and how you control them.</p>
<div class="card">
  <div class="prose">
    <h2>1. What are cookies?</h2>
    <p>Cookies are small text files a website stores on your device. LotCal also uses browser <strong>local storage</strong> for the same purpose. They help the site remember your preferences and let third parties, with your consent, understand traffic and show ads.</p>

    <h2>2. Essential cookies / local storage</h2>
    <table>
      <thead><tr><th>Name</th><th>Purpose</th><th>Can you refuse?</th></tr></thead>
      <tbody>
        <tr><td><code>lotcal_cookie</code></td><td>Remembers your cookie consent choice</td><td>No — needed for the banner to work</td></tr>
        <tr><td><code>lotcal_disc</code></td><td>Remembers you&rsquo;ve dismissed the disclaimer notice</td><td>No — needed for the notice</td></tr>
      </tbody>
    </table>
    <p>These do not track you. They only store a yes/no preference on your own device.</p>

    <h2>3. Analytics cookies</h2>
    <p>If you accept them, we or a third-party analytics provider may set cookies to count visits and see which pages are popular. This helps us improve the site. They are set <strong>only with your consent</strong> via the cookie banner.</p>

    <h2>4. Advertising cookies</h2>
    <p>If you accept them, advertising networks such as Google AdSense may set cookies to show ads relevant to you, including Google&rsquo;s &ldquo;cookies for personalised ads&rdquo; mechanism. You can opt out at <a href="https://adssettings.google.com" rel="nofollow noopener" target="_blank">Google Ads Settings</a> or <a href="https://www.aboutads.info" rel="nofollow noopener" target="_blank">aboutads.info</a>.</p>

    <h2>5. Your consent</h2>
    <p>The cookie banner on every page asks you to <strong>Accept all</strong> or accept <strong>Only essential</strong>. If you choose &ldquo;Only essential&rdquo;, no analytics or advertising cookies are set. You can change your mind at any time by clearing the site&rsquo;s cookies in your browser settings and reloading — the banner will ask again. Your choice is stored in <code>lotcal_cookie</code>.</p>

    <h2>6. EU / UK visitors</h2>
    <p>For visitors in the European Union, the UK and Switzerland, consent-based cookies are set only after you actively accept them in the banner, in line with the GDPR and the ePrivacy Directive. Essential items are required for the site to function.</p>

    <h2>7. Managing cookies in your browser</h2>
    <p>You can also block or delete cookies through your browser settings. Doing so may reset your preferences and show the banner again.</p>

    <h2>8. Contact</h2>
    <p>Questions about cookies: <a href="mailto:node9555@gmail.com">node9555@gmail.com</a>.</p>
  </div>
</div>
"""
page('cookies.html', 'Cookie Policy — LotCal', 'Which cookies and local storage LotCal uses, what they do, and how to accept or reject them. Essential, analytics and advertising cookies explained.', 'LotCal Cookie Policy — essential, analytics and advertising cookies and your consent options.', cookies_body, 'cookies')

# ============ FAQ ============
faq_body = """
<p class="eyebrow">Help</p>
<h1>Frequently asked questions</h1>
<p class="lede">The questions people actually ask about the calculator.</p>
<div class="faq">
  <details><summary>Will my broker actually give me this leverage?</summary><div class="a"><p>Not necessarily. LotCal assumes your <em>entire</em> balance is available as initial margin, so the number it shows is the maximum your account could theoretically support. Real brokers cap leverage (e.g. 1:30 for retail forex in some regions, higher for crypto), apply tiers, and set their own margin requirements, spread and maintenance margin. Treat the result as an upper bound and check your broker&rsquo;s specification before relying on it.</p></div></details>
  <details><summary>Why isn&rsquo;t the price live?</summary><div class="a"><p>LotCal uses reference snapshot prices so the tool works without a live feed and without asking you to connect an account. Replace the price with your broker&rsquo;s current quote — the calculator only needs a number, and the exact price you&rsquo;d actually trade at. The P&amp;L per $1 move does not depend on the price at all: it comes straight from the contract size.</p></div></details>
  <details><summary>What does &ldquo;P&amp;L per $1 move&rdquo; mean?</summary><div class="a"><p>It&rsquo;s how much your position gains or loses for every $1 the price moves, based on the lot size and the pair&rsquo;s contract size. For gold (1 lot = 100 oz), 0.01 lot = 1 oz, so it&rsquo;s $1 per $1 move. For 0.001 lot it&rsquo;s $0.10. Green is the gain if price rises $1, red the loss if it falls $1.</p></div></details>
  <details><summary>What is a lot, and why does 1 lot of gold equal 100 oz?</summary><div class="a"><p>A lot is a standardised contract size. For metals, 1 standard lot is 100 troy oz (gold, platinum, palladium) or 5,000 oz (silver). For forex majors it&rsquo;s 100,000 units of the base currency. For crypto futures it&rsquo;s usually 1 coin (1 BTC, 1 ETH). The <a href="contract-size.html">Contract Size Guide</a> lists them all.</p></div></details>
  <details><summary>Is LotCal financial advice?</summary><div class="a"><p>No. LotCal is an educational calculator. It does not recommend any trade, instrument or leverage level, and it is not a broker, advisor or platform. Read the <a href="disclaimer.html">full disclaimer</a>.</p></div></details>
  <details><summary>Which pairs are supported?</summary><div class="a"><p>Gold (XAUUSD), silver (XAGUSD), platinum, palladium, Bitcoin, Ethereum, Solana, XRP, BNB, Dogecoin, Cardano, Litecoin, and the main forex pairs — EURUSD, GBPUSD, AUDUSD, NZDUSD, USDJPY, USDCHF, USDCAD.</p></div></details>
  <details><summary>Why is the price field disabled for USDJPY, USDCHF and USDCAD?</summary><div class="a"><p>For those pairs USD is the base currency, so position value in USD is simply lot &times; contract size — the price doesn&rsquo;t enter the calculation. So the field is disabled and the hint explains it.</p></div></details>
  <details><summary>How accurate is the leverage number?</summary><div class="a"><p>It&rsquo;s exact arithmetic for the values you enter, but it is a <em>theoretical</em> estimate: it assumes your entire balance is initial margin and ignores fees, spread, and broker margin tiers. It will not match a real broker&rsquo;s actual margin requirement exactly. Use it to understand the size of a position, not as a guaranteed quote.</p></div></details>
  <details><summary>Can I use it for spot trading?</summary><div class="a"><p>Yes, with a caveat. Spot trades don&rsquo;t use leverage the same way, but you can still enter your balance and size to see position value and quantity. The leverage figure is meaningful for margin and futures accounts.</p></div></details>
  <details><summary>Is there a mobile app?</summary><div class="a"><p>No — LotCal is a responsive website that works on any phone browser. It&rsquo;s deliberately small and fast.</p></div></details>
  <details><summary>How do I report a bug or suggest a pair?</summary><div class="a"><p>Email <a href="mailto:node9555@gmail.com">node9555@gmail.com</a>. Real messages get a real reply, usually within 24&ndash;48 hours on working days.</p></div></details>
</div>
"""
page('faq.html', 'FAQ — LotCal', 'Frequently asked questions about the LotCal leverage calculator: will the broker give this leverage, why prices aren\'t live, what P&L per $1 means, and which pairs are supported.', 'Common questions about LotCal, answered honestly.', faq_body, 'faq')

# ============ CONTRACT SIZE GUIDE ============
pairs = [
 ('XAUUSD','Gold',100,'oz',4121),('XAGUSD','Silver',5000,'oz',52.78),
 ('XPTUSD','Platinum',100,'oz',980),('XPDUSD','Palladium',100,'oz',1020),
 ('BTCUSD','Bitcoin',1,'BTC',76024),('ETHUSD','Ethereum',1,'ETH',2239.5),
 ('SOLUSD','Solana',1,'SOL',180),('XRPUSD','Ripple',1,'XRP',1.15),
 ('BNBUSD','BNB',1,'BNB',580),('DOGEUSD','Dogecoin',1,'DOGE',0.16),
 ('ADAUSD','Cardano',1,'ADA',0.55),('LTCUSD','Litecoin',1,'LTC',85),
 ('EURUSD','Euro',100000,'EUR',1.1232),('GBPUSD','Pound',100000,'GBP',1.3472),
 ('AUDUSD','Aussie',100000,'AUD',0.7011),('NZDUSD','Kiwi',100000,'NZD',0.5625),
 ('USDJPY','Yen',100000,'USD',158.25),('USDCHF','Franc',100000,'USD',0.8169),
 ('USDCAD','Canadian $',100000,'USD',1.3963),
]
rows = ''
for cid,name,contract,unit,price in pairs:
    pos = contract*price
    rows += '<tr><td><code>%s</code></td><td>%s</td><td>%s %s</td><td>$%s</td></tr>' % (cid,name,contract,unit,format(pos,',.2f'))
contract_body = """
<p class="eyebrow">Reference</p>
<h1>Contract Size Guide</h1>
<p class="lede">Standard contract sizes for every pair LotCal supports — 1 lot, what it is, and the position value at the reference price.</p>
<div class="card">
  <div class="prose">
    <p>Contract sizes below are <strong>common broker defaults</strong>. Your broker may differ — especially for metals and crypto futures — so always confirm before trading. Position value assumes the reference price shown on the calculator.</p>
    <table>
      <thead><tr><th>Pair</th><th>Market</th><th>1 lot =</th><th>Position value (1 lot)</th></tr></thead>
      <tbody>
""" + rows + """
      </tbody>
    </table>
    <h2>Quick rules of thumb</h2>
    <ul>
      <li><strong>Gold (XAUUSD):</strong> 1 lot = 100 oz. 0.01 lot = 1 oz, so P&amp;L is $1 per $1 move.</li>
      <li><strong>Silver (XAGUSD):</strong> 1 lot = 5,000 oz. 0.01 lot = 50 oz, so P&amp;L is $50 per $1 move.</li>
      <li><strong>Forex majors:</strong> 1 lot = 100,000 units of the base currency. 0.01 lot = 1,000 units.</li>
      <li><strong>Crypto:</strong> 1 lot = 1 coin. 0.01 lot = 0.01 BTC (or 0.01 ETH, 0.01 SOL, etc.).</li>
    </ul>
    <p>Use the <a href="index.html">calculator</a> with your balance to turn any of these into a leverage figure.</p>
  </div>
</div>
"""
page('contract-size.html', 'Contract Size Guide — LotCal', 'Standard contract sizes for gold, silver, bitcoin, forex and more — 1 lot equals what, and the position value per lot for every pair LotCal supports.', 'Contract sizes for every pair LotCal supports, plus quick rules of thumb.', contract_body, 'contract-size')

# ============ HOW IT WORKS ============
how_body = """
<p class="eyebrow">Methodology</p>
<h1>How It Works</h1>
<p class="lede">The exact formula, the assumptions behind it, and what LotCal deliberately does not do.</p>
<div class="card">
  <div class="prose">
    <h2>The formula</h2>
    <p><code>quantity = lot size &times; contract size</code><br>
    <code>position value = quantity &times; price</code> (for USD-quote pairs)<br>
    <code>position value = quantity</code> (for USD-base pairs — price not used)<br>
    <code>required leverage = position value &divide; account balance</code><br>
    <code>P&amp;L per $1 move = lot size &times; contract size</code> (USD-quote pairs)</p>
    <p>For USD-base pairs (USDJPY, USDCHF, USDCAD) the position value in USD is lot &times; contract size, so the price field is disabled and no P&amp;L per $1 is shown (a $1 move in JPY isn&rsquo;t a $1 move in USD).</p>

    <h2>Assumptions</h2>
    <ul>
      <li><strong>Contract sizes</strong> are common broker defaults: 1 lot gold/platinum/palladium = 100 oz, silver = 5,000 oz, forex = 100,000 units, crypto = 1 coin.</li>
      <li><strong>Margin:</strong> your entire balance is assumed available as initial margin. Real brokers reserve more (margin calls, maintenance margin), so the real requirement is higher.</li>
      <li><strong>Prices</strong> are reference snapshots (4&ndash;6 Nov 2026) and are not live — replace them with your broker&rsquo;s quote.</li>
      <li><strong>No fees</strong> — spread, commission, swap and funding are ignored.</li>
    </ul>

    <h2>Limits</h2>
    <ul>
      <li>It does not know your broker&rsquo;s margin tiers, leverage cap, spread or liquidation rules.</li>
      <li>It does not predict price, place trades or hold funds.</li>
      <li>Results are estimates for education, not a guarantee a broker will accept the order.</li>
      <li>It is not financial advice.</li>
    </ul>

    <h2>What it is not</h2>
    <p>LotCal is not a broker, dealer, investment advisor or trading platform, and is not regulated by any financial authority. See the <a href="disclaimer.html">Disclaimer</a>.</p>
  </div>
</div>
"""
page('how-it-works.html', 'How It Works — LotCal', 'The exact formula LotCal uses — quantity, position value, required leverage and P&L per $1 move — plus the assumptions and limits behind it.', 'The formula, assumptions and limits behind the LotCal calculator.', how_body, 'how-it-works')

# ============ 404 ============
nf_body = """
<div class="nf">
  <div class="code">404</div>
  <h1>Page not found</h1>
  <p>That page doesn&rsquo;t exist or was moved. The calculator is where you want to be.</p>
  <a class="btnline" href="index.html">Back to the calculator &rarr;</a>
</div>
"""
page('404.html', 'Page Not Found — LotCal', 'The page you requested could not be found on LotCal.', '404 — page not found.', nf_body, '404', narrow='')

# ============ BLOG INDEX ============
posts = [
 ('leverage-kya-hai','What Is Leverage in Trading? A Beginner\'s Guide','Leverage','Leverage lets you control more than you have — here\'s the plain-English explanation with a worked example.'),
 ('leverage-kaise-kam-karta-hai','How Leverage Actually Works: Margin, Liquidation, and What the Broker Lends','Leverage','The mechanics behind the number: margin, the broker\'s loan, and the point where a position gets closed.'),
 ('leverage-risk','The Real Risk of High Leverage: Why 1% Can Wipe You Out','Risk','A small adverse move at high leverage can take your whole margin. Here\'s the arithmetic that shows why.'),
 ('lot-size-kaise-samjhe','Lot Size Explained: Standard, Mini, and Micro Lots','Lots','Standard, mini and micro lots — what they are, what they control, and how to move between them.'),
 ('lot-size-position-value','Lot Size to Position Value: The Quick Math Every Trader Should Know','Lots','Turn any lot size into a position value in seconds, with examples for gold, forex and crypto.'),
 ('gold-contract-size','Gold Contract Size: What 1 Lot of XAUUSD Really Is','Contracts','1 lot of gold is 100 oz. Here\'s what that means for your P&L per $1 move, on every lot size.'),
 ('silver-contract-size','Silver Contract Size: XAGUSD Lots, Ounces, and Dollars','Contracts','Silver uses 5,000 oz per lot — bigger swings than gold. Here\'s the exact math.'),
 ('btc-contract-size','Bitcoin Futures Contract Size: 1 BTC, 0.001 BTC, and Everything Between','Contracts','Crypto futures are simple: 1 lot = 1 coin. What that means for position value and P&L.'),
 ('forex-contract-size','Forex Contract Sizes: EURUSD, GBPUSD, and the 100,000-Unit Standard','Contracts','Why a standard forex lot is 100,000 units, and how that maps to position value.'),
 ('margin-vs-leverage','Margin vs Leverage: What\'s the Difference?','Concepts','They get used interchangeably but they\'re not the same thing. Here\'s the clean distinction.'),
 ('risk-management-basics','Risk Management Basics: The 1–2% Rule and Stop Losses','Risk','Risk per trade, where to put the stop, and why position size — not win rate — keeps you alive.'),
 ('risk-management-strategies','Five Simple Risk Management Rules That Actually Work','Risk','Small, concrete rules you can apply today: fixed risk, max daily loss, and the two-loss pause.'),
 ('position-sizing','Position Sizing: How Much Should You Risk Per Trade?','Risk','The single most important number in trading. How to decide it, with a worked example.'),
 ('position-sizing-formula','Position Sizing Formulas: Fixed Fractional and Fixed Risk','Risk','The two common formulas, side by side, with the arithmetic for each.'),
 ('lot-size-mistakes','7 Lot Size Mistakes Beginners Make (and How to Avoid Them)','Lots','The common errors — wrong contract size, over-sized lots, ignoring pip value — and the fix for each.'),
]
cards = ''
for slug,title,cat,ex in posts:
    cards += '<a class="post" href="blog/%s.html"><span class="cat">%s</span><h3>%s</h3><p>%s</p><span class="read">Read &rarr;</span></a>\n    ' % (slug,cat,title,ex)
blog_body = """
<p class="eyebrow">Blog</p>
<h1>LotCal blog</h1>
<p class="lede">Original, plain-English writing on leverage, lot size, contract sizes and risk management.</p>
<div class="article-grid">
    """ + cards + """
</div>
<p style="margin-top:calc(24*var(--u));color:var(--mid);font-size:calc(14*var(--u))">Everything here is written from scratch for LotCal. No copy-paste, no &ldquo;5 secret strategies&rdquo; — just the arithmetic behind trading, explained clearly.</p>
"""
page('blog.html', 'Blog — LotCal', 'Original articles on leverage, lot size, contract size and risk management — written in plain English for people who trade futures.', 'The LotCal blog: leverage, lots, contract sizes and risk management, explained plainly.', blog_body, 'blog')

print('ALL PAGES DONE')
