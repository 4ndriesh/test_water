import QtQuick 2.1
import QtQuick.Layouts 1.0

  ColumnLayout {
      Text {
          text: "Scope"
          font.pointSize: 18
          color: "white"
      }

      MultiButton {
          id: openGLButton
          text: "RANDOM"
          items: [""]
          currentSelection: 0
      }


  }