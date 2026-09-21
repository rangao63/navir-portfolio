#target photoshop
app.displayDialogs = DialogModes.NO;
var root = "C:/Users/ecmax/Desktop/05/燃/亚马逊a+/Visual_Sample_v01/";
var files = [
    root + "NAVIR_S1_A01_Hero_CN_v01.psd",
    root + "NAVIR_S1_A02_Performance_CN_v01.psd"
];

function inspectContainer(container, stats, names) {
    for (var i = 0; i < container.layers.length; i++) {
        var l = container.layers[i];
        names.push(l.name);
        if (l.typename == "LayerSet") {
            stats.groups++;
            inspectContainer(l, stats, names);
        } else {
            stats.layers++;
            if (l.kind == LayerKind.TEXT) stats.text++;
            try { if (l.kind == LayerKind.SMARTOBJECT) stats.smart++; } catch (e) {}
        }
    }
}

var lines = [];
for (var f = 0; f < files.length; f++) {
    var doc = app.open(new File(files[f]));
    var stats = {groups:0,layers:0,text:0,smart:0};
    var names = [];
    inspectContainer(doc, stats, names);
    lines.push(doc.name + "|" + doc.width.as("px") + "x" + doc.height.as("px") + "|mode=" + doc.mode + "|bits=" + doc.bitsPerChannel + "|groups=" + stats.groups + "|layers=" + stats.layers + "|text=" + stats.text + "|smart=" + stats.smart + "|top=" + names.slice(0,12).join(","));
    doc.close(SaveOptions.DONOTSAVECHANGES);
}
lines.join("\n");
