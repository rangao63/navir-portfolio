#target photoshop

app.displayDialogs = DialogModes.NO;
app.preferences.rulerUnits = Units.PIXELS;

var ROOT = "C:/Users/ecmax/Desktop/05/燃/亚马逊a+/Visual_Sample_v01/";
var PRODUCT = ROOT + "Assets/NAVIR_S1_3Q_ScreenAsset_v01.png";

var C = {
    WHITE: "F7F9FC",
    PAPER: "EDF1F6",
    PEARL: "E5E9F0",
    BLUE: "3157FF",
    BLUE2: "5B79FF",
    DEEP: "0A1940",
    DEEP2: "111F46",
    GRAPHITE: "111722",
    GRAY: "697386",
    MID: "AAB3C2",
    SILVER: "CAD0DA"
};

function sc(hex) {
    var color = new SolidColor();
    color.rgb.hexValue = hex;
    return color;
}

function newDoc(w, h, name, bgHex) {
    var d = app.documents.add(w, h, 72, name, NewDocumentMode.RGB, DocumentFill.TRANSPARENT, 1.0, BitsPerChannelType.EIGHT);
    var layer = d.artLayers.add();
    layer.name = "BASE / " + bgHex;
    d.selection.selectAll();
    d.selection.fill(sc(bgHex));
    d.selection.deselect();
    return d;
}

function group(doc, name) {
    var g = doc.layerSets.add();
    g.name = name;
    return g;
}

function addRect(doc, parent, name, x, y, w, h, hex, opacity) {
    var l = doc.artLayers.add();
    l.name = name;
    if (parent) l.move(parent, ElementPlacement.INSIDE);
    doc.selection.select([[x,y],[x+w,y],[x+w,y+h],[x,y+h]]);
    doc.selection.fill(sc(hex));
    doc.selection.deselect();
    if (opacity !== undefined) l.opacity = opacity;
    return l;
}

function ellipsePoints(x, y, w, h, n) {
    var pts = [];
    var cx = x + w / 2, cy = y + h / 2;
    for (var i = 0; i < n; i++) {
        var a = Math.PI * 2 * i / n;
        pts.push([cx + Math.cos(a) * w / 2, cy + Math.sin(a) * h / 2]);
    }
    return pts;
}

function addEllipse(doc, parent, name, x, y, w, h, hex, opacity, blur) {
    var l = doc.artLayers.add();
    l.name = name;
    if (parent) l.move(parent, ElementPlacement.INSIDE);
    doc.selection.select(ellipsePoints(x,y,w,h,96));
    doc.selection.fill(sc(hex));
    doc.selection.deselect();
    if (opacity !== undefined) l.opacity = opacity;
    if (blur && blur > 0) l.applyGaussianBlur(blur);
    return l;
}

function addRing(doc, parent, name, x, y, w, h, thickness, hex, opacity) {
    var l = addEllipse(doc, parent, name, x, y, w, h, hex, opacity, 0);
    doc.activeLayer = l;
    doc.selection.select(ellipsePoints(x+thickness,y+thickness,w-2*thickness,h-2*thickness,96));
    doc.selection.clear();
    doc.selection.deselect();
    return l;
}

function addText(doc, parent, name, content, x, y, size, hex, font, tracking, opacity) {
    var l = doc.artLayers.add();
    l.kind = LayerKind.TEXT;
    l.name = name;
    if (parent) l.move(parent, ElementPlacement.INSIDE);
    var ti = l.textItem;
    ti.kind = TextType.POINTTEXT;
    ti.contents = content;
    ti.position = [x, y];
    ti.size = size;
    ti.color = sc(hex);
    ti.antiAliasMethod = AntiAlias.SHARP;
    if (font) {
        try { ti.font = font; } catch (e) { try { ti.font = "MicrosoftYaHei"; } catch (e2) {} }
    }
    if (tracking !== undefined) ti.tracking = tracking;
    if (opacity !== undefined) l.opacity = opacity;
    return l;
}

