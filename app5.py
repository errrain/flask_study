from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/user', methods=['GET','POST'])
def user():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            return render_template('user.html', message='이름을 입력하세요.')
        return render_template('user.html', message=f'{name}님, 반갑습니다!')

        # GET 방식인 경우: 입력 폼 보여줌
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True, port=5004)
"""
이거는 /user 가 호출될때 데이터 전송 타입을 GET, POST 둘다 사용한다고 선언한거 같아
user() 가 실행되면 일단 최초는 request가 없기 때문에 그냥 user.html 을 실행함
message 값이 없기 때문에  <p><strong>{{ message }}</strong></p> 는 최초는 출력되지 않음
user.html 에서 submit 했을때 name이 없으면 이름을 입력하세요 있으면 name 님 반갑습니다를 출력

질문  
1. @app.route('/user', methods=['POST']) 로 해도 정상작동 되는거 아닌가
2. 혹시 데이터의 입력은 POST 출력은 GET 으로 보낸 건가?
"""