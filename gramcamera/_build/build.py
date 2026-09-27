# GramCamera 첫 페이지 생성기 — 틀 하나 + text.json(언어별 문구) → gramcamera/<언어>/index.html
# 지원·개인정보 페이지는 손으로 쓴 그대로 둔다(이 생성기는 index.html 만 쓴다).
# text.json 은 2026-09-27 에 기존 11개 언어 페이지 문구 + 스토어 스크린샷 자막(LeanCam/marketing/captions.json)을 모아 굳힌 것이다.
# 사용: python3 build.py   (이 폴더는 사이트에 올라가도 무해하다 — 링크되지 않는다)
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
LOCALES = [  # (폴더, html lang, 언어 이름)
    ("en", "en", "English"), ("ko", "ko", "한국어"), ("ja", "ja", "日本語"), ("zh-Hans", "zh-Hans", "简体中文"),
    ("zh-Hant", "zh-Hant", "繁體中文"), ("es-ES", "es", "Español"), ("de-DE", "de", "Deutsch"), ("fr-FR", "fr", "Français"),
    ("it", "it", "Italiano"), ("pt-BR", "pt-BR", "Português"), ("ru", "ru", "Русский"),
]
STORE = "https://apps.apple.com/app/id6804235227"
APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.37 12.64c-.02-2.2 1.8-3.26 1.88-3.31-1.02-1.5-2.61-1.7-3.18-1.72-1.35-.14-2.64.8-3.33.8-.69 0-1.74-.78-2.87-.76-1.47.02-2.83.86-3.59 2.18-1.53 2.66-.39 6.59 1.1 8.75.73 1.05 1.6 2.24 2.73 2.2 1.1-.04 1.51-.71 2.84-.71 1.32 0 1.7.71 2.86.69 1.18-.02 1.93-1.07 2.65-2.13.83-1.22 1.18-2.4 1.2-2.46-.03-.01-2.3-.88-2.33-3.5zM14.2 6.17c.6-.73 1.01-1.75.9-2.76-.87.04-1.92.58-2.54 1.31-.56.65-1.05 1.69-.92 2.68.97.08 1.96-.49 2.56-1.23z"/></svg>'
ICONS = [  # 기능 카드 그림 — text.json feats 0~3 순서(얼마나 아낄지 · 사진 앱 · 절약 표시 · 카메라 기능)
    '<path d="M4 7h10M18 7h2M4 17h2M10 17h10"/><circle cx="16" cy="7" r="2"/><circle cx="8" cy="17" r="2"/>',
    '<rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="2"/>',
    '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="4"/>',
]
SHOTS = ["presets", "album", "tuning", "recording"]  # text.json steps 순서. 절약 화면(scene3)은 옛 이름 'LeanCam' 배지가 찍혀 있어 뺐다.
e = html.escape


def pct(s):
    return int(re.search(r"\d+", s).group(0))


def page(T, loc, lang):
    langs = " ".join(
        f'<span class="cur">{name}</span>' if folder == loc else f'<a href="../{folder}/index.html">{name}</a>'
        for folder, _, name in LOCALES)
    shot = lambda n: f"../assets/{loc}/shot-{n}.jpg"
    rows = "\n".join(
        f"""      <div class="srow">
        <div class="shead"><b>{e(c['name'])}</b><span>{e(c['detail'])}</span><em>{e(c['pct'])}</em></div>
        <div class="sbar"><div class="sfill" style="--w:{100 - pct(c['pct'])}%"></div></div>
      </div>""" for c in T["stats"]["columns"])
    shots = "\n".join(
        f'      <figure><div class="phone"><img src="{shot(n)}" alt="{e(s["headline"])}" loading="lazy"></div><figcaption>{e(s["headline"])}<span>{e(s["sub"])}</span></figcaption></figure>'
        for n, s in zip(SHOTS, T["steps"]))
    feats = "\n".join(
        f'      <div class="feat"><div class="ic"><svg viewBox="0 0 24 24">{ICONS[i]}</svg></div><b>{e(b)}</b><p>{e(p)}</p></div>'
        for i, (b, p) in enumerate(T["feats"][:4]))
    pb, pp = T["feats"][4]
    nav = T["nav"]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(T['title'])}</title>
<meta name="description" content="{e(T['desc'])}">
<link rel="icon" href="../assets/icon.png">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<div class="wrap wide">
  <header class="site">
    <img class="appicon" src="../assets/icon.png" alt=""><div class="name">GramCamera</div>
    <nav><a href="index.html">{e(nav[0])}</a><a href="support.html">{e(nav[1])}</a><a href="privacy.html">{e(nav[2])}</a></nav>
  </header>
  <div class="langs">{langs}</div>

  <section class="hero">
    <div>
      <h1>{e(T['h1'])}</h1>
      <p class="lede">{e(T['lede'])}</p>
      <a class="store" href="{STORE}">{APPLE}{e(T['store'])}</a>
      <p class="fine">{e(T['fine'])}</p>
    </div>
    <div class="hero-shot"><div class="phone"><img src="{shot('camera')}" alt="{e(T['hero_alt'])}"></div></div>
  </section>

  <section class="block">
    <span class="kicker">{e(T['stats']['footer'])}</span>
    <h2>{e(T['h_save'])}</h2>
    <div class="save">
{rows}
    </div>
  </section>

  <section class="block">
    <span class="kicker">{e(T['k_how'])}</span>
    <h2>{e(T['h_how'])}</h2>
    <div class="shots">
{shots}
    </div>
  </section>

  <section class="block">
    <span class="kicker">{e(T['k_more'])}</span>
    <h2>{e(T['h_more'])}</h2>
    <div class="grid two">
{feats}
    </div>
  </section>

  <section class="block">
    <div class="privacy-band">
      <div class="ic"><svg viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg></div>
      <div><b>{e(pb)}</b><p>{e(pp)} — <a href="privacy.html">{e(nav[2])}</a></p></div>
    </div>
  </section>

  <section class="cta">
    <img src="../assets/icon.png" alt="GramCamera">
    <h2>{e(T['cta'])}</h2>
    <a class="store" href="{STORE}">{APPLE}{e(T['store'])}</a>
  </section>

  <footer>© 2026 Cream · <a href="support.html">{e(nav[1])}</a> · <a href="privacy.html">{e(nav[2])}</a></footer>
</div>
</body>
</html>
"""


def main():
    text = json.load(open(os.path.join(HERE, "text.json"), encoding="utf-8"))
    for folder, lang, _ in LOCALES:
        out = os.path.join(SITE, folder, "index.html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(page(text[folder], folder, lang))
        print("wrote", os.path.relpath(out, SITE))


if __name__ == "__main__":
    main()