function placeSmart(doc, parent, name, filePath, centerX, centerY, targetH, angle, blendMode, opacity) {
    var desc = new ActionDescriptor();
    desc.putPath(charIDToTypeID("null"), new File(filePath));
    executeAction(charIDToTypeID("Plc "), desc, DialogModes.NO);
    var l = doc.activeLayer;
    l.name = name;
    var b = l.bounds;
    var h = b[3].as("px") - b[1].as("px");
    var pct = targetH / h * 100;
    l.resize(pct, pct, AnchorPosition.MIDDLECENTER);
    if (angle) l.rotate(angle, AnchorPosition.MIDDLECENTER);
    b = l.bounds;
    var cx = (b[0].as("px") + b[2].as("px")) / 2;
    var cy = (b[1].as("px") + b[3].as("px")) / 2;
    l.translate(centerX - cx, centerY - cy);
    if (blendMode) l.blendMode = blendMode;
    if (opacity !== undefined) l.opacity = opacity;
    if (parent) l.move(parent, ElementPlacement.INSIDE);
    return l;
}

function savePsdAndPng(doc, psdPath, pngPath) {
    try { doc.convertProfile("sRGB IEC61966-2.1", Intent.PERCEPTUAL, true, true); } catch (e) {}
    var psd = new PhotoshopSaveOptions();
    psd.layers = true;
    psd.embedColorProfile = true;
    psd.alphaChannels = true;
    doc.saveAs(new File(psdPath), psd, true, Extension.LOWERCASE);
    var png = new PNGSaveOptions();
    png.interlaced = false;
    doc.saveAs(new File(pngPath), png, true, Extension.LOWERCASE);
}

function savePngOnly(doc, pngPath) {
    try { doc.convertProfile("sRGB IEC61966-2.1", Intent.PERCEPTUAL, true, true); } catch (e) {}
    var png = new PNGSaveOptions();
    png.interlaced = false;
    doc.saveAs(new File(pngPath), png, true, Extension.LOWERCASE);
}

