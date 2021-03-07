from flask import Flask

app = Flask('zerowide')

@app.route('/')
def helloWorld():
    return 'hello,world'

if __name__ == '__main__':
    app.run('127.0.0.1')

