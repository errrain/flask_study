from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'app2의 루트 페이지입니다.'
"""
 경로가 / 일경우 localhost/ 이면 home 함수를 사용한다.
"""


@app.route('/hello/<name>')
def hello(name):
    return f'안녕하세요, {name}님! 여긴 app2입니다.'

"""
 경로가 /hello/ 일경우 localhost/hello/문자열 이면
 hello() 함수를 실행하는데 주소창에서 넘어온 문자열을 name 이라는 변수에 넣고 
 출력한다. 
"""

@app.route('/age/<int:age>')
def show_age(age):
    if age >= 20:
        return f'{age}세는 성인입니다.'
    else:
        return f'{age}세는 미성년자입니다.'

"""
 경로가 /hello/ 일경우 localhost/age/정수 이면
 show_age() 함수를 실행하는데 주소창에서 넘어온 수를 비교하여 20보다 크거나 같으면 성인 출력하고 그렇지 않으면 미성년자를  
 출력한다. 
"""
"""
즉 route는 인자로 path를 받고 파싱하여 형식에 맞는 값이 있으면 해당 함수를 실행한다.
"""

if __name__ == '__main__':
    app.run(debug=True, port=5001)
