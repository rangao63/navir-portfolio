from pathlib import Path
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
ASSET = ROOT / "assets" / "navir-s1-product-v1.png"
OUT = ROOT / "deliverables"
OUT.mkdir(parents=True, exist_ok=True)

WARM = (244, 242, 239)
SILVER = (200, 200, 196)
GRAPHITE = (32, 32, 32)
MIST = (220, 218, 213)
BURGUNDY = (107, 31, 50)
WHITE = (250, 249, 247)

FONT_DIR = ROOT / "assets" / "fonts"
REG = FONT_DIR / "InstrumentSans-Regular.ttf"
BOLD = FONT_DIR / "InstrumentSans-Bold.ttf"
MONO = FONT_DIR / "DMMono-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(str(path), size=size)


def tracked(draw, xy, text, fnt, fill, tracking=0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        box = draw.textbbox((x, y), ch, font=fnt)
        x += box[2] - box[0] + tracking


def bezier_points(p0, p1, p2, p3, count=180):
    pts = []
    for i in range(count + 1):
        t = i / count
        u = 1 - t
        x = u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0]
        y = u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]
        pts.append((int(x), int(y)))
    return pts


def product_cutout():
    img = Image.open(ASSET).convert("RGB")
    a = np.asarray(img).astype(np.float32)
    corners = np.concatenate([
        a[:80, :80].reshape(-1, 3), a[:80, -80:].reshape(-1, 3),
        a[-80:, :80].reshape(-1, 3), a[-80:, -80:].reshape(-1, 3)
    ])
    bg = np.median(corners, axis=0)
    dist = np.sqrt(((a - bg) ** 2).sum(axis=2))
    alpha = np.clip((dist - 5) / 34, 0, 1)
    alpha = Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.1))
    out = img.convert("RGBA")
    out.putalpha(alpha)
    return out


PRODUCT = product_cutout()


def resize_h(img, height):
    width = round(img.width * height / img.height)
    return img.resize((width, height), Image.Resampling.LANCZOS)


def render_brand_board():
    im = Image.new("RGB", (1920, 1200), WARM)
    d = ImageDraw.Draw(im)

    # Header and wordmark
    tracked(d, (88, 54), "NAVIR", font(BOLD, 42), GRAPHITE, 8)
    tracked(d, (1588, 69), "BRAND BOARD  01", font(MONO, 16), GRAPHITE, 2)
    d.line((88, 126, 1832, 126), fill=(32, 32, 32, 55), width=2)
    tracked(d, (88, 188), "NAVIR", font(BOLD, 170), GRAPHITE, 13)
    d.text((96, 374), "SHAPE THE AIR.", font=font(REG, 30), fill=BURGUNDY)
    d.text((96, 423), "BEAUTY TECHNOLOGY / FLOW SYSTEM", font=font(MONO, 14), fill=GRAPHITE)

    # Central flow system
    d.text((650, 180), "FLOW 01", font=font(MONO, 14), fill=BURGUNDY)
    d.text((650, 210), "AIR RING", font=font(BOLD, 24), fill=GRAPHITE)
    d.ellipse((708, 265, 1140, 697), outline=MIST, width=72)
    d.arc((752, 309, 1096, 653), 205, 346, fill=BURGUNDY, width=8)
    pts = bezier_points((608, 690), (760, 450), (975, 850), (1218, 565))
    d.line(pts, fill=GRAPHITE, width=7, joint="curve")
    hair = bezier_points((622, 720), (805, 525), (1025, 870), (1240, 610))
    d.line(hair, fill=(107, 31, 50), width=2, joint="curve")
    d.text((650, 744), "FLOW 02 / SCULPTED LINE", font=font(MONO, 13), fill=GRAPHITE)

    # Product sculpture
    d.ellipse((1280, 160, 1930, 810), outline=(228, 226, 221), width=76)
    prod = resize_h(PRODUCT, 780)
    im.paste(prod, (1245, 115), prod)
    d.text((1396, 834), "NAVIR S1", font=font(BOLD, 26), fill=GRAPHITE)
    d.text((1396, 874), "SOFT SILVER / BURGUNDY", font=font(MONO, 12), fill=BURGUNDY)

    # Bottom system strip
    d.line((88, 930, 1832, 930), fill=GRAPHITE, width=2)
    d.text((88, 969), "COLOR", font=font(MONO, 13), fill=GRAPHITE)
    swatches = [
        (WARM, "WARM WHITE", "F4F2EF"), (SILVER, "SOFT SILVER", "C8C8C4"),
        (GRAPHITE, "GRAPHITE", "202020"), (MIST, "MIST GREY", "DCDAD5"),
        (BURGUNDY, "BURGUNDY", "6B1F32")
    ]
    x = 88
    for color, name, hexv in swatches:
        d.rounded_rectangle((x, 1008, x + 104, 1072), radius=4, fill=color, outline=(185, 182, 177), width=1)
        d.text((x, 1088), name, font=font(MONO, 10), fill=GRAPHITE)
        d.text((x, 1110), hexv, font=font(MONO, 10), fill=(80, 80, 80))
        x += 140

    d.text((875, 969), "TYPOGRAPHY", font=font(MONO, 13), fill=GRAPHITE)
    d.text((875, 1010), "Air, Sculpted.", font=font(REG, 46), fill=GRAPHITE)
    d.text((878, 1075), "INSTRUMENT SANS / DM MONO", font=font(MONO, 11), fill=BURGUNDY)

    d.text((1370, 969), "CHARACTER", font=font(MONO, 13), fill=GRAPHITE)
    for i, word in enumerate(["PRECISE", "AIRY", "SCULPTURAL", "CALM", "SENSUAL"]):
        d.text((1370, 1008 + i*27), word, font=font(MONO, 12), fill=GRAPHITE if i != 2 else BURGUNDY)

    path = OUT / "NAVIR_Brand_Board_1.0.png"
    im.save(path, quality=96)
    return im, path


