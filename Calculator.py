from graphics import *
win = GraphWin('Calculator', 600, 600)
win.setBackground("Lightgray")
a = Rectangle(Point(0, 0), Point(600, 100))
a.draw(win)
b = Rectangle(Point(0, 100), Point(150, 200))
be = Text(b.getCenter(), 'AC')
b.draw(win)
be.draw(win)
c = Rectangle(Point(150, 100), Point(300, 200))
ce = Text(c.getCenter(), '+/-')
c.draw(win)
ce.draw(win)
d = Rectangle(Point(300, 100), Point(450, 200))
de = Text(d.getCenter(), '%')
d.draw(win)
de.draw(win)
e = Rectangle(Point(450, 100), Point(600, 200))
el = Text(e.getCenter(), '/')
e.draw(win)
el.draw(win)
f = Rectangle(Point(0, 200), Point(150, 300))
fe = Text(f.getCenter(), 7)
f.draw(win)
fe.draw(win)
g = Rectangle(Point(150, 200), Point(300, 300))
ge = Text(g.getCenter(), 8)
g.draw(win)
ge.draw(win)
h = Rectangle(Point(300, 200), Point(450, 300))
he = Text(h.getCenter(), 9)
h.draw(win)
he.draw(win)
j = Rectangle(Point(450, 200), Point(600, 300))
je = Text(j.getCenter(), '*')
j.draw(win)
je.draw(win)
k = Rectangle(Point(0, 300), Point(150, 400))
ke = Text(k.getCenter(), 4)
k.draw(win)
ke.draw(win)
l = Rectangle(Point(150, 300), Point(300, 400))
le = Text(l.getCenter(), 5)
l.draw(win)
le.draw(win)
m = Rectangle(Point(300, 300), Point(450, 400))
me = Text(m.getCenter(), 6)
m.draw(win)
me.draw(win)
n = Rectangle(Point(450, 300), Point(600, 400))
ne = Text(n.getCenter(), '-')
n.draw(win)
ne.draw(win)
o = Rectangle(Point(0, 400), Point(150, 500))
ol = Text(o.getCenter(), 1)
o.draw(win)
ol.draw(win)
p = Rectangle(Point(150, 400), Point(300, 500))
pe = Text(p.getCenter(), 2)
p.draw(win)
pe.draw(win)
r = Rectangle(Point(300, 400), Point(450, 500))
re = Text(r.getCenter(), 3)
r.draw(win)
re.draw(win)
s = Rectangle(Point(450, 400), Point(600, 500))
se = Text(s.getCenter(), '+')
s.draw(win)
se.draw(win)
t = Rectangle(Point(0, 500), Point(300, 600))
te = Text(t.getCenter(), 0)
t.draw(win)
te.draw(win)
u = Rectangle(Point(300, 500), Point(450, 600))
ul = Text(u.getCenter(), '**')
u.draw(win)
ul.draw(win)
v = Rectangle(Point(450, 500), Point(600, 600))
ve = Text(v.getCenter(), '=')
v.draw(win)
ve.draw(win)
input = Entry(a.getCenter(), 20)
input.draw(win)
input.setText('0')
chap = Text(Point(290,10),"CALCULATOR")
chap.setFace("courier")
chap.draw(win)
lis = []
exp = ""
n = ""
exp1 = ""
def main():
    global lis
    global m
    global n
    n = ""
    lis = []
    input.setText("0")
    while True:
        try:
            q = win.getMouse()
            q1 = q.getX()
            q2 = q.getY()
        except GraphicsError:
            win.close()
            break
        if 0 < q1 < 150 and 100 < q2 < 200:
            continue
        if 150 < q1 < 300 and 100 < q2 < 200:
            continue
        if 300 < q1 < 450 and 100 < q2 < 200:
            continue
        if 450 < q1 < 600 and 100 < q2 < 200:
            continue
        if 0 < q1 < 150 and 200 < q2 < 300:
            input.setText("7")
            n = n + "7"
            break
        if 150 < q1 < 300 and 200 < q2 < 300:
            input.setText("8")
            n = n + "8"
            break
        if 300 < q1 < 450 and 200 < q2 < 300:
            input.setText("9")
            n = n +"9"
            break
        if 450 < q1 < 600 and 200 < q2 < 300:
            continue
        if 0 < q1 < 150 and 300 < q2 < 400:
            input.setText("4")
            n = n + "4"
            break
        if 150 < q1 < 300 and 300 < q2 < 400:
            input.setText("5")
            n = n + "5"
            break
        if 300 < q1 < 450 and 300 < q2 < 400:
            input.setText("6")
            n = n + "6"
            break
        if 450 < q1 < 600 and 300 < q2 < 400:
            continue
        if 0 < q1 < 150 and 400 < q2 < 500:
            input.setText("1")
            n = n + "1"
            break
        if 150 < q1 < 300 and 400 < q2 < 500:
            input.setText("2")
            n = n + "2"
            break
        if 300 < q1 < 450 and 400 < q2 < 500:
            input.setText("3")
            n = n + "3"
            break
        if 450 < q1 < 600 and 400 < q2 < 500:
            continue
        if 0 < q1 < 300 and 500 < q2 < 600:
            continue
        if 300 < q1 < 450 and 500 < q2 < 600:
            continue
        if 450 < q1 < 600 and 500 < q2 < 600:
            continue
    lis.append(n)
    return func(n, lis)
