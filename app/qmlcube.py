from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QUrl
from PyQt5.QtQml import QQmlListProperty, QQmlApplicationEngine
from sys import argv

from matrix import Matrix
from generator import Generator
app = QGuiApplication(argv)
path_to_qml='./qml/cube3d.qml'

from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QUrl
from config import Config
gen=Generator()
class Pars_project(QObject):
    name_prj_or_st = pyqtSignal()

    def __init__(self, name, *args, **kwargs):
        # print('Channel')
        super().__init__(*args, **kwargs)

        self._name = name

    @pyqtProperty('QString', notify=name_prj_or_st)
    def name(self):
        return self._name

class Pars_station(QObject):
    Pars_project_Changed = pyqtSignal()

    def __init__(self, *args, **kwargs):
        # print('Store')
        super().__init__(*args, **kwargs)
        self.prj_or_st = []

    @pyqtProperty(QQmlListProperty, notify=Pars_project_Changed)
    def channels(self):
        return QQmlListProperty(Pars_project, self, self.prj_or_st)

    @channels.setter
    def channels(self, value):
        if value: self.prj_or_st.append(value)
        self.Pars_project_Changed.emit()
report = Pars_station()
class Signalslotsgen(QObject):

    sumResult = pyqtSignal([list],arguments=['sum'])

    @pyqtSlot(name="gener")
    def run(self):
        setting = Config.inst()
        self.matrix = Matrix(gen.create_matrix())
        self.matrix.change_matrix()
        self.matrix.delete_water_last_row()
        project = self.matrix.delete_water_last_row().transpose()[::-1].tolist()
        setting.version = project
        report.prj_or_st = []
        for rp in setting.version:
            report.channels = Pars_project(rp)
        self.sumResult.emit(project)

    def qml(self):

        sig=Signalslotsgen()
        view = QQmlApplicationEngine()
        view.rootContext().setContextProperty('sig', sig)
        view.rootContext().setContextProperty('store', report)
        view.load(path_to_qml)


        app.exec_()
