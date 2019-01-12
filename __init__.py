from products import *
from users import user
from contacts import contact
from orders import order
from carts import cart
from about import aboutdb
from datetime import timedelta
import json
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

# admin = user( username="oumaAdmin", password="ouma111")

# db.session.add(admin)

# order1 = order(name ="salah", address="sidibeshr", phone="5556303", email="a7mad.sala7@live.com", cost=500,notes ="Edwededdddddddddddddd")
# db.session.add(order1)
# db.session.commit()

# cart1 = cart(order_id =1, product_id=1)
# db.session.add(cart1)
# cart1 = cart(order_id =1, product_id=2)
# db.session.add(cart1)
# cart1 = cart(order_id =1, product_id=3)
# db.session.add(cart1)
# cart1 = cart(order_id =1, product_id=4)
# db.session.add(cart1)
# db.session.commit()
# about1 = aboutdb(message ='To create and deploy a key with Linux or Mac OS X:Create a key on your local computer.Open a terminal session.Create ~/.ssh, if it does not already exist. Enter mkdir -p $HOME/.ssh. Switch to the ~/.ssh directory. Enter cd ~/.ssh and press Enter.press Enter.Secure the SSH keys. Enter chmod 600 ~/.ssh/authorized_keys and press Enter.Secure the SSH directory. Enter chmod 700 ~/.ssh and press Enter'
# , img='')
# db.session.add(about1)
# db.session.commit()
@app.route('/')

def HomePage():
    """ returns index page """
    products = product.query.filter().order_by(product.id.desc()).limit(5).all()
    return render_template('index.html',products=products)



@app.route('/adminProducts')

def adminProducts():
    if 'id' in login_session :
        from pprint import pprint
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



@app.route('/ordersAdmin')

def orderAdmin():
    if 'id' in login_session :

        orders = order.query.filter_by(checkDone=1).all()
        

        return render_template('orders.html',orders=orders)
    else :
        return redirect(url_for('HomePage'))






@app.route('/DeleteOrder', methods=['POST','GET'])

def DeleteOrder():
    orderID =request.form["orderID"]

    orders = order.query.filter_by(id=orderID).first()
    orders.checkDone = 1
    db.session.commit()
    return "DONE"    






@app.route('/aboutAdmin', methods=['POST','GET'])

def aboutAdmin():
    if 'id' in login_session :
        if  request.method == 'POST':



            abo = aboutdb.query.filter().first()
            if  'msg' in request.args:
                abo.message =request.form["msg"]

            if 'img' in request.files:

                

                file = request.files['img']
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                abo.img = filename

                
            db.session.commit()
        return render_template('adminAbout.html')
    else :
        return redirect(url_for('HomePage'))


@app.route('/orderProducts', methods=['POST','GET'])

def orderProducts():

    id =request.form["orderID"]
    

    
    

    products = cart.query.join(product, cart.product_id==product.id).add_columns(cart.occur,product.price, product.name, product.picture).filter(cart.order_id == id).all()

    return makeITCallable(products)


def makeITCallable(products):
    names, prices,pictures,occ = [], [],[], []
    for product in products:
        occ.append(product[1])
        prices.append(product[2])
        names.append(product[3])
        pictures.append(product[4])



    products_arr = [{"Names": n, "Occur": o,"Price":p,"Picture":pic} for n,o,p,pic in zip(names, occ,prices,pictures)]

    return  json.dumps(products_arr)
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

@app.route('/ClearCart', methods=['POST','GET'])
def ClearCart():
    if 'productid' in login_session :

        login_session.clear()
    return "0"
    

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
        total = price+ 50
        login_session["total"] =total
        return render_template('cart.html',total=total ,products=products,arrOccurances=arrOccurances,price=price)

    else :
        price = 0
        
        
        return render_template('cart.html',price =price)

def calculatingMoney(products):
    price = 0

    for i in range(len(products)):
        price = price + (products[i].price * login_session["productocc"][i])
       

    return price
@app.route('/makeOrder', methods=['POST','GET'])
def makeOrder():
     
    if request.method == 'POST' :
        name =request.form["name"]
        address =request.form["city"]
        address +=request.form["address"]
        phone =request.form["phone"]
        email =request.form["email"]
        notes =request.form["notes"]
        cost =login_session["total"]


        orderx = order( name=name, phone =phone, email=email, address=address ,cost=cost,notes=notes)
        db.session.add(orderx)
        
        db.session.commit()
  
        
        for i in range(len(login_session['productocc'])):
            cartx = cart( product_id=login_session["productid"][i], order_id =orderx.id, occur=login_session["productocc"][i])
            db.session.add(cartx)
            
            db.session.commit()

          
        del login_session["productid"]
        del login_session["productocc"]
        del login_session["total"]

        return redirect(url_for('Cart'))

    else :
        
        return redirect(url_for('HomePage'))




@app.route('/About')

def About():
    """ returns index page """


    abo = aboutdb.query.filter().all()
    


    return render_template('about.html',abouts=abo)


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
    app.permanent_session_lifetime = timedelta(minutes=30)
    app.run(host='0.0.0.0', threaded = True)
            
