from flask import Flask
from flask import request
import math

app = Flask(__name__)

@app.route('/')
def readme():
    return 'Api имеет следующий функционал:<br><br>Для операций с двумя числами (в кавычках): "/действие/число1/число2?mode=int_или_float", где вместо "действие" может быть "add" (сложение), "sub" (вычитание), "mul" (умножение), "div" (деление), "pow" (возведение в степень), "mod" (остаток от деления).<br><br>Для извлечения квадратного корня: "/sqrt/число?mode=int_или_float".<br><br>Для тригонометрических функций: "/действие/число?mode=int_или_float&rad=yes_или_no", где вместо "действие" может быть "sin" (синус), "cos" (косинус), "tan" (тангенс). '

def convert_int(a, b):
    return [int(a), int(b)]

def convert_float(a, b):
    return [float(a), float(b)]

def convert_radian(a):
    return a * math.pi / 180

@app.route('/add/<a>/<b>')
def add(a, b):
    format = request.args.get('mode')
    if format == 'int':
        a, b = convert_int(a, b)
    elif format == 'float':
        a, b = convert_float(a, b)
    else:
        return 'Incorrect mode input'

    return str(a + b)

@app.route('/sub/<a>/<b>')
def sub(a, b):
    format = request.args.get('mode')
    if format == 'int':
        a, b = convert_int(a, b)
    elif format == 'float':
        a, b = convert_float(a, b)
    else:
        return 'Incorrect mode input'

    return str(a - b)

@app.route('/mul/<a>/<b>')
def mul(a, b):
    format = request.args.get('mode')
    if format == 'int':
        a, b = convert_int(a, b)
    elif format == 'float':
        a, b = convert_float(a, b)
    else:
        return 'Incorrect mode input'

    return str(a * b)

@app.route('/div/<a>/<b>')
def div(a, b):
    format = request.args.get('mode')
    if format == 'int':
        a, b = convert_int(a, b)
    elif format == 'float':
        a, b = convert_float(a, b)
    else:
        return 'Incorrect mode input'

    if b == 0:
        return "Can't divide by null"

    return str(a / b)

@app.route('/sqrt/<a>')
def sqrt(a):
    if float(a) < 0:
        return "Number must be >= 0"

    format = request.args.get('mode')
    if format == 'int':
        return str(int(math.sqrt(float(a))))
    elif format == 'float':
        return str(math.sqrt(float(a)))
    else:
        return "Incorrect mode input"

@app.route('/mod/<a>/<b>')
def mod(a, b):
    format = request.args.get('mode')
    if format == 'int':
        a, b = convert_int(a, b)
    elif format == 'float':
        a, b = convert_float(a, b)
    else:
        return 'Incorrect mode input'

    if b == 0:
        return "Can't divide by null"

    return str(a % b)

@app.route('/pow/<a>/<b>')
def pow(a, b):
    format = request.args.get('mode')
    if format == 'int':
        a, b = convert_int(a, b)
    elif format == 'float':
        a, b = convert_float(a, b)
    else:
        return 'Incorrect mode input'

    return str(a ** b)

@app.route('/sin/<a>')
def sin(a):
    format = request.args.get('mode')
    if format == 'int':
        a = int(a)
    elif format == 'float':
        a = float(a)
    else:
        return 'Incorrect mode input'

    measure = request.args.get('rad')
    if measure == 'yes':
        return str(math.sin(a))
    elif measure == 'no':
        return str(math.sin(a * math.pi / 180))
    else:
        return 'Incorrect rad input'

@app.route('/cos/<a>')
def cos(a):
    format = request.args.get('mode')
    if format == 'int':
        a = int(a)
    elif format == 'float':
        a = float(a)
    else:
        return 'Incorrect mode input'

    measure = request.args.get('rad')
    if measure == 'yes':
        return str(math.cos(a))
    elif measure == 'no':
        return str(math.cos(a * math.pi / 180))
    else:
        return 'Incorrect rad input'

@app.route('/tan/<a>')
def tan(a):
    format = request.args.get('mode')
    if format == 'int':
        a = int(a)
    elif format == 'float':
        a = float(a)
    else:
        return 'Incorrect mode input'

    if (a == math.pi / 2 or a == 3 * math.pi / 2):
        return "Can't calculate tangens for this number"

    measure = request.args.get('rad')
    if measure == 'yes':
        return str(math.tan(a))
    elif measure == 'no':
        return str(math.tan(a * math.pi / 180))
    else:
        return 'Incorrect rad input'
