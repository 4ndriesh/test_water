/**
 * Created by andriesh on 07.02.19.
 */
var tmp = [];
function createspinbox() {
    var tilesizew = 110;
    var tilesizeh = tilesizew;
    var component = Qt.createComponent("Label1.qml");
        for (var til = -1; til < 5; til++) {
            var tx = -tilesizew * til / 2;
            var ty = 500;
            var object = component.createObject(container, {
                "x": tx + width / 1.5,
                "y": ty
            });
        }
    }

function createObject(component,tx, ty, valop, nimage) {
    var object=component.createObject(container, {
        "x": tx + controlPanel1.width/1.5,
        "y": ty + controlPanel1.height-300,
        "opacity": valop,
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
    var listobjectlabel=[];
    var component = Qt.createComponent("Tile.qml");
    var label = Qt.createComponent("Label1.qml");
    for (var til = 0; til < store.length; til++) {
        var block=0;
        var tx=0;
        for (var tileid = 0; tileid < store[til].length; tileid++) {
            tx = -tilesizew * til / 2;
            var ty = -tilesizeh * tileid + tilesizeh * til / 2;

            if (store[til][tileid] === 1) {

            listobject.push(createObject(component,tx,ty,1,"0001.png"))
                block++;
            }
            else if (store[til][tileid] > 1) {
                listobject.push(createObject(component,tx,ty,0.7,"0002.png"))
            }

        }
       listobjectlabel.push(label.createObject(container, {
                "x": tx+controlPanel1.width-125,
                "y": til*tilesizeh/2+controlPanel1.height-200,
                "number":block
            }));


    }

    return [listobject,listobjectlabel];
}

function updateCanvas(tmp) {
    for(var j=0;j < tmp.length; j++)
        for (var i = 0; i < tmp[j].length; i++) {
            tmp[j][i].destroy();
    }
}

function test(sum) {
    updateCanvas(tmp);
    tmp = createCanvas(sum);

}
