import sys
from PyQt5.QtWidgets import (QLineEdit, QInputDialog)
import disein
import commands.gPonZTE
from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        self.ui = disein.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ip_address = self.ui.ipAddressEdit.text  # IP адрес из строки ввода
        self.login = self.ui.loginEdit.text  # Ввод логина
        self.password = self.ui.passwordEdit.text  # ввод пароля

        self.ui.BTN_ListOfRegistONU.clicked.connect(self.listRegistrOnu)  # Список зареганных онушек
        self.ui.BTN_SignalStrenght.clicked.connect(self.signalStrenght)  # Уровень сигнала
        self.ui.BTN_showOnuNoReristration.clicked.connect(self.showOnuNoRegistration)  # не зареганные онушки
        self.ui.BTN_infoOnu.clicked.connect(self.infoRegisteredOnuGpon)  # Информация о зареганых онушек
        self.ui.BTN_whatIsPrescribed.clicked.connect(self.whatIsPrescribedOnuGpon)  # Что прописанно на ОНУ G-PON ZTE
        self.ui.BTN_ShowMacOnu.clicked.connect(self.showMacOnuGpon)  # Просмотр Маков на ону
        self.ui.info_ONU_BTN_GPON_ZTE.clicked.connect(self.showInfoONU)  # Просмотр информации об онушки
        self.ui.info_port_ONU_BTN_GPON_ZTE.clicked.connect(self.infoAboutPortONU)  # Просмотр информации портов на ОНУ

    # Диалоговое окно с получением значения число
    def inputDialog(self):
        le = QLineEdit(self)
        text, ok = QInputDialog.getInt(self, 'Number port', 'Номер порта ->')
        if ok:
            le.setText(str(text))
            return text

    # Диалоговое окно с получением значения строка
    def inputStrDialog(self):
        le = QLineEdit(self)
        text, ok = QInputDialog.getText(self, 'Enter Macc', 'Введите Мак ->')
        if ok:
            le.setText(str(text))
            return text

        # Диалоговое окно с получением значения ПОН порта

    def inputPonDialog(self):
        le = QLineEdit(self)
        text, ok = QInputDialog.getText(self, 'Enter Pon port', 'Введите Pon порт ->')
        if ok:
            le.setText(str(text))
            return text

    # Просмотри не зарегистрированных анушек G-PON ZTE
    def showOnuNoRegistration(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.showNoRegistOnuComm(self.ip_address, self.login, self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    # Список зарегистрированных ону G-PON ZTE
    def listRegistrOnu(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.listRegistrOnu(self.ip_address, self.inputPonDialog(), self.login, self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    # Уровень сигнала G-PON ZTE
    def signalStrenght(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.signalStrenghtCommnd(self.ip_address, self.inputPonDialog(), self.login,
                                                            self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    # Информация о зарегистрированных анушек G-PON ZTE
    def infoRegisteredOnuGpon(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.infoRegisteredOnuCommand(self.ip_address, self.inputPonDialog(), self.login,
                                                                self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    # Что прописано на ОНУ G-PON ZTE
    def whatIsPrescribedOnuGpon(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.whatIsPrescribed(self.ip_address, self.inputPonDialog(), self.login,
                                                        self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    # Просмотр Маков на ону G-PON ZTE
    def showMacOnuGpon(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.showMac(self.ip_address, self.inputPonDialog(), self.login, self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    def showInfoONU(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.showInforOnu(self.ip_address, self.inputPonDialog(), self.login, self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    def infoAboutPortONU(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.infoAboutPortONU(self.ip_address, self.inputPonDialog(), self.login,
                                                        self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
