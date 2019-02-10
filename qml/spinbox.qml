import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
SpinBox {
      style: SpinBoxStyle{
          background: Rectangle {
              implicitWidth: 50
              implicitHeight: 30
              border.color: "black"
          }

      }

      onValueChanged: console.log(value)
  }