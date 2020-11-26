import PyQt5.QtWidgets as QW
import sys
import sqlite3
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 353)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 471, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 471, 266))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(10, 40, 231, 23))
        self.btn.setObjectName("btn")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(250, 40, 231, 23))
        self.btn2.setObjectName("btn2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кофеёчек"))
        self.comboBox.setCurrentText(_translate("MainWindow", "-"))
        self.comboBox.setItemText(0, _translate("MainWindow", "-"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Эспрессо"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Кофе по-венски"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Медовый раф"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Айриш"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Капуччино"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Гляссе"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Кофе по-турецки"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Ристретто"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Латте"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Мокко"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Американо"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Мокаччино"))
        self.btn.setText(_translate("MainWindow", "Добавить вид кофе"))
        self.btn2.setText(_translate("MainWindow", "Редактировать вид кофе"))


class Ui_DialogWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 276)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(120, 10, 331, 20))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 40, 331, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 70, 331, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 100, 331, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 130, 331, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 160, 331, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(120, 190, 331, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 220, 331, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 91, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 91, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 91, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 91, 21))
        self.label_8.setObjectName("label_8")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(10, 250, 441, 23))
        self.save_btn.setObjectName("save_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить/Изменить кофе"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.label_3.setText(_translate("MainWindow", "Сорт"))
        self.label_4.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_5.setText(_translate("MainWindow", "Вид"))
        self.label_6.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_7.setText(_translate("MainWindow", "Цена"))
        self.label_8.setText(_translate("MainWindow", "Объем упаковки"))
        self.save_btn.setText(_translate("MainWindow", "Сохранить"))


class CoffeeInfo(QW.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.setCurrentText("-")
        self.comboBox.currentTextChanged.connect(self.set_info)
        self.btn.clicked.connect(self.add_coffee)
        self.btn2.clicked.connect(self.edit_coffee)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.title = ["ID",
                      "Название",
                      "Сорт",
                      "Степень обжарки",
                      "Вид",
                      "Описание вкуса",
                      "Цена",
                      "Объем упаковки"]

    def add_coffee(self):
        self.dialog = AddDialog(par=self)
        self.dialog.show()

    def edit_coffee(self):
        self.dialog = AddDialog(self.comboBox.currentText(), self)
        self.dialog.show()

    def set_info(self):
        try:
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setRowCount(8)
            self.tableWidget.setVerticalHeaderLabels(self.title)
            self.tableWidget.setHorizontalHeaderLabels(["Характеристики"])
            title = self.comboBox.currentText()
            info = self.cur.execute(f"""SELECT * FROM coffee WHERE Name = '{title}'""").fetchall()[0]
            for i, elem in enumerate(info):
                self.tableWidget.setItem(i, 0, QW.QTableWidgetItem(str(elem)))
            self.tableWidget.setColumnWidth(0, 360)
        except:
            pass


class AddDialog(QW.QMainWindow, Ui_DialogWindow):
    def __init__(self, title="", par=None):
        super().__init__()
        self.setupUi(self)
        self.title = title
        self.par = par
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        if self.title != "":
            self.set_params()
        self.save_btn.clicked.connect(self.accept)

    def accept(self):
        if self.check_all():
            Id = list(map(lambda x: str(x[0]), self.cur.execute("""SELECT ID FROM coffee""").fetchall()))
            if self.lineEdit_1.text() in Id and self.title == "":
                message = QW.QMessageBox.question(
                    self, '', f"Кофе с таким ID уже существует! Попробуйте другой",
                    QW.QMessageBox.Ok)
            else:
                self.cur.execute(f"""DELETE FROM coffee
                            WHERE Name = '{self.lineEdit_2.text()}'""")
                self.cur.execute(f"""INSERT INTO coffee
                                VALUES ('{self.lineEdit_1.text()}', '{self.lineEdit_2.text()}',
                                '{self.lineEdit_3.text()}', '{self.lineEdit_4.text()}',
                                '{self.lineEdit_5.text()}', '{self.lineEdit_6.text()}',
                                '{self.lineEdit_7.text()}', '{self.lineEdit_8.text()}');""")
                self.con.commit()
                self.par.comboBox.clear()
                content = self.cur.execute("""SELECT DISTINCT Name, ID FROM coffee
                        ORDER BY ID ASC""").fetchall()
                content = list(map(lambda x: [x[0], int(x[1])], content))
                content.sort(key=lambda x: x[1])
                for i in content:
                    self.par.comboBox.addItem(i[0])
                self.destroy()
        else:
            message = QW.QMessageBox.question(
                self, '', f"Не все поля заполнены! Заполните всё.",
                QW.QMessageBox.Ok)

    def set_params(self):
        params = self.cur.execute(f"""SELECT * FROM coffee WHERE Name = '{self.title}'""").fetchall()[0]
        for i in range(8):
            eval(f"self.lineEdit_{i + 1}.setText('{params[i]}')")

    def check_all(self):
        c = 0
        for i in range(1, 9):
            if eval(f"self.lineEdit_{i}.text() == ''"):
                break
            c += 1
        return c == 8


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QW.QApplication(sys.argv)
    ex = CoffeeInfo()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
