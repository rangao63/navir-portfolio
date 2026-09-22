"""Create a layered A01 PSD from the approved front-facing product and scene assets.

Requires photoshopapi and numpy. Photoshop text remains as native type layers;
the visible text-reference layer guarantees a readable fallback preview.
"""
from pathlib import Path
import numpy as np
from PIL import Image
import photoshopapi as ps

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'portfolio'/'Amazon_APlus'/'Visual_Sample_v04'
AST=OUT/'Assets'
W,H=1464,3416


def pixel(path,name):
    im=Image.open(path).convert('RGBA')
    arr=np.moveaxis(np.asarray(im,dtype=np.uint8),2,0).copy()
    return ps.ImageLayer_8bit(arr,name,width=im.width,height=im.height)


def text(name,value,x,y,size,rgb,font):
    # Native Photoshop text in a hidden group. The raster reference is visible
    # so the PSD composite stays readable in applications without Chinese fonts.
    return ps.TextLayer_8bit(name,value,font=font,font_size=size,
        fill_color=[1,*[c/255 for c in rgb]],position_x=x,position_y=y,
        box_width=W-x-16,box_height=size*1.6)


def main():
    doc=ps.LayeredFile_8bit(ps.enum.ColorMode.rgb,W,H)
    specs=[
        ('01 BACKGROUND','01_Background.png','Deep navy gradient'),
        ('02 AIRFLOW BEHIND PRODUCT','02_Airflow_Behind.png','Cobalt airflow filaments'),
        ('04 TITANIUM UI AND CHANNELS','04_Chrome_UI.png','Titanium CTA and channel fields'),
        ('05 TEXT RENDER REFERENCE','05_Text_Reference.png','Visible Chinese text reference'),
    ]
    for group_name,filename,layer_name in specs[:2]:
        group=ps.GroupLayer_8bit(group_name)
        doc.add_layer(group)
        group.add_layer(doc,pixel(AST/filename,layer_name))

    turbine=ps.GroupLayer_8bit('03 PRECISION TURBINE CORE')
    doc.add_layer(turbine)
    turbine.add_layer(doc,pixel(AST/'03_Turbine_Core.png','Dark rotor and restrained ion blue hub'))

    group=ps.GroupLayer_8bit('04 PRODUCT - REPLACEABLE SMART OBJECT')
    doc.add_layer(group)
    product=ps.SmartObjectLayer_8bit(doc,str(AST/'NAVIR_S1_FrontFacing_Product_Fade_v04.png'),
                                   'NAVIR S1 / replaceable smart object')
    product.move(0,-603)
    group.add_layer(doc,product)

    for group_name,filename,layer_name in specs[2:]:
        group=ps.GroupLayer_8bit(group_name)
        doc.add_layer(group)
        group.add_layer(doc,pixel(AST/filename,layer_name))

    native=ps.GroupLayer_8bit('06 NATIVE EDITABLE TYPE - enable after hiding reference',is_visible=False)
    doc.add_layer(native)
    lines=[
        ('NAVIR','NAVIR',160,2295,102,(247,249,253),'Arial-BoldMT'),
        ('S1 model','S1',601,2294,52,(41,94,245),'Arial-BoldMT'),
        ('Product name','高速吹风机',765,2280,86,(247,249,253),'MicrosoftYaHei-Bold'),
        ('Slogan','让气流塑形。',530,2450,64,(231,237,248),'MicrosoftYaHei'),
        ('Benefits','定向气流  ·  温和控温  ·  轻盈握持',440,2567,39,(195,209,232),'MicrosoftYaHei'),
        ('Search','探索 NAVIR S1',260,2795,38,(183,199,226),'MicrosoftYaHei'),
        ('CTA','了解更多',1035,2794,43,(31,75,193),'MicrosoftYaHei-Bold'),
        ('Channel heading','购买渠道',58,3342,32,(238,241,247),'MicrosoftYaHei'),
        ('Official site','NAVIR 官网',392,3340,34,(19,27,42),'MicrosoftYaHei'),
        ('Amazon','amazon',733,3337,37,(24,28,36),'Arial-BoldMT'),
        ('MediaMarkt','MediaMarkt',1072,3337,32,(210,50,50),'Arial-ItalicMT'),
    ]
    for spec in lines: native.add_layer(doc,text(*spec))
    output=OUT/'NAVIR_S1_A01_Hero_CN_v04.psd'
    doc.write(output,True)
    print(output)

if __name__=='__main__': main()
