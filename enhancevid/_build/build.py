# EnhanceVid 지원 사이트 생성기 — 틀 하나 + 언어별 문구(i18n/<언어>.py) → enhancevid/<언어>/{index,support,privacy}.html
# 영어는 enhancevid/ 바로 아래. 사용: python3 build.py   (이 폴더는 사이트에 올라가도 무해하다 — 링크되지 않는다)
import html, importlib.util, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
LOCALES = [  # (폴더, html lang, 언어 이름)
    ("en", "en", "English"), ("ko", "ko", "한국어"), ("ja", "ja", "日本語"), ("zh-Hans", "zh-Hans", "简体中文"),
    ("zh-Hant", "zh-Hant", "繁體中文"), ("es-ES", "es", "Español"), ("de-DE", "de", "Deutsch"), ("fr-FR", "fr", "Français"),
    ("it", "it", "Italiano"), ("pt-BR", "pt-BR", "Português"), ("ru", "ru", "Русский"),
]
STORE = "https://apps.apple.com/app/id6816116747"
APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.37 12.64c-.02-2.2 1.8-3.26 1.88-3.31-1.02-1.5-2.61-1.7-3.18-1.72-1.35-.14-2.64.8-3.33.8-.69 0-1.74-.78-2.87-.76-1.47.02-2.83.86-3.59 2.18-1.53 2.66-.39 6.59 1.1 8.75.73 1.05 1.6 2.24 2.73 2.2 1.1-.04 1.51-.71 2.84-.71 1.32 0 1.7.71 2.86.69 1.18-.02 1.93-1.07 2.65-2.13.83-1.22 1.18-2.4 1.2-2.46-.03-.01-2.3-.88-2.33-3.5zM14.2 6.17c.6-.73 1.01-1.75.9-2.76-.87.04-1.92.58-2.54 1.31-.56.65-1.05 1.69-.92 2.68.97.08 1.96-.49 2.56-1.23z"/></svg>'
ICONS = [  # 기능 카드 그림(선 그림) — 순서는 문구 파일의 feats 와 같다
    '<path d="M12 3v2M12 19v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M3 12h2M19 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/><circle cx="12" cy="12" r="4"/>',
    '<path d="M7 4v16M7 4l-3 3M7 4l3 3M17 20V4M17 20l-3-3M17 20l3-3"/>',
    '<rect x="3" y="4" width="8" height="16" rx="2"/><rect x="13" y="4" width="8" height="16" rx="2"/>',
    '<circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor"/>',
    '<path d="M4 4h10l6 6v10H4z"/><path d="M14 4v6h6"/>',
    '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
]
e = html.escape

