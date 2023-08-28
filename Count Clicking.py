import sys

from PyQt5 import QtWidgets,QtGui

class Window(QtWidgets.QWidget):
    # To using Qtwidgets' function
    def __init__(self):
        super().__init__()
        self.user_interface()

    def user_interface(self):

        # It is identified for receiving data how many clicked.
        self.count  = 0

                                # Setting windows title.
        self.setWindowTitle("GORKIDEV Application")

        # Setting windows title,icon and default size.
        self.setWindowIcon(QtGui.QIcon("telefon.png"))  #You can indicate image path there like "C:/Users/User/Desktop/telefon.png".
        self.resize(500,500)

        # Creating a label to place an image on the background.
        background_picture = QtWidgets.QLabel(self)
        background_picture.setPixmap(QtGui.QPixmap("telefon.png"))

                # Adding label for what tell us how many times clicked button and adding Push button which are 'Click Here','Exit'.
        self.tag1 = QtWidgets.QLabel("\n                                          I haven't been clicked yet.\n\n")
        self.tag2   = QtWidgets.QPushButton("Click Here!")
        self.tag3 = QtWidgets.        QPushButton("Exit")

        # To change button colors you could change 'Azure' part with color name or color codes.
        self.tag2.setStyleSheet("background-color : Azure")
        self.tag3.setStyleSheet("background-color : Azure")

                # Creating layout to change widgets'places on the window.
        v_box = QtWidgets.QVBoxLayout()

                # Keeping widget on the middle because we want to display center. ( Vertical Align )
        v_box.addStretch()
        v_box.addWidget(background_picture)
        v_box.addWidget(self.tag1)
        v_box.addWidget(self.tag2)
        v_box.addWidget(self.tag3)
        v_box.addStretch()

        # Keeping widget on the middle because we want to display center. ( Horizonal Align )
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

                # Implementing layouts to main window.
        self.setLayout(h_box)

        # In the clicking cases these codes will direct related function.
        self.tag2.clicked.connect(self.clicked)
        self.tag3.clicked.connect(self.exit)

        # We are using .show() function to display window.
        self.show()

    # Identifying what will happen at clicked button. ( 'Click Here' ) Button.
    def clicked(self):
        self.count += 1
        self.tag1.setText("\n                                             I have clicked " + str(self.count)  + " times.\n\n")

    # Identifying what will happen at clicked button. ( 'Exit' ) Button.
    def exit(self):
        sys.exit()

#Creating app to working on it.
app = QtWidgets.QApplication(sys.argv)

# Using class
my_window = Window()

# There is indicated system will stopped when pushing X button on the top of window.
sys.exit(app.exec_())