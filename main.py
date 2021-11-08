# 尝试用echarts和qtwebengine来做一个供应商审核spyder chart显示GUI
# reference https://zetcode.com/all/#pyqt

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from canlenderChart import calender_chart


class Window(QWidget):
    # with open('calendar_base.html', 'r') as f:
    #     html_calender = f.read()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("XXXX")  # change tittle
        self.setGeometry(200, 200, 1355, 730)
        # self.resize(1600, 800)
        # 创建view窗口
        self.view = QWebEngineView(self)
        # self.view.load(QUrl('http://www.baidu.com'))
        # self.view.setHtml(self.html_calender)
        self.view.setGeometry(300, 5, 1000, 720)
        # generate a button
        self.btn = QPushButton('BTN', self)
        self.btn.clicked.connect(self.setup_ui)

    # 点击按钮，首先生成一个新的calender，然后再显示在view中,每次点击重新打开
    def setup_ui(self):
        with open('calendar_base.html', 'r') as f:
             self.html_calender = f.read()
        calender_chart()
        self.view.setHtml(self.html_calender)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
