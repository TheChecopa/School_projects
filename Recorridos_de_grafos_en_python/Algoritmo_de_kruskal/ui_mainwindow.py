# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(999, 565)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionPrim = QAction(MainWindow)
        self.actionPrim.setObjectName(u"actionPrim")
        self.actionKruskal = QAction(MainWindow)
        self.actionKruskal.setObjectName(u"actionKruskal")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 51, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 71, 16))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 90, 71, 16))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 120, 71, 16))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 150, 71, 16))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 180, 71, 16))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 210, 71, 16))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 240, 71, 16))
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 270, 71, 16))
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 300, 71, 16))
        self.origenX_spinBox = QSpinBox(self.groupBox)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")
        self.origenX_spinBox.setGeometry(QRect(100, 60, 61, 22))
        self.origenX_spinBox.setMaximum(500)
        self.origenY_spinBox = QSpinBox(self.groupBox)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setGeometry(QRect(100, 90, 61, 22))
        self.origenY_spinBox.setMaximum(500)
        self.destinoX_spinBox = QSpinBox(self.groupBox)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setGeometry(QRect(100, 120, 61, 22))
        self.destinoX_spinBox.setMaximum(500)
        self.destinoY_spinBox = QSpinBox(self.groupBox)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setGeometry(QRect(100, 150, 61, 22))
        self.destinoY_spinBox.setMaximum(500)
        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setGeometry(QRect(100, 240, 61, 22))
        self.red_spinBox.setMaximum(255)
        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setGeometry(QRect(100, 270, 61, 22))
        self.green_spinBox.setMaximum(255)
        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setGeometry(QRect(100, 300, 61, 22))
        self.blue_spinBox.setMaximum(255)
        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")
        self.agregar_final_pushButton.setGeometry(QRect(40, 350, 161, 23))
        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")
        self.agregar_inicio_pushButton.setGeometry(QRect(40, 380, 161, 23))
        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")
        self.mostrar_pushButton.setGeometry(QRect(40, 410, 161, 23))
        self.salida = QPlainTextEdit(self.groupBox)
        self.salida.setObjectName(u"salida")
        self.salida.setGeometry(QRect(220, 70, 271, 211))
        self.ordenar_Id_pushButton = QPushButton(self.groupBox)
        self.ordenar_Id_pushButton.setObjectName(u"ordenar_Id_pushButton")
        self.ordenar_Id_pushButton.setGeometry(QRect(210, 350, 151, 23))
        self.ordenar_Distancia_pushButton = QPushButton(self.groupBox)
        self.ordenar_Distancia_pushButton.setObjectName(u"ordenar_Distancia_pushButton")
        self.ordenar_Distancia_pushButton.setGeometry(QRect(210, 380, 151, 23))
        self.ordenar_Velocidad_pushButton = QPushButton(self.groupBox)
        self.ordenar_Velocidad_pushButton.setObjectName(u"ordenar_Velocidad_pushButton")
        self.ordenar_Velocidad_pushButton.setGeometry(QRect(210, 410, 151, 23))
        self.graphicsView_Grafo = QGraphicsView(self.groupBox)
        self.graphicsView_Grafo.setObjectName(u"graphicsView_Grafo")
        self.graphicsView_Grafo.setGeometry(QRect(540, 50, 391, 391))
        self.Profundidad_pushButton = QPushButton(self.groupBox)
        self.Profundidad_pushButton.setObjectName(u"Profundidad_pushButton")
        self.Profundidad_pushButton.setGeometry(QRect(370, 350, 141, 23))
        self.Amplitud_pushButton = QPushButton(self.groupBox)
        self.Amplitud_pushButton.setObjectName(u"Amplitud_pushButton")
        self.Amplitud_pushButton.setGeometry(QRect(370, 380, 141, 23))
        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(100, 30, 61, 22))
        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(100, 180, 61, 22))

        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_2.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_2.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_2.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_2.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_4.addWidget(self.limpiar, 1, 1, 1, 1)

        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_4.addWidget(self.dibujar, 1, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 999, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionPrim)
        self.menuArchivo.addAction(self.actionKruskal)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrim.setText(QCoreApplication.translate("MainWindow", u"Algoritmo de Prim", None))
        self.actionKruskal.setText(QCoreApplication.translate("MainWindow", u"Algoritmo de Kruskal", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en X:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en Y:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR FINAL", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR INICIO", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.ordenar_Id_pushButton.setText(QCoreApplication.translate("MainWindow", u"ORDENAR ID", None))
        self.ordenar_Distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"ORDENAR DISTANCIA", None))
        self.ordenar_Velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"ORDENAR VELOCIDAD", None))
        self.Profundidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"BUSQUEDA PROFUNDIDAD", None))
        self.Amplitud_pushButton.setText(QCoreApplication.translate("MainWindow", u"BUSQUEDA AMPLITUD", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id de la particula", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

