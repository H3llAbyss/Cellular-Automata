from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtGui import QPainter, QBrush, QColor
import sys, time, re
import main


class Ui(QtWidgets.QMainWindow):

    test_rules = main.parse_input("2/2/9")

    test_field = [[int(0) for i in range(200)] for j in range(200)]

    test_field[100][100] = test_rules[2]
    test_field[100][101] = test_rules[2]
    test_field[101][101] = test_rules[2]
    test_field[101][100] = test_rules[2]

    current_field = test_field
    current_rules = test_rules

    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('MainWindow.ui', self)  # Load the .ui fi
        self.setWindowIcon(QtGui.QIcon('logologlo.png'))

        print("Initializing variables")
        self.transition_field = [[0 for j in range(5)] for i in range(5)]
        self.transition_field[2][2] = 1
        self.transition_field[2][3] = 1
        self.transition_field[3][2] = 1
        self.transition_field[3][3] = 1

        self.lineEdit.setText('2/2/9')
        self.next_step_button.clicked.connect(self.next_generation_button_clicked)
        self.auto_mode_checkbox = self.findChild(QtWidgets.QCheckBox, 'auto_mode_checkbox')
        self.edit_button.clicked.connect(self.edit_inputs)
        self.clear_button.clicked.connect(self.clear_all)
        self.image_button.clicked.connect(self.save_image)

        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.generation_counter = 0

        self.show()

        self.draw_field(self.current_field, self.current_rules)




    def input_field(self):
        return

    # current_field = input_field()

    def color_from_hp(self, hp):

        maxhp = self.current_rules[2]
        red = (1 - hp/maxhp) * 256
        green = hp/maxhp * 256
        blue = 0

        color = QColor(red, green, blue)
        return color

    def auto_generation(self, pause_time):
        while True:
            self.generation()
            time.sleep(pause_time/1000)

    def next_generation_button_clicked(self):



        pending_input = self.lineEdit.text()
        reg = re.match("[1-8]+\/[1-8]+\/[1-9][0-9]*", pending_input)
        if reg is None:
            parseErrorWarning = QtWidgets.QMessageBox(0, 'Warning',
                                                      "Incorrect value in input line")
            pew = parseErrorWarning.exec_()
            return
        self.edit_button.setEnabled(False)
        self.current_rules = main.parse_input(pending_input)

        if self.generation_counter == 0:
            self.apply_field()


        if self.auto_mode_checkbox.isChecked():
            self.auto_generation(5000)
        else:
            self.generation()
        return

    def generation(self):
        self.current_field = main.next_generation_field(self.current_field, self.current_rules, 200)
        self.generation_counter += 1
        self.generation_label.setText("Current generation:" + str(self.generation_counter))
        self.scene.clear()
        self.draw_field(self.current_field, self.current_rules)

    def draw_field(self, field, rules):
        print('drawing now')
        self.scene.clear()
        for i in range(200):
            for j in range(200):
                if field[i][j] != 0:

                    rect = QtCore.QRect(i,j,1,1)
                    qp = QtGui.QPen()
                    qp.setColor(self.color_from_hp(field[i][j]))
                    if self.generation_counter == 0 or self.generation_counter == 1 or self.generation_counter == 2:
                        qp.setColor(QColor(0,255,0))
                    # qp.setColor(QtCore.Qt.red)
                    self.scene.addRect(i*4,j*4,2,2,qp)
                    print(i,j)
                    # qp = QPainter()
                    # qp.setPen(QtCore.Qt.red)
                    # # qp.setPen(QColor.red)
                    # # QPainter.setPen(QColor((1-field[i][j]/self.current_rules[2], field[i][j]/self.current_rules[2], 0)))
                    # qp.drawPoint(i, j)

    def edit_inputs(self):
        editor.show()
        editor.ok_button.clicked.connect(self.ok_button_clicked)

    def ok_button_clicked(self):
        self.transition_field = [[0 for j in range(5)] for i in range(5)]

        for i in range(5):
              for j in range(5):
                  editor.button_check=editor.findChild(QtWidgets.QCheckBox, 'checkBox_'+str(i)+str(j))
                  if editor.button_check.isChecked():
                    self.transition_field[j][i] = 1 # intentionally swapped i and j
                  else:
                    self.transition_field[j][i] = 0

        ttemp_field = [[int(0) for i in range(200)] for j in range(200)]
        for i in range(5):
            for j in range(5):
                if self.transition_field[i][j] == 1:
                    ttemp_field[i + 98][j + 98] = self.current_rules[2]
        self.draw_field(ttemp_field, self.current_rules)

    def apply_field(self):

        self.current_field = [[int(0) for i in range(200)] for j in range(200)]
        for i in range(5):
              for j in range(5):
                  if self.transition_field[i][j]==1:
                    self.current_field[i+98][j+98] = self.current_rules[2]

    def clear_all(self):
        self.generation_counter = 0
        self.current_field = [[int(0) for i in range(200)] for j in range(200)]
        self.edit_button.setEnabled(True)
        self.scene.clear()
#     def edit_inputs(self):
#
#
#         editor.show()
#         editor.editor_graphicsView = edit_view()
#
#         editor.coordinates = [[[0 for j in range(5)] for i in range(5)]]
#
#
# class edit_view(QtWidgets.QGraphicsView):
#
#     def __init__(self):
#         super(edit_view, self).__init__()
#         self.resize(250, 250)
#         self.editor_scene = QtWidgets.QGraphicsScene()
#         editor.editor_graphicsView.setScene(self.editor_scene)
#         print('i am alive')
#
#     def mousePressEvent(self, e):
#         self.editor_scene.addRect(e.x()-e.x()%50,e.y()-e.y()%50,50,50)
#         print(e.x(), e.y())        test_field = [[int(0) for i in range(200)] for j in range(200)]
    def save_image(self):

        # Get region of scene to capture from somewhere.
        area1 = QtCore.QRectF(0,0,200,200)
        area2 = QtCore.QRect(0, 0, 200, 200)
        # Create a QImage to render to and fix up a QPainter for it.
        image = QtGui.QImage(area2.size(), QtGui.QImage.Format_ARGB32_Premultiplied)
        image.fill(QtCore.Qt.transparent)
        painter = QPainter(image)

        # Render the region of interest to the QImage.
        self.scene.render(painter, QtCore.QRectF(image.rect()) )
        painter.end()

        # Save the image to a file.
        image.save("capture.bmp")

app = QtWidgets.QApplication(sys.argv)
editor = uic.loadUi('editor.ui')
window = Ui()
app.exec_()
