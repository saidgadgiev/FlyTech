import sys
from PyQt5.QtWidgets import (QLineEdit, QInputDialog)
import disein
import commands.huawei
import commands.dlink
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

        # self.ui.connectDLink.clicked.connect(self.connectDLink)  # Подключение к комм DLink
        # self.ui.connectHuawei.clicked.connect(self.connectHuawei)  # Подключение к комм Huawei
        self.ui.interfBTN_Huawei.clicked.connect(self.switchbord_interf)  # кнопка просмотр портов Huawei
        self.ui.interfBTN_Dlink.clicked.connect(self.switchbord_interf_dlink)  # кнопка просмотр портов DLink
        self.ui.listMacBTN_Huawei.clicked.connect(self.listMac)  # Кнопка список маков Huawei
        self.ui.listMacBTN_Dlink.clicked.connect(self.listMac_dlink)  # Кнопка список маков DLink
        self.ui.shundownPortBTN_Huawei.clicked.connect(self.shutdownPort)  # Отключение порта Huawei
        self.ui.shundownPortBTN_Dlink.clicked.connect(self.shutdownPortDlink)  # Отключение порта DLink
        self.ui.noShundownPortBTN_Huawei.clicked.connect(self.noShutdownPort)  # Включение порта Huawei
        self.ui.noShundownPortBTN_Dlink.clicked.connect(self.noShutdownPortDlink)  # Включение порта DLink
        self.ui.listVlanBTN_Huawei.clicked.connect(self.listVlan)  # Просмотр вланов Huawei
        self.ui.listVlanBTN_Dlink.clicked.connect(self.listVlanDl)  # Просмотр вланов Dlink
        self.ui.infoPortBTN_Huawei.clicked.connect(self.infoPort)  # информация о порте Huawei
        self.ui.infoPortBTN_Dlink.clicked.connect(self.infoPortDl)  # информация о порте Dlink
        self.ui.serchMacBTN_Huawei.clicked.connect(self.serchMacAddress)  # поиск по маку Huawei
        self.ui.serchMacBTN_Dlink.clicked.connect(self.serchMacAddressDl)  # поиск по маку Dlink
        self.ui.macPortBTN_Huawei.clicked.connect(self.macAboutPort)  # маки на порту Huawei
        self.ui.macPortBTN_Dlink.clicked.connect(self.macAboutPortDl)  # маки на порту Dlink
        self.ui.BTN_ListOfRegistONU.clicked.connect(self.listRegistrOnu)  # Список зареганных онушек
        self.ui.BTN_SignalStrenght.clicked.connect(self.signalStrenght)  # Уровень сигнала
        self.ui.BTN_showOnuNoReristration.clicked.connect(self.showOnuNoRegistration)  #не зареганные онушки
        self.ui.BTN_infoOnu.clicked.connect(self.infoRegisteredOnuGpon)  # Информация о зареганых онушек
        self.ui.BTN_whatIsPrescribed.clicked.connect(self.whatIsPrescribedOnuGpon)  # Что прописанно на ОНУ G-PON ZTE
        self.ui.BTN_ShowMacOnu.clicked.connect(self.showMacOnuGpon)  # Просмотр Маков на ону
        self.ui.info_ONU_BTN_GPON_ZTE.clicked.connect(self.showInfoONU)  # Просмотр информации об онушки
        self.ui.info_port_ONU_BTN_GPON_ZTE.clicked.connect(self.infoAboutPortONU)  # Просмотр информации портов на ОНУ
        

        # self.ui.checkPortBTN.clicked.connect(self.checkPort)  # Диагностика порта
        # self.ui.disThisBTN.clicked.connect(self.disThisPort)  # что прописанно на порту
        # self.ui.label_3.setText(self.btnTest())

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

    # Подключение к коммут DLink
    '''
    def connectDLink(self):
        if 0 < len(self.ip_address()):
            try:
                ssh = doСonnection.comm_dlink(self.ip_address, self.login, self.password)
                ssh = netmiko.ConnectHandler(**ssh)
                connect = ssh
                return ssh
            except netmiko.NetmikoTimeoutException:
                return ("Не удалось установить TCP-соединение с устройством. \nРаспространенными причинами этой проблемы "
                        "являются:\n1. Неверное имя хоста или IP-адрес.\n2. Неправильный TCP-порт.\n3. Промежуточный "
                        "брандмауэр, блокирующий доступ.\n")
            except netmiko.NetmikoAuthenticationException:
                return ("Не удалось выполнить аутентификацию на устройстве. \nРаспространенными причинами этой проблемы "
                        "являются:\nНеверные имя пользователя и пароль")
        else:
            self.ui.resultEdit_2.setText("Введите IP устройства")
    '''
    # Подключение к коммутатору Huawei
    """
    def connectHuawei(self):
        if 0 < len(self.ip_address()):
            huawei = doСonnection.comm_huawei(self.ip_address, self.login, self.password)
            
            self.ui.resultEdit.setText("huawei подключено")
            return huawei
        else:
            self.ui.resultEdit.setText("Введите IP устройства")
    """

    # просмотр интерфейсов Huawei
    def switchbord_interf(self):
        if 0 < len(self.ip_address()):
            huawei = commands.huawei.interfHuawei(self.ip_address, self.login, self.password)
            self.ui.resultEdit_Huawei.setText(huawei)
        else:
            self.ui.resultEdit_Huawei.setText("Введите IP устройства")
            
    # список маков Huawei
    def listMac(self):
        if 0 < len(self.ip_address()):
            huawei = commands.huawei.listMacHuawei(self.ip_address, self.login, self.password)
            self.ui.resultEdit_Huawei.setText(huawei)
        else:
            self.ui.resultEdit_Huawei.setText("Введите IP устройства")

    # Просмотр вланов Huawei
    def listVlan(self):
        if 0 < len(self.ip_address()):
            huawei = commands.huawei.listVlanHuawei(self.ip_address, self.login, self.password)
            self.ui.resultEdit_Huawei.setText(huawei)
        else:
            self.ui.resultEdit_Huawei.setText("Введите IP устройства")

    # Информация о порте Huawei
    def infoPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = commands.huawei.infoPortHuawei(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit_Huawei.setText(huawei)
        else:
            self.ui.resultEdit_Huawei.setText("Введите IP устройства")

    # Поиск по маку Huawei
    def serchMacAddress(self):
        if 0 < len(self.ip_address()):
            macAddress = self.inputStrDialog()
            huawei = commands.huawei.serchMacAddressHuawei(self.ip_address, macAddress, self.login, self.password)
            self.ui.resultEdit_Huawei.setText(huawei)
        else:
            self.ui.resultEdit_Huawei.setText("Введите IP устройства")
            
    # Маки на порту Huawei
    def macAboutPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = commands.huawei.maccAboutPortHuawei(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit_Huawei.setText(huawei)
        else:
            self.ui.resultEdit_Huawei.setText("Введите IP устройства")

    # Диагностика порта Huawei
    def checkPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = commands.huawei.checkPortHuawei(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit_Huawei.setText(huawei)
        else:
            self.ui.resultEdit_Huawei.setText("Введите IP устройства")

    # Что прописано на порту Huawei
    def disThisPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = commands.huawei.disThisPortHuawei(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit_Huawei.setText(huawei)
        else:
            self.ui.resultEdit_Huawei.setText("Введите IP устройства")
            
    # Отключение порта Huawei
    def shutdownPort(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            huawei = commands.huawei.shutdown_port(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit_Huawei.setText(f'Порт {port} отключен')
        else:
            self.ui.resultEdit_Huawei.setText("Введите IP устройства")
            
            

    # просмотр интерфейсов D-link
    def switchbord_interf_dlink(self):
        if 0 < len(self.ip_address()):
            dlink = commands.dlink.interfDLink(self.ip_address, self.login, self.password)
            self.ui.resultEdit_Dlink.setText(dlink)
        else:
            self.ui.resultEdit_Dlink.setText("Введите IP устройства")

    # список маков DLink
    def listMac_dlink(self):
        if 0 < len(self.ip_address()):
            dlink = commands.dlink.listMacDLink(self.ip_address, self.login, self.password)
            self.ui.resultEdit_Dlink.setText(dlink)
        else:
            self.ui.resultEdit_Dlink.setText("Введите IP устройства")

    
    # Просмотр вланов DLink
    def listVlanDl(self):
        if 0 < len(self.ip_address()):
            dlink = commands.dlink.listVlanDlink(self.ip_address, self.login, self.password)
            self.ui.resultEdit_Dlink.setText(dlink)
        else:
            (self.ui.resultEdit_Dlink.setText("Введите IP устройства"))

    # Информация о порте Dlink
    def infoPortDl(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            dlink = commands.dlink.infoPortDlink(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit_Dlink.setText(dlink)
        else:
            self.ui.resultEdit_Dlink.setText("Введите IP устройства")

    # Поиск по маку Dlink
    def serchMacAddressDl(self):
        if 0 < len(self.ip_address()):
            macAddress = self.inputStrDialog()
            dlink = commands.dlink.serchMacAddressDlink(self.ip_address, macAddress, self.login, self.password)
            self.ui.resultEdit_Dlink.setText(dlink)
        else:
            self.ui.resultEdit_Dlink.setText("Введите IP устройства")

    # Маки на порту Dlink
    def macAboutPortDl(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            dlink = commands.dlink.maccAboutPortDlink(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit_Dlink.setText(dlink)
        else:
            self.ui.resultEdit_Dlink.setText("Введите IP устройства")

    # Отключение порта Dlink
    def shutdownPortDlink(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            dlink = commands.dlink.shutdown_port_dlink(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit_Dlink.setText(f'Порт {port} отключен')
        else:
            self.ui.resultEdit_Dlink.setText("Введите IP устройства")

    # Включение порта Dlink
    def noShutdownPortDlink(self):
        if 0 < len(self.ip_address()):
            port = self.inputDialog()
            dlink = commands.dlink.undo_shutdown_port_dlink(self.ip_address, port, self.login, self.password)
            self.ui.resultEdit_Dlink.setText(f'Порт {port} включен')
        else:
            self.ui.resultEdit_Dlink.setText("Введите IP устройства")

    # Просмотри не зарегестрированных онушек G-PON ZTE

    def showOnuNoRegistration(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.showNoRegistOnuComm(self.ip_address, self.login, self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    # Список зарегестрированных ону G-PON ZTE
    def listRegistrOnu(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.listRegistrOnu(self.ip_address, self.inputPonDialog(), self.login, self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    # Уровень сигнала G-PON ZTE
    def signalStrenght(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.signalStrenghtCommnd(self.ip_address, self.inputPonDialog(), self.login, self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    # Информация о зареганых онушек G-PON ZTE
    def infoRegisteredOnuGpon(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.infoRegisteredOnuCommand(self.ip_address, self.inputPonDialog(), self.login, self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

    # Что прописанно на ОНУ G-PON ZTE
    def whatIsPrescribedOnuGpon(self):
        if 0 < len(self.ip_address()):
            gPonZte = commands.gPonZTE.whatIsPrescribed(self.ip_address, self.inputPonDialog(), self.login, self.password)
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
            gPonZte = commands.gPonZTE.infoAboutPortONU(self.ip_address, self.inputPonDialog(), self.login, self.password)
            self.ui.resultEdit_GPON_ZTE.setText(gPonZte)
        else:
            self.ui.resultEdit_GPON_ZTE.setText("Введите IP устройства")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