def func(n, lis):
    global exp
    while True:
        try:
            q = win.getMouse()
            q1 = q.getX()
            q2 = q.getY()
        except GraphicsError:
            win.close()
            break
        if 0 < q1 < 150 and 100 < q2 < 200:
            exp = "AC"
            return main()
        if 150 < q1 < 300 and 100 < q2 < 200:
            exp = "+/-"
            if lis[-1] == "=":
                try:
                    n = eval("n")
                    input.setText(eval("int(n) * -1"))
                    n = eval("eval(str(n))*-1")
                    lis.append("+/-")
                    return func(n, lis)
                except:
                    n = eval("eval(str(n))*-1")
                    input.setText(n)
                    lis.append("+/-")
                    return func(n, lis)
            if lis[-1]=="1" or lis[-1]=="2" or lis[-1]=="3" or lis[-1]=="4" or lis[-1]=="5" or lis[-1]=="6" or lis[-1]=="7" or lis[-1]=="8" or lis[-1]=="9" or lis[-1]=="0":
                try:
                    n = eval("n")
                    input.setText(eval("int(n) * -1"))
                    n = eval("eval(str(n))*-1")
                    lis.append("+/-")
                    return func(n, lis)
                except:
                    n = eval("eval(str(n))*-1")
                    input.setText(n)
                    lis.append("+/-")
                    return func(n, lis)
        if 300 < q1 < 450 and 100 < q2 < 200:
            exp = "%"
            if lis[-1]=="%" or lis[-1]=="+" or lis[-1]=="-" or lis[-1]=="*" or lis[-1]=="**" or lis[-1]=="/":
                return main()
            if lis[-1]=="1" or lis[-1]=="2" or lis[-1]=="3" or lis[-1]=="4" or lis[-1]=="5" or lis[-1]=="6" or lis[-1]=="7" or lis[-1]=="8" or lis[-1]=="9" or lis[-1]=="0":
                n = str(n) + exp
                lis.append("%")
                return func(n, lis)
            if lis[-1] == "=" or lis[-1] == "+/-":
                n = str(n) + exp
                lis.append("%")
                return func(n, lis)
        if 450 < q1 < 600 and 100 < q2 < 200:
            exp = "/"
            if lis[-1]=="%" or lis[-1]=="+" or lis[-1]=="-" or lis[-1]=="*" or lis[-1]=="**" or lis[-1]=="/":
                return main()
            if lis[-1]=="1" or lis[-1]=="2" or lis[-1]=="3" or lis[-1]=="4" or lis[-1]=="5" or lis[-1]=="6" or lis[-1]=="7" or lis[-1]=="8" or lis[-1]=="9" or lis[-1]=="0":
                n = str(n) + exp
                lis.append("/")
                return func(n, lis)
            if lis[-1] == "=" or lis[-1] == "+/-":
                n = str(n) + exp
                lis.append("/")
                return func(n, lis)
        if 0 < q1 < 150 and 200 < q2 < 300:
            input.setText("7")
            if lis[-1] == "=" or lis[-1] == "+/-":
                return main()
            try:
                n = n + "7"
                input.setText(eval(n))
                lis.append("7")
            except:
                n = str(n) + "7"
                input.setText(str(eval(n)))
                lis.append("7")
            return func(n, lis)
        if 150 < q1 < 300 and 200 < q2 < 300:
            input.setText("8")
            if lis[-1] == "=" or lis[-1] == "+/-":
                return main()
            try:
                n = n + "8"
                input.setText(eval(n))
                lis.append("8")
            except:
                n = str(n) + "8"
                input.setText(str(eval(n)))
                lis.append("8")
            return func(n, lis)
        if 300 < q1 < 450 and 200 < q2 < 300:
            input.setText("9")
            if lis[-1]=="=" or lis[-1]=="+/-":
                return main()
            try:
                n = n + "9"
                input.setText(eval(n))
                lis.append("9")
            except:
                n = str(n) + "9"
                input.setText(str(eval(n)))
                lis.append("9")
            return func(n, lis)
        if 450 < q1 < 600 and 200 < q2 < 300:
            exp = "*"
            if lis[-1] == "%" or lis[-1] == "+" or lis[-1] == "-" or lis[-1] == "*" or lis[-1] == "**" or lis[-1] == "/":
                return main()
            if lis[-1] == "1" or lis[-1] == "2" or lis[-1] == "3" or lis[-1] == "4" or lis[-1] == "5" or lis[-1] == "6" or lis[-1] == "7" or lis[-1] == "8" or lis[-1] == "9" or lis[-1] == "0":
                n = str(n) + exp
                lis.append("*")
                return func(n, lis)
            if lis[-1] == "=" or lis[-1] == "+/-":
                n = str(n) + exp
                lis.append("*")
                return func(n, lis)
        if 0 < q1 < 150 and 300 < q2 < 400:
            input.setText("4")
            if lis[-1] == "=" or lis[-1] == "+/-":
                return main()
            try:
                n = n + "4"
                input.setText(eval(n))
                lis.append("4")
            except:
                n = str(n) + "4"
                input.setText(str(eval(n)))
                lis.append("4")
            return func(n, lis)
        if 150 < q1 < 300 and 300 < q2 < 400:
            input.setText("5")
            if lis[-1] == "=" or lis[-1] == "+/-":
                return main()
            try:
                n = n + "5"
                input.setText(eval(n))
                lis.append("5")
            except:
                n = str(n) + "5"
                input.setText(str(eval(n)))
                lis.append("5")
            return func(n, lis)
        if 300 < q1 < 450 and 300 < q2 < 400:
            input.setText("6")
            if lis[-1] == "=" or lis[-1] == "+/-":
                return main()
            try:
                n = n + "6"
                input.setText(eval(n))
                lis.append("6")
            except:
                n = str(n) + "6"
                input.setText(str(eval(n)))
                lis.append("6")
            return func(n, lis)
        if 450 < q1 < 600 and 300 < q2 < 400:
            exp = "-"
            if lis[-1] == "%" or lis[-1] == "+" or lis[-1] == "-" or lis[-1] == "*" or lis[-1] == "**" or lis[-1] == "/":
                return main()
            if lis[-1] == "1" or lis[-1] == "2" or lis[-1] == "3" or lis[-1] == "4" or lis[-1] == "5" or lis[-1] == "6" or lis[-1] == "7" or lis[-1] == "8" or lis[-1] == "9" or lis[-1] == "0":
                n = str(n) + exp
                lis.append("-")
                return func(n, lis)
            if lis[-1] == "=" or lis[-1] == "+/-":
                n = str(n) + exp
                lis.append("-")
                return func(n, lis)
        if 0 < q1 < 150 and 400 < q2 < 500:
            input.setText("1")
            if lis[-1] == "=" or lis[-1] == "+/-":
                return main()
            try:
                n = n + "1"
                input.setText(eval(n))
                lis.append("1")
            except:
                n = str(n) + "1"
                input.setText(str(eval(n)))
                lis.append("1")
            return func(n, lis)
        if 150 < q1 < 300 and 400 < q2 < 500:
            input.setText("2")
            if lis[-1] == "+/-":
                return main()
            try:
                n = (n + "2")
                input.setText(eval(n))
                lis.append("2")
            except:
                n = str(n) + "2"
                input.setText(str(eval(n)))
                lis.append("2")
            return func(n, lis)
        if 300 < q1 < 450 and 400 < q2 < 500:
            input.setText("3")
            if lis[-1] == "=" or lis[-1] == "+/-":
                return main()
            try:
                n = n + "3"
                input.setText(eval(n))
                lis.append("3")
            except:
                n = str(n) + "3"
                input.setText(str(eval(n)))
                lis.append("3")
            return func(n, lis)
        if 450 < q1 < 600 and 400 < q2 < 500:
            exp = "+"
            if lis[-1] == "%" or lis[-1] == "+" or lis[-1] == "-" or lis[-1] == "*" or lis[-1] == "**" or lis[-1] == "/":
                return main()
            if lis[-1] == "1" or lis[-1] == "2" or lis[-1] == "3" or lis[-1] == "4" or lis[-1] == "5" or lis[-1] == "6" or lis[-1] == "7" or lis[-1] == "8" or lis[-1] == "9" or lis[-1] == "0":
                n = str(n) + exp
                lis.append("+")
                return func(n, lis)
            if lis[-1] == "=" or lis[-1] == "+/-":
                n = str(n) + exp
                lis.append("+")
                return func(n, lis)
        if 0 < q1 < 300 and 500 < q2 < 600:
            input.setText("0")
            if lis[-1] == "=" or lis[-1] == "+/-":
                return main()
            if lis[-1] == "/":
                return main()
            try:
                n = n + "0"
                input.setText(eval(n))
                lis.append("0")
            except:
                n = str(n) + "0"
                input.setText((eval(n)))
                lis.append("0")
            return func(n, lis)
        if 300 < q1 < 450 and 500 < q2 < 600:
            exp = "**"
            if lis[-1] == "%" or lis[-1] == "+" or lis[-1] == "-" or lis[-1] == "*" or lis[-1] == "**" or lis[-1] == "/":
                return main()
            if lis[-1] == "1" or lis[-1] == "2" or lis[-1] == "3" or lis[-1] == "4" or lis[-1] == "5" or lis[-1] == "6" or lis[-1] == "7" or lis[-1] == "8" or lis[-1] == "9" or lis[-1] == "0":
                n = str(n) + exp
                lis.append("**")
                return func(n, lis)
            if lis[-1] == "=" or lis[-1] == "+/-":
                n = str(n) + exp
                lis.append("**")
                return func(n, lis)
        if 450 < q1 < 600 and 500 < q2 < 600:
            exp = "="
            if lis[-1] == "%" or lis[-1] == "+" or lis[-1] == "-" or lis[-1] == "*" or lis[-1] == "**" or lis[-1] == "/":
                return main()
            if lis[-1]=="1" or lis[-1]=="2" or lis[-1]=="3" or lis[-1]=="4" or lis[-1]=="5" or lis[-1]=="6" or lis[-1]=="7" or lis[-1]=="8" or lis[-1]=="9" or lis[-1]=="0":
                lis.append("=")
                return func(n, lis)


main()


































































































































