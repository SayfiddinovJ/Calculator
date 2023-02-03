from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
oyna = QWidget()
oyna.setWindowTitle("Calculator")
oyna.setGeometry(340, 130, 320, 510)
oyna.setStyleSheet("")
oyna.setFixedSize(320,510)

yozuv = QLabel(f"Normal",oyna)
yozuv.move(45, 0)
yozuv.setFont(QFont("Times",25))

yechish = QLabel("0", oyna)
yechish.move(5, 70)
yechish.setFont(QFont("Times", 35))

menu = QPushButton("=", oyna)
menu.setGeometry(0,0,40,40)
menu.setFont(QFont("Times", 10))

back = QPushButton("◀", oyna)
back.setGeometry(275,0,40,40)
back.setFont(QFont("Times", 20))

foyiz = QPushButton("%", oyna)
foyiz.setGeometry(5,175,75,55)
foyiz.setFont(QFont("Times", 10))

ildiz = QPushButton("V", oyna)
ildiz.setGeometry(83,175,75,55)
ildiz.setFont(QFont("Times", 10))

def kvad():
    yechish.setText(f"{int(yechish.text())*int(yechish.text())}")
    yechish.adjustSize()
kvadrat = QPushButton("X2", oyna)
kvadrat.setGeometry(161,175,75,55)
kvadrat.setFont(QFont("Times", 10))
kvadrat.clicked.connect(kvad)

def kvad():
    pass
x = QPushButton("1/x", oyna)
x.setGeometry(238,175,75,55)
x.setFont(QFont("Times", 10))

def ochir():
    yechish.setText(f"0")
    yechish.adjustSize()
ce = QPushButton("CE", oyna)
ce.setGeometry(5,233,75,55)
ce.setFont(QFont("Times", 10))
ce.clicked.connect(ochir)

c = QPushButton("C", oyna)
c.setGeometry(83,233,75,55)
c.setFont(QFont("Times", 10))
c.clicked.connect(ochir)

def cle():
    yechish.setText(f"{yechish.text()}")
    yechish.setText(f"{yechish.text()[:-1:]}")
    if yechish.text()=="":
        yechish.setText("0")
        yechish.adjustSize()
    yechish.adjustSize()
    yechish.adjustSize()
clear = QPushButton("◀️", oyna)
clear.setGeometry(161,233,75,55)
clear.setFont(QFont("Times", 20))
clear.clicked.connect(cle)

def yoz_boluv():
    if yechish.text()!="0":
        a = yechish.text()
        yechish.setText(a+"/")
        yechish.adjustSize()
    elif yechish.text()[::-1]=="/":
        pass
boluv = QPushButton("/", oyna)
boluv.setGeometry(238,233,75,55)
boluv.setFont(QFont("Times", 10))
boluv.clicked.connect(yoz_boluv)

def yoz7():
    if yechish.text()=="0":
        yechish.setText(f"7")
        yechish.adjustSize()
    else:
        a = yechish.text()+"7"
        yechish.setText(a)
        yechish.adjustSize()
yetti = QPushButton("7", oyna)
yetti.setGeometry(5,291,75,53)
yetti.setFont(QFont("Times", 10))
yetti.clicked.connect(yoz7)

def yoz8():
    if yechish.text()=="0":
        yechish.setText(f"8")
        yechish.adjustSize()
    else:
        a = yechish.text()+"8"
        yechish.setText(a)
        yechish.adjustSize()
sakkiz = QPushButton("8", oyna)
sakkiz.setGeometry(83,291,75,53)
sakkiz.setFont(QFont("Times", 10))
sakkiz.clicked.connect(yoz8)

def yoz9():
    if yechish.text()=="0":
        yechish.setText(f"9")
        yechish.adjustSize()
    else:
        a = yechish.text()+"9"
        yechish.setText(a)
        yechish.adjustSize()
toqqiz = QPushButton("9", oyna)
toqqiz.setGeometry(161,291,75,53)
toqqiz.setFont(QFont("Times", 10))
toqqiz.clicked.connect(yoz9)

def yoz_x():
    if yechish.text()!="0":
        a = yechish.text()
        yechish.setText(a+"*")
        yechish.adjustSize()
    elif yechish.text()[::-1]=="*":
        pass
x = QPushButton("*", oyna)
x.setGeometry(238,291,75,53)
x.setFont(QFont("Times", 10))
x.clicked.connect(yoz_x)

def yoz4():
    if yechish.text()=="0":
        yechish.setText(f"4")
        yechish.adjustSize()
    else:
        a = yechish.text()+"4"
        yechish.setText(a)
        yechish.adjustSize()
tort = QPushButton("4", oyna)
tort.setGeometry(5,347,75,53)
tort.setFont(QFont("Times", 10))
tort.clicked.connect(yoz4)

