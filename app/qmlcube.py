from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QUrl
from PyQt5.QtQml import QQmlListProperty, QQmlApplicationEngine
from sys import argv

from matrix import Matrix
from generator import Generator
app = QGuiApplication(argv)
path_to_qml='./qml/cube3d.qml'

from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QUrl
gen=Generator()
class Signalslotsgen(QObject):
    sumResult = pyqtSignal([list],arguments=['sum'])
    @pyqtSlot(name="gener")
    def run(self):
        self.matrix = Matrix(gen.create_matrix())
        self.matrix.change_matrix()
        self.matrix.delete_water_last_row()
        project = self.matrix.delete_water_last_row().transpose().tolist()
        self.sumResult.emit(project)

    def qml(self):
        self.run()
        sig=Signalslotsgen()
        project = self.matrix.delete_water_last_row().transpose().tolist()
        # project = [[1, 7, 7,4], [5, 6, 4], [7,1],[],[7, 8, 9,1],[0, 8, 9,1],[0, 8, 9,7]]
        view = QQmlApplicationEngine()
        view.rootContext().setContextProperty('store', project)
        view.rootContext().setContextProperty('sig', sig)
        view.load(path_to_qml)
        app.exec_()