function buildA01() {
    var d = newDoc(1464, 3416, "NAVIR_S1_A01_Hero_CN_v01", C.WHITE);
    d.layers[0].name = "01_BACKGROUND / COOL WHITE";

    var flow = group(d, "02_FLOW_COLOR_FIELDS");
    addRect(d, flow, "DEEP CIRCUIT HERO FIELD", 0, 0, 1464, 2430, C.DEEP, 100);
    addEllipse(d, flow, "ION BLUE VOLUME / RIGHT", 540, -240, 1180, 1450, C.BLUE, 100, 0);
    addEllipse(d, flow, "SOFT BLUE LIGHT", 120, 240, 1260, 1400, C.BLUE2, 28, 105);
    addRing(d, flow, "AIR RING / BROAD", -390, 580, 1450, 1450, 150, C.WHITE, 14);
    addEllipse(d, flow, "NEUTRAL MATERIAL SHIELD", 120, 20, 1130, 2140, C.GRAPHITE, 88, 72);
    // A broad transition plate carries the page into the following module.
    addRect(d, flow, "COOL WHITE TRANSITION", 0, 2430, 1464, 986, C.WHITE, 100);
    addRect(d, flow, "ION BLUE CONTINUITY BAR", 0, 2388, 1464, 42, C.BLUE, 100);

    var copy = group(d, "05_COPY_CN / EDITABLE");
    addText(d, copy, "BRAND", "NAVIR S1", 108, 176, 58, C.WHITE, "MicrosoftYaHei-Bold", 160, 100);
    addText(d, copy, "LAUNCH LABEL", "新品上市", 112, 260, 34, C.WHITE, "MicrosoftYaHei", 90, 74);
    addText(d, copy, "MAIN TITLE", "高速吹风机", 104, 2110, 178, C.WHITE, "MicrosoftYaHei-Bold", -30, 100);
    addText(d, copy, "TAGLINE CN", "让气流塑形。", 112, 2255, 42, C.WHITE, "MicrosoftYaHei", 80, 88);
    addText(d, copy, "TAGLINE EN", "SHAPE THE AIR.", 112, 2320, 24, C.WHITE, "Arial-BoldMT", 230, 62);

    addText(d, copy, "SECTION LABEL", "三项核心体验", 108, 2592, 29, C.DEEP, "MicrosoftYaHei-Bold", 80, 100);
    var cardY = 2684, cardH = 520, gap = 24, cardW = 400;
    addRect(d, flow, "FEATURE CARD 01", 108, cardY, cardW, cardH, "EEF2F7", 100);
    addRect(d, flow, "FEATURE CARD 02", 532, cardY, cardW, cardH, "E7ECF5", 100);
    addRect(d, flow, "FEATURE CARD 03", 956, cardY, cardW, cardH, C.DEEP, 100);
    addRect(d, flow, "CARD 01 ACCENT", 108, cardY, cardW, 18, C.BLUE, 100);
    addRect(d, flow, "CARD 02 ACCENT", 532, cardY, cardW, 18, C.BLUE, 100);
    addRect(d, flow, "CARD 03 ACCENT", 956, cardY, cardW, 18, C.BLUE, 100);
    addText(d, copy, "CARD01 TITLE", "高速干发", 146, 2802, 36, C.DEEP, "MicrosoftYaHei-Bold", 20, 100);
    addText(d, copy, "CARD01 VALUE", "110,000", 146, 2908, 58, C.BLUE, "Arial-BoldMT", -15, 100);
    addText(d, copy, "CARD01 UNIT", "RPM", 148, 2970, 24, C.GRAY, "Arial-BoldMT", 100, 100);
    addText(d, copy, "CARD01 COPY", "高速动力概念参数", 146, 3100, 24, C.GRAY, "MicrosoftYaHei", 15, 100);
    addText(d, copy, "CARD02 TITLE", "定向气流", 570, 2802, 36, C.DEEP, "MicrosoftYaHei-Bold", 20, 100);
    addText(d, copy, "CARD02 VALUE", "20 m/s", 570, 2910, 54, C.BLUE, "Arial-BoldMT", -15, 100);
    addText(d, copy, "CARD02 COPY", "宽幅空气体块表达", 570, 3100, 24, C.GRAY, "MicrosoftYaHei", 15, 100);
    addText(d, copy, "CARD03 TITLE", "实时温控", 994, 2802, 36, C.WHITE, "MicrosoftYaHei-Bold", 20, 100);
    addText(d, copy, "CARD03 VALUE", "50次/秒", 994, 2910, 49, C.WHITE, "MicrosoftYaHei-Bold", -10, 100);
    addText(d, copy, "CARD03 COPY", "持续监测出风温度", 994, 3100, 24, C.SILVER, "MicrosoftYaHei", 15, 100);
    addText(d, copy, "CONCEPT NOTE", "概念参数 / 作品集展示", 108, 3330, 22, C.GRAY, "MicrosoftYaHei", 80, 100);

    var shadow = group(d, "03_PRODUCT_SHADOW");
    addEllipse(d, shadow, "SOFT PRODUCT SHADOW", 310, 1730, 850, 460, C.GRAPHITE, 26, 72);

    var product = group(d, "04_PRODUCT_SMART_OBJECT");
    placeSmart(d, product, "NAVIR S1 / REPLACEABLE SMART OBJECT", PRODUCT, 735, 1170, 1870, 17, BlendMode.SCREEN, 100);

    savePsdAndPng(d, ROOT + "NAVIR_S1_A01_Hero_CN_v01.psd", ROOT + "NAVIR_S1_A01_Hero_CN_v01.png");
    d.close(SaveOptions.DONOTSAVECHANGES);
}

