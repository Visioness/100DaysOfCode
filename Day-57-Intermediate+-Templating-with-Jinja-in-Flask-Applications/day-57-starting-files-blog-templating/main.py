from flask import Flask, render_template
import requests
import sys
from post import Post

app = Flask(__name__)

blog_posts = [Post(id=post['id'], 
                title=post['title'],
                subtitle=post['subtitle'],
                body=post['body']) for post in requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()]

@app.route('/')
def home():
    try:
        return render_template("index.html", blog_posts=blog_posts)
    except:
        sys.exit(1)


@app.route('/post/<int:index>')
def show_post(index):
    for blog in blog_posts:
        if blog.id == index:
            return render_template('post.html', blog=blog)

if __name__ == "__main__":
    app.run()
