from products import *
from users import user
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# db.create_all()

# product3 = product( name="shtna1", price =200, oldPrice=200, picture="admin", category="0",rate=3)

# product1 = product( name="shnta2", price =150, oldPrice=500, picture="admin", category="0",rate=10)


# product2 = product( name="shnta3", price =300, oldPrice=300, picture="admin", category="0",rate=5)
# db.session.add(product3)
# db.session.add(product1)
# db.session.add(product2)
# db.session.commit()

# admin = user( username="oumaAdmin", password="ouma111")

# db.session.add(admin)
# db.session.commit()



@app.route('/')

def HomePage():
    """ returns index page """
    return render_template('index.html')



@app.route('/adminProducts')

def adminProducts():
    if 'id' in login_session :

        products = product.query.filter().all()

        return render_template('adminProducts.html',products=products)
    else :
        return redirect(url_for('HomePage'))



@app.route('/DeleteProduct', methods=['POST','GET'])

def DeleteProduct():
    


    if 'id' in login_session :
  
        id =request.form["productId"]
        theProduct = product.query.filter_by(id=id).first()
        db.session.delete(theProduct)
        db.session.commit()

        return render_template('adminProducts.html',products=products)
    else :
        return redirect(url_for('HomePage'))










@app.route('/login', methods=['POST','GET'])

def login():
        username =request.form["username"]
        password =request.form["password"]
        
        TheUser = user.query.filter_by(username=username , password=password).first()
        if TheUser is not None:

            login_session['id'] = TheUser.id
            login_session['username'] = TheUser.username

            return redirect(url_for('HomePage'))
        else :
            return redirect(url_for('HomePage'))






@app.route('/editProduct', methods=['POST','GET'])

def editProduct():
    if 'id' in login_session :
        id =request.form["productId"]
        price =request.form["price"]

        cat =request.form["category"]
        oldPrice =request.form["oldPrice"]


        theProduct = product.query.filter_by(id=id).first()
        theProduct.price = price
        theProduct.oldPrice = oldPrice
        theProduct.category = cat
        db.session.commit()
        
        return redirect(url_for('adminProducts'))
    else :
        return redirect(url_for('HomePage'))

    


@app.route('/addProduct', methods=['POST','GET'])
def addProduct():

    if request.method == 'POST' :
                
        name =request.form["name"]
        price =request.form["price"]
        cat =request.form["cat"]

        if 'fileToUpload' in request.files:
            file = request.files['fileToUpload']
            
        
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            productx = product( name=name, price =price, oldPrice=price, picture=filename, category=" "+cat,rate=0)
            db.session.add(productx)
            db.session.commit()            
                
                        
                        

    
    """ returns index page """
    return render_template('addProduct.html')

@app.route('/Shop/<string:category>',)

def Shop(category="ALL"):
    """ returns index page """
    product3 = product( name="Leather", price =200, oldPrice=200, picture="1.jpg", category="1",rate=3)

    product1 = product( name="Belt Bags", price =150, oldPrice=500, picture="2.jpg", category="2",rate=10)


    product2 = product( name="Crossbody", price =300, oldPrice=300, picture="3.jpg", category="3",rate=5)
    
    product4 = product( name="Large Bags", price =150, oldPrice=500, picture="4.jpg", category="4",rate=10)


    product5 = product( name="Handbags", price =300, oldPrice=300, picture="5.jpg", category="5",rate=5)
    product6 = product( name="mini bags", price =200, oldPrice=200, picture="6.jpg", category="6",rate=5)
    
    
    products = []
    products.append(product1)
    products.append(product3)
    products.append(product2)
    products.append(product4)
    products.append(product5)
    products.append(product6)    
    return render_template('product.html',products=products)

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
            