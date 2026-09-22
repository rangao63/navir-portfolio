"""Build deterministic pixel assets and a review preview for NAVIR A01 v04."""
from pathlib import Path
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "portfolio" / "Amazon_APlus" / "Visual_Sample_v04"
AST = OUT / "Assets"
PRODUCT = AST / "NAVIR_S1_FrontFacing_Product_v04.png"
W, H = 1464, 3416
NAVY = (5, 18, 42, 255)
WHITE = (247, 249, 253, 255)
BLUE = (41, 94, 245, 255)
CN = r"C:\Windows\Fonts\msyh.ttc"
CNB = r"C:\Windows\Fonts\msyhbd.ttc"
ENB = r"C:\Windows\Fonts\arialbd.ttf"


def blank(): return Image.new("RGBA", (W, H), (0, 0, 0, 0))
def f(path, size): return ImageFont.truetype(path, size)


def gradient():
    top, mid, bot = np.array((8, 28, 68)), np.array((7, 25, 58)), np.array((4, 14, 32))
    out = np.zeros((H, W, 4), np.uint8); out[..., 3] = 255
    for y in range(H):
        if y < 2200:
            t=y/2200; c=top*(1-t)+mid*t
        else:
            t=(y-2200)/(H-2200); c=mid*(1-t)+bot*t
        out[y,:,0:3]=c
    return Image.fromarray(out, "RGBA")


def airflow():
    im=blank(); d=ImageDraw.Draw(im); cx,cy=732,610
    for i in range(25):
        a=math.radians(202 + i*(136/24))
        r1=260; r2=1100 + (i%4)*85
        p0=(cx+math.cos(a)*r1, cy+math.sin(a)*r1)
        p1=(cx+math.cos(a)*r2, cy+math.sin(a)*r2)
        d.line((p0,p1), fill=(73,141,255,25+(i%3)*10), width=18 if i%4==0 else 9)
    glow=im.filter(ImageFilter.GaussianBlur(28))
    fine=blank(); fd=ImageDraw.Draw(fine)
    for i in range(19):
        a=math.radians(204 + i*(132/18)); r1=280; r2=1180
        fd.line((cx+math.cos(a)*r1,cy+math.sin(a)*r1,cx+math.cos(a)*r2,cy+math.sin(a)*r2),
                fill=(133,199,255,55),width=3)
    glow.alpha_composite(fine)
    return glow


def turbine_core():
    im=blank(); d=ImageDraw.Draw(im)
    cx,cy=732,420
    # Sits behind the transparent outlet opening, independent of the product.
    d.ellipse((cx-119,cy-119,cx+119,cy+119),fill=(5,13,28,255),outline=(35,91,182,255),width=5)
    for i in range(8):
        a=math.radians(i*45+10)
        vertices=[]
        for radius,offset in [(32,-13),(105,-18),(100,17),(39,10)]:
            vertices.append((cx+math.cos(a+math.radians(offset))*radius,
                             cy+math.sin(a+math.radians(offset))*radius))
        d.polygon(vertices,fill=(38,52,73,255),outline=(84,112,151,230),width=2)
    d.ellipse((cx-45,cy-45,cx+45,cy+45),fill=(13,25,44,255),outline=(92,131,184,255),width=3)
    d.ellipse((cx-15,cy-15,cx+15,cy+15),fill=(46,98,188,255))
    return im


