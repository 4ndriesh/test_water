/**
 * Created by andriesh on 07.02.19.
 */
var tmp=[];
function createCanvas(store) {
    var tilesizew= 110;
    var tilesizeh= tilesizew / 2;
    var object=[]
    var component = Qt.createComponent("Tile.qml");
    for (var til = 0; til < store.length; til++) {
        for (var tileid = 0; tileid < store[til].length; tileid++) {
            var tx = -tilesizew * til / 2;
            var ty = -tilesizeh * tileid + tilesizeh * til / 2;

            if (store[til][tileid] === 1) {
                object.push(component.createObject(container,{
                "x" : tx + width / 2,
                "y" : ty + height / 2,
                "numimage" : "0002.png"
                }));
                if (object === null) {
                console.log("Error creating canvas");
                }


            }
            else if (store[til][tileid] > 1) {
                object.push(component.createObject(container,{
                "x" : tx + width / 2,
                "y" : ty + height / 2,
                "numimage" : "0005.png"
                }));



            }
        }
    }
    return object;
}

function updateCanvas(tmp) {
    // sig.gener()
    //         var tmp = createCanvas();
            for (var i=0;i<tmp.length;i++){
                tmp[i].destroy();
            }

        }

function test(sum) {

    updateCanvas(tmp);
    tmp= createCanvas(sum);

        }
