from flask import Flask, app, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    datosobtenido=requests.get('https://api.dailymotion.com/videos?channel=sport&limit=10')
    datosFormtoJSON= datosobtenido.json()
    print(datosFormtoJSON)
    
    return render_template('index.html', datos=datosFormtoJSON['list'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
