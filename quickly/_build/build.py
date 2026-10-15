# Quickly 지원 사이트 생성기 — 틀 하나 + 언어별 문구(i18n/<언어>.py) → quickly/<언어>/{index,support,privacy}.html
# 영어는 quickly/ 바로 아래. 사용: python3 build.py   (이 폴더는 사이트에 올라가도 무해하다 — 링크되지 않는다)
# 같은 사이트의 영상 향상 앱 생성기(enhancevid/_build)를 옮겨 왔다. 그 앱 전용 그림(비교 슬라이더·프레임율)은 뺐다.
import html, importlib.util, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
LOCALES = [  # (폴더, html lang, 언어 이름)
    ("en", "en", "English"), ("ko", "ko", "한국어"), ("ja", "ja", "日本語"), ("zh-Hans", "zh-Hans", "简体中文"),
    ("zh-Hant", "zh-Hant", "繁體中文"), ("es-ES", "es", "Español"), ("de-DE", "de", "Deutsch"), ("fr-FR", "fr", "Français"),
    ("it", "it", "Italiano"), ("pt-BR", "pt-BR", "Português"), ("ru", "ru", "Русский"),
]
# App Store 주소. 아직 출시 전이라 None — 이때는 링크 대신 "App Store 출시 예정" 표시를 그린다.
# 출시 뒤 "https://apps.apple.com/app/id<번호>" 를 넣고 다시 실행하면 내려받기 단추로 바뀐다.
STORE = None
APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.37 12.64c-.02-2.2 1.8-3.26 1.88-3.31-1.02-1.5-2.61-1.7-3.18-1.72-1.35-.14-2.64.8-3.33.8-.69 0-1.74-.78-2.87-.76-1.47.02-2.83.86-3.59 2.18-1.53 2.66-.39 6.59 1.1 8.75.73 1.05 1.6 2.24 2.73 2.2 1.1-.04 1.51-.71 2.84-.71 1.32 0 1.7.71 2.86.69 1.18-.02 1.93-1.07 2.65-2.13.83-1.22 1.18-2.4 1.2-2.46-.03-.01-2.3-.88-2.33-3.5zM14.2 6.17c.6-.73 1.01-1.75.9-2.76-.87.04-1.92.58-2.54 1.31-.56.65-1.05 1.69-.92 2.68.97.08 1.96-.49 2.56-1.23z"/></svg>'
ICONS = [  # 기능 카드 그림(선 그림) — 순서는 문구 파일의 feats 와 같다
    # AI가 써 줌 — 반짝이
    '<path d="M12 3l1.8 4.2L18 9l-4.2 1.8L12 15l-1.8-4.2L6 9l4.2-1.8z"/><path d="M18 15l.9 2.1L21 18l-2.1.9L18 21l-.9-2.1L15 18l2.1-.9z"/>',
    # AI 고르기 — 셋 중 하나를 고른 목록
    '<circle cx="6" cy="7" r="2"/><circle cx="6" cy="12" r="2" fill="currentColor"/><circle cx="6" cy="17" r="2"/><path d="M11 7h9M11 12h9M11 17h9"/>',
    # 어느 앱에서든 키보드
    '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 15h10M7 9h.01M11 9h.01M15 9h.01M7 12h.01M11 12h.01M15 12h.01"/>',
    # 계산기 필요 없음
    '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 7h8M8 11h2M14 11h2M8 15h2M14 15h2"/>',
    # 다시 쓰고 찾기 — 목록과 돋보기
    '<path d="M4 7h16M4 12h10M4 17h7"/><circle cx="17" cy="16" r="3"/><path d="M19.2 18.2L21 20"/>',
    # iPhone·iPad 동기화 — 기기 둘
    '<rect x="2" y="6" width="9" height="13" rx="2"/><rect x="13" y="3" width="9" height="16" rx="2"/><path d="M6 16h1M17 16h1"/>',
]
SHOTS = ["ai", "keyboard", "amount", "privacy"]  # assets/<언어>/shot-<이름>.jpg — 문구 파일의 steps 와 같은 순서
e = html.escape

def load(loc):
    spec = importlib.util.spec_from_file_location(loc, os.path.join(HERE, "i18n", loc.replace("-", "_") + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.S

def store(I, logo=True):
    """App Store 단추. STORE 가 없으면(출시 전) 누를 수 없는 '출시 예정' 표시."""
    mark = APPLE if logo else ""
    if STORE:
        return f'<a class="store" href="{STORE}">{mark}{e(I["store"])}</a>'
    return f'<span class="store soon">{mark}{e(I["soon"])}</span>'

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
    <img class="appicon" src="{up}assets/icon.png" alt=""><div class="name">Quickly</div>
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
        for n, (b, s, alt) in zip(SHOTS, I["steps"]))
    return head(S, lang, I["title"], I["desc"], up) + '<div class="wrap wide">\n' + header(S, loc, "index.html", up) + f"""
  <section class="hero">
    <div>
      <h1>{I['h1']}</h1>
      <p class="lede">{e(I['lede'])}</p>
      {store(I)}
      <p class="fine">{e(I['fine'])}</p>
    </div>
    <div class="hero-shot"><div class="phone"><img src="{shot('ai')}" alt="{e(I['steps'][0][2])}"></div></div>
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
    <img src="{up}assets/icon.png" alt="Quickly">
    <h2>{e(I['cta'])}</h2>
    {store(I, logo=False)}
  </section>

  <footer>© 2026 Cream · <a href="support.html">{e(S['nav'][1])}</a> · <a href="privacy.html">{e(S['nav'][2])}</a> · {e(I['tm'])}</footer>
</div>
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
    <p><a class="btn" href="mailto:creamhelp@gmail.com?subject=Quickly%20Support">{e(P['contact_btn'])}</a></p>
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
