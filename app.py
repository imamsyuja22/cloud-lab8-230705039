from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return {'pesan': 'Halo', 'nim': '230705039'}

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)