function buildA02() {
    var d = newDoc(1464, 3416, "NAVIR_S1_A02_Performance_CN_v01", C.DEEP);
    d.layers[0].name = "01_BACKGROUND / DEEP CIRCUIT";

    var flow = group(d, "02_PERFORMANCE_COLOR_FIELDS");
    addRect(d, flow, "DEEP CIRCUIT FIELD", 0, 0, 1464, 2310, C.DEEP, 100);
    addEllipse(d, flow, "ION BLUE AIR VOLUME", 610, 190, 1200, 1550, C.BLUE, 100, 0);
    addRing(d, flow, "WIDE AIR RING", 620, 255, 950, 950, 115, C.WHITE, 15);
    addEllipse(d, flow, "BLUE DIFFUSION", 330, 640, 1120, 1320, C.BLUE2, 25, 95);
    addEllipse(d, flow, "NEUTRAL MATERIAL SHIELD", 440, 120, 1080, 1960, C.GRAPHITE, 90, 70);
    addRect(d, flow, "COOL WHITE PROOF FIELD", 0, 2310, 1464, 1106, C.WHITE, 100);
    addRect(d, flow, "BLUE SEAM", 0, 2270, 1464, 40, C.BLUE, 100);

    var copy = group(d, "05_COPY_CN / EDITABLE");
    addText(d, copy, "SECTION", "02  性能参数", 104, 170, 28, C.WHITE, "MicrosoftYaHei-Bold", 120, 76);
    addText(d, copy, "KICKER", "高速动力", 106, 330, 52, C.WHITE, "MicrosoftYaHei-Bold", 45, 100);
    addText(d, copy, "PRIMARY VALUE", "110,000", 92, 610, 176, C.WHITE, "Arial-BoldMT", -35, 100);
    addText(d, copy, "PRIMARY UNIT", "RPM", 102, 770, 67, C.WHITE, "Arial-BoldMT", 65, 100);
    addText(d, copy, "PRIMARY COPY", "强劲气流快速带走湿气", 106, 930, 34, C.WHITE, "MicrosoftYaHei", 32, 84);
    addText(d, copy, "CONCEPT NOTE TOP", "概念参数 / 作品集展示", 106, 1005, 22, C.WHITE, "MicrosoftYaHei", 70, 58);

    addText(d, copy, "AIRFLOW TITLE", "空气被塑形，而不是被堆叠。", 104, 2160, 42, C.WHITE, "MicrosoftYaHei-Bold", 15, 100);

    addText(d, copy, "PROOF LABEL", "辅助参数", 104, 2478, 27, C.BLUE, "MicrosoftYaHei-Bold", 100, 100);
    addRect(d, flow, "SECONDARY CARD 01", 104, 2550, 604, 580, "EEF2F8", 100);
    addRect(d, flow, "SECONDARY CARD 02", 756, 2550, 604, 580, C.DEEP, 100);
    addRect(d, flow, "SECONDARY ACCENT 01", 104, 2550, 604, 20, C.BLUE, 100);
    addRect(d, flow, "SECONDARY ACCENT 02", 756, 2550, 604, 20, C.BLUE, 100);
    addText(d, copy, "SECONDARY VALUE 01", "20 m/s", 152, 2730, 72, C.BLUE, "Arial-BoldMT", -10, 100);
    addText(d, copy, "SECONDARY TITLE 01", "高速定向气流", 154, 2838, 34, C.DEEP, "MicrosoftYaHei-Bold", 25, 100);
    addText(d, copy, "SECONDARY COPY 01", "外部气流表现\r不展示虚构内部结构", 154, 2960, 25, C.GRAY, "MicrosoftYaHei", 15, 100);
    addText(d, copy, "SECONDARY VALUE 02", "50次/秒", 804, 2730, 66, C.WHITE, "MicrosoftYaHei-Bold", -20, 100);
    addText(d, copy, "SECONDARY TITLE 02", "实时温度监测", 806, 2838, 34, C.WHITE, "MicrosoftYaHei-Bold", 25, 100);
    addText(d, copy, "SECONDARY COPY 02", "持续感知出风温度\r辅助舒适干发体验", 806, 2960, 25, C.SILVER, "MicrosoftYaHei", 15, 100);
    addText(d, copy, "FOOTNOTE", "所有数值为概念设定，仅用于作品集视觉展示。", 104, 3324, 22, C.GRAY, "MicrosoftYaHei", 35, 100);

    var product = group(d, "04_OUTLET_SMART_OBJECT");
    placeSmart(d, product, "NAVIR S1 OUTLET / REPLACEABLE SMART OBJECT", PRODUCT, 1110, 1300, 1850, -4, BlendMode.SCREEN, 100);

    var highlight = group(d, "03_OUTLET_LIGHT_AND_SHADOW");
    addEllipse(d, highlight, "OUTLET LIGHT", 610, 290, 830, 830, C.WHITE, 12, 55);

    // Keep product above the lighting layer.
    product.move(highlight, ElementPlacement.PLACEBEFORE);

    savePsdAndPng(d, ROOT + "NAVIR_S1_A02_Performance_CN_v01.psd", ROOT + "NAVIR_S1_A02_Performance_CN_v01.png");
    d.close(SaveOptions.DONOTSAVECHANGES);
}

