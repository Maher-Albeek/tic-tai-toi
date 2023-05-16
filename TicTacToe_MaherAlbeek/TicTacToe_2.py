
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSound
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel,  QListWidget, QMessageBox
import sys, os

winner = ""
# Start Window
class Start(QMainWindow):
    def __init__(self):
        super(Start, self).__init__()
        self.ui = Ui()
        self.sitting = Setting()
        self.sitting.playAudio()

        self.player = QMediaPlayer()

        uic.loadUi('ui/Start_ticTacToe2.ui', self)

        self.btnStart.clicked.connect(self.open)
        self.btnSetting.clicked.connect(self.openSitting)
        self.pushButton.clicked.connect(self.feedback)
        self.btnHelp.clicked.connect(self.help)
        self.imag()

        self.setWindowTitle("HOME")
        self.setWindowIcon(QtGui.QIcon('img/home.png'))
    # Feedback option as a MessageBox
    def feedback(self):
        feedback = QMessageBox()
        feedback.setText("the Feedback option is comming in new Versions!! tnx :)")
        feedback.setWindowTitle("Warnning")
        feedback.exec_()
        self.msgBoxSoundEffekt()
    #Help option as a MessageBox
    def help(self):
        help = QMessageBox()
        help.setText("the Help option is comming in new Versions!! tnx :)")
        help.setWindowTitle("Warnning")
        help.exec_()
        self.msgBoxSoundEffekt()
    # sound effect when Feedback or Help option pressed
    def msgBoxSoundEffekt(self):
        full_file_path = os.path.join(os.getcwd(), 'sounds/point-in-space-36199.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.setVolume(100)
        self.player.play()
    # open the Game Window
    def open(self):
        self.ui.show()
        self.hide()
    # open the sitting window
    def openSitting(self):
        self.sitting.show()
    # function to put an image in background of first window / or start window
    def imag(self):

        oImage = QtGui.QImage("img/HD.jpg")
        sImage = oImage.scaled(QtCore.QSize(440,440))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)
