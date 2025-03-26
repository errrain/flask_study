from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
         <form method="POST" action="/result">
            이름: <input type="text" name="name"><br>
            나이: <input type="number" name="age"><br>
            <input type="submit" value="전송">
        </form>   
    '''

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    age = int(request.form['age'])
    if age >= 20:
        result = '성인입니다.'
    else:
        result = '미성년자입니다.'
    return f'{name}님은 {age}세이고, {result}'

if __name__ == '__main__':
    app.run(debug=True, port=5002)
