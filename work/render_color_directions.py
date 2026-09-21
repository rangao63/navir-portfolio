from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "deliverables"
OUT.mkdir(parents=True, exist_ok=True)
PRODUCT = Image.open(ROOT / "assets" / "NAVIR_S1_Front_View_v1.png").convert("RGB")

FONT_DIR = ROOT / "assets" / "fonts"
REG = FONT_DIR / "InstrumentSans-Regular.ttf"
BOLD = FONT_DIR / "InstrumentSans-Bold.ttf"
MONO = FONT_DIR / "DMMono-Regular.ttf"

WHITE = (255, 255, 255)
GRAPHITE = (22, 27, 34)
SILVER = (199, 204, 212)


def font(path, size):
    return ImageFont.truetype(str(path), size)


def tracked(draw, xy, text, fnt, fill, tracking=0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        b = draw.textbbox((x, y), ch, font=fnt)
        x += b[2] - b[0] + tracking


directions = [
    {
        "number": "01",
        "name": "ION BLUE",
        "role": "PRIMARY RECOMMENDATION",
        "primary": (49, 87, 255),
        "deep": (10, 25, 64),
        "hex": "#3157FF",
        "deep_hex": "#0A1940",
    },
    {
        "number": "02",
        "name": "ARCTIC CYAN",
        "role": "CLEAN / SCIENTIFIC",
        "primary": (0, 166, 184),
        "deep": (6, 44, 54),
        "hex": "#00A6B8",
        "deep_hex": "#062C36",
    },
    {
        "number": "03",
        "name": "ULTRAVIOLET",
        "role": "BEAUTY / EDITORIAL",
        "primary": (101, 80, 232),
        "deep": (33, 26, 71),
        "hex": "#6550E8",
        "deep_hex": "#211A47",
    },
]

im = Image.new("RGB", (1920, 1200), WHITE)
d = ImageDraw.Draw(im)

tracked(d, (80, 48), "NAVIR", font(BOLD, 42), GRAPHITE, 8)
d.text((80, 108), "COLOR DIRECTION / COLD CURRENT", font=font(MONO, 14), fill=GRAPHITE)
tracked(d, (1590, 64), "STUDY  01", font(MONO, 14), GRAPHITE, 2)
d.line((80, 154, 1840, 154), fill=GRAPHITE, width=2)

card_y = 205
card_w = 540
gap = 38
start_x = 80

for i, item in enumerate(directions):
    x = start_x + i * (card_w + gap)
    # Large brand-color field.
    d.rectangle((x, card_y, x + card_w, 780), fill=item["primary"])
    d.text((x + 34, card_y + 28), item["number"], font=font(MONO, 15), fill=WHITE)
    d.text((x + 34, card_y + 75), item["name"], font=font(BOLD, 31), fill=WHITE)
    d.text((x + 34, card_y + 118), item["role"], font=font(MONO, 12), fill=WHITE)

    # Product remains on a literal white window so its material is never color-contaminated.
    window = (x + 112, card_y + 185, x + 428, card_y + 535)
    d.rectangle(window, fill=WHITE)
    prod = PRODUCT.resize((175, 350), Image.Resampling.LANCZOS)
    im.paste(prod, (x + 182, card_y + 185))

    # Palette architecture.
    d.rectangle((x, 780, x + card_w, 1085), fill=WHITE, outline=(225, 228, 232), width=2)
    d.text((x + 30, 815), "PRIMARY", font=font(MONO, 11), fill=GRAPHITE)
    d.text((x + 30, 850), item["hex"], font=font(BOLD, 24), fill=GRAPHITE)
    d.rectangle((x + 30, 908, x + 260, 982), fill=item["primary"])
    d.rectangle((x + 278, 908, x + 392, 982), fill=item["deep"])
    d.rectangle((x + 410, 908, x + 510, 982), fill=SILVER)
    d.text((x + 30, 1002), item["hex"], font=font(MONO, 10), fill=GRAPHITE)
    d.text((x + 278, 1002), item["deep_hex"], font=font(MONO, 10), fill=GRAPHITE)
    d.text((x + 410, 1002), "#C7CCD4", font=font(MONO, 10), fill=GRAPHITE)
    if i == 0:
        d.rectangle((x + card_w - 19, card_y, x + card_w, 780), fill=item["deep"])

d.text((80, 1130), "PURE WHITE  #FFFFFF", font=font(MONO, 12), fill=GRAPHITE)
d.text((335, 1130), "TITANIUM SILVER  #C7CCD4", font=font(MONO, 12), fill=GRAPHITE)
d.text((1585, 1130), "SHAPE THE AIR.", font=font(REG, 18), fill=GRAPHITE)

path = OUT / "NAVIR_Color_Directions_01.png"
im.save(path, optimize=True)
print(path)
