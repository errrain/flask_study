from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')
"""
/ 를 기다리고 있다가 호출이 오면 index 함수가 호출되고 render_template() 함수에 의하여 form.html 릏 읽어 들인후 브라우저에 출력한다 
디렉토리 templates 를 어디서 경로가 세팅 되었는지는 모르겠음
"""

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name', '이름없음')
    age = request.form.get('age')

    if not age or not age.isdigit():
        return render_template('result.html', name=name, message='나이는 숫자로 입력해주세요.')

    age = int(age)
    message = '성인입니다.' if age >= 20 else '미성년자입니다.'
    return render_template('result.html', name=name, age=age, message=message)
"""
form.html의 action /result 에 post 로 넘기기 때문에 submit을 실행하면 @app.route('/result', methods=['POST'])가 실행됨
form 의 input name과 같은 이름으로 변수가 선언되었고 name 은 request.form.get 해서 name 의 값을 가저오고 없을 경우 '이름없음' 이라는 텍스트를 기본 값으로 넣는거 같음
age 는 없거나 숫자가 아니면  result.htm 에 이름과 메세지만 전달하고 종료

age = int(age) 이거는 형변환 인데....위에서 age.isdigit()로 점검되어 안되는 되는 것 아닌가?
   
if 문의 결과에 따라 result.html에  name=name, age=age, message=message 을 전달하고 프로그램 종료
"""
"""
result.html 에 보면 
{     } 사이에 python 문법을 쓸수 있는거 같고
로직의 경우 {%   로직     %}
변수의 경우 {{   변수명    }}

이렇게쓰이는 건가?

"""


if __name__ == '__main__':
    app.run(debug=True, port=5003)