function buildMaster() {
    var d = newDoc(1464, 4392, "NAVIR_S1_VisualMaster_1x3_v01", C.WHITE);
    d.layers[0].name = "BASE";
    var bg = group(d, "VISUAL MASTER COLOR FIELDS");
    addRect(d, bg, "HEADER DEEP", 0, 0, 1464, 1210, C.DEEP, 100);
    addEllipse(d, bg, "HEADER ION VOLUME", 760, -300, 980, 1180, C.BLUE, 100, 0);
    addRing(d, bg, "HEADER AIR RING", 720, 60, 870, 870, 105, C.WHITE, 13);
    addEllipse(d, bg, "HEADER NEUTRAL MATERIAL SHIELD", 700, -90, 790, 1170, C.GRAPHITE, 88, 58);
    addRect(d, bg, "PALETTE FIELD", 0, 1210, 1464, 790, C.PAPER, 100);
    addRect(d, bg, "TYPE FIELD", 0, 2000, 1464, 930, C.WHITE, 100);
    addRect(d, bg, "MATERIAL FIELD", 0, 2930, 1464, 760, C.BLUE, 100);
    addRect(d, bg, "CONTINUITY FIELD", 0, 3690, 1464, 702, C.DEEP, 100);

    var copy = group(d, "MASTER COPY / EDITABLE");
    addText(d, copy, "MASTER BRAND", "NAVIR S1", 92, 150, 45, C.WHITE, "MicrosoftYaHei-Bold", 170, 100);
    addText(d, copy, "MASTER TITLE", "视觉母版 01", 92, 320, 92, C.WHITE, "MicrosoftYaHei-Bold", 20, 100);
    addText(d, copy, "MASTER META", "珍珠白 × 钛银 × Ion Blue\r光线从左上方进入，产品保持中性材质。", 96, 470, 28, C.WHITE, "MicrosoftYaHei", 35, 78);
    addText(d, copy, "PALETTE TITLE", "品牌色与明度节奏", 92, 1350, 46, C.DEEP, "MicrosoftYaHei-Bold", 25, 100);
    var swY = 1480, swW = 248, swH = 260;
    addRect(d, bg, "SWATCH WHITE", 92, swY, swW, swH, C.WHITE, 100);
    addRect(d, bg, "SWATCH SILVER", 356, swY, swW, swH, C.SILVER, 100);
    addRect(d, bg, "SWATCH BLUE", 620, swY, swW, swH, C.BLUE, 100);
    addRect(d, bg, "SWATCH DEEP", 884, swY, swW, swH, C.DEEP, 100);
    addRect(d, bg, "SWATCH GRAPHITE", 1148, swY, 224, swH, C.GRAPHITE, 100);
    addText(d, copy, "SWATCH 01", "冷白\r#F7F9FC", 112, 1805, 23, C.DEEP, "MicrosoftYaHei", 20, 100);
    addText(d, copy, "SWATCH 02", "钛银\r#CAD0DA", 376, 1805, 23, C.DEEP, "MicrosoftYaHei", 20, 100);
    addText(d, copy, "SWATCH 03", "Ion Blue\r#3157FF", 640, 1805, 23, C.DEEP, "MicrosoftYaHei", 20, 100);
    addText(d, copy, "SWATCH 04", "Deep Circuit\r#0A1940", 904, 1805, 23, C.DEEP, "MicrosoftYaHei", 20, 100);
    addText(d, copy, "SWATCH 05", "石墨黑\r#111722", 1168, 1805, 23, C.DEEP, "MicrosoftYaHei", 20, 100);

    addText(d, copy, "TYPE TITLE", "中文字体层级", 92, 2150, 46, C.DEEP, "MicrosoftYaHei-Bold", 25, 100);
    addText(d, copy, "TYPE DISPLAY", "高速吹风机", 92, 2385, 138, C.DEEP, "MicrosoftYaHei-Bold", -25, 100);
    addText(d, copy, "TYPE NUMERIC", "110,000 RPM", 94, 2565, 70, C.BLUE, "Arial-BoldMT", -20, 100);
    addText(d, copy, "TYPE BODY", "主标题负责记忆点；数值只保留一个核心层级。", 96, 2720, 29, C.GRAY, "MicrosoftYaHei", 30, 100);

    addText(d, copy, "MATERIAL TITLE", "产品材质不受环境色污染", 92, 3085, 43, C.WHITE, "MicrosoftYaHei-Bold", 20, 100);
    addText(d, copy, "MATERIAL BODY", "珍珠白 / 钛银 / 石墨黑\r冷白高光 + 克制反射 + 清晰轮廓", 94, 3225, 29, C.WHITE, "MicrosoftYaHei", 35, 82);
    addEllipse(d, bg, "MATERIAL PEARL", 820, 3050, 260, 260, C.WHITE, 100, 0);
    addEllipse(d, bg, "MATERIAL SILVER", 1030, 3200, 260, 260, C.SILVER, 100, 0);
    addEllipse(d, bg, "MATERIAL GRAPHITE", 1180, 2990, 190, 190, C.GRAPHITE, 100, 0);

    addText(d, copy, "CONT TITLE", "A01 → A02", 92, 3860, 62, C.WHITE, "Arial-BoldMT", 20, 100);
    addText(d, copy, "CONT BODY", "由产品认知进入性能证明\r同一光线、同一蓝色体块、同一中文层级。", 96, 3995, 29, C.WHITE, "MicrosoftYaHei", 30, 78);
    addRect(d, bg, "CONT BLUE", 880, 3810, 420, 470, C.BLUE, 100);
    addRing(d, bg, "CONT RING", 990, 3840, 390, 390, 60, C.WHITE, 18);

    var prod = group(d, "MASTER PRODUCT SMART OBJECT");
    placeSmart(d, prod, "NAVIR S1 / MATERIAL REFERENCE", PRODUCT, 1080, 615, 1040, 14, BlendMode.SCREEN, 100);

    savePngOnly(d, ROOT + "NAVIR_S1_VisualMaster_1x3_v01.png");
    d.close(SaveOptions.DONOTSAVECHANGES);
}

