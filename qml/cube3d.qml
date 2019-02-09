import QtQuick 2.2
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4
import "test_water.js" as MyScript

ApplicationWindow {

    color: "#C0C0C0"
    visible: true
    x: 400
    y: 200
    width: 1000
    height: 550
    title: "Create report"

            Item {
             id: container
//             Component.onCompleted: sig.gener(),MyScript.createspinbox();
            }
    Button {
            text: "Ok"
            onClicked:
            sig.gener();
        }

    Rectangle {
    anchors.right: parent.right
    height: parent.height
    width: 200
    GridLayout{
            anchors.fill: parent
            columns: 1
                Projectlist{
                pixelSize:15
                internalModel: store
                objectName : "project"
                dialogview: false
                }

    }

    }
 Connections {
        target: sig

        // Обработчик сигнала сложения
        onSumResult: {
            // sum было задано через arguments=['sum']
//            sumResult.text = sum
        MyScript.test(sum);
        }

    }
}
