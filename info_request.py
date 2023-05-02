import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 키움 로그인
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        # OpenAPI+ Event
        self.kiwoom.OnEventConnect.connect(self.OnEventConnect)
        self.kiwoom.OnReceiveTrData.connect(self.OnReceiveTrData)
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        label = QLabel('종목코드: ', self)
        label.move(20, 20)

        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 20)
        self.code_edit.setText("039490")

        btn1 = QPushButton("조회", self)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        # 사용자가 QTextEdit 위젯을 통해 입력할 수 없고 오직 읽기 모드로만 사용하도록
        self.text_edit.setEnabled(False)

    def btn1_clicked(self):
        code = self.code_edit.text()
        self.text_edit.append("종목코드: " + code)

        # SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)

        # CommRqData
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "Request1", "opt10001", 0, "0101")

    def OnEventConnect(self, ErrCode):
        if ErrCode == 0:
            self.text_edit.append("로그인 성공")

    def OnReceiveTrData(self, ScrNo, RQName, TrCode, RecordName, PrevNext, DataLength, ErrorCode, Message, SplmMsg):
        if RQName == "Request1":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, 0, "PER")

            self.text_edit.append("종목명: " + name.strip())
            self.text_edit.append("거래량: " + volume.strip())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_() 