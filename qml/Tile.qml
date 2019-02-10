import QtQuick 2.5

Image {
    id: img
    property var numimage
    width: 100; height: 100
    source: "../texture/"+numimage
}