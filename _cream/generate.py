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
APP_STORE_LEANVID = "https://apps.apple.com/app/id6796710561"
APP_STORE_GRAMCAMERA = "https://apps.apple.com/app/id6804235227"
APP_STORE_ENHANCEVID = "https://apps.apple.com/app/id6816116747"
STORE_LABEL = {
    "": "Download on the App Store", "ko": "App Store에서 다운로드하기", "ja": "App Storeからダウンロード",
    "zh-Hans": "在 App Store 下载", "zh-Hant": "在 App Store 下載", "es-ES": "Descárgalo en el App Store",
    "de-DE": "Laden im App Store", "fr-FR": "Télécharger dans l’App Store", "it": "Scarica su App Store",
    "pt-BR": "Baixar na App Store", "ru": "Загрузите в App Store",
}

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
    lv_desc="Compresses videos from your photo library and the Files app by lowering only the bitrate. Resolution, frame rate, color and HDR stay intact, and every result is verified before it replaces the original. Files your iPhone can't play (MKV, WebM, AVI, WMV, FLV, MPG, VP9, AV1) are converted by the built-in converter.",
    gc_tag="Same shot, smaller file.",
    gc_desc="A camera that shoots the same way your stock camera does but saves smaller photos and videos. Choose Saver, Standard or Max, keep shooting straight into the Photos app, and see how much space you saved on every capture.",
    website="Website", support="Support", privacy="Privacy", contact="Contact",
),
"ko": dict(
    title="Cream — 용량을 아끼는 작은 앱들",
    desc="Cream은 저장 공간을 아끼는 작은 iOS 앱을 만듭니다. LeanVid는 눈에 띄는 화질 저하 없이 동영상을 압축하고, GramCamera는 처음부터 더 작은 사진과 동영상을 찍습니다.",
    h1="용량을 아끼는 작은 앱들.",
    lede="Cream은 한 가지 생각으로 작은 iOS 앱을 만듭니다. 사진과 동영상은 그대로 두고, 저장 공간은 덜 쓰기. 어떤 것도 업로드하지 않고 모두 기기 안에서 처리합니다.",
    lv_tag="화질은 그대로, 용량만 줄이세요.",
    lv_desc="사진 보관함과 파일 앱의 동영상을 비트레이트만 낮춰 압축합니다. 해상도·프레임레이트·색·HDR은 그대로이고, 모든 결과는 원본을 교체하기 전에 검증합니다. iPhone이 재생하지 못하는 파일(MKV, WebM, AVI, WMV, FLV, MPG, VP9, AV1)도 내장 변환기로 바꿉니다.",
    gc_tag="같은 장면, 더 작은 파일.",
    gc_desc="기본 카메라와 같은 방식으로 찍되, 저장할 때 용량을 아끼는 카메라입니다. 절약·표준·최대 중에서 고르고, 사진과 동영상은 그대로 기본 사진 앱에 저장되며, 매 촬영마다 얼마나 아꼈는지 확인할 수 있습니다.",
    website="웹사이트", support="지원", privacy="개인정보", contact="문의",
),
"ja": dict(
    title="Cream — 容量を節約する小さなアプリ",
    desc="Cream はストレージを節約する小さな iOS アプリを作っています。LeanVid は目に見える画質低下なしに動画を圧縮し、GramCamera は最初から小さな写真と動画を撮影します。",
    h1="容量を節約する、小さなアプリ。",
    lede="Cream はひとつの考えで小さな iOS アプリを作っています。写真と動画はそのままに、使うストレージは少なく。何もアップロードせず、すべて端末の中で処理します。",
    lv_tag="画質はそのままに、容量だけ小さく。",
    lv_desc="写真ライブラリとファイルアプリの動画を、ビットレートだけ下げて圧縮します。解像度・フレームレート・色・HDR はそのままで、すべての結果は元の動画を置き換える前に検証されます。iPhone で再生できないファイル(MKV、WebM、AVI、WMV、FLV、MPG、VP9、AV1)も内蔵コンバーターで変換します。",
    gc_tag="同じ一枚を、もっと軽く。",
    gc_desc="標準カメラと同じように撮りながら、保存するときの容量を抑えるカメラです。節約・標準・最大から選び、写真と動画はそのまま標準の写真アプリに保存され、一枚ごとにどれだけ節約できたかを確認できます。",
    website="ウェブサイト", support="サポート", privacy="プライバシー", contact="お問い合わせ",
),
"zh-Hans": dict(
    title="Cream — 节省空间的小应用",
    desc="Cream 开发节省存储空间的小型 iOS 应用:LeanVid 在没有明显画质损失的前提下压缩视频,GramCamera 从拍摄开始就生成更小的照片和视频。",
    h1="节省空间的小应用。",
    lede="Cream 围绕一个想法开发小而专注的 iOS 应用:照片和视频照常保留,占用的空间更少。不上传任何内容,一切都在你的设备上完成。",
    lv_tag="压缩视频,保留画质。",
    lv_desc="只降低比特率来压缩照片图库和“文件”应用中的视频。分辨率、帧率、色彩和 HDR 保持不变,每个结果在替换原片之前都会经过验证。iPhone 无法播放的文件(MKV、WebM、AVI、WMV、FLV、MPG、VP9、AV1)也可由内置转换器转换。",
    gc_tag="同样的画面,更小的文件。",
    gc_desc="以与系统相机相同的方式拍摄、但保存时更省容量的相机。在省容量、标准、最高之间选择,照片和视频照常存入系统“照片”应用,每次拍摄都能看到节省了多少。",
    website="网站", support="支持", privacy="隐私", contact="联系我们",
),
"zh-Hant": dict(
    title="Cream — 節省空間的小應用程式",
    desc="Cream 開發節省儲存空間的小型 iOS 應用程式:LeanVid 在沒有明顯畫質損失的前提下壓縮影片,GramCamera 從拍攝開始就產生更小的照片和影片。",
    h1="節省空間的小應用程式。",
    lede="Cream 圍繞一個想法開發小而專注的 iOS 應用程式:照片和影片照常保留,佔用的空間更少。不上傳任何內容,一切都在你的裝置上完成。",
    lv_tag="縮小影片,畫質不變。",
    lv_desc="只降低位元率來壓縮照片圖庫和「檔案」App 中的影片。解析度、影格率、色彩和 HDR 保持不變,每個結果在取代原始檔之前都會經過驗證。iPhone 無法播放的檔案(MKV、WebM、AVI、WMV、FLV、MPG、VP9、AV1)也可由內建轉換器轉換。",
    gc_tag="同樣的畫面,更小的檔案。",
    gc_desc="以與系統相機相同的方式拍攝、但儲存時更省容量的相機。在省容量、標準、最高之間選擇,照片和影片照常存入系統「照片」App,每次拍攝都能看到節省了多少。",
    website="網站", support="支援", privacy="隱私", contact="聯絡我們",
),
"es-ES": dict(
    title="Cream — Apps pequeñas que ahorran espacio",
    desc="Cream crea pequeñas apps para iOS que ahorran almacenamiento: LeanVid comprime vídeos sin pérdida visible de calidad y GramCamera captura fotos y vídeos más pequeños desde el principio.",
    h1="Apps pequeñas que ahorran espacio.",
    lede="Cream crea apps para iOS pequeñas y centradas en una sola idea: conserva tus fotos y vídeos usando menos almacenamiento. No se sube nada; todo se procesa en tu dispositivo.",
    lv_tag="Reduce tus vídeos sin perder calidad.",
    lv_desc="Comprime los vídeos de tu fototeca y de la app Archivos bajando solo la tasa de bits. La resolución, la frecuencia de fotogramas, el color y el HDR se mantienen intactos, y cada resultado se verifica antes de sustituir el original. Los archivos que tu iPhone no puede reproducir (MKV, WebM, AVI, WMV, FLV, MPG, VP9, AV1) se convierten con el conversor integrado.",
    gc_tag="La misma escena, un archivo menor.",
    gc_desc="Una cámara que captura igual que la cámara del sistema pero guarda fotos y vídeos más pequeños. Elige Ahorro, Estándar o Máximo, sigue disparando directamente a la app Fotos y comprueba cuánto espacio has ahorrado en cada captura.",
    website="Sitio web", support="Soporte", privacy="Privacidad", contact="Contacto",
),
"de-DE": dict(
    title="Cream — Kleine Apps, die Speicherplatz sparen",
    desc="Cream entwickelt kleine iOS-Apps, die Speicherplatz sparen: LeanVid verkleinert Videos ohne sichtbaren Qualitätsverlust, GramCamera nimmt Fotos und Videos von Anfang an kleiner auf.",
    h1="Kleine Apps, die Speicherplatz sparen.",
    lede="Cream baut kleine, fokussierte iOS-Apps rund um eine Idee: Fotos und Videos behalten, weniger Speicher verbrauchen. Nichts wird hochgeladen – alles läuft auf deinem Gerät.",
    lv_tag="Videos verkleinern, Qualität behalten.",
    lv_desc="Komprimiert Videos aus deiner Fotomediathek und der Dateien-App, indem nur die Bitrate gesenkt wird. Auflösung, Bildrate, Farbe und HDR bleiben erhalten, und jedes Ergebnis wird geprüft, bevor es das Original ersetzt. Dateien, die dein iPhone nicht abspielen kann (MKV, WebM, AVI, WMV, FLV, MPG, VP9, AV1), wandelt der eingebaute Konverter um.",
    gc_tag="Gleiches Motiv, kleinere Datei.",
    gc_desc="Eine Kamera, die genauso fotografiert wie die System-Kamera, aber kleinere Fotos und Videos speichert. Wähle Sparsam, Standard oder Maximum, fotografiere weiter direkt in die Fotos-App und sieh bei jeder Aufnahme, wie viel Platz du gespart hast.",
    website="Website", support="Support", privacy="Datenschutz", contact="Kontakt",
),
"fr-FR": dict(
    title="Cream — De petites apps qui économisent de l'espace",
    desc="Cream crée de petites apps iOS qui économisent du stockage : LeanVid compresse les vidéos sans perte visible de qualité, GramCamera enregistre des photos et vidéos plus légères dès la prise de vue.",
    h1="De petites apps qui économisent de l'espace.",
    lede="Cream conçoit de petites apps iOS centrées sur une seule idée : garder vos photos et vidéos en utilisant moins de stockage. Rien n'est envoyé en ligne, tout se fait sur votre appareil.",
    lv_tag="Réduisez vos vidéos, gardez la qualité.",
    lv_desc="Compresse les vidéos de votre photothèque et de l'app Fichiers en ne réduisant que le débit. Résolution, cadence, couleurs et HDR restent intacts, et chaque résultat est vérifié avant de remplacer l'original. Les fichiers que votre iPhone ne peut pas lire (MKV, WebM, AVI, WMV, FLV, MPG, VP9, AV1) sont convertis par le convertisseur intégré.",
    gc_tag="Même scène, fichier plus léger.",
    gc_desc="Un appareil photo qui prend vos photos comme l'appareil d'origine, mais enregistre des photos et vidéos plus légères. Choisissez Économe, Standard ou Maximum, continuez à photographier directement dans l'app Photos et voyez à chaque prise combien d'espace vous avez gagné.",
    website="Site web", support="Assistance", privacy="Confidentialité", contact="Contact",
),
"it": dict(
    title="Cream — Piccole app che fanno risparmiare spazio",
    desc="Cream crea piccole app per iOS che fanno risparmiare spazio: LeanVid comprime i video senza perdita visibile di qualità, GramCamera scatta foto e video più leggeri fin dall'inizio.",
    h1="Piccole app che fanno risparmiare spazio.",
    lede="Cream realizza app per iOS piccole e mirate, attorno a un'unica idea: tenere foto e video usando meno spazio. Nulla viene caricato online, tutto avviene sul tuo dispositivo.",
    lv_tag="Riduci i video, mantieni la qualità.",
    lv_desc="Comprime i video della libreria foto e dell'app File abbassando solo il bitrate. Risoluzione, frequenza dei fotogrammi, colore e HDR restano intatti, e ogni risultato viene verificato prima di sostituire l'originale. I file che il tuo iPhone non riproduce (MKV, WebM, AVI, WMV, FLV, MPG, VP9, AV1) vengono convertiti dal convertitore integrato.",
    gc_tag="Stessa scena, file più piccolo.",
    gc_desc="Una fotocamera che scatta come quella di sistema, ma salva foto e video più leggeri. Scegli Risparmio, Standard o Massimo, continua a scattare direttamente nell'app Foto e vedi a ogni scatto quanto spazio hai risparmiato.",
    website="Sito web", support="Assistenza", privacy="Privacy", contact="Contatti",
),
"pt-BR": dict(
    title="Cream — Apps pequenos que economizam espaço",
    desc="A Cream cria apps pequenos para iOS que economizam armazenamento: o LeanVid comprime vídeos sem perda visível de qualidade e o GramCamera captura fotos e vídeos menores desde o início.",
    h1="Apps pequenos que economizam espaço.",
    lede="A Cream cria apps para iOS pequenos e focados em uma só ideia: manter suas fotos e vídeos usando menos armazenamento. Nada é enviado para a internet; tudo acontece no seu aparelho.",
    lv_tag="Reduza seus vídeos, mantenha a qualidade.",
    lv_desc="Comprime os vídeos da sua fototeca e do app Arquivos reduzindo apenas a taxa de bits. Resolução, taxa de quadros, cor e HDR permanecem intactos, e cada resultado é verificado antes de substituir o original. Arquivos que o seu iPhone não reproduz (MKV, WebM, AVI, WMV, FLV, MPG, VP9, AV1) são convertidos pelo conversor integrado.",
    gc_tag="A mesma cena, arquivo menor.",
    gc_desc="Uma câmera que fotografa como a câmera do sistema, mas salva fotos e vídeos menores. Escolha Economia, Padrão ou Máximo, continue fotografando direto para o app Fotos e veja em cada captura quanto espaço você economizou.",
    website="Site", support="Suporte", privacy="Privacidade", contact="Contato",
),
"ru": dict(
    title="Cream — Небольшие приложения, экономящие место",
    desc="Cream создаёт небольшие приложения для iOS, которые экономят место: LeanVid сжимает видео без заметной потери качества, а GramCamera с самого начала снимает фото и видео меньшего размера.",
    h1="Небольшие приложения, которые экономят место.",
    lede="Cream делает небольшие, сфокусированные приложения для iOS вокруг одной идеи: сохранить фото и видео, занимая меньше места. Ничего не загружается в сеть — всё выполняется на вашем устройстве.",
    lv_tag="Уменьшайте видео, сохраняя качество.",
    lv_desc="Сжимает видео из медиатеки и приложения «Файлы», снижая только битрейт. Разрешение, частота кадров, цвет и HDR остаются без изменений, а каждый результат проверяется перед заменой оригинала. Файлы, которые iPhone не воспроизводит (MKV, WebM, AVI, WMV, FLV, MPG, VP9, AV1), преобразует встроенный конвертер.",
    gc_tag="Тот же кадр, меньше файл.",
    gc_desc="Камера, которая снимает так же, как обычная камера, но сохраняет фото и видео меньшего размера. Выберите Экономия, Стандарт или Максимум, продолжайте снимать прямо в приложение «Фото» и смотрите при каждом снимке, сколько места сэкономили.",
    website="Сайт", support="Поддержка", privacy="Конфиденциальность", contact="Контакты",
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
  /* Cream 첫 화면 — 공용 style.css(LeanVid 초록) 위에 중립 크림색을 덮고, 앱마다 제 색을 쓴다(2026-09-27) */
  :root{{ --bg:#F8F6F1; --surface:#FFFFFF; --ink:#1B1A17; --ink-2:#4B4842; --ink-3:#7A766E; --accent:#8A5A2B; --accent-2:#C08A4E; --border:#E7E2D8;
    --lv:#0A5C3E; --lv-2:#2E9C77; --gc:#1E8E4E; --gc-2:#34C759; --ev:#5B45D6; --ev-2:#8A6CF0; }}
  @media (prefers-color-scheme: dark){{ :root{{ --bg:#121110; --surface:#1C1B19; --ink:#F1EEE8; --ink-2:#BDB7AC; --ink-3:#8E887D; --accent:#E0B27A; --accent-2:#C08A4E; --border:#2C2A27;
    --lv:#3FBE8C; --lv-2:#2E9C77; --gc:#4CD97B; --gc-2:#2FB45C; --ev:#9B87FF; --ev-2:#7A62F0; }} }}
  .wrap.wide{{max-width:1040px}}
  .hero{{text-align:center;margin:12px 0 64px}}
  .hero h1{{font-size:46px;line-height:1.16;letter-spacing:-.02em;margin:0 0 16px}}
  .hero h1 em{{font-style:normal;background:linear-gradient(120deg,var(--lv),var(--gc) 45%,var(--ev));-webkit-background-clip:text;background-clip:text;color:transparent}}
  .hero .lede{{font-size:18px;max-width:640px;margin:0 auto 34px}}
  .icons{{display:flex;justify-content:center;gap:28px;flex-wrap:wrap}}
  .icons a{{display:flex;flex-direction:column;align-items:center;gap:10px;color:var(--ink);font-weight:700;font-size:14px;text-decoration:none}}
  .icons img{{width:96px;height:96px;border-radius:22px;box-shadow:0 12px 30px rgba(0,0,0,.18);animation:float 4s ease-in-out infinite}}
  .icons a:nth-child(2) img{{animation-delay:.6s}} .icons a:nth-child(3) img{{animation-delay:1.2s}}
  @keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-8px)}}}}
  .app{{display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:center;margin:0 0 28px;padding:30px;border-radius:24px;background:var(--surface);border:1px solid var(--border)}}
  .app.rev .vis{{order:-1}}
  .app .title{{display:flex;align-items:center;gap:12px;margin:0 0 6px}}
  a.title{{color:var(--ink);text-decoration:none;width:fit-content}} a.title:hover h2{{text-decoration:underline}}
  .app .title .go{{font-size:28px;font-weight:300;color:var(--ink-3);transition:transform .2s}} a.title:hover .go{{transform:translateX(4px)}}
  .app .title img{{width:44px;height:44px;border-radius:11px;box-shadow:0 2px 8px rgba(0,0,0,.18)}}
  .app h2{{margin:0;font-size:26px}}
  .app .tag{{font-weight:700;margin:0 0 12px}}
  .app p{{color:var(--ink-2);margin:0 0 14px}}
  .app .links{{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:15px}}
  .app.lean .tag,.app.lean .links a{{color:var(--lv)}} .app.gram .tag,.app.gram .links a{{color:var(--gc)}} .app.enh .tag,.app.enh .links a{{color:var(--ev)}}
  .vis{{border-radius:18px;padding:22px;background:var(--bg);min-height:220px;display:flex;flex-direction:column;justify-content:center;gap:12px}}
  .row{{display:flex;justify-content:space-between;align-items:baseline;gap:10px;font-size:13px;color:var(--ink-3)}}
  .row b{{color:var(--ink);font-size:14px}}
  .bar{{height:30px;border-radius:10px;background:color-mix(in srgb,var(--ink-3) 22%,var(--surface));overflow:hidden}}
  .fill{{height:100%;width:var(--w);border-radius:10px;animation:shrink 3.4s ease-in-out infinite}}
  .lean .fill{{background:linear-gradient(90deg,var(--lv),var(--lv-2))}} .gram .fill{{background:linear-gradient(90deg,var(--gc),var(--gc-2))}}
  @keyframes shrink{{0%,15%{{width:100%}}55%,100%{{width:var(--w)}}}}
  .big{{font-size:32px;font-weight:800;letter-spacing:-.02em;color:var(--lv)}}
  .gram .big{{color:var(--gc)}}
  .note{{font-size:12px;color:var(--ink-3)}}
  .cmp{{position:relative;border-radius:14px;overflow:hidden;aspect-ratio:16/9;background:#000}}
  .cmp img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
  .cmp .b{{animation:sweep 5s ease-in-out infinite}}
  .cmp .l{{position:absolute;top:0;bottom:0;width:3px;margin-left:-1.5px;background:#fff;box-shadow:0 0 10px rgba(0,0,0,.4);animation:line 5s ease-in-out infinite}}
  @keyframes sweep{{0%,100%{{clip-path:inset(0 75% 0 0)}}50%{{clip-path:inset(0 25% 0 0)}}}}
  @keyframes line{{0%,100%{{left:25%}}50%{{left:75%}}}}
  .cmp .t{{position:absolute;top:10px;padding:4px 9px;border-radius:999px;font-size:12px;font-weight:700;color:#fff;background:rgba(0,0,0,.55)}}
  .cmp .l2{{left:10px}} .cmp .r2{{right:10px;background:rgba(91,69,214,.85)}}
  .chips{{display:flex;gap:8px;flex-wrap:wrap}}
  .chips span{{font-size:13px;font-weight:700;padding:6px 10px;border-radius:999px;background:color-mix(in srgb,var(--ev) 14%,transparent);color:var(--ev)}}
  .promise{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:48px 0}}
  .promise div{{text-align:center;padding:22px;border-radius:18px;background:var(--surface);border:1px solid var(--border)}}
  .promise svg{{width:30px;height:30px;fill:none;stroke:var(--accent);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}}
  .promise b{{display:block;margin:8px 0 4px}}
  .promise p{{margin:0;font-size:14px;color:var(--ink-2)}}
  .mark{{flex:none}}
  @media (max-width:760px){{ header.site{{flex-wrap:wrap;row-gap:10px}} header.site nav{{margin-left:0;width:100%;flex-wrap:wrap;gap:6px 16px}} .hero h1{{font-size:32px}} .app{{grid-template-columns:1fr;padding:20px}} .app.rev .vis{{order:0}} .promise{{grid-template-columns:1fr}} .icons{{gap:16px}} .icons img{{width:72px;height:72px}} }}
  @media (prefers-reduced-motion:reduce){{ *{{animation:none!important}} }}
</style>
</head>
<body>
<div class="wrap wide">
  <header class="site">
    <div class="mark">C</div><div class="name">Cream</div>
    <nav><a href="{lv}index.html">LeanVid</a><a href="{gc}index.html">GramCamera</a><a href="{ev}index.html">EnhanceVid</a><a href="mailto:creamhelp@gmail.com">{contact}</a></nav>
  </header>
  <div class="langs">{langs}</div>

  <section class="hero">
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="icons">
      <a href="#leanvid"><img src="{pfx}assets/leanvid-icon.png" alt="">LeanVid</a>
      <a href="#gramcamera"><img src="{pfx}gramcamera/assets/icon.png" alt="">GramCamera</a>
      <a href="#enhancevid"><img src="{pfx}enhancevid/assets/icon.png" alt="">EnhanceVid</a>
    </div>
  </section>

  <section class="app lean" id="leanvid">
    <div>
      <a class="title" href="{lv}index.html"><img src="{pfx}assets/leanvid-icon.png" alt=""><h2>LeanVid</h2><span class="go">›</span></a>
      <p class="tag">{lv_tag}</p>
      <p>{lv_desc}</p>
      <p class="links"><a href="{app_store_lv}"><b>{store}</b></a><a href="{lv}index.html">{website}</a><a href="{lv}support.html">{support}</a><a href="{lv}privacy.html">{privacy}</a></p>
    </div>
    <div class="vis">
      <div class="row"><b>{original}</b><span>1.24GB</span></div>
      <div class="bar"><div class="fill" style="--w:100%;animation:none;background:color-mix(in srgb,var(--ink-3) 45%,var(--surface))"></div></div>
      <div class="row"><b>LeanVid</b><span>99.4MB</span></div>
      <div class="bar"><div class="fill" style="--w:8%"></div></div>
      <div class="big">{lv_big}</div>
      <span class="note">{lv_note}</span>
    </div>
  </section>

  <section class="app gram rev" id="gramcamera">
    <div>
      <a class="title" href="{gc}index.html"><img src="{pfx}gramcamera/assets/icon.png" alt=""><h2>GramCamera</h2><span class="go">›</span></a>
      <p class="tag">{gc_tag}</p>
      <p>{gc_desc}</p>
      <p class="links"><a href="{app_store_gc}"><b>{store}</b></a><a href="{gc}index.html">{website}</a><a href="{gc}support.html">{support}</a><a href="{gc}privacy.html">{privacy}</a></p>
    </div>
    <div class="vis">
{gc_rows}
      <span class="note">{gc_note}</span>
    </div>
  </section>

  <section class="app enh" id="enhancevid">
    <div>
      <a class="title" href="{ev}index.html"><img src="{pfx}enhancevid/assets/icon.png" alt=""><h2>EnhanceVid</h2><span class="go">›</span></a>
      <p class="tag">{ev_tag}</p>
      <p>{ev_desc}</p>
      <p class="links"><a href="{app_store_ev}"><b>{store}</b></a><a href="{ev}index.html">{website}</a><a href="{ev}support.html">{support}</a><a href="{ev}privacy.html">{privacy}</a></p>
    </div>
    <div class="vis">
      <div class="cmp"><img src="{pfx}enhancevid/assets/after.jpg" alt=""><img class="b" src="{pfx}enhancevid/assets/before.jpg" alt=""><div class="l"></div><span class="t l2">{ev_before}</span><span class="t r2">{ev_after}</span></div>
      <div class="chips">{ev_chips}</div>
    </div>
  </section>

  <section class="promise">
    <div><svg viewBox="0 0 24 24"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg><b>{p1b}</b><p>{p1p}</p></div>
    <div><svg viewBox="0 0 24 24"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 20h16"/><path d="M3 3l18 18"/></svg><b>{p2b}</b><p>{p2p}</p></div>
    <div><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/><path d="M3 3l18 18"/></svg><b>{p3b}</b><p>{p3p}</p></div>
  </section>

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


def extras(d):
    """2026-09-27 개편 문구: _cream/extra.json(첫머리·LeanVid 실측·약속 셋) + 각 앱 사이트의 문구 파일."""
    import html, importlib.util, json, re
    e = html.escape
    loc = d or "en"
    x = json.load(open(os.path.join(HERE, "extra.json"), encoding="utf-8"))[d]
    spec = importlib.util.spec_from_file_location("ev", os.path.join(ROOT, "enhancevid", "_build", "i18n", loc.replace("-", "_") + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); ev = m.S["index"]
    gc = json.load(open(os.path.join(ROOT, "gramcamera", "_build", "text.json"), encoding="utf-8"))[loc]
    rows = []
    for c in gc["stats"]["columns"][:2]:
        w = 100 - int(re.search(r"\d+", c["pct"]).group(0))
        rows.append(f'      <div class="row"><b>{e(c["name"])}</b><span>{e(c["detail"])} · <b>{e(c["pct"])}</b></span></div>\n'
                    f'      <div class="bar"><div class="fill" style="--w:{w}%"></div></div>')
    chips = [ev["k2"].split(" · ")[-1], ev["k1"].split(" · ")[-1], ev["feats"][0][0]]
    return dict(
        title=e(x["title"]), desc=e(x["desc"]), h1=x["h1"], lede=e(x["lede"]),
        lv_big=e(x["lv_big"]), lv_note=e(x["lv_note"]), original=e(ev["tags"][0]), ev_before=e(ev["tags"][0]), ev_after=e(ev["tags"][1]),
        gc_rows="\n".join(rows), gc_note=e(gc["stats"]["footer"]),
        ev_tag=e(ev["title"].split(" — ", 1)[1]), ev_desc=e(ev["desc"]),
        ev_chips="".join(f"<span>{e(c)}</span>" for c in chips),
        p1b=e(x["promise"][0][0]), p1p=e(x["promise"][0][1]), p2b=e(x["promise"][1][0]), p2p=e(x["promise"][1][1]),
        p3b=e(x["promise"][2][0]), p3p=e(x["promise"][2][1]),
    )


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
        ev = f"{pfx}enhancevid/" if d == "" else f"{pfx}enhancevid/{d}/"
        t = {**t, **extras(d)}
        html = PAGE.format(
            lang=lang, canonical=page_url(d), alternates=alternates, pfx=pfx,
            langs=" ".join(langs), lv=lv, ev=ev, app_store_ev=APP_STORE_ENHANCEVID, gc=f"{pfx}gramcamera/{gc_dir}/",
            app_store_lv=APP_STORE_LEANVID, app_store_gc=APP_STORE_GRAMCAMERA, store=STORE_LABEL[d], **t,
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
