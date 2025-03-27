from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def styled():
    return render_template('styled_page.html')

if __name__ == '__main__':
    app.run(debug=True, port=5009)