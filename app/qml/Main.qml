import QtQuick 2.7
import QtQuick.Controls 2.3
import "test_water.js" as MyScript

ApplicationWindow {
    color: "#C0C0C0"
    visible: true
    x: 400
    y: 200
    width: 1000
    height: 600
    title: "Test"
    Item {
        id: main
        width: 1000
        height: 600

        ControlPanel {
            id: controlPanel
            anchors.top: parent.top
            anchors.topMargin: 10
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.leftMargin: 10
        }

        Rectangle {
            id: controlPanel1
            border.color: "black"
            color: "Gainsboro"
            anchors.top: parent.top
            anchors.topMargin: 10
            anchors.bottom: parent.bottom
            anchors.left: controlPanel.right
            anchors.leftMargin: 10
            width: 600
            Item {
                id: container
                Component.onCompleted: store.gener()
            }

        }

        Projectlist{
            id: scopeView
            anchors.top: parent.top
            anchors.topMargin: 10
            anchors.bottom: parent.bottom
            anchors.right: parent.right
            anchors.left: controlPanel1.right
            anchors.leftMargin: 10
            height: main.height
            pixelSize:15
            internalModel: store
            objectName : "project"
        }

    }
    Connections {
        target: store
        onSumResult: {
        MyScript.test(generat);
        }

    }
}

