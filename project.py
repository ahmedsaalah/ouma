from products import *

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





@app.route('/')

def HomePage():
    """ returns index page """
    return render_template('index.html')



@app.route('/adminProducts')

def adminProducts():
    """ returns index page """
    return render_template('adminProducts.html')




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
            