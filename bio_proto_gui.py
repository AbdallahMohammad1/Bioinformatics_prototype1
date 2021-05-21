from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 419)
        MainWindow.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 31))
        self.menubar.setObjectName("menubar")
        self.menuopen = QtWidgets.QMenu(self.menubar)
        self.menuopen.setObjectName("menuopen")
        self.menuoptions = QtWidgets.QMenu(self.menubar)
        self.menuoptions.setObjectName("menuoptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionText_File = QtWidgets.QAction(MainWindow)
        self.actionText_File.setObjectName("actionText_File")
        self.actionGC_Content = QtWidgets.QAction(MainWindow)
        self.actionGC_Content.setObjectName("actionGC_Content")
        self.actionFrequency = QtWidgets.QAction(MainWindow)
        self.actionFrequency.setObjectName("actionFrequency")
        self.actionTranslate_Seq = QtWidgets.QAction(MainWindow)
        self.actionTranslate_Seq.setObjectName("actionTranslate_Seq")
        self.actionTranscription = QtWidgets.QAction(MainWindow)
        self.actionTranscription.setObjectName("actionTranscription")
        self.actionReverse = QtWidgets.QAction(MainWindow)
        self.actionReverse.setObjectName("actionReverse")
        self.actionCodon_Usage = QtWidgets.QAction(MainWindow)
        self.actionCodon_Usage.setObjectName("actionCodon_Usage")
        self.menuopen.addAction(self.actionText_File)
        self.menuoptions.addAction(self.actionGC_Content)
        self.menuoptions.addAction(self.actionFrequency)
        self.menuoptions.addAction(self.actionTranslate_Seq)
        self.menuoptions.addAction(self.actionTranscription)
        self.menuoptions.addAction(self.actionReverse)
        self.menuoptions.addAction(self.actionCodon_Usage)
        self.menubar.addAction(self.menuopen.menuAction())
        self.menubar.addAction(self.menuoptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuopen.setTitle(_translate("MainWindow", "open"))
        self.menuoptions.setTitle(_translate("MainWindow", "options"))
        self.actionText_File.setText(_translate("MainWindow", "Text File"))
        self.actionGC_Content.setText(_translate("MainWindow", "GC_Content"))
        self.actionFrequency.setText(_translate("MainWindow", "Frequency"))
        self.actionTranslate_Seq.setText(_translate("MainWindow", "Translate_Seq"))
        self.actionTranscription.setText(_translate("MainWindow", "Transcription"))
        self.actionReverse.setText(_translate("MainWindow", "Reverse"))
        self.actionCodon_Usage.setText(_translate("MainWindow", "Codon Usage"))