import os
from flask import Flask, render_template
from werkzeug import SharedDataMiddleware

app = Flask(__name__)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/': os.path.join(os.path.dirname(__file__), 'static')
})

@app.route('/')
def index():
    CONTACT = {
        'email':
        'mailto:&#x67;&#x65;&#x6f;&#x72;&#x67;&#x65;&#x2e;&#x74;&#x61;&#x6e;&#x6b;&#x65;&#x72;&#x73;&#x6c;&#x65;&#x79;&#x40;&#x67;&#x6d;&#x61;&#x69;&#x6c;&#x2e;&#x63;&#x6f;&#x6d;',
        'hn': 'https://news.ycombinator.com/user?id=gtank',
        'github': 'https://github.com/gtank',
        'twitter': 'https://twitter.com/_gtank'
    }
    return render_template("index.html", contact=CONTACT)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
