#!/usr/bin/env python3
"""Cream 루트 소개 페이지 생성기.

출력: ../index.html(영어, 정본) + ../<locale>/index.html(10개 번역) + ../en/index.html(루트로 리디렉션).
로케일·언어 표기·링크 규약은 leanvid/, gramcamera/ 와 같다. `_` 접두 디렉터리라 GitHub Pages(Jekyll)가 서빙하지 않는다.

실행: python3 _cream/generate.py   (저장소 루트에서)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BASE = "https://creamhelp.github.io/"

# (디렉터리, html lang, hreflang, 자기표기)
LOCALES = [
    ("", "en", "en", "English"),
    ("ko", "ko", "ko", "한국어"),
    ("ja", "ja", "ja", "日本語"),
    ("zh-Hans", "zh-Hans", "zh-Hans", "简体中文"),
    ("zh-Hant", "zh-Hant", "zh-Hant", "繁體中文"),
    ("es-ES", "es", "es", "Español"),
    ("de-DE", "de", "de", "Deutsch"),
    ("fr-FR", "fr", "fr", "Français"),
    ("it", "it", "it", "Italiano"),
    ("pt-BR", "pt-BR", "pt", "Português"),
    ("ru", "ru", "ru", "Русский"),
]

T = {
"": dict(
    title="Cream — Small apps that save space",
    desc="Cream makes small iOS apps that save storage: LeanVid compresses videos without visible quality loss, GramCamera shoots smaller photos and videos from the start.",
    h1="Small apps that save space.",
    lede="Cream builds small, focused iOS apps around one idea: keep your photos and videos, use less storage. Nothing is uploaded — everything runs on your device.",
    lv_tag="Shrink videos, keep the quality.",
    lv_desc="Compresses videos from your photo library and the Files app by lowering only the bitrate. Resolution, frame rate, color and HDR stay intact, and every result is verified before it replaces the original. Files your iPhone can't play (MKV, WebM, AVI, VP9, AV1) are converted by the built-in converter.",
    gc_tag="Same shot, smaller file.",
    gc_desc="A camera that shoots the same way your stock camera does but saves smaller photos and videos. Choose Saver, Standard or Max, keep shooting straight into the Photos app, and see how much space you saved on every capture.",
    formerly="(formerly LeanCam)", website="Website", support="Support", privacy="Privacy", contact="Contact",
),
"ko": dict(
    title="Cream — 용량을 아끼는 작은 앱들",
    desc="Cream은 저장 공간을 아끼는 작은 iOS 앱을 만듭니다. LeanVid는 눈에 띄는 화질 저하 없이 동영상을 압축하고, GramCamera는 처음부터 더 작은 사진과 동영상을 찍습니다.",
    h1="용량을 아끼는 작은 앱들.",
    lede="Cream은 한 가지 생각으로 작은 iOS 앱을 만듭니다. 사진과 동영상은 그대로 두고, 저장 공간은 덜 쓰기. 어떤 것도 업로드하지 않고 모두 기기 안에서 처리합니다.",
    lv_tag="화질은 그대로, 용량만 줄이세요.",
    lv_desc="사진 보관함과 파일 앱의 동영상을 비트레이트만 낮춰 압축합니다. 해상도·프레임레이트·색·HDR은 그대로이고, 모든 결과는 원본을 교체하기 전에 검증합니다. iPhone이 재생하지 못하는 파일(MKV, WebM, AVI, VP9, AV1)도 내장 변환기로 바꿉니다.",
    gc_tag="같은 장면, 더 작은 파일.",
    gc_desc="기본 카메라와 같은 방식으로 찍되, 저장할 때 용량을 아끼는 카메라입니다. 절약·표준·최대 중에서 고르고, 사진과 동영상은 그대로 기본 사진 앱에 저장되며, 매 촬영마다 얼마나 아꼈는지 확인할 수 있습니다.",
    formerly="(구 LeanCam)", website="웹사이트", support="지원", privacy="개인정보", contact="문의",
),
"ja": dict(
    title="Cream — 容量を節約する小さなアプリ",
    desc="Cream はストレージを節約する小さな iOS アプリを作っています。LeanVid は目に見える画質低下なしに動画を圧縮し、GramCamera は最初から小さな写真と動画を撮影します。",
    h1="容量を節約する、小さなアプリ。",
    lede="Cream はひとつの考えで小さな iOS アプリを作っています。写真と動画はそのままに、使うストレージは少なく。何もアップロードせず、すべて端末の中で処理します。",
    lv_tag="画質はそのままに、容量だけ小さく。",
    lv_desc="写真ライブラリとファイルアプリの動画を、ビットレートだけ下げて圧縮します。解像度・フレームレート・色・HDR はそのままで、すべての結果は元の動画を置き換える前に検証されます。iPhone で再生できないファイル(MKV、WebM、AVI、VP9、AV1)も内蔵コンバーターで変換します。",
    gc_tag="同じ一枚を、もっと軽く。",
    gc_desc="標準カメラと同じように撮りながら、保存するときの容量を抑えるカメラです。節約・標準・最大から選び、写真と動画はそのまま標準の写真アプリに保存され、一枚ごとにどれだけ節約できたかを確認できます。",
    formerly="(旧 LeanCam)", website="ウェブサイト", support="サポート", privacy="プライバシー", contact="お問い合わせ",
),
"zh-Hans": dict(
    title="Cream — 节省空间的小应用",
    desc="Cream 开发节省存储空间的小型 iOS 应用:LeanVid 在没有明显画质损失的前提下压缩视频,GramCamera 从拍摄开始就生成更小的照片和视频。",
    h1="节省空间的小应用。",
    lede="Cream 围绕一个想法开发小而专注的 iOS 应用:照片和视频照常保留,占用的空间更少。不上传任何内容,一切都在你的设备上完成。",
    lv_tag="压缩视频,保留画质。",
    lv_desc="只降低比特率来压缩照片图库和“文件”应用中的视频。分辨率、帧率、色彩和 HDR 保持不变,每个结果在替换原片之前都会经过验证。iPhone 无法播放的文件(MKV、WebM、AVI、VP9、AV1)也可由内置转换器转换。",
    gc_tag="同样的画面,更小的文件。",
    gc_desc="以与系统相机相同的方式拍摄、但保存时更省容量的相机。在省容量、标准、最高之间选择,照片和视频照常存入系统“照片”应用,每次拍摄都能看到节省了多少。",
    formerly="(原 LeanCam)", website="网站", support="支持", privacy="隐私", contact="联系我们",
),
"zh-Hant": dict(
    title="Cream — 節省空間的小應用程式",
    desc="Cream 開發節省儲存空間的小型 iOS 應用程式:LeanVid 在沒有明顯畫質損失的前提下壓縮影片,GramCamera 從拍攝開始就產生更小的照片和影片。",
    h1="節省空間的小應用程式。",
    lede="Cream 圍繞一個想法開發小而專注的 iOS 應用程式:照片和影片照常保留,佔用的空間更少。不上傳任何內容,一切都在你的裝置上完成。",
    lv_tag="縮小影片,畫質不變。",
    lv_desc="只降低位元率來壓縮照片圖庫和「檔案」App 中的影片。解析度、影格率、色彩和 HDR 保持不變,每個結果在取代原始檔之前都會經過驗證。iPhone 無法播放的檔案(MKV、WebM、AVI、VP9、AV1)也可由內建轉換器轉換。",
    gc_tag="同樣的畫面,更小的檔案。",
    gc_desc="以與系統相機相同的方式拍攝、但儲存時更省容量的相機。在省容量、標準、最高之間選擇,照片和影片照常存入系統「照片」App,每次拍攝都能看到節省了多少。",
    formerly="(原 LeanCam)", website="網站", support="支援", privacy="隱私", contact="聯絡我們",
),
"es-ES": dict(
    title="Cream — Apps pequeñas que ahorran espacio",
    desc="Cream crea pequeñas apps para iOS que ahorran almacenamiento: LeanVid comprime vídeos sin pérdida visible de calidad y GramCamera captura fotos y vídeos más pequeños desde el principio.",
    h1="Apps pequeñas que ahorran espacio.",
    lede="Cream crea apps para iOS pequeñas y centradas en una sola idea: conserva tus fotos y vídeos usando menos almacenamiento. No se sube nada; todo se procesa en tu dispositivo.",
    lv_tag="Reduce tus vídeos sin perder calidad.",
    lv_desc="Comprime los vídeos de tu fototeca y de la app Archivos bajando solo la tasa de bits. La resolución, la frecuencia de fotogramas, el color y el HDR se mantienen intactos, y cada resultado se verifica antes de sustituir el original. Los archivos que tu iPhone no puede reproducir (MKV, WebM, AVI, VP9, AV1) se convierten con el conversor integrado.",
    gc_tag="La misma escena, un archivo menor.",
    gc_desc="Una cámara que captura igual que la cámara del sistema pero guarda fotos y vídeos más pequeños. Elige Ahorro, Estándar o Máximo, sigue disparando directamente a la app Fotos y comprueba cuánto espacio has ahorrado en cada captura.",
    formerly="(antes LeanCam)", website="Sitio web", support="Soporte", privacy="Privacidad", contact="Contacto",
),
"de-DE": dict(
    title="Cream — Kleine Apps, die Speicherplatz sparen",
    desc="Cream entwickelt kleine iOS-Apps, die Speicherplatz sparen: LeanVid verkleinert Videos ohne sichtbaren Qualitätsverlust, GramCamera nimmt Fotos und Videos von Anfang an kleiner auf.",
    h1="Kleine Apps, die Speicherplatz sparen.",
    lede="Cream baut kleine, fokussierte iOS-Apps rund um eine Idee: Fotos und Videos behalten, weniger Speicher verbrauchen. Nichts wird hochgeladen – alles läuft auf deinem Gerät.",
    lv_tag="Videos verkleinern, Qualität behalten.",
    lv_desc="Komprimiert Videos aus deiner Fotomediathek und der Dateien-App, indem nur die Bitrate gesenkt wird. Auflösung, Bildrate, Farbe und HDR bleiben erhalten, und jedes Ergebnis wird geprüft, bevor es das Original ersetzt. Dateien, die dein iPhone nicht abspielen kann (MKV, WebM, AVI, VP9, AV1), wandelt der eingebaute Konverter um.",
    gc_tag="Gleiches Motiv, kleinere Datei.",
    gc_desc="Eine Kamera, die genauso fotografiert wie die System-Kamera, aber kleinere Fotos und Videos speichert. Wähle Sparsam, Standard oder Maximum, fotografiere weiter direkt in die Fotos-App und sieh bei jeder Aufnahme, wie viel Platz du gespart hast.",
    formerly="(ehemals LeanCam)", website="Website", support="Support", privacy="Datenschutz", contact="Kontakt",
),
"fr-FR": dict(
    title="Cream — De petites apps qui économisent de l'espace",
    desc="Cream crée de petites apps iOS qui économisent du stockage : LeanVid compresse les vidéos sans perte visible de qualité, GramCamera enregistre des photos et vidéos plus légères dès la prise de vue.",
    h1="De petites apps qui économisent de l'espace.",
    lede="Cream conçoit de petites apps iOS centrées sur une seule idée : garder vos photos et vidéos en utilisant moins de stockage. Rien n'est envoyé en ligne, tout se fait sur votre appareil.",
    lv_tag="Réduisez vos vidéos, gardez la qualité.",
    lv_desc="Compresse les vidéos de votre photothèque et de l'app Fichiers en ne réduisant que le débit. Résolution, cadence, couleurs et HDR restent intacts, et chaque résultat est vérifié avant de remplacer l'original. Les fichiers que votre iPhone ne peut pas lire (MKV, WebM, AVI, VP9, AV1) sont convertis par le convertisseur intégré.",
    gc_tag="Même scène, fichier plus léger.",
    gc_desc="Un appareil photo qui prend vos photos comme l'appareil d'origine, mais enregistre des photos et vidéos plus légères. Choisissez Économe, Standard ou Maximum, continuez à photographier directement dans l'app Photos et voyez à chaque prise combien d'espace vous avez gagné.",
    formerly="(anciennement LeanCam)", website="Site web", support="Assistance", privacy="Confidentialité", contact="Contact",
),
"it": dict(
    title="Cream — Piccole app che fanno risparmiare spazio",
    desc="Cream crea piccole app per iOS che fanno risparmiare spazio: LeanVid comprime i video senza perdita visibile di qualità, GramCamera scatta foto e video più leggeri fin dall'inizio.",
    h1="Piccole app che fanno risparmiare spazio.",
    lede="Cream realizza app per iOS piccole e mirate, attorno a un'unica idea: tenere foto e video usando meno spazio. Nulla viene caricato online, tutto avviene sul tuo dispositivo.",
    lv_tag="Riduci i video, mantieni la qualità.",
    lv_desc="Comprime i video della libreria foto e dell'app File abbassando solo il bitrate. Risoluzione, frequenza dei fotogrammi, colore e HDR restano intatti, e ogni risultato viene verificato prima di sostituire l'originale. I file che il tuo iPhone non riproduce (MKV, WebM, AVI, VP9, AV1) vengono convertiti dal convertitore integrato.",
    gc_tag="Stessa scena, file più piccolo.",
    gc_desc="Una fotocamera che scatta come quella di sistema, ma salva foto e video più leggeri. Scegli Risparmio, Standard o Massimo, continua a scattare direttamente nell'app Foto e vedi a ogni scatto quanto spazio hai risparmiato.",
    formerly="(in precedenza LeanCam)", website="Sito web", support="Assistenza", privacy="Privacy", contact="Contatti",
),
"pt-BR": dict(
    title="Cream — Apps pequenos que economizam espaço",
    desc="A Cream cria apps pequenos para iOS que economizam armazenamento: o LeanVid comprime vídeos sem perda visível de qualidade e o GramCamera captura fotos e vídeos menores desde o início.",
    h1="Apps pequenos que economizam espaço.",
    lede="A Cream cria apps para iOS pequenos e focados em uma só ideia: manter suas fotos e vídeos usando menos armazenamento. Nada é enviado para a internet; tudo acontece no seu aparelho.",
    lv_tag="Reduza seus vídeos, mantenha a qualidade.",
    lv_desc="Comprime os vídeos da sua fototeca e do app Arquivos reduzindo apenas a taxa de bits. Resolução, taxa de quadros, cor e HDR permanecem intactos, e cada resultado é verificado antes de substituir o original. Arquivos que o seu iPhone não reproduz (MKV, WebM, AVI, VP9, AV1) são convertidos pelo conversor integrado.",
    gc_tag="A mesma cena, arquivo menor.",
    gc_desc="Uma câmera que fotografa como a câmera do sistema, mas salva fotos e vídeos menores. Escolha Economia, Padrão ou Máximo, continue fotografando direto para o app Fotos e veja em cada captura quanto espaço você economizou.",
    formerly="(antes LeanCam)", website="Site", support="Suporte", privacy="Privacidade", contact="Contato",
),
"ru": dict(
    title="Cream — Небольшие приложения, экономящие место",
    desc="Cream создаёт небольшие приложения для iOS, которые экономят место: LeanVid сжимает видео без заметной потери качества, а GramCamera с самого начала снимает фото и видео меньшего размера.",
    h1="Небольшие приложения, которые экономят место.",
    lede="Cream делает небольшие, сфокусированные приложения для iOS вокруг одной идеи: сохранить фото и видео, занимая меньше места. Ничего не загружается в сеть — всё выполняется на вашем устройстве.",
    lv_tag="Уменьшайте видео, сохраняя качество.",
    lv_desc="Сжимает видео из медиатеки и приложения «Файлы», снижая только битрейт. Разрешение, частота кадров, цвет и HDR остаются без изменений, а каждый результат проверяется перед заменой оригинала. Файлы, которые iPhone не воспроизводит (MKV, WebM, AVI, VP9, AV1), преобразует встроенный конвертер.",
    gc_tag="Тот же кадр, меньше файл.",
    gc_desc="Камера, которая снимает так же, как обычная камера, но сохраняет фото и видео меньшего размера. Выберите Экономия, Стандарт или Максимум, продолжайте снимать прямо в приложение «Фото» и смотрите при каждом снимке, сколько места сэкономили.",
    formerly="(ранее LeanCam)", website="Сайт", support="Поддержка", privacy="Конфиденциальность", contact="Контакты",
),
}

PAGE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{alternates}
<link rel="stylesheet" href="{pfx}style.css">
<style>
  .apps {{ display: grid; gap: 16px; margin: 0 0 28px; }}
  .apps .card {{ margin: 0; }}
  .apps h2 {{ margin: 0 0 4px; font-size: 20px; }}
  .apps .tag {{ color: var(--ink-3); font-size: 14px; margin: 0 0 10px; }}
  .apps .links a {{ margin-right: 14px; }}
  .muted {{ color: var(--ink-3); font-size: 14px; font-weight: 400; }}
</style>
</head>
<body>
<div class="wrap">
  <header class="site">
    <div class="mark">C</div><div class="name">Cream</div>
    <nav><a href="{lv}index.html">LeanVid</a><a href="{gc}index.html">GramCamera</a><a href="mailto:creamhelp@gmail.com">{contact}</a></nav>
  </header>
  <div class="langs">{langs}</div>

  <h1>{h1}</h1>
  <p class="lede">{lede}</p>

  <div class="apps">
    <section class="card" id="leanvid">
      <h2>LeanVid</h2>
      <p class="tag">{lv_tag}</p>
      <p>{lv_desc}</p>
      <p class="links"><a href="{lv}index.html">{website}</a><a href="{lv}support.html">{support}</a><a href="{lv}privacy.html">{privacy}</a></p>
    </section>

    <section class="card" id="gramcamera">
      <h2>GramCamera <span class="muted">{formerly}</span></h2>
      <p class="tag">{gc_tag}</p>
      <p>{gc_desc}</p>
      <p class="links"><a href="{gc}index.html">{website}</a><a href="{gc}support.html">{support}</a><a href="{gc}privacy.html">{privacy}</a></p>
    </section>
  </div>

  <footer>© 2026 Cream · <a href="mailto:creamhelp@gmail.com">creamhelp@gmail.com</a></footer>
</div>
</body>
</html>
"""

