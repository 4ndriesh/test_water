import os
from sys import argv

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlListProperty, QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot

from matrix import Matrix
from generator import Generator

from config import Config

gen = Generator()
setting = Config.inst()

class Pars_project(QObject):
    name_prj_or_st = pyqtSignal()

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name

    @pyqtProperty('QString', notify=name_prj_or_st)
    def name(self):
        return self._name


class Pars_station(QObject):
    Pars_project_Changed = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prj_or_st = []

    sumResult = pyqtSignal([list], arguments=['generat'])

    @pyqtSlot(str, name="generat_cube")
    def generat_cube(self, checked):
        setting = Config.inst()
        mass = setting.version[checked]
        if mass: self.emitproject(mass)

    @pyqtProperty(QQmlListProperty, notify=Pars_project_Changed)
    def channels(self):
        return QQmlListProperty(Pars_project, self, self.prj_or_st)

    @channels.setter
    def channels(self, value):
        if value: self.prj_or_st.append(value)
        self.Pars_project_Changed.emit()

    @pyqtSlot(name="gener")
    def getmatrix(self):
        mass = gen.create_matrix_rnd()
        self.run(mass)

    def run(self, mass):

        self.matrix = Matrix(mass)
        self.matrix.change_matrix()
        self.matrix.delete_water_last_row()
        project = self.matrix.delete_water_last_row().transpose()[::-1].tolist()
        report.prj_or_st = []
        setting.version = project
        for rp in sorted(setting.version.keys(), reverse=True):
            report.channels = Pars_project(rp)
        self.emitproject(project)

    def emitproject(self, project):
        self.sumResult.emit(project)


report = Pars_station()
app = QGuiApplication(argv)

def qml():
    path_to_qml = os.path.join(setting.BASE_DIR, 'qml', 'Main.qml')
    view = QQmlApplicationEngine()
    view.rootContext().setContextProperty('store', report)
    view.load(path_to_qml)
    app.exec_()
