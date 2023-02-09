from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import sys, mysql.connector, time
from screeninfo import get_monitors
from PyQt5.QtCore import Qt

db = mysql.connector.connect(host= '192.169.144.133', user = 'jrmcctc6', password = 'mcctcrocks', database ='jr_team_6')
cursor = db.cursor()
# mk tb
try: cursor.execute('CREATE TABLE PLAYERS_JON (ID int NOT NULL AUTO_INCREMENT, PLAYER_ID int, FIRST_NAME VARCHAR(50), LAST_NAME VARCHAR(50), PHONE_NUMBER int, DISCORD_ID VARCHAR(50), ESPORT_GAME VARCHAR(50), PRIMARY KEY (ID))')
except Exception: pass


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow , self).__init__()
        self.x = 300
        self.y = 400
        self.centerX = self.x/2
        self.centerY = self.y/2
        self.setGeometry(300,200,self.x,self.y) # pos then size
        self.setWindowTitle('ESPORTS')
        self.initUI()
    def initUI(self):

        self.lblTitle = QtWidgets.QLabel(self) 
        self.lblTitle.setText('Esports')
        self.lblTitle.move(10,10)
        self.lblTitle.setFont(QFont('Arial', 16))

        self.btnSubmit = QtWidgets.QPushButton(self)
        self.btnSubmit.setText('Submit')
        self.btnSubmit.move(self.centerX - 50,400-40)
        self.btnSubmit.clicked.connect(self.send)

        compaered2 = 0
        self.lblID = QtWidgets.QLabel(self)
        self.lblID.setText('Player ID:')
        self.lblID.setFont(QFont('Arial', 10))
        self.lblID.move(20,40+compaered2)
        
        self.entID = QtWidgets.QLineEdit(self)
        self.entID.move(100, 45)
        self.entID.resize(180, 20)
        compaered2 += 40

        self.lblFN = QtWidgets.QLabel(self) 
        self.lblFN.setText('First Name:')
        self.lblFN.setFont(QFont('Arial', 10))
        self.lblFN.move(20,40+compaered2)
        
        self.entFN = QtWidgets.QLineEdit(self)
        self.entFN.move(100, 45+compaered2)
        self.entFN.resize(180, 20)
        compaered2 += 40

        self.lblLN = QtWidgets.QLabel(self) 
        self.lblLN.setText('Last Name:')
        self.lblLN.setFont(QFont('Arial', 10))
        self.lblLN.move(20,40+compaered2)
        
        self.entLN = QtWidgets.QLineEdit(self)
        self.entLN.move(100, 45+compaered2)
        self.entLN.resize(180, 20)
        compaered2 += 40

        self.lblPN = QtWidgets.QLabel(self) 
        self.lblPN.setText('Phone Num:')
        self.lblPN.setFont(QFont('Arial', 10))
        self.lblPN.move(20,40+compaered2)
        
        self.entPN = QtWidgets.QLineEdit(self)
        self.entPN.move(100, 45+compaered2)
        self.entPN.resize(180, 20)
        compaered2 += 40

        self.lblDID = QtWidgets.QLabel(self) 
        self.lblDID.setText('Discord ID')
        self.lblDID.setFont(QFont('Arial', 10))
        self.lblDID.move(20,40+compaered2)
        
        self.entDID = QtWidgets.QLineEdit(self)
        self.entDID.move(100, 45+compaered2)
        self.entDID.resize(180, 20)
        compaered2 += 40

        self.lblGME = QtWidgets.QLabel(self) 
        self.lblGME.setText('Game Name:')
        self.lblGME.setFont(QFont('Arial', 10))
        self.lblGME.move(20,40+compaered2)

        self.entGME = QtWidgets.QLineEdit(self)
        self.entGME.move(100, 45+compaered2)
        self.entGME.resize(180, 20)

    def send(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.lblTitle.setText('Submited')
        statment = f'INSERT INTO PLAYERS_JON (PLAYER_ID, FIRST_NAME, LAST_NAME, PHONE_NUMBER, DISCORD_ID, ESPORT_GAME) VALUES ({self.entID.text()},{self.entFN.text()},{self.entLN.text()},{self.entPN.text()},{self.entDID.text()},{self.entGME.text()})'
        cursor.execute(statment)
        db.commit()
        QApplication.restoreOverrideCursor()
        self.update()
        self.ShowPop()

    def update(self):
        self.lblTitle.adjustSize() 

    def ShowPop(self):
        msg = QMessageBox()
        msg.setWindowTitle('Finnished')
        msg.setText('The Inputed Data has been Subbmited')
        msg.move(300,200)
        msg.resize(200,50)

        x = msg.exec_()

def start():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

# mk/show/delete/stop
while True:
    action = input('Input Action (mk/show/del/up/exit):')
    if action == 'mk' or action == 'show' or action == 'del' or action == 'exit' or action == 'up': break
    else: pass

if action == 'mk':      
    start()
elif action == 'show':
    query = input('LastName:')
    cursor.execute('SELECT * FROM PLAYERS_JON WHERE LAST_NAME = '+query+';')
    result = cursor.fetchall()
    if result != None:
        print(f'''
        DATA:
        {result}
        ''')
    else:
        print('No Data\n create Data(y/n):')
        y = input()
        if y == 'y':
            start()
        else:
            pass
elif action == 'del':
    while True:
        y = input('ID:')
        confirm = input('U Sure?(y/n)')
        if confirm == 'y': pass
        else: break
        cursor.execute(f'DELETE FROM PLAYERS_JON WHERE ID = {y}')
        db.commit()
        print('DELETED')
        break
elif action == 'up':
    y = input('ID:')
    while True:
        x = input('What? (PLAYER_ID(p), FIRST_NAME(f), LAST_NAME(l), PHONE_NUMBER(pn), DISCORD_ID(d) AND ESPORT_GAME(e)): ')
        if x == 'p' or x == 'f' or x == 'l' or x == 'pn' or x == 'd' or x == 'e':
            pass
        else: break
    if x == 'p': x = 'PLAYER_ID'
    elif x == 'f': x = 'FIRST_NAME'
    elif x == 'l': x = 'LAST_NAME'
    elif x == 'pn': x = 'PHONE_NUMBER'
    elif x == 'd': x = 'DISCORD_ID'
    elif x == 'e': x = 'ESPORT_GAME'

    new = input('NEW DATA:')
    cursor.execute(f'UPDATE PLAYERS_JON SET {x} = {new} WHERE ID = {y};')
    db.commit()
    print('UPDATED')
elif action == 'exit':
    quit()