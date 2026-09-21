#target photoshop
app.displayDialogs = DialogModes.NO;
var inputFile = new File("C:/Users/ecmax/Desktop/05/燃/亚马逊a+/Visual_Sample_v01/Assets/NAVIR_S1_3Q_Raw_v01.png");
var outputFile = new File("C:/Users/ecmax/Desktop/05/燃/亚马逊a+/Visual_Sample_v01/Assets/NAVIR_S1_3Q_ScreenAsset_v01.png");
var doc = app.open(inputFile);
doc.crop([130, 10, 900, 1530]);
var png = new PNGSaveOptions();
png.interlaced = false;
doc.saveAs(outputFile, png, true, Extension.LOWERCASE);
doc.close(SaveOptions.DONOTSAVECHANGES);
"SCREEN_ASSET_OK";
