# -*- coding: UTF-8 -*-
import pandas as pd
from IPython.display import HTML
import csv
import test
from flask import Flask, render_template,url_for,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',howtouse='How to use',htu1='Insert the English  ')

@app.route('/search',methods= ("GET","POST"))
def search():
    return render_template("search.html")

@app.route('/result',methods= ("GET","POST"))
def result():   
    try:
        
        select = request.form.getlist('selectbox')
        r_list = test.action(select)
        # print(select) 
        # 排序項目:便利商店、診所，select = ['convenienceStore', 'clinic']
    except:
        print('none')
    try:
        # 回傳運算結果
        if request.method == 'POST':
            # r_list = []
            # r_list = ['第一個','第二個','第三個','第四個','第五個']
            return render_template("result.html",r_title = '推薦鄰里：',r_list = r_list)
        else:
            return render_template("search.html")
    except:
        return render_template("search.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='6138',debug = True)