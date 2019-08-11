from flask import Flask, render_template
import settings

app = Flask(__name__)



@app.route('/')
def index():


   return render_template('index.html',
                          menu = settings.menu,
                          tagline = settings.tagline,
                          numbers = ['2650', '5350', '19999'])


if __name__ == '__main__':
   app.run(debug = True)
