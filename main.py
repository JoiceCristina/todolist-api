from flask import Flask;

app = Flask(__name__)

@app.route('/api')
def index():
    return 'Api rodando'

if __name__ == '__main__':
    app.run(debug=True)