function buildConcat() {
    var a = app.open(new File(ROOT + "NAVIR_S1_A01_Hero_CN_v01.png"));
    a.selection.selectAll();
    a.selection.copy();
    a.close(SaveOptions.DONOTSAVECHANGES);
    var out = app.documents.add(1464, 6832, 72, "NAVIR_S1_A01-A02_Concat_CN_v01", NewDocumentMode.RGB, DocumentFill.WHITE);
    out.paste();
    var l1 = out.activeLayer;
    l1.name = "A01 HERO";
    var b = l1.bounds;
    l1.translate(-b[0].as("px"), -b[1].as("px"));

    var bdoc = app.open(new File(ROOT + "NAVIR_S1_A02_Performance_CN_v01.png"));
    bdoc.selection.selectAll();
    bdoc.selection.copy();
    bdoc.close(SaveOptions.DONOTSAVECHANGES);
    app.activeDocument = out;
    out.paste();
    var l2 = out.activeLayer;
    l2.name = "A02 PERFORMANCE";
    var bb = l2.bounds;
    l2.translate(-bb[0].as("px"), 3416 - bb[1].as("px"));
    out.flatten();
    try { out.convertProfile("sRGB IEC61966-2.1", Intent.PERCEPTUAL, true, true); } catch (e) {}
    var jpg = new JPEGSaveOptions();
    jpg.quality = 11;
    jpg.embedColorProfile = true;
    out.saveAs(new File(ROOT + "NAVIR_S1_A01-A02_Concat_CN_v01.jpg"), jpg, true, Extension.LOWERCASE);
    out.close(SaveOptions.DONOTSAVECHANGES);
}

buildMaster();
buildA01();
buildA02();
buildConcat();

"NAVIR_VISUAL_SAMPLE_V01_OK";
