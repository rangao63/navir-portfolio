#target photoshop
app.displayDialogs = DialogModes.NO;
app.preferences.rulerUnits = Units.PIXELS;

var inputFile = new File("C:/Users/ecmax/Desktop/05/燃/亚马逊a+/Visual_Sample_v01/Assets/NAVIR_S1_3Q_ScreenAsset_v01.png");
var outputFile = new File("C:/Users/ecmax/Desktop/05/燃/亚马逊a+/Visual_Sample_v01/Assets/NAVIR_S1_3Q_Cutout_v02.png");
var src = app.open(inputFile);

// Outer silhouette, traced from the approved generated 3/4 viewpoint.
// Dense points keep the mask smooth while preserving the dark vents inside.
var p = [
 [30,122],[40,82],[70,48],[120,27],[190,18],[280,16],[390,20],[500,28],
 [590,44],[655,72],[704,116],[736,174],[752,235],[752,318],[742,382],
 [716,430],[680,465],[636,486],[586,501],[543,520],[518,552],[506,608],
 [502,720],[500,850],[494,980],[487,1066],[475,1114],[455,1152],[431,1181],
 [420,1220],[420,1270],[410,1335],[405,1410],[402,1514],[318,1514],[318,1420],
 [323,1345],[329,1270],[325,1217],[300,1190],[274,1162],[253,1128],[242,1080],
 [239,1000],[243,890],[248,770],[252,655],[253,570],[245,526],[222,498],
 [181,478],[132,458],[92,428],[60,392],[39,350],[24,302],[17,252],[18,196]
];

src.activeLayer.isBackgroundLayer = false;
src.activeLayer.name = "NAVIR S1 3Q Neutral Product";
src.selection.select(p);
src.selection.feather(1.5);
src.selection.invert();
src.selection.clear();
src.selection.deselect();

// Open the signature hollow air tunnel while leaving the black inner ring intact.
var hole = [];
var cx = 210, cy = 248, rx = 62, ry = 67;
for (var i = 0; i < 96; i++) {
    var a = Math.PI * 2 * i / 96;
    hole.push([cx + Math.cos(a) * rx, cy + Math.sin(a) * ry]);
}
src.selection.select(hole);
src.selection.feather(1.0);
src.selection.clear();
src.selection.deselect();

var png = new PNGSaveOptions();
png.interlaced = false;
src.saveAs(outputFile, png, true, Extension.LOWERCASE);
src.close(SaveOptions.DONOTSAVECHANGES);
"POLYGON_CUTOUT_OK";