def render_kv():
    im = Image.new("RGB", (2400, 3000), WARM)
    d = ImageDraw.Draw(im)

    # Monumental ring and restrained frame
    d.ellipse((1060, 250, 2930, 2120), outline=(222, 220, 215), width=150)
    d.arc((1185, 375, 2805, 1995), 166, 314, fill=(198, 197, 193), width=12)

    # Editorial title
    d.text((150, 590), "SHAPE", font=font(BOLD, 310), fill=GRAPHITE)
    d.text((150, 870), "THE AIR.", font=font(BOLD, 310), fill=GRAPHITE)

    # Background airflow
    back = bezier_points((-120, 2140), (470, 1540), (1150, 1320), (2050, 920))
    d.line(back, fill=(187, 185, 181), width=18, joint="curve")
    d.line(back, fill=WARM, width=5, joint="curve")

    # Product
    prod = resize_h(PRODUCT, 1980)
    im.paste(prod, (850, 610), prod)

    # Foreground release and hair lines
    front = bezier_points((1310, 1260), (1700, 1115), (2030, 850), (2550, 650))
    d.line(front, fill=BURGUNDY, width=13, joint="curve")
    h1 = bezier_points((1090, 1810), (1510, 1510), (1860, 1430), (2460, 1210))
    h2 = bezier_points((1050, 1875), (1510, 1580), (1980, 1550), (2510, 1320))
    d.line(h1, fill=(82, 81, 79), width=3, joint="curve")
    d.line(h2, fill=(107, 31, 50), width=2, joint="curve")

    # Meta typography
    tracked(d, (150, 126), "NAVIR", font(BOLD, 46), GRAPHITE, 9)
    tracked(d, (1860, 144), "FLOW STUDY  01/03", font(MONO, 18), GRAPHITE, 2)
    d.line((150, 224, 2250, 224), fill=GRAPHITE, width=2)
    d.rectangle((150, 2524, 310, 2536), fill=BURGUNDY)
    d.text((150, 2585), "NAVIR S1", font=font(BOLD, 42), fill=GRAPHITE)
    d.text((150, 2643), "HIGH-SPEED HAIR DRYER", font=font(MONO, 20), fill=GRAPHITE)
    d.text((150, 2782), "INVISIBLE FLOW, VISIBLE PRECISION.", font=font(REG, 28), fill=GRAPHITE)
    d.text((1905, 2585), "110,000 RPM", font=font(BOLD, 30), fill=GRAPHITE)
    d.text((1905, 2633), "CONCEPT SPECIFICATION", font=font(MONO, 15), fill=BURGUNDY)
    d.text((1905, 2782), "PERSONAL CONCEPT / 2026", font=font(MONO, 15), fill=GRAPHITE)
    d.line((150, 2865, 2250, 2865), fill=GRAPHITE, width=2)

    path = OUT / "NAVIR_KV01_SHAPE_THE_AIR_v1.png"
    im.save(path, quality=96)
    return im, path


board, board_path = render_brand_board()
kv, kv_path = render_kv()

pdf_path = OUT / "NAVIR_BrandBoard_KV01_v1.pdf"
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

pdf = canvas.Canvas(str(pdf_path), pagesize=(1152, 720), invariant=1)
pdf.drawImage(ImageReader(board), 0, 0, width=1152, height=720)
pdf.showPage()
pdf.setPageSize((800, 1000))
pdf.drawImage(ImageReader(kv), 0, 0, width=800, height=1000)
pdf.showPage()
pdf.save()

print(board_path)
print(kv_path)
print(pdf_path)
