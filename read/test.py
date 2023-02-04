from read import ui, randfi
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QScatterSeries, QChart, QLegend, QValueAxis
import sys

class login(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        self.nums = []
        super().__init__()
        self.setupUi(self)
        self.chart_init()
        self.pushButton.clicked.connect(self.up_xy)

    def chart_init(self):
        self.chart = QChart()
        self.series = QScatterSeries()
        self.series.setName("散点图")  # 设置曲线名称
        self.series.setPointLabelsFormat("@yPoint")
        self.series.setPointLabelsVisible()
        self.series.setMarkerSize(16)  # 设置节点大小
        self.chart.addSeries(self.series)  # 把曲线添加到QChart的实例中

        # 声明并初始化X轴、Y轴
        self.dtaxisX = QValueAxis()
        self.vlaxisY = QValueAxis()

        # 设置坐标轴显示范围
        self.dtaxisX.setMin(0)
        self.dtaxisX.setMax(7)
        self.vlaxisY.setMin(0)
        self.vlaxisY.setMax(50)

        # 设置坐标轴名称
        self.dtaxisX.setTitleText("X轴")
        self.vlaxisY.setTitleText("Y轴")

        # 把坐标轴添加到chart中
        self.chart.addAxis(self.dtaxisX, Qt.AlignBottom)
        self.chart.addAxis(self.vlaxisY, Qt.AlignLeft)

        # 把曲线关联到坐标轴
        self.series.attachAxis(self.dtaxisX)
        self.series.attachAxis(self.vlaxisY)
        self.charview.setChart(self.chart)

    def up_xy(self):
        k = randfi.number_get().get()
        self.nums.append(k)
        self.series.append(k['I'], k['F'])
        print(self.nums)
        # self.charview.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = login()
    win.show()

    sys.exit(app.exec_())