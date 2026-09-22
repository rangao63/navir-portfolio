"""Build the editable A01 v05 PSD with the revised sculpted airflow."""
from pathlib import Path
import photoshopapi as ps
from build_navir_a01_v04_psd import pixel, text

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'portfolio'/'Amazon_APlus'/'Visual_Sample_v05'
AST=OUT/'Assets'
W,H=1464,3416


def add_image(doc,group_name,filename,layer_name):
    group=ps.GroupLayer_8bit(group_name)
    doc.add_layer(group)
    group.add_layer(doc,pixel(AST/filename,layer_name))


def main():
    doc=ps.LayeredFile_8bit(ps.enum.ColorMode.rgb,W,H)
    add_image(doc,'01 BACKGROUND','01_Background.png','Deep navy field')
    add_image(doc,'02 SCULPTED AIRFLOW','02_Sculpted_Airflow_Behind.png','Volumetric cobalt streams')
    add_image(doc,'03 OUTLET ATMOSPHERE','02_Outlet_Atmospheric_Halo.png','Soft outlet halo')
    add_image(doc,'04 PRECISION TURBINE','03_Turbine_Core.png','Dark machined rotor')

    product_group=ps.GroupLayer_8bit('05 PRODUCT - REPLACEABLE SMART OBJECT')
    doc.add_layer(product_group)
    product=ps.SmartObjectLayer_8bit(doc,str(AST/'NAVIR_S1_FrontFacing_Product_Fade_v04.png'),
                                   'NAVIR S1 / replaceable smart object')
    product.move(0,-603)
    product_group.add_layer(doc,product)

    add_image(doc,'06 TITANIUM UI AND CHANNELS','04_Chrome_UI.png','Titanium CTA and channel fields')
    add_image(doc,'07 TEXT RENDER REFERENCE','05_Text_Reference.png','Visible Chinese text reference')

    native=ps.GroupLayer_8bit('08 NATIVE EDITABLE TYPE - enable after hiding reference',is_visible=False)
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
    out=OUT/'NAVIR_S1_A01_Hero_CN_v05.psd'
    doc.write(out,False)
    print(out)


if __name__=='__main__': main()