def product_layer():
    src=Image.open(PRODUCT).convert("RGBA")
    # Fade only the final cable segment.
    a=np.array(src.getchannel("A"),dtype=np.float32)
    start=int(src.height*.91)
    fade=np.ones(src.height,dtype=np.float32)
    fade[start:]=np.linspace(1,0,src.height-start)
    a=(a*fade[:,None]).astype(np.uint8)
    src.putalpha(Image.fromarray(a))
    target_h=2140
    src=src.resize((round(src.width*target_h/src.height),target_h),Image.Resampling.LANCZOS)
    im=blank(); im.alpha_composite(src,((W-src.width)//2,35))
    src.save(AST / "NAVIR_S1_FrontFacing_Product_Fade_v04.png")
    return im


def chrome_and_channels():
    im=blank(); d=ImageDraw.Draw(im)
    # Search field.
    d.rounded_rectangle((118,2700,1346,2838),radius=69,fill=(8,25,57,180),outline=(188,207,236,240),width=3)
    d.ellipse((168,2742,211,2785),outline=WHITE,width=4); d.line((205,2779,235,2807),fill=WHITE,width=4)
    # Titanium call-to-action.
    metal=Image.new("RGBA",(W,H),(0,0,0,0)); md=ImageDraw.Draw(metal)
    for x in range(940,1335):
        t=(x-940)/395
        shade=int(231-38*abs(t-.5)*2)
        md.line((x,2710,x,2828),fill=(shade,shade+2,min(255,shade+8),255))
    mask=Image.new("L",(W,H),0)
    ImageDraw.Draw(mask).rounded_rectangle((940,2710,1335,2828),radius=60,fill=255)
    metal.putalpha(mask)
    im.alpha_composite(metal)
    d.rounded_rectangle((940,2710,1335,2828),radius=60,outline=(255,255,255,190),width=3)
    # Bottom channel strip and pills.
    d.rectangle((0,3210,W,H),fill=(33,39,51,255)); d.line((0,3210,W,3210),fill=(91,106,133,170),width=2)
    for box in [(330,3272,625,3366),(660,3272,955,3366),(990,3272,1380,3366)]:
        d.rounded_rectangle(box,radius=48,fill=(206,211,219,255),outline=(238,241,246,210),width=2)
    # S1 badge.
    d.rounded_rectangle((568,2214,724,2314),radius=28,fill=(247,249,253,255),outline=(153,185,245,255),width=2)
    return im


def center(draw,text,y,font,fill):
    box=draw.textbbox((0,0),text,font=font); x=(W-(box[2]-box[0]))/2
    draw.text((x,y),text,font=font,fill=fill)


def text_layer():
    im=blank(); d=ImageDraw.Draw(im)
    # Split title, visually centered as one line.
    d.text((160,2200),"NAVIR",font=f(ENB,102),fill=WHITE)
    d.text((601,2222),"S1",font=f(ENB,52),fill=BLUE)
    d.text((765,2203),"高速吹风机",font=f(CNB,86),fill=WHITE)
    center(d,"让气流塑形。",2375,f(CN,64),(231,237,248,255))
    center(d,"定向气流  ·  温和控温  ·  轻盈握持",2505,f(CN,39),(195,209,232,255))
    d.text((260,2744),"探索 NAVIR S1",font=f(CN,38),fill=(183,199,226,255))
    d.text((1035,2742),"了解更多",font=f(CNB,43),fill=(31,75,193,255))
    d.text((58,3294),"购买渠道",font=f(CN,32),fill=(238,241,247,255))
    d.text((392,3290),"NAVIR 官网",font=f(CN,34),fill=(19,27,42,255))
    d.text((733,3286),"amazon",font=f(ENB,37),fill=(24,28,36,255))
    d.text((1072,3290),"MediaMarkt",font=ImageFont.truetype(r"C:\Windows\Fonts\ariali.ttf",32),fill=(210,50,50,255))
    return im


def main():
    AST.mkdir(parents=True,exist_ok=True)
    layers={"01_Background":gradient(),"02_Airflow_Behind":airflow(),
            "03_Turbine_Core":turbine_core(),"03_Product":product_layer(),
            "04_Chrome_UI":chrome_and_channels(),"05_Text_Reference":text_layer()}
    for name,im in layers.items(): im.save(AST/(name+".png"))
    comp=blank()
    for im in layers.values(): comp.alpha_composite(im)
    comp.convert("RGB").save(OUT/"NAVIR_S1_A01_Hero_CN_v04_preview.png",quality=96)
    print(OUT/"NAVIR_S1_A01_Hero_CN_v04_preview.png")

if __name__=="__main__": main()
