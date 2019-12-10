from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from multiapp import Ui_LoginWindow
import sys, sqlite3, random, re, datetime


conn = sqlite3.connect('C:/Users/user/Desktop/project/main.db')
cursor = conn.cursor()

quests = {}
ans = {}
ans_rnd = {}
quests_rnd = {}

nums = list(range(1, 6))
random.shuffle(nums)
# print(nums)

sql_quests = "SELECT * FROM questions"
cursor.execute(sql_quests)
for i in cursor.fetchall():
    quests[i[0]] = i[1]
# print('вопр'+str(quests))

sql_ans = "SELECT * FROM answers"
cursor.execute(sql_ans)
for i in cursor.fetchall():
    ans[i[0]] = i[1]
# print('отв'+str(ans))

for i in range(len(nums)):
    quests_rnd[i] = quests[nums[i]]
    ans_rnd[i] = ans[nums[i]]
#print('вопросы рнд' +str(quests_rnd))
#print('ответы рнд' +str(ans_rnd))


class mywindow(QtWidgets.QMainWindow):

    

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        qss_file = open('style.qss').read()
        self.ui.centralwidget.setStyleSheet(qss_file)

        self.mark = 0

        self.ui.pushButton_7.setDisabled(True)
        self.ui.pushButton_8.setDisabled(True)
        self.ui.tabWidget.setTabEnabled(2, False)
        self.ui.tabWidget.setTabEnabled(3, False)
        self.ui.pushButton.clicked.connect(self.register_Clicked)
        self.ui.pushButton_2.clicked.connect(self.regGoLog)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.checkBox.stateChanged.connect(self.checked)
        self.ui.pushButton_3.clicked.connect(self.login_Clicked)
        self.ui.pushButton_4.clicked.connect(self.login)
        self.ui.pushButton_6.clicked.connect(self.start)
        self.ui.pushButton_7.clicked.connect(self.checkTest)
        self.ui.pushButton_8.clicked.connect(self.exitTest)
        self.ui.tableWidget.setVisible(False)
        self.ui.pushButton_5.clicked.connect(self.showResults)
        self.ui.label_11.setVisible(False)
        self.ui.label_12.setVisible(False)
        self.ui.label_13.setVisible(False)
        self.ui.label_14.setVisible(False)
        self.ui.label_15.setVisible(False)
        self.ui.lineEdit_8.setVisible(False)
        self.ui.lineEdit_9.setVisible(False)
        self.ui.lineEdit_10.setVisible(False)
        self.ui.lineEdit_11.setVisible(False)
        self.ui.lineEdit_12.setVisible(False)

    def login(self):
        login = self.ui.lineEdit_6.text()
        password = self.ui.lineEdit_7.text()
        query = "SELECT * FROM users WHERE login = ? and password = ?"
        cursor.execute(query, (login, password))
        if (len(cursor.fetchall()) > 0):
            self.showMessageBox("Успешно!", "Авторизация прошла успешно!")
            self.ui.tabWidget.setCurrentIndex(2)
            self.ui.tab_3.setEnabled(True)
            self.ui.tab.setDisabled(True)
            self.ui.tab_2.setDisabled(True)
            self.ui.tabWidget.setTabEnabled(2, True)
        else:
            self.showMessageBox("Ошибка!", "Логин или пароль введены неверно!")

    def showMessageBox(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def regGoLog(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def checked(self):
        if self.ui.checkBox.isChecked():
            self.ui.lineEdit_5.setEchoMode(0)
        else:
            self.ui.lineEdit_5.setEchoMode(2)

    def register_Clicked(self):
        self.showMessageBox(
            'Успешно!', 'Пользователь успешно зарегистрирован!')
        self.ui.tabWidget.setCurrentIndex(1)

        name = self.ui.lineEdit.text()
        groupnum = self.ui.lineEdit_2.text()
        mail = self.ui.lineEdit_3.text()
        login = self.ui.lineEdit_4.text()
        password = self.ui.lineEdit_5.text()

        cursor.execute("INSERT INTO users(login, name, groupnum, mail, password) VALUES(?,?,?,?,?)",
                       (login, name, groupnum, mail, password))
        conn.commit()

    def login_Clicked(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def start(self):
        self.ui.label_11.setVisible(True)
        self.ui.label_12.setVisible(True)
        self.ui.label_13.setVisible(True)
        self.ui.label_14.setVisible(True)
        self.ui.label_15.setVisible(True)
        self.ui.lineEdit_8.setVisible(True)
        self.ui.lineEdit_9.setVisible(True)
        self.ui.lineEdit_10.setVisible(True)
        self.ui.lineEdit_11.setVisible(True)
        self.ui.lineEdit_12.setVisible(True)

        self.ui.label_11.setText(quests_rnd[0])
        self.ui.label_12.setText(quests_rnd[1])
        self.ui.label_13.setText(quests_rnd[2])
        self.ui.label_14.setText(quests_rnd[3])
        self.ui.label_15.setText(quests_rnd[4])
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_6.setDisabled(True)

    def checkTest(self):
        self.ui.pushButton_7.setDisabled(True)
        self.ui.pushButton_8.setEnabled(True)
        if self.ui.lineEdit_8.text() == ans_rnd[0]:
            self.mark += 1
        if self.ui.lineEdit_9.text() == ans_rnd[1]:
            self.mark += 1
        if self.ui.lineEdit_10.text() == ans_rnd[2]:
            self.mark += 1
        if self.ui.lineEdit_11.text() == ans_rnd[3]:
            self.mark += 1
        if self.ui.lineEdit_12.text() == ans_rnd[4]:
            self.mark += 1
        self.showMessageBox('Оценка', 'Ваша оценка {}/5'.format(self.mark))
        now = str(datetime.date.today())

        name_query = "SELECT name FROM users WHERE login = ?"
        cursor.execute(name_query, (self.ui.lineEdit_6.text(),))

        name = cursor.fetchone()
        cursor.execute("INSERT INTO results(name, mark, date) VALUES(?,?,?)", (str(name), self.mark, now,))
        conn.commit()

        self.ui.pushButton_6.setDisabled(True)
        self.ui.pushButton_7.setDisabled(True)
        #self.ui.tab_3.setDisabled(True)
        self.ui.tabWidget.setTabEnabled(3, True)
        self.load_initial_data()

    def exitTest(self):
        self.close()

    def load_initial_data(self):
        cursor.execute('''SELECT * FROM results ''')
        rows = cursor.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.ui.tableWidget.insertRow(inx)
            self.ui.tableWidget.setItem(inx, 0, QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(inx, 1, QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(inx, 2, QTableWidgetItem(row[3]))
            self.ui.tableWidget.resizeColumnsToContents()

    def showResults(self):
        if self.ui.lineEdit_13.text() == '':
            self.showMessageBox('Ошибка', 'Нужно ввести пароль!')
        elif self.ui.lineEdit_13.text() == 'admin':
            self.ui.tableWidget.setVisible(True)
        else:
            self.showMessageBox('Ошибка', 'Пароль введен неверно!')

    conn.close()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
