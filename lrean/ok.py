import sys
import random
from PyQt5.QtChart import QDateTimeAxis,QValueAxis,QSplineSeries,QChart,QChartView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QDateTime,Qt,QTimer


class ChartView(QChartView,QChart):
    def __init__(self, *args, **kwargs):
        super(ChartView, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.chart_init()
        self.timer_init()

    def timer_init(self):
        #使用QTimer，2秒触发一次，更新数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.drawLine)
        self.timer.start(500)

    def chart_init(self):
        self.series = QSplineSeries()
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.setChart(self.chart)
    def drawLine(self):
        #获取当前时间
        bjtime = QDateTime.currentDateTime()
        #当曲线上的点超出X轴的范围时，移除最早的点
        yint = random.randint(0, 500)
        print(yint)
        #添加数据到曲线末端
        self.series.append(bjtime.toMSecsSinceEpoch(), yint)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = ChartView()
    view.show()
    sys.exit(app.exec_())