from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
guestbook = []  # 메모리 상 저장 리스트
# 빈 리스트 생성

# /호출되면 index() 실행
@app.route('/', methods=['GET', 'POST'])
def index():
    #  최초에는 request가 없으니까 if 문 에 진입못하고  guestbook.html에 guestbook 리스트 전달
    #  guestbook.html 에서 POST 로 값이 넘어오고 메세지에 값이 있으면 guestbook 리스트에 값 추가
    #  추가후 다시 index() 호출 request가 없어 if 안으로 진입은 못하지만 이제  guestbook에 값이 있기 때문에
    #  {% if entries %} 가 만족하여 리스트의 값을 출력함
    if request.method == 'POST':
        name = request.form.get('name', '익명')
        message = request.form.get('message', '')
        if message:
            guestbook.append({'name': name, 'message': message})
        return redirect(url_for('index'))

    return render_template('guestbook.html', entries=guestbook)

if __name__ == '__main__':
    app.run(debug=True, port=5010)
