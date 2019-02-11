# обработка сигналов окна
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
matrix = Matrix()


class List_save(QObject):
    name_prj_or_st = pyqtSignal()

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name

    @pyqtProperty('QString', notify=name_prj_or_st)
    def name(self):
        return self._name


class Emit_save_to_qml(QObject):
    Save_Changed = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prj_or_st = []

    sumResult = pyqtSignal([list], arguments=['generat'])

    @pyqtSlot(str, name="generat_cube")
    def generat_cube(self, checked):
        setting = Config.inst()
        mass = setting.version[checked]
        if mass: self.emitproject(mass)

    @pyqtProperty(QQmlListProperty, notify=Save_Changed)
    def channels(self):
        return QQmlListProperty(List_save, self, self.prj_or_st)

    @channels.setter
    def channels(self, value):
        if value: self.prj_or_st.append(value)
        self.Save_Changed.emit()

    @pyqtSlot(name="gener")
    def getmatrix(self):
        mass = gen.getGenerator
        self.run(mass)

    def run(self, mass):
        matrix.get_obj_with_water = mass
        project = matrix.get_obj_with_water
        report.prj_or_st = []
        setting.version = project
        for rp in sorted(setting.version.keys(), reverse=True):
            report.channels = List_save(rp)
        self.emitproject(project)
        return project

    def emitproject(self, project):
        self.sumResult.emit(project)


report = Emit_save_to_qml()
app = QGuiApplication(argv)


def qml():
    path_to_qml = os.path.join(setting.BASE_DIR, 'qml', 'Main.qml')
    view = QQmlApplicationEngine()
    view.rootContext().setContextProperty('store', report)
    view.load(path_to_qml)
    app.exec_()
