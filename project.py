from products import *
app = Flask(__name__)





# product1 = product( name="shtna1", price =200, oldPrice=200, picture="admin", category="0",rate=3)

# db.session.add(product1)
# db.session.commit()

# product1 = product( name="shnta2", price =150, oldPrice=500, picture="admin", category="0",rate=10)

# db.session.add(product1)
# db.session.commit()


# product2 = product( name="shnta3", price =300, oldPrice=300, picture="admin", category="0",rate=5)

# db.session.add(product2)
# db.session.commit()



# db.create_all()

@app.route('/')

def HomePage():
    """ returns index page """
    return render_template('index.html')



@app.route('/Shop')

def Shop():
    """ returns index page """
    return render_template('product.html')

@app.route('/Cart')

def Cart():
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
            