from products import *
from users import user
from contacts import contact
from datetime import timedelta
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
import datetime
from collections import Counter
# db.create_all()

# product3 = product( name="Leather", price =200, oldPrice=200, picture="1.jpg", category="1",rate=3)

# product1 = product( name="Belt Bags", price =150, oldPrice=500, picture="2.jpg", category="2",rate=10)


# product2 = product( name="Crossbody", price =300, oldPrice=300, picture="3.jpg", category="3",rate=5)

# product4 = product( name="Large Bags", price =150, oldPrice=500, picture="4.jpg", category="4",rate=10)


# product5 = product( name="Handbags", price =300, oldPrice=300, picture="5.jpg", category="5",rate=5)
# product6 = product( name="mini bags", price =200, oldPrice=200, picture="6.jpg", category="6",rate=5)
# db.session.add(product3)
# db.session.add(product1)
# db.session.add(product2)
# db.session.add(product4)
# db.session.add(product5)
# db.session.add(product6)
# db.session.commit()

# admin = user( username="oumaAdmin", password="ouma111")

# db.session.add(admin)
# db.session.commit()



@app.route('/')

def HomePage():
    """ returns index page """
    return render_template('index.html')
@app.template_filter('TimeEgypt')
def TimeEgypt(time):

    return 'time'


@app.route('/adminProducts')

def adminProducts():
    if 'id' in login_session or True:

        products = product.query.filter().all()

        return render_template('adminProducts.html',products=products)
    else :
        return redirect(url_for('HomePage'))


@app.route('/contactAdmin')

def contactAdmin():
    if 'id' in login_session :

        contacts = contact.query.filter().all()
        

        return render_template('contactAdmin.html',contacts=contacts)
    else :
        return redirect(url_for('HomePage'))


@app.route('/DeleteProduct', methods=['POST','GET'])

def DeleteProduct():
    id =request.form["productId"]


    if 'id' in login_session :
  

        theProduct = product.query.filter_by(id=id).first()
        db.session.delete(theProduct)
        db.session.commit()
        return "dedfe"
        
    else :
        return redirect(url_for('HomePage'))



@app.route('/addToCart', methods=['POST','GET'])

def addToCart():

    id =request.form["pid"]
    
    if 'productid' in login_session :

        arrayPid = login_session["productid"]
        arrOccurances = login_session["productocc"]
        if id in arrayPid :

            index = arrayPid.index(id)
            arrOccurances[index] = arrOccurances[index] +1
        else :
            arrayPid.append(id)
            arrOccurances.append(1)
    else :
        arrayPid = []
        arrOccurances =[]
        arrayPid.append(id)
        arrOccurances.append(1)
    
    login_session["productid"] = arrayPid
    login_session["productocc"] = arrOccurances
    value =Cartvalue()
    return value



@app.route('/loginPage', methods=['POST','GET'])

def loginpage():
    if 'id' in login_session :
        return redirect(url_for('adminProducts'))
        

    else:
        return  render_template('login.html')
    

@app.route('/logout', methods=['POST','GET'])

def logout():
    login_session.clear()
    return redirect(url_for('HomePage'))
    




@app.route('/login', methods=['POST','GET'])

def login():
        username =request.form["username"]
        password =request.form["password"]
        
        TheUser = user.query.filter_by(username=username , password=password).first()
        if TheUser is not None:

            login_session['id'] = TheUser.id
            login_session['username'] = TheUser.username

            return redirect(url_for('adminProducts'))
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

@app.route('/Shop/<string:category>/page/<int:page>/',)
@app.route('/Shop/<string:category>',)
@app.route('/Shop',)

def Shop(category=0,page =1):
    """ returns index page """
    per_page = 9
    if category == 0 or category == "0":
        products = product.query.filter().paginate(page,per_page,error_out=False)
    else:
        
        products = product.query.filter_by(category=category).paginate(page,per_page,error_out=False)


    return render_template('product.html',products=products.items,category=category,page=page,pages=products.pages)

@app.route('/Cart')

def Cart():
    """ returns index page """
    products =[]
    price = 0
    arrOccurances =[]
    if 'productid' in login_session :
        cart = login_session["productid"]
        arrOccurances = login_session["productocc"]
        
        
        
        products = product.query.filter(product.id.in_(cart)).all()
        price = calculatingMoney(products)
        return render_template('cart.html',products=products,arrOccurances=arrOccurances,price=price)

    else :
        price = 0
        
        return render_template('cart.html',price =price)

def calculatingMoney(products):
    price = 0

    for i in range(len(products)):
        price = price + (products[i].price * login_session["productocc"][i])
       

    return price



@app.route('/About')

def About():
    """ returns index page """
    return render_template('about.html')


@app.route('/Contact', methods=['POST','GET'])

def Contact():
    """ returns index page """
    if request.method == 'POST' :
        name =request.form["name"]
        phone =request.form["number"]
        email =request.form["email"]
        message =request.form["message"]


        contactx = contact( name=name, phone =phone, email=email, message=message)
        db.session.add(contactx)
        db.session.commit()  


        return render_template('contact.html')

    else :
        
        return render_template('contact.html')

@app.route('/Cartvalue', methods=['POST','GET'])
def Cartvalue():
    
    if 'productocc' in login_session :
        
        return str(sum(login_session["productocc"]))
    else :
        
        return "0"





if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jJHDmN]LWX/,?RT'
    app.debug = True
    # app.permanent_session_lifetime = timedelta(minutes=30)
    app.run(host='0.0.0.0', threaded = True)
            