def load(loc):
    spec = importlib.util.spec_from_file_location(loc, os.path.join(HERE, "i18n", loc.replace("-", "_") + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.S

def head(S, lang, title, desc, up):
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="{up}assets/icon.png">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
"""

def header(S, loc, page, up):
    langs = []
    for folder, _, name in LOCALES:
        if folder == loc:
            langs.append(f'<span class="cur">{name}</span>')
        else:
            path = (up + ("" if folder == "en" else folder + "/")) + page
            langs.append(f'<a href="{path}">{name}</a>')
    return f"""  <header class="site">
    <img class="appicon" src="{up}assets/icon.png" alt=""><div class="name">EnhanceVid</div>
    <nav><a href="index.html">{e(S['nav'][0])}</a><a href="support.html">{e(S['nav'][1])}</a><a href="privacy.html">{e(S['nav'][2])}</a></nav>
  </header>
  <div class="langs">{' '.join(langs)}</div>
"""

def index(S, loc, lang, up):
    shot = lambda n: f"{up}assets/{loc}/shot-{n}.jpg"
    I = S["index"]
    feats = "\n".join(
        f'      <div class="feat"><div class="ic"><svg viewBox="0 0 24 24">{ICONS[i]}</svg></div><b>{e(b)}</b><p>{e(p)}</p></div>'
        for i, (b, p) in enumerate(I["feats"]))
    shots = "\n".join(
        f'      <figure><div class="phone"><img src="{shot(n)}" alt="{e(alt)}" loading="lazy"></div><figcaption>{e(b)}<span>{e(s)}</span></figcaption></figure>'
        for n, (b, s, alt) in zip(["select", "progress", "info", "done"], I["steps"]))
    frames = "\n".join(
        f'      <div class="frame{" new" if i == 1 else ""}"><div class="pane"><div class="dot" style="left:{x}%"></div></div><b>{e(b)}</b><span>{e(s)}</span></div>'
        for i, ((b, s), x) in enumerate(zip(I["frames"], [18, 44, 70])))
    return head(S, lang, I["title"], I["desc"], up) + '<div class="wrap wide">\n' + header(S, loc, "index.html", up) + f"""
  <section class="hero">
    <div>
      <h1>{I['h1']}</h1>
      <p class="lede">{e(I['lede'])}</p>
      <a class="store" href="{STORE}">{APPLE}{e(I['store'])}</a>
      <p class="fine">{e(I['fine'])}</p>
    </div>
    <div class="hero-shot"><div class="phone"><img src="{shot('select')}" alt="{e(I['steps'][0][2])}"></div></div>
  </section>

  <section class="block">
    <span class="kicker">{e(I['k1'])}</span>
    <h2>{e(I['h1_2'])}</h2>
    <p>{e(I['p1'])}</p>
    <div class="compare" id="compare" style="--pos:50%">
      <img src="{up}assets/after.jpg" alt="{e(I['alt_after'])}">
      <img class="before" src="{up}assets/before.jpg" alt="{e(I['alt_before'])}">
      <span class="tag l">{e(I['tags'][0])}</span><span class="tag r">{e(I['tags'][1])}</span>
      <div class="line"></div><div class="knob">⇆</div>
      <input type="range" min="0" max="100" value="50" aria-label="{e(I['aria'])}">
    </div>
    <p class="caption-note">{e(I['note1'])}</p>
  </section>

  <section class="block">
    <span class="kicker">{e(I['k2'])}</span>
    <h2>{e(I['h2_2'])}</h2>
    <p>{e(I['p2'])}</p>
    <div class="fps">
      <div class="track low"><span class="label">30fps</span><div class="ball"></div></div>
      <div class="track up"><span class="label">60fps</span><div class="ball"></div></div>
    </div>
    <div class="frames" aria-hidden="true">
{frames}
    </div>
    <p class="caption-note">{e(I['note2'])}</p>
  </section>

  <section class="block">
    <span class="kicker">{e(I['k3'])}</span>
    <h2>{e(I['h2_3'])}</h2>
    <div class="shots">
{shots}
    </div>
  </section>

  <section class="block">
    <span class="kicker">{e(I['k4'])}</span>
    <h2>{e(I['h2_4'])}</h2>
    <div class="grid">
{feats}
    </div>
  </section>

  <section class="block">
    <div class="privacy-band">
      <div class="ic"><svg viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg></div>
      <div><b>{e(I['priv_b'])}</b><p>{e(I['priv_p'])} <a href="privacy.html">{e(S['nav'][2])}</a></p></div>
    </div>
  </section>

  <section class="cta">
    <img src="{up}assets/icon.png" alt="EnhanceVid">
    <h2>{e(I['cta'])}</h2>
    <a class="store" href="{STORE}">{e(I['store'])}</a>
  </section>

  <footer>© 2026 Cream · <a href="support.html">{e(S['nav'][1])}</a> · <a href="privacy.html">{e(S['nav'][2])}</a> · {e(I['photo'])}</footer>
</div>
<script>
(function () {{
  var box = document.getElementById('compare'); if (!box) return;
  var input = box.querySelector('input'), auto = true, t0 = null;
  function set(v) {{ box.style.setProperty('--pos', v + '%'); input.value = v; }}
  input.addEventListener('input', function () {{ auto = false; set(input.value); }});
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  function tick(ts) {{ if (!auto) return; if (t0 === null) t0 = ts; set(50 + 30 * Math.sin((ts - t0) / 1400)); requestAnimationFrame(tick); }}
  requestAnimationFrame(tick);
}})();
</script>
</body>
</html>
"""

def support(S, loc, lang, up):
    P = S["support"]
    body = []
    for h2, qa in P["sections"]:
        body.append(f"  <h2>{e(h2)}</h2>")
        for q, a in qa:
            body.append(f'  <details class="card"><summary>{e(q)}</summary>\n    <p>{a}</p>\n  </details>')
    return head(S, lang, P["title"], P["lede"], up) + '<div class="wrap">\n' + header(S, loc, "support.html", up) + f"""
  <h1>{e(P['h1'])}</h1>
  <p class="lede">{e(P['lede'])}</p>

""" + "\n".join(body) + f"""

  <h2>{e(P['contact_h'])}</h2>
  <div class="card">
    <p>{e(P['contact_p'])}</p>
    <p><a class="btn" href="mailto:creamhelp@gmail.com?subject=EnhanceVid%20Support">{e(P['contact_btn'])}</a></p>
  </div>

  <h2>{e(P['req_h'])}</h2>
  <p>{e(P['req_p'])}</p>

  <footer>© 2026 Cream · <a href="privacy.html">{e(S['nav'][2])}</a></footer>
</div>
</body>
</html>
"""

def privacy(S, loc, lang, up):
    P = S["privacy"]
    body = "\n\n".join(f"  <h2>{e(h)}</h2>\n  <p>{p}</p>" for h, p in P["sections"])
    return head(S, lang, P["title"], P["summary"], up) + '<div class="wrap">\n' + header(S, loc, "privacy.html", up) + f"""
  <h1>{e(P['h1'])}</h1>
  <p class="lede">{e(P['effective'])}</p>

  <div class="card"><p><b>{e(P['summary_b'])}</b> {e(P['summary'])}</p></div>

{body}

  <footer>© 2026 Cream · <a href="support.html">{e(S['nav'][1])}</a></footer>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    made = 0
    for folder, lang, _ in LOCALES:
        S = load(folder)
        out = SITE if folder == "en" else os.path.join(SITE, folder)
        up = "" if folder == "en" else "../"
        os.makedirs(out, exist_ok=True)
        for name, fn in (("index.html", index), ("support.html", support), ("privacy.html", privacy)):
            open(os.path.join(out, name), "w", encoding="utf-8").write(fn(S, folder, lang, up)); made += 1
    print("만든 페이지", made)
