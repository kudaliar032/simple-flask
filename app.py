from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return 'Hello, this simple Flask!'


@app.route('/other')
def other_page():
  return 'Other flask page oh!'


if __name__ == '__main__':
  app.run()
