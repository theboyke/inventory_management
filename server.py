import peeweedbevolve
from flask import Flask, render_template, request,url_for, redirect, flash
from models import db,Store 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super sercret key'

@app.before_request 
def before_request():
   db.connect()

@app.after_request 
def after_request(response):
   db.close()
   return response

@app.cli.command() 
def migrate(): 
   db.evolve(ignore_tables={'base_model'}) 

@app.route("/",methods=['GET'])
def index():
   return render_template('index.html')

@app.route("/store",methods=['GET'])
def store():
   return render_template('store.html')

@app.route("/store",methods=['POST'])
def create_store():
   name = request.form.get('name_user_input')
   create_store = Store(name=name)

   if Store.select().where(Store.name == name):
      flash("Store already exist")
      return redirect(url_for('create_store'))
   else:
      flash("Store added!")
      create_store.save
      # return render_template('store.html', name=request.form.get('create_store'))
      return redirect(url_for('create_store'))

@app.route("/warehouse",methods=['GET'])
def warehouse():
   return render_template('warehouse.html')
   locations = Store.select()
   for i in locations:
      print(i)

@app.route("/warehouse",methods=['POST'])
def create_warehouse():
   pass
   
   
if __name__ == '__main__':
   app.run()