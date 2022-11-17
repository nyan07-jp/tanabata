from flask import Flask, render_template

app = Flask(__name__, static_folder='./templates/images')


# 表示するため、routingする
@app.route('/')
def start():
    return 'ALOHA!'
    
# http://127.0.0.1:5000/hello
@app.route('/hello')
def hello():
    msg = 'こんにちは'
    return msg


# http://127.0.0.1:5000/weather
@app.route('/weather')
def weather():
    msg = '雨がふっています'
    return msg

# HTMLファイルを表示する
@app.route('/me')
def me():
    return render_template('me.html')


if __name__=='__main__':
    app.run(debug=True)
