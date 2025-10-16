from flask import Flask, render_template

app = Flask(__name__)

# 模擬資料庫
posts = [
    {
        'title': '第一篇文章',
        'author': '小明',
        'content': '這是我寫的第一篇文章，內容很簡單。'
    },
    {
        'title': '第二篇文章',
        'author': '小華',
        'content': '這是第二篇文章，討論一下 Python 和 Flask 的應用。'
    },
    {
        'title': '第三篇文章',
        'author': '小李',
        'content': '這篇文章討論了部落格開發的一些心得。'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
