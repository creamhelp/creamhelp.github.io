# LeanVid 첫 페이지 생성기 — 틀 하나 + text.json(언어별 문구) → leanvid/index.html(영어) · leanvid/en/ · leanvid/<언어>/index.html
# 지원·개인정보 페이지는 손으로 쓴 그대로 둔다(이 생성기는 index.html 만 쓴다).
# text.json 은 2026-09-27 에 기존 11개 언어 페이지 문구 + LeanVid 스토어 스크린샷 자막 + 메인 페이지 실측 문구를 모아 굳힌 것이다.
# 그림: assets/<언어>/screen-cover.jpg(스토어 스크린샷 4번에서 화면만 잘라 냄) · shot-*.jpg(스토어 스크린샷 그대로).
# 사용: python3 build.py
import html, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
LOCALES = [  # (폴더, html lang, 언어 이름)
    ("en", "en", "English"), ("ko", "ko", "한국어"), ("ja", "ja", "日本語"), ("zh-Hans", "zh-Hans", "简体中文"),
    ("zh-Hant", "zh-Hant", "繁體中文"), ("es-ES", "es", "Español"), ("de-DE", "de", "Deutsch"), ("fr-FR", "fr", "Français"),
    ("it", "it", "Italiano"), ("pt-BR", "pt-BR", "Português"), ("ru", "ru", "Русский"),
]
STORE = "https://apps.apple.com/app/id6796710561"
APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.37 12.64c-.02-2.2 1.8-3.26 1.88-3.31-1.02-1.5-2.61-1.7-3.18-1.72-1.35-.14-2.64.8-3.33.8-.69 0-1.74-.78-2.87-.76-1.47.02-2.83.86-3.59 2.18-1.53 2.66-.39 6.59 1.1 8.75.73 1.05 1.6 2.24 2.73 2.2 1.1-.04 1.51-.71 2.84-.71 1.32 0 1.7.71 2.86.69 1.18-.02 1.93-1.07 2.65-2.13.83-1.22 1.18-2.4 1.2-2.46-.03-.01-2.3-.88-2.33-3.5zM14.2 6.17c.6-.73 1.01-1.75.9-2.76-.87.04-1.92.58-2.54 1.31-.56.65-1.05 1.69-.92 2.68.97.08 1.96-.49 2.56-1.23z"/></svg>'
ICONS = [  # 기능 카드 그림 — text.json feats 0~3(화질 보존 · 검증된 교체 · 눈으로 비교 · 파일 앱·형식)
    '<path d="M4 7h16M4 12h10M4 17h6"/><path d="M17 14l3 3-3 3"/>',
    '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    '<rect x="3" y="4" width="8" height="16" rx="2"/><rect x="13" y="4" width="8" height="16" rx="2"/>',
    '<path d="M4 4h10l6 6v10H4z"/><path d="M14 4v6h6"/>',
]
CLOCK = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
LOCK = '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>'
SHOTS = ["cover", "picker", "progress", "celebration", "compare", "report", "spec", "history"]  # text.json shots 순서
e = html.escape


def page(T, loc, lang, root):
    """root: 영어 정본(leanvid/index.html)이면 True — 경로에 ../ 가 없다."""
    up = "" if root else "../"
    def lang_href(folder):
        if folder == "en":
            return f"{up}index.html"
        return f"{folder}/index.html" if root else f"../{folder}/index.html"
    langs = " ".join(
        f'<span class="cur">{name}</span>' if folder == loc else f'<a href="{lang_href(folder)}">{name}</a>'
        for folder, _, name in LOCALES)
    a = lambda n: f"{up}assets/{loc}/{n}.jpg"
    shots = "\n".join(
        f'      <img src="{a("shot-" + n)}" alt="{e(s["headline"])}" loading="lazy">'
        for n, s in zip(SHOTS, T["shots"]))
    feats = "\n".join(
        f'      <div class="feat"><div class="ic"><svg viewBox="0 0 24 24">{ICONS[i]}</svg></div><b>{e(b)}</b><p>{e(p)}</p></div>'
        for i, (b, p) in enumerate(T["feats"][:4]))
    wb, wp = T["feats"][4]
    pb, pp = T["feats"][5]
    nav = T["nav"]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(T['title'])}</title>
<meta name="description" content="{e(T['desc'])}">
<link rel="icon" href="{up}assets/icon.png">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<div class="wrap wide">
  <header class="site">
    <img class="appicon" src="{up}assets/icon.png" alt=""><div class="name">LeanVid</div>
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
    <div class="hero-shot"><div class="phone"><img src="{a('screen-cover')}" alt="{e(T['shots'][3]['headline'])}"></div></div>
  </section>

  <section class="block">
    <span class="kicker">{e(T['k_save'])}</span>
    <h2>{e(T['h_save'])}</h2>
    <div class="save">
      <div class="srow"><div class="shead"><b>{e(T['original'])}</b><span>3:34</span><em class="plain">1.24 GB</em></div>
        <div class="sbar"><div class="sfill before" style="--w:100%"></div></div></div>
      <div class="srow"><div class="shead"><b>LeanVid</b><span>3:34</span><em>99.4 MB</em></div>
        <div class="sbar"><div class="sfill" style="--w:8%"></div></div></div>
      <div class="big">{e(T['lv_big'])}</div>
      <p class="caption-note">{e(T['lv_note'])}</p>
    </div>
  </section>

  <section class="block">
    <span class="kicker">{e(T['k_how'])}</span>
    <h2>{e(T['h_how'])}</h2>
    <div class="gallery">
{shots}
    </div>
  </section>

  <section class="block">
    <span class="kicker">{e(T['k_more'])}</span>
    <h2>{e(T['h_more'])}</h2>
    <div class="grid two">
{feats}
    </div>
    <div class="privacy-band soft">
      <div class="ic"><svg viewBox="0 0 24 24">{CLOCK}</svg></div>
      <div><b>{e(wb)}</b><p>{e(wp)}</p></div>
    </div>
  </section>

  <section class="block">
    <div class="privacy-band">
      <div class="ic"><svg viewBox="0 0 24 24">{LOCK}</svg></div>
      <div><b>{e(pb)}</b><p>{e(pp)} — <a href="privacy.html">{e(nav[2])}</a></p></div>
    </div>
  </section>

  <section class="cta">
    <img src="{up}assets/icon.png" alt="LeanVid">
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
    outs = [("en", "en", True, os.path.join(SITE, "index.html"))]
    outs += [(folder, lang, False, os.path.join(SITE, folder, "index.html")) for folder, lang, _ in LOCALES]
    for folder, lang, root, out in outs:
        with open(out, "w", encoding="utf-8") as f:
            f.write(page(text[folder], folder, lang, root))
        print("wrote", os.path.relpath(out, SITE))


if __name__ == "__main__":
    main()
