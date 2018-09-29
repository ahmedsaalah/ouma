#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash


from flask import session as login_session
from sqlalchemy import or_

import requests
import platform
import json
import httpagentparser
from pprint import pprint


from companies import company ,db,app
from orders import orders
from transaction import transaction


@app.template_filter('datetime')
def _datetime(string):
    

    return datetimeConvert(string)


# session.query(User).filter(User.name.like('e%'))
def datetimeConvert(date):
    dateArr = str(date).split(" ")
    hr = int(dateArr[1].split(":")[0])
    typ =""
    if hr > 12 :
        typ = "PM"
        hr = hr -12
    else :
        typ = "AM"
    
    date = dateArr[0] + " " + str(hr)+ ":"+dateArr[1].split(":")[1]+":"+dateArr[1].split(":")[2]+" "+typ
    return date



@app.route('/beg')
def beg():
    db.create_all()

    return redirect(url_for('HomePage'))    

@app.route('/login', methods=['POST','GET'])
def Login():

    return render_template('login.html' )


''' Views  '''
@app.route('/', methods=['POST','GET'])
def HomePage():
    if request.method == 'POST' and request.form["search"]:
        word =request.form["search"]
        word  = "%" + word + "%"

        companies = company.query.filter(or_(company.name.like(word) , company.address.like(word) ,
        company.telephone.like(word), company.price1.like(word), company.price2.like(word)
        ) ).all()

    else :
    
    
        companies = company.query.filter().all()

    return render_template('home.html' ,companies = companies)

@app.route('/AddCompany', methods=['POST','GET'])
def AddCompany():
    name =request.form["name"]
    address =request.form["address"]
    mobile =request.form["mobile"]
    price1 =request.form["price1"]
    price2 =request.form["price2"]
    newcompany = company(name=name , address =address,telephone=mobile,price1 = price1 ,price2= price2)
    
    db.session.add(newcompany)
    db.session.commit()
  
    return redirect(url_for('HomePage'))
     
@app.route('/EditCompany', methods=['POST','GET'])
def EditCompany():
    id =request.form["id"]
    name =request.form["name"]
    address =request.form["address"]
    mobile =request.form["mobile"]
    price1 =request.form["price1"]
    price2 =request.form["price2"]
    comp = company.query.filter_by(id=id).first()
    comp.name = name
    comp.address = address
    comp.telephone = mobile
    comp.price1 = price1
    comp.price2 = price2
    db.session.commit()
    return redirect(url_for('HomePage'))

@app.route('/DeleteCompany', methods=['POST','GET'])
def DeleteCompany():
    id =request.form["id"]
    comp = company.query.filter_by(id=id).first()
    db.session.delete(comp)
    db.session.commit()
    return redirect(url_for('HomePage'))

@app.route('/AddOrder', methods=['POST','GET'])
def AddOrder():

    company_id =request.form["id"]
    taxes =request.form["taxes"]
    discount =request.form["discount"]
    quantity1 =request.form["quantity1"]
    quantity2 =request.form["quantity2"]
    paymentDay = request.form["paymentDay"]
    comp = company.query.filter_by(id=company_id).first()
    
    price = float(( comp.price1 * float(quantity1)) + (comp.price2 * float(quantity2)))

    totalTaxes = price *float(taxes)

    totalPrice = price + totalTaxes

    discount = float(discount)*totalPrice

    totalPrice = totalPrice - discount

    newOreder = orders(company_id=company_id ,paymentDay=paymentDay,  taxes =taxes,discount= discount ,quantity1 = quantity1,quantity2= quantity2 ,price= totalPrice)

    db.session.add(newOreder)
    db.session.commit()
    return redirect(url_for('HomePage'))


