from versionList import addToBox
from downolandServer import downoland
from firstLaunch import launch,setProperties
from run import run
from ui import Ui_MainWindow
from database import firstLaunch,add,refresh

from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.add)

        addToBox(self.comboBox_2)

        self.pushButton_2.clicked.connect(self.browse)
        self.pushButton.clicked.connect(self.run)

        firstLaunch()

        refresh(self.comboBox)

    def run(self):
        run(self.comboBox.currentText())

    def browse(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory()
        filename = filename.replace("/","\\")
        self.lineEdit_4.setText(filename)

    def add(self):
        path = self.lineEdit_4.text()
        if(self.lineEdit.text().strip()!="" and self.lineEdit_2.text().strip().isnumeric() and self.lineEdit_3.text().strip().isnumeric()):
            if(downoland(self.comboBox_2.currentText(),path)):
                add(self.lineEdit.text(),path)
                launch(self.lineEdit_3.text(),path)
                setProperties(self.lineEdit.text(),self.comboBox_3.currentText(),self.lineEdit_2.text(),self.comboBox_4.currentText(),self.comboBox_5.currentText(),self.comboBox_6.currentText(),path)
                refresh(self.comboBox)
        else:
            print("Check values!")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()