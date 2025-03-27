from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('prg_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '이름없음')
    return redirect(url_for('result', username=name))

@app.route('/result')
def result():
    username = request.args.get('username', '익명')
    return render_template('prg_result.html', name=username)

if __name__ == '__main__':
    app.run(debug=True, port=5005)

"""
submit()이 호출되면 request로 넘어온 name 값을 가저오고 result()로 username 변수명으로 값을 전달 
result()에서는 prg_result.html 에 name 값 전달
redirect() 함수의 기본기능 확인 필요
url_for() 함수의 기본기능 확인 필요
"""