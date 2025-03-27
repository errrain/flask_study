from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users')
def users():
    user_list = [
        {'name': '홍길동', 'age': 25},
        {'name': '이순신', 'age': 35},
        {'name': '김유신', 'age': 45}
    ]
    return render_template('user_list.html', users=user_list)

if __name__ == '__main__':
    app.run(debug=True, port=5006)