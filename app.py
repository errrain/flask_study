from flask import Flask
"""
flask라는 페키지 안에서 'Flask'라는 클래스만 사용
"""
app = Flask(__name__)
"""
Flask()  : 생성자를 사용해서
__name__ : 현재 이 파일로  
app 변수? 객체? 를 생성한다.


 기다리고 있다가 경로 / 가 호출되면 함수 HELLO를 실행해라
 app의 route() 는 근본적으로 flask 페키지의 Flask 클래스에 있는 route() 라는 함수
"""
@app.route('/')
def hello():
    return '안녕하세요! Flask 첫 서버입니다.'

"""
만약에 이 파일("__name__") 이  실행되는 자체파일 이면 Flask 의 run() 함수를 실행하고 디버그 모드로 동작한다.
"""
if __name__ == '__main__':
    app.run(debug=True)