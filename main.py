# 尝试用echarts和qtwebengine来做一个供应商审核spyder chart显示GUI
# reference https://zetcode.com/all/#pyqt
# 项目文件导打包，导出exe都没问题了，放在本地运行ok，
# 但是尝试放到share folder中无法显示网页，cmd报是因为Qtwebengine.exe在sandbox中不允许运行，
# 这种案例网上太少了，解决办法涉及到公司IT和

# from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from all_charts.canlenderChart import calender_chart
from all_charts.radarCharts import radar_chart


class Window(QWidget):
    # with open('calendar_base.html', 'r') as f:
    #     html_calender = f.read()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("XXXX")  # change tittle
        self.setGeometry(200, 200, 1355, 730)
        # self.resize(1600, 800)
        # 创建view窗口
        vbox = QVBoxLayout(self)

        self.view = QWebEngineView()
        vbox.addWidget(self.view)
        self.setLayout(vbox)

        # self.view.load(QUrl('http://www.baidu.com'))
        self.view.setHtml('HELLO')
        self.view.setGeometry(300, 5, 1300, 900)
        # generate a button
        self.cal_btn = QPushButton('Calender', self)
        self.cal_btn.clicked.connect(self.setup_cal)
        self.rad_btn = QPushButton('Radar', self)
        self.rad_btn.move(0, 50)
        self.rad_btn.clicked.connect(self.setup_radar)

    # 点击按钮，首先生成一个新的calender，然后再显示在view中,每次点击重新打开
    def setup_cal(self):
        calender_chart()
        with open('calendar_base.html', 'r') as f:
            html_calender = f.read()
        self.view.setHtml(html_calender)
        print('cal')

    def setup_radar(self):
        radar_chart()
        with open('basic_radar_chart.html', 'r') as g:
            html_radar = g.read()
        self.view.setHtml(html_radar)
        print('rad')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
