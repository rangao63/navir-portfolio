from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "deliverables"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1920, 6000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_DIR = ROOT / "assets" / "fonts"
REG = ImageFont.truetype(str(FONT_DIR / "InstrumentSans-Regular.ttf"), 20)
BOLD = ImageFont.truetype(str(FONT_DIR / "InstrumentSans-Bold.ttf"), 28)
MONO = ImageFont.truetype(str(FONT_DIR / "DMMono-Regular.ttf"), 15)

im = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(im)


def label(x, y, index, name, color):
    d.text((x, y), f"{index}  /  {name}", font=MONO, fill=color)


def bars(x, y, widths, height=24, gap=18, color=BLACK):
    for i, width in enumerate(widths):
        d.rectangle((x, y + i * (height + gap), x + width, y + i * (height + gap) + height), fill=color)


# 01 / HERO - high-impact identity opener
y0, y1 = 0, 1080
label(84, 64, "01", "HERO", BLACK)
d.rectangle((84, 122, 270, 160), fill=BLACK)
for x in (1360, 1500, 1640, 1780):
    d.rectangle((x, 130, x + 72, 144), fill=BLACK)
d.rectangle((84, 330, 820, 470), fill=BLACK)
d.rectangle((84, 502, 660, 642), fill=BLACK)
bars(88, 706, [410, 330], height=15, gap=14)
d.rectangle((84, 828, 286, 894), fill=BLACK)
d.rectangle((1060, 230, 1836, 940), fill=BLACK)
d.rectangle((1310, 340, 1588, 858), fill=WHITE)

# 02 / BENEFIT OVERVIEW - compressed black chapter
y0, y1 = 1080, 2050
d.rectangle((0, y0, W, y1), fill=BLACK)
label(84, y0 + 70, "02", "CORE BENEFITS", WHITE)
d.rectangle((84, y0 + 190, 930, y0 + 760), fill=WHITE)
d.rectangle((220, y0 + 292, 794, y0 + 654), fill=BLACK)
d.rectangle((1080, y0 + 202, 1722, y0 + 294), fill=WHITE)
bars(1080, y0 + 362, [528, 448, 592], height=20, gap=40, color=WHITE)
for i, x in enumerate((1080, 1300, 1520)):
    d.rectangle((x, y0 + 648, x + 168, y0 + 810), outline=WHITE, width=4)
    d.rectangle((x + 26, y0 + 682, x + 88, y0 + 706), fill=WHITE)
    d.rectangle((x + 26, y0 + 736, x + 134, y0 + 748), fill=WHITE)

# 03 / AIRFLOW TECHNOLOGY - open technical chapter
y0, y1 = 2050, 3310
label(84, y0 + 72, "03", "AIRFLOW TECHNOLOGY", BLACK)
d.rectangle((84, y0 + 190, 760, y0 + 292), fill=BLACK)
bars(84, y0 + 350, [520, 430], height=18, gap=18)
d.rectangle((850, y0 + 150, 1836, y0 + 890), outline=BLACK, width=8)
d.rectangle((1030, y0 + 286, 1656, y0 + 650), fill=BLACK)
d.rectangle((84, y0 + 770, 610, y0 + 1120), fill=BLACK)
d.rectangle((650, y0 + 770, 1176, y0 + 1120), fill=BLACK)
d.rectangle((1216, y0 + 770, 1836, y0 + 1120), fill=BLACK)
for x, width in ((118, 250), (684, 310), (1250, 360)):
    d.rectangle((x, y0 + 1028, x + width, y0 + 1043), fill=WHITE)

# 04 / MATERIAL + ATTACHMENTS - dense detail climax
y0, y1 = 3310, 4800
d.rectangle((0, y0, W, y1), fill=BLACK)
label(84, y0 + 70, "04", "DETAILS / ATTACHMENTS", WHITE)
d.rectangle((84, y0 + 164, 1160, y0 + 774), fill=WHITE)
d.rectangle((1230, y0 + 164, 1836, y0 + 774), outline=WHITE, width=6)
d.rectangle((1320, y0 + 260, 1746, y0 + 678), fill=WHITE)
d.rectangle((84, y0 + 850, 586, y0 + 1340), outline=WHITE, width=5)
d.rectangle((628, y0 + 850, 1130, y0 + 1340), fill=WHITE)
d.rectangle((1172, y0 + 850, 1836, y0 + 1340), outline=WHITE, width=5)
bars(122, y0 + 1202, [220, 340], height=13, gap=16, color=WHITE)
bars(666, y0 + 1202, [250, 350], height=13, gap=16, color=BLACK)
bars(1210, y0 + 1202, [260, 420], height=13, gap=16, color=WHITE)

# 05 / COLORWAY + CLOSE - quiet archive and CTA
y0, y1 = 4800, 5720
label(84, y0 + 70, "05", "COLORWAYS / CLOSE", BLACK)
d.rectangle((84, y0 + 175, 770, y0 + 710), fill=BLACK)
d.rectangle((220, y0 + 252, 460, y0 + 638), fill=WHITE)
d.rectangle((810, y0 + 175, 1150, y0 + 710), outline=BLACK, width=6)
d.rectangle((878, y0 + 260, 1082, y0 + 638), fill=BLACK)
d.rectangle((1270, y0 + 214, 1836, y0 + 326), fill=BLACK)
bars(1270, y0 + 382, [470, 360, 420], height=18, gap=25)
d.rectangle((1270, y0 + 600, 1545, y0 + 674), fill=BLACK)

# FOOTER / visual stop
y0 = 5720
d.rectangle((0, y0, W, H), fill=BLACK)
d.rectangle((84, y0 + 82, 292, y0 + 122), fill=WHITE)
d.rectangle((1510, y0 + 92, 1836, y0 + 108), fill=WHITE)

path = OUT / "NAVIR_PC_Detail_Template_BW_v1.png"
im.save(path, optimize=True)
print(path)

# Grey-white blueprint variations derived from the approved five-section structure.
def tint_monochrome(source, dark_hex):
    return ImageOps.colorize(ImageOps.grayscale(source), black=dark_hex, white="#FFFFFF")


# A / Airy silver-grey: preserves the original composition with the lightest pressure.
variant_a = tint_monochrome(im, "#D2D7DD")
path_a = OUT / "NAVIR_PC_Template_GreyWhite_A_Airy.png"
variant_a.save(path_a, optimize=True)

# B / Reverse editorial: flips only content zones while keeping section labels readable.
reverse = im.copy()
content_zones = [
    (0, 175, W, 1060),
    (0, 1200, W, 2030),
    (0, 2220, W, 3290),
    (0, 3440, W, 4780),
    (0, 4940, W, 5700),
]
for box in content_zones:
    crop = reverse.crop(box).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    reverse.paste(crop, box[:2])
variant_b = tint_monochrome(reverse, "#B5BDC6")
path_b = OUT / "NAVIR_PC_Template_GreyWhite_B_Reverse.png"
variant_b.save(path_b, optimize=True)

# C / Technical graphite-grey: higher contrast without returning to pure black.
variant_c = tint_monochrome(im, "#7F8994")
path_c = OUT / "NAVIR_PC_Template_GreyWhite_C_Technical.png"
variant_c.save(path_c, optimize=True)

print(path_a)
print(path_b)
print(path_c)
