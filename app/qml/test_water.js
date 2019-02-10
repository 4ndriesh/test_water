/**
 * Created by andriesh on 07.02.19.
 */
var tmp = [];
function createspinbox() {
    var tilesizew = 110;
    var tilesizeh = tilesizew;
    var component = Qt.createComponent("spinbox.qml");
        for (var til = -1; til < 5; til++) {
            var tx = -tilesizew * til / 2;
            var ty = 500;
            var object = component.createObject(container, {
                "x": tx + width / 1.5,
                "y": ty
            });
        }
    }

function createObject(component,tx, ty, nimage) {
    var object=component.createObject(container, {
        "x": tx + controlPanel1.width/1.5,
        "y": ty + controlPanel1.height-250,
        "numimage": nimage
    });
    if (object === null) {
        console.log("Error creating canvas");
    }
    return object
}
function createCanvas(store) {
    var tilesizew = 110;
    var tilesizeh = tilesizew / 2;
    var listobject=[];
    var component = Qt.createComponent("Tile.qml");
    for (var til = 0; til < store.length; til++) {
        for (var tileid = 0; tileid < store[til].length; tileid++) {
            var tx = -tilesizew * til / 2;
            var ty = -tilesizeh * tileid + tilesizeh * til / 2;

            if (store[til][tileid] === 1) {

            listobject.push(createObject(component,tx,ty,"0001.png"))
            }
            else if (store[til][tileid] > 1) {
                listobject.push(createObject(component,tx,ty,"0002.png"))
            }
        }
    }
    return listobject;
}

function updateCanvas(tmp) {
    for (var i = 0; i < tmp.length; i++) {
        tmp[i].destroy();
    }
}

function test(sum) {
    updateCanvas(tmp);
    tmp = createCanvas(sum);

}