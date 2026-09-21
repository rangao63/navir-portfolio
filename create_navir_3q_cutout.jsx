#target photoshop

app.displayDialogs = DialogModes.NO;

var inputFile = new File("C:/Users/ecmax/Desktop/05/燃/亚马逊a+/Visual_Sample_v01/Assets/NAVIR_S1_3Q_Raw_v01.png");
var outputFile = new File("C:/Users/ecmax/Desktop/05/燃/亚马逊a+/Visual_Sample_v01/Assets/NAVIR_S1_3Q_Cutout_v01.png");

var src = app.open(inputFile);
src.activeLayer = src.layers[0];

// Photoshop Select Subject keeps the high-frequency vents and cable more reliably
// than a color-range selection against the dark render background.
var autoDesc = new ActionDescriptor();
autoDesc.putBoolean(stringIDToTypeID("sampleAllLayers"), false);
executeAction(stringIDToTypeID("autoCutout"), autoDesc, DialogModes.NO);

src.selection.copy();
var out = app.documents.add(src.width, src.height, src.resolution, "NAVIR_S1_3Q_Cutout_v01", NewDocumentMode.RGB, DocumentFill.TRANSPARENT);
out.paste();
out.activeLayer.name = "NAVIR S1 3Q Product";

// Restore the defining open air tunnel. The coordinates are limited to the
// erroneous center cap in the raw 1024 x 1536 render and leave the inner ring.
var cx = 340, cy = 258, rx = 61, ry = 66;
var pts = [];
for (var i = 0; i < 64; i++) {
    var a = Math.PI * 2 * i / 64;
    pts.push([cx + Math.cos(a) * rx, cy + Math.sin(a) * ry]);
}
out.selection.select(pts);
out.selection.feather(1.2);
out.selection.clear();
out.selection.deselect();

var pngOpt = new PNGSaveOptions();
pngOpt.interlaced = false;
out.saveAs(outputFile, pngOpt, true, Extension.LOWERCASE);

out.close(SaveOptions.DONOTSAVECHANGES);
src.close(SaveOptions.DONOTSAVECHANGES);

"CUTOUT_OK";
