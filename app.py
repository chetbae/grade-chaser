from flask import Flask, request, render_template

app = Flask(__name__)

yosemite_grades = {
    '5.2-3': '',
    '5.4-5': '',
    '5.6': '',
    '5.7': '',
    '5.8': '',
    '5.9': 'V0 (4)',
    '5.10a': '',
    '5.10b': 'V0+ (4+)',
    '5.10c': 'V1 (5)',
    '5.10d': '',
    '5.11a': 'V2 (6a)',
    '5.11b': 'V3 (6a+)',
    '5.11c/d': '',
    '5.12a': 'V4 (6b/c)',
    '5.12b': 'V5 (6c)',
    '5.12c': 'V6 (6c+)',
    '5.12d': '7a',
    '5.13a': 'V7 (7a+)',
    '5.13b': 'V8 (7b)',
    '5.13c': '7c',
    '5.13d': 'V9',
    '5.14a': 'V10 (7c+)',
    '5.14b': 'V11',
    '5.14c': 'V12/13 (8a+)',
    '5.14d/5.15': ''
}

font_grades = {
    'V0': '4',
    'V0+': '4+',
    'V1': '5',
    'V2': '6a',
    'V3': '6a+',
    'V4': '6b/c',
    'V5': '6c',
    'V6': '6c+',
    'V7': '7a+',
    'V8': '7b',
    'V9': '',
    'V10': '7c+',
    'V11': '',
    'V12/13': '8a+'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert')
def convert_grade():
    grade_value = request.args.get('grade')
    grade_system = request.args.get('system')

    if grade_system == 'yosemite':
        converted_grade = yosemite_grades.get(grade_value)
    elif grade_system == 'font':
        converted_grade = font_grades.get(grade_value)
    else:
        converted_grade = "Invalid grade system. Available options: 'yosemite' and 'font'."

    return converted_grade or "Grade not found."

if __name__ == '__main__':
    app.run()
