#target photoshop

// Native Photoshop assembly for A01 v04. Run from Photoshop > File > Scripts > Browse.
app.displayDialogs = DialogModes.NO;
app.preferences.rulerUnits = Units.PIXELS;

var root = new File($.fileName).parent.parent.fsName.replace(/\\/g, "/") + "/";
var out = root + "portfolio/Amazon_APlus/Visual_Sample_v04/";
var assets = out + "Assets/";
var name = "NAVIR_S1_A01_Hero_CN_v04";
var doc = app.documents.add(1464, 3416, 72, name, NewDocumentMode.RGB,
                            DocumentFill.TRANSPARENT, 1, BitsPerChannelType.EIGHT);

function color(hex) {
    var c = new SolidColor(); c.rgb.hexValue = hex; return c;
}
function grp(s) { var g=doc.layerSets.add(); g.name=s; return g; }
function place(parent, filename, layerName) {
    var d = new ActionDescriptor();
    d.putPath(charIDToTypeID("null"), new File(assets + filename));
    executeAction(charIDToTypeID("Plc "), d, DialogModes.NO);
    var l=doc.activeLayer; l.name=layerName;
    var b=l.bounds;
    var cx=(b[0].as("px")+b[2].as("px"))/2;
    var cy=(b[1].as("px")+b[3].as("px"))/2;
    l.translate(732-cx,1708-cy);
    l.move(parent,ElementPlacement.INSIDE);
    return l;
}
function type(parent, label, value, x, baseline, size, hex, face) {
    var l=doc.artLayers.add(); l.kind=LayerKind.TEXT; l.name=label;
    l.move(parent,ElementPlacement.INSIDE);
    var t=l.textItem; t.kind=TextType.POINTTEXT; t.contents=value;
    t.position=[x,baseline]; t.size=size; t.color=color(hex);
    t.antiAliasMethod=AntiAlias.SHARP;
    try {t.font=face;} catch(e) {t.font="MicrosoftYaHei";}
    return l;
}

var bg=grp("01 BACKGROUND / NAVY");
place(bg,"01_Background.png","Navy gradient / replaceable");

var air=grp("02 AIRFLOW / BEHIND PRODUCT");
place(air,"02_Airflow_Behind.png","Cobalt airflow / independently editable");

var product=grp("03 PRODUCT / SMART OBJECT");
place(product,"NAVIR_S1_FrontFacing_Product_Fade_v04.png",
      "NAVIR S1 / REPLACEABLE SMART OBJECT");

var chrome=grp("04 BUTTON AND CHANNEL MATERIALS");
place(chrome,"04_Chrome_UI.png","Titanium search, CTA, channels and S1 plate");

var copy=grp("05 COPY / NATIVE EDITABLE TEXT");
type(copy,"NAVIR","NAVIR",160,2295,102,"F7F9FD","Arial-BoldMT");
type(copy,"S1 blue on white","S1",601,2294,52,"295EF5","Arial-BoldMT");
type(copy,"Product name","高速吹风机",765,2280,86,"F7F9FD","MicrosoftYaHei-Bold");
type(copy,"Chinese slogan","让气流塑形。",530,2450,64,"E7EDF8","MicrosoftYaHei");
type(copy,"Three benefits","定向气流  ·  温和控温  ·  轻盈握持",440,2567,39,"C3D1E8","MicrosoftYaHei");
type(copy,"Search phrase","探索 NAVIR S1",260,2795,38,"B7C7E2","MicrosoftYaHei");
type(copy,"CTA label","了解更多",1035,2794,43,"1F4BC1","MicrosoftYaHei-Bold");
type(copy,"Channel heading","购买渠道",58,3342,32,"EEF1F7","MicrosoftYaHei");
type(copy,"Official site","NAVIR 官网",392,3340,34,"131B2A","MicrosoftYaHei");
type(copy,"Amazon","amazon",733,3337,37,"181C24","Arial-BoldMT");
type(copy,"MediaMarkt","MediaMarkt",1072,3337,32,"D23232","Arial-ItalicMT");

var psd=new PhotoshopSaveOptions(); psd.layers=true; psd.embedColorProfile=true;
doc.saveAs(new File(out+name+".psd"),psd,true,Extension.LOWERCASE);
var png=new PNGSaveOptions(); png.interlaced=false;
doc.saveAs(new File(out+name+".png"),png,true,Extension.LOWERCASE);

// The marker lets an unattended caller detect whether Photoshop reached the end.
var marker=new File(out+name+".build-ok.txt");
marker.open("w"); marker.write("Photoshop native export completed\n"); marker.close();