# Game Window
class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        self.setting = Setting()
        # Load the UI file
        uic.loadUi('ui/TicTacToe.ui', self)

        self.imag()

        self.player = QMediaPlayer()
        # rename your game's Name
        self.setWindowTitle("Tic Tac Toe")
        self.setWindowIcon(QtGui.QIcon('img/Tic-Tac-Toe-Game.png'))
        # buttons Style
        self.setStyleSheet('QPushButton{ border-radius:10px}')
        # define A counter to keep Track of Who's Turn is it
        self.counter = 0
        self.count = 0
        # Define our Widgets
        self.button1 = self.findChild(QPushButton, "pushButton_1")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.buttonStart = self.findChild(QPushButton, "pushButton_Start")
        self.buttonClear = self.findChild(QPushButton, "pushButton_Start_2")
        self.label = self.findChild(QLabel, "label")
        self.label3 = self.findChild(QLabel, "label_3")
        self.listewinner = self.findChild(QListWidget, "listWidget")


        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.buttonStart.clicked.connect(self.rest)
        self.buttonClear.clicked.connect(self.clear)
        self.buttonHome.clicked.connect(self.home)
    # a function return back to start window
    def home(self):
        self.hide()
        self.start = Start()
        self.start.show()
    # click the button
    def clicker(self, b):

        if self.counter % 2 == 0:
            mark = "X"
            self.label.setText("O's Turn")
        else:
            mark = "O"
            self.label.setText("X's Turn")

        b.setText(mark)
        b.setEnabled(False)
        self.counter += 1
        self.buttonVoiceEffect()
        # check if won

        if self.counter == 9:
            self.checkDraw()
        else:
            self.checkWin()
    # Check win
    def checkWin(self):
        # across
        if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
            self.win( self.button1, self.button4, self.button7)
        if self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
            self.win(self.button2, self.button5, self.button8)
        if self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text():
            self.win(self.button3, self.button6, self.button9)

        # down
        if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.win(self.button1, self.button2, self.button3)
        if self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            self.win(self.button4, self.button5, self.button6)
        if self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            self.win(self.button7, self.button8, self.button9)

        # Diagnoal
        if self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            self.win(self.button1, self.button5, self.button9)
        if self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text():
            self.win(self.button3, self.button5, self.button7)
    def checkDraw(self):
        self.label.setText("Draw")
        self.draw()
   # when someone is won that will happen
    def win(self, a, b, c):
        # the colors well be changed if a player win
        a.setStyleSheet('QPushButton{color: red;}')
        b.setStyleSheet('QPushButton{color: red;}')
        c.setStyleSheet('QPushButton{color: red;}')
        #
        self.winVoiceEffect()
        #
        winner = (f"{a.text()} 's Win!")
        # add winner in label
        self.label.setText(winner)
        # disable the Bord
        self.disabled()

        self.adding(winner)

    # Disabled the Buttons when someone is won
    def disabled(self):
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
        ]
        for b in button_list:
            b.setEnabled(False)
    # create a function that will reset the game
    def rest(self):
        # create a list of all buttons
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
        ]
        for b in button_list:
            b.setText("")
            b.setEnabled(True)
            # reset the button color
            b.setStyleSheet('QPushButton{color: rgba(212, 212, 212, 0.93);background-color:rgba(65, 145, 225, 0.0);}')
        # Reset the label
        self.label.setText("X wird anfangen")
        # voice effect by restarting the Game
        self.restartVoiceEffect()
        # Reset the counter
        self.counter = 0
        # count the games when pressing new game button
        self.count += 1
        self.label3.setText(f"Game: {str(self.count)}")
    # restart the game after Draw
    def draw(self):
        # create a list of all buttons
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
        ]
        for b in button_list:
            b.setText("")
            b.setEnabled(True)
            # reset the button color
            b.setStyleSheet('QPushButton{color: rgba(212, 212, 212, 0.93);background-color:rgba(65, 145, 225, 0.0);}')

        # Reset the label
        self.label.setText("X wird anfangen")
        # voice effect by restarting the Game
        self.drawVoiceEffect()
        # Reset the counter
        self.counter = 0
        # count the games when pressing new game button
        self.count += 1
        self.label3.setText(f"Game: {str(self.count)}")

        winner = "!!Draw!!"
        self.adding(winner)

    # adding the winner name if was X or was O in QlistWidget
    def adding(self, winner):
        # this code will put the winners names in listWidget on the right side
        self.listewinner.addItem(winner)


    #  create a function that will clear a QListWidget
    def clear (self):
        self.listewinner.clear()
        self.clearVoiceEffect()
    # voice Effect for a winner
    def winVoiceEffect(self):
        full_file_path = os.path.join(os.getcwd(), 'sounds/success-1-6297.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.setVolume(100)
        self.player.play()
    # voice Effect for restarting
    def restartVoiceEffect(self):
        full_file_path = os.path.join(os.getcwd(), 'sounds/game-bonus-144751.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.setVolume(100)
        self.player.play()
    # voice Effect for restarting
    def buttonVoiceEffect(self):
        full_file_path = os.path.join(os.getcwd(), 'sounds/k.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.setVolume(100)
        self.player.play()
    # voice Effect for clear the win list
    def clearVoiceEffect(self):
        full_file_path = os.path.join(os.getcwd(), 'sounds/ripping-paper-7123.mp3')
        url = QUrl.fromLocalFile(full_file_path)

        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.setVolume(100)
        self.player.play()
    # the sound effect by draw the game
    def drawVoiceEffect(self):
        full_file_path = os.path.join(os.getcwd(), 'sounds/alert-sound-87478.mp3')
        url = QUrl.fromLocalFile(full_file_path)

        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.setVolume(100)
        self.player.play()
    # the background of the Main Window
    def imag(self):

        oImage = QtGui.QImage("img/tic-tac-toe.jpg")
        sImage = oImage.scaled(QtCore.QSize(440, 440))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)


# Setting Window
class Setting(QMainWindow):
    def __init__(self):
        super(Setting, self).__init__()
        uic.loadUi('ui/Sitting_TicTacToe.ui', self)
        self.imag()
        self.player = QMediaPlayer()

        self.checkBox.clicked.connect(self.mute)
        self.setWindowTitle("Setting")
        self.setWindowIcon(QtGui.QIcon('img/setting.png'))
    # Volume Mute of music
    def mute(self):
        self.player.setMuted(not self.player.isMuted())
    # play music on the background of the Game
    def playAudio(self):

        full_file_path = os.path.join(os.getcwd(), 'music/1_Hour_Music_Mix___The_Best_Video_Game_Soundtracks.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.setVolume(75)

        self.player.play()


    # Background für sitting Window
    def imag(self):
        oImage = QtGui.QImage("img/sitting_background_2.jpg")
        sImage = oImage.scaled(QtCore.QSize(440, 440))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)

# class of FeedBack Window in new version
# class of help Window in new version


app = QApplication(sys.argv)
window = Start()
window.show()
sys.exit(app.exec_())
