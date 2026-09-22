"""Compose A01 v05 with a sculpted blue airflow plate behind the approved product."""
from pathlib import Path
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT=Path(__file__).resolve().parents[1]
V04=ROOT/'portfolio'/'Amazon_APlus'/'Visual_Sample_v04'/'Assets'
OUT=ROOT/'portfolio'/'Amazon_APlus'/'Visual_Sample_v05'
AST=OUT/'Assets'
W,H=1464,3416


def main():
    AST.mkdir(parents=True,exist_ok=True)
    for name in ['01_Background.png','04_Chrome_UI.png',
                 '05_Text_Reference.png','NAVIR_S1_FrontFacing_Product_Fade_v04.png',
                 'NAVIR_S1_FrontFacing_Product_v04.png']:
        shutil.copyfile(V04/name,AST/name)

    # Sculpt a compact rotor at 4x resolution for clean metallic contours.
    ss=4; cx,cy=130*ss,130*ss
    core=Image.new('RGBA',(260*ss,260*ss),(0,0,0,0))
    cd=ImageDraw.Draw(core)
    cd.ellipse((cx-119*ss,cy-119*ss,cx+119*ss,cy+119*ss),
               fill=(7,14,27,255),outline=(23,72,151,255),width=3*ss)
    for i in range(8):
        a=np.deg2rad(i*45+12)
        # Swept asymmetrical blades, with a recessed shadow and a narrow lit edge.
        polar=[(35,-16),(102,-27),(108,-4),(62,12),(35,10)]
        pts=[(cx+int(np.cos(a+np.deg2rad(da))*r*ss),
              cy+int(np.sin(a+np.deg2rad(da))*r*ss)) for r,da in polar]
        cd.polygon([(x+3*ss,y+3*ss) for x,y in pts],fill=(2,8,19,235))
        cd.polygon(pts,fill=(30+i%2*7,41+i%2*7,57+i%2*7,255))
        cd.line(pts[0:3],fill=(90,111,137,235),width=2*ss)
    cd.ellipse((cx-39*ss,cy-39*ss,cx+39*ss,cy+39*ss),
               fill=(13,25,43,255),outline=(85,116,151,255),width=2*ss)
    cd.ellipse((cx-17*ss,cy-17*ss,cx+17*ss,cy+17*ss),
               fill=(27,42,63,255),outline=(74,129,213,255),width=2*ss)
    core=core.resize((260,260),Image.Resampling.LANCZOS)
    core_layer=Image.new('RGBA',(W,H),(0,0,0,0))
    core_layer.alpha_composite(core,(732-130,420-130))
    core_layer.save(AST/'03_Turbine_Core.png')

    # The generated plate is a true background asset. Scale once to document
    # width, then fade its lower portion into the existing deep navy field.
    source=Image.open(AST/'NAVIR_S1_Sculpted_Blue_Airflow_v05.png').convert('RGBA')
    h=round(source.height*W/source.width)
    source=source.resize((W,h),Image.Resampling.LANCZOS)
    arr=np.asarray(source).copy()
    start,end=1050,min(h,2200)
    alpha=np.ones(h,dtype=np.float32)
    alpha[start:end]=np.linspace(1,0,end-start)
    alpha[end:]=0
    arr[:,:,3]=(arr[:,:,3].astype(np.float32)*alpha[:,None]).astype(np.uint8)
    air=Image.new('RGBA',(W,H),(0,0,0,0))
    air.alpha_composite(Image.fromarray(arr,'RGBA'),(0,0))
    air.save(AST/'02_Sculpted_Airflow_Behind.png')

    # A soft blue reflection in the atmosphere behind the outlet integrates
    # the product with the effect without recoloring its pearl-white shell.
    halo=Image.new('RGBA',(W,H),(0,0,0,0))
    d=ImageDraw.Draw(halo)
    d.ellipse((302,2,1162,862),outline=(47,119,255,160),width=38)
    halo=halo.filter(ImageFilter.GaussianBlur(58))
    halo.save(AST/'02_Outlet_Atmospheric_Halo.png')

    comp=Image.new('RGBA',(W,H),(0,0,0,0))
    for name in ['01_Background.png','02_Sculpted_Airflow_Behind.png',
                 '02_Outlet_Atmospheric_Halo.png','03_Turbine_Core.png']:
        comp.alpha_composite(Image.open(AST/name).convert('RGBA'))
    product=Image.open(AST/'NAVIR_S1_FrontFacing_Product_Fade_v04.png').convert('RGBA')
    comp.alpha_composite(product,((W-product.width)//2,35))
    for name in ['04_Chrome_UI.png','05_Text_Reference.png']:
        comp.alpha_composite(Image.open(AST/name).convert('RGBA'))
    output=OUT/'NAVIR_S1_A01_Hero_CN_v05_preview.png'
    comp.convert('RGB').save(output,optimize=True)
    print(output)


if __name__=='__main__': main()