EN_REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=../">
<link rel="canonical" href="https://creamhelp.github.io/">
<title>Cream</title>
</head>
<body><p><a href="../">Cream</a></p></body>
</html>
"""


def page_url(d):
    return BASE if d == "" else f"{BASE}{d}/"


def main():
    alternates = [f'<link rel="alternate" hreflang="x-default" href="{BASE}">']
    for d, _, hl, _ in LOCALES:
        alternates.append(f'<link rel="alternate" hreflang="{hl}" href="{page_url(d)}">')
    alternates = "\n".join(alternates)

    for d, lang, _, _ in LOCALES:
        t = T[d]
        pfx = "" if d == "" else "../"
        langs = []
        for od, _, _, native in LOCALES:
            if od == d:
                langs.append(f'<span class="cur">{native}</span>')
            else:
                href = f"{pfx}index.html" if od == "" else f"{pfx}{od}/index.html"
                langs.append(f'<a href="{href}">{native}</a>')
        gc_dir = "en" if d == "" else d
        lv = f"{pfx}leanvid/" if d == "" else f"{pfx}leanvid/{d}/"
        html = PAGE.format(
            lang=lang, canonical=page_url(d), alternates=alternates, pfx=pfx,
            langs=" ".join(langs), lv=lv, gc=f"{pfx}gramcamera/{gc_dir}/", **t,
        )
        outdir = ROOT if d == "" else os.path.join(ROOT, d)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", os.path.relpath(os.path.join(outdir, "index.html"), ROOT))

    en_dir = os.path.join(ROOT, "en")
    os.makedirs(en_dir, exist_ok=True)
    with open(os.path.join(en_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(EN_REDIRECT)
    print("wrote en/index.html (redirect to root)")


if __name__ == "__main__":
    main()
