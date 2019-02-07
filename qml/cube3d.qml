import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4
import QtQuick 2.11
import "test_water.js" as MyScript

ApplicationWindow {
id: win
    color: "#C0C0C0"
    visible: true
    x: 400
    y: 200
    width: 1000
    height: 550
    title: "Create report"

Item {
     id: container
     width: 500; height: 100

 }
 Button {
        text: "Ok"
        onClicked:
        sig.gener();

//        MyScript.updateCanvas();


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