@app.route('/GetOrders', methods=['POST','GET'])
def GetOrders():
    company_id =request.form["id"]
    i=0
    AllOrders = orders.query.filter_by(company_id=company_id).all()
    print(AllOrders)

    output = "<table id='emptable' class='table table-striped table-bordered table-hover table-condensed'>"
    output += "<thead><tr><th>المسلسل</th><th>الحجم الاول </th><th>الحجم الثاني </th>"
    output += "<th>معاد الطلبيه</th><th>معاد التحصيل</th><th>سعر</th></tr></thead>"
    for order in AllOrders:
        i= i + 1  
        output +="<tr>" 
            
        output +="<td>"+str(i)+"</td>"
        output +="<td>"+str(order.quantity1) +"</td>"
        output +="<td>"+str(order.quantity2) +"</td>"
        output +="<td>"+datetimeConvert(str(order.time)) +"</td>"
        output +="<td>"+str(order.paymentDay) +"</td>"
        output +="<td>"+str(order.price) +"</td>"
        output +="</tr>"
                    
    output += "</table>"
    return output

     




### transactions page
@app.route('/transactions', methods=['POST','GET'])
def transactions():
    if request.method == 'POST' :
        if request.form["end"]:
            end= request.form["end"] +" 23:59:59"
        if request.form["search"]:
            word =request.form["search"]
        if request.form["beg"]:
            beg =request.form["beg"]

        if request.form["search"] and request.form["beg"] and request.form["end"]:

            transactions = transaction.query.filter(transaction.name.like(word) 
            ,transaction.time >= beg ,transaction.time <= end
            ).all()
        elif request.form["beg"] and request.form["end"]:


            transactions = transaction.query.filter(transaction.time >= beg ,transaction.time <= end
            ).all()
            print(end)
        

        elif request.form["search"]  and request.form["end"]:

            transactions = transaction.query.filter(transaction.name.like(word) 
            ,transaction.time <= end
            ).all()
        elif request.form["search"] and request.form["beg"] :

            transactions = transaction.query.filter(transaction.name.like(word) 
            ,transaction.time >= beg 
            ).all()
        elif request.form["search"] :

            transactions = transaction.query.filter(transaction.name.like(word) 
            
            ).all()

        elif  request.form["beg"] :

            transactions = transaction.query.filter(transaction.time >= beg 
            ).all()

        elif request.form["end"]  :

            transactions = transaction.query.filter(transaction.time <= end 
            ).all()


    else :
    
    
        transactions = transaction.query.filter().all()
        print(vars(transactions[0]))
    totalpaid , totalleft = GetAllPaidAndAllLeft(transactions)
    return render_template('transactions.html'  ,transactions=transactions ,totalpaid=totalpaid
    ,totalleft =totalleft)



@app.route('/AddTransaction', methods=['POST','GET'])
def AddTransaction():
    details =request.form["details"]
    paid =request.form["paid"]
    left =request.form["left"]

    newTransaction = transaction(details=details , paid =paid,left=left)
    
    db.session.add(newTransaction)
    db.session.commit()
  
    return redirect(url_for('transactions'))
     
@app.route('/EditTransaction', methods=['POST','GET'])
def EditTransaction():
    id =request.form["id"]
    details =request.form["details"]
    paid =request.form["paid"]
    left =request.form["left"]

    thetransaction = transaction.query.filter_by(id=id).first()
    thetransaction.details = details
    thetransaction.paid = paid
    thetransaction.left = left
    db.session.commit()
    return redirect(url_for('transactions'))

@app.route('/DeleteTransaction', methods=['POST','GET'])
def DeleteTransaction():
    id =request.form["id"]
    THEtransaction = transaction.query.filter_by(id=id).first()
    db.session.delete(THEtransaction)
    db.session.commit()
    return redirect(url_for('transactions'))
    
def GetAllPaidAndAllLeft(transcs):
    allpaid , allleft = 0.0 , 0.0
    for transc in transcs:
        allpaid += float(transc.paid)
        allleft += float(transc.left)
    
    return allpaid , allleft 
if __name__ == '__main__':
   app.run(debug = True)