def yoz5():
    if yechish.text()=="0":
        yechish.setText(f"5")
        yechish.adjustSize()
    else:
        a = yechish.text()+"5"
        yechish.setText(a)
        yechish.adjustSize()
besh = QPushButton("5", oyna)
besh.setGeometry(83,347,75,53)
besh.setFont(QFont("Times", 10))
besh.clicked.connect(yoz5)

def yoz6():
    if yechish.text()=="0":
        yechish.setText(f"6")
        yechish.adjustSize()
    else:
        a = yechish.text()+"6"
        yechish.setText(a)
        yechish.adjustSize()
olti = QPushButton("6", oyna)
olti.setGeometry(161,347,75,53)
olti.setFont(QFont("Times", 10))
olti.clicked.connect(yoz6)

def yoz_minus():
    if yechish.text()!="0":
        a = yechish.text()
        yechish.setText(a+"-")
        yechish.adjustSize()
    elif yechish.text()[::-1]=="-":
        pass
minus = QPushButton("-", oyna)
minus.setGeometry(238,347,75,53)
minus.setFont(QFont("Times", 10))
minus.clicked.connect(yoz_minus)

def yoz1():
    if yechish.text()=="0":
        yechish.setText(f"1")
        yechish.adjustSize()
    else:
        a = yechish.text()+"1"
        yechish.setText(a)
        yechish.adjustSize()
bir = QPushButton("1", oyna)
bir.setGeometry(5,402,75,53)
bir.setFont(QFont("Times", 10))
bir.clicked.connect(yoz1)

def yoz2():
    if yechish.text()=="0":
        yechish.setText(f"2")
        yechish.adjustSize()
    else:
        a = yechish.text()+"2"
        yechish.setText(a)
        yechish.adjustSize()
ikki = QPushButton("2", oyna)
ikki.setGeometry(83,402,75,53)
ikki.setFont(QFont("Times", 10))
ikki.clicked.connect(yoz2)

def yoz3():
    if yechish.text()=="0":
        yechish.setText(f"3")
        yechish.adjustSize()
    else:
        a = yechish.text()+"3"
        yechish.setText(a)
        yechish.adjustSize()
uch = QPushButton("3", oyna)
uch.setGeometry(161,402,75,53)
uch.setFont(QFont("Times", 10))
uch.clicked.connect(yoz3)

def yoz_plus():
    if yechish.text()!="0":
        a = yechish.text()
        yechish.setText(a+"+")
        yechish.adjustSize()
    elif yechish.text()[::-1]=="+":
        pass
plus = QPushButton("+", oyna)
plus.setGeometry(238,402,75,53)
plus.setFont(QFont("Times", 10))
plus.clicked.connect(yoz_plus)

def yoz00():
    if yechish.text()=="0":
        yechish.setText(f"00")
        yechish.adjustSize()
    else:
        a = yechish.text()+"00"
        yechish.setText(a)
        yechish.adjustSize()
nolnol = QPushButton("00", oyna)
nolnol.setGeometry(5,455,75,53)
nolnol.setFont(QFont("Times", 10))
nolnol.clicked.connect(yoz00)

def yoz_vergul():
    if yechish.text()=="0":
        yechish.setText("0,")
        yechish.adjustSize()
    elif yechish.text()!="0":
        a = yechish.text()
        yechish.setText(a+",")
        yechish.adjustSize()
    elif yechish.text()[::-1]==",":
        pass
vergul = QPushButton(",", oyna)
vergul.setGeometry(161,455,75,53)
vergul.setFont(QFont("Times", 10))
vergul.clicked.connect(yoz_vergul)

def otvet():
    try:    
        if "+" in  yechish.text() or "-" in  yechish.text() or "/" in  yechish.text() or "*" in  yechish.text() or "+" in  yechish.text():    
            if yechish.text()[-1:] == "+" or yechish.text()[-1:] == "-" or yechish.text()[-1:] == "/" or yechish.text()[-1:] == "*":    
                pass
            else:
                yechish.setText(f"{eval(yechish.text())}")
                yechish.adjustSize()
        else:
            pass
    except SyntaxError:
        pass
teng = QPushButton("=", oyna)
teng.setGeometry(238,455,75,53)
teng.setFont(QFont("Times", 10))
teng.clicked.connect(otvet)

def yoz0():
    if yechish.text()=="0":
        yechish.setText("0")
        yechish.adjustSize()
    else:
        a = yechish.text()+"0"
        yechish.setText(a)
        yechish.adjustSize()
nol = QPushButton("0", oyna)
nol.setGeometry(83,455,75,53)
nol.setFont(QFont("Times", 10))
nol.clicked.connect(yoz0)

oyna.show()
app.exec_()