from flask import (Flask, render_template, request, redirect,
jsonify, url_for, flash, make_response, session as login_session)


app = Flask(__name__)


@app.route('/')

def HomePage():
    """ returns index page """
    return render_template('index.html')



@app.route('/Shop')

def Shop():
    """ returns index page """
    return render_template('product.html')

@app.route('/Features')

def Features():
    """ returns index page """
    return render_template('cart.html')

@app.route('/About')

def About():
    """ returns index page """
    return render_template('about.html')


@app.route('/Contact')

def Contact():
    """ returns index page """
    return render_template('contact.html')






if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jJHDmN]LWX/,?RT'
    app.debug = True
    app.run(host='0.0.0.0', threaded = True)
            