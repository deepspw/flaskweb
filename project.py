from flask import Flask, render_template, url_for, redirect, request, flash # Import the Flask class from class library
app = Flask(__name__)  # Creates instant of the class using the name of the running application 

from sqlalchemy import create_engine, and_, asc, desc, func, update
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')        # @app decorators are used to enclose a function. Genrally the one following them
def homepage():
    """Displays homepage"""
    title = "Food'Co"
    subtitle = "temp"
    return render_template('index.html', 
        title=title, subtitle=subtitle)

@app.route('/restaurants/')
def restaurantsList():
    """Displays restaurants in DB"""
    restaurantName = session.query(Restaurant).all()
    restaurantId = session.query(Restaurant).all()
        
    return render_template('restaurants.html', 
        restaurantName=restaurantName, restaurantId=restaurantId)

@app.route('/restaurants/<int:restaurant_id>/')   # In this case the HelloWorld
def restaurantMenu(restaurant_id):
    """Displays a restaurants menu"""
    restaurant = session.query(Restaurant).filter_by(id =
        restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id =
        restaurant_id)
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route('/restaurants/<int:restaurant_id>/add/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST': # if request method was post
        newItem = MenuItem(
            name = request.form['name'],
            description = request.form['description'],
            price = request.form['price'],
            restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("New item created!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET', 'POST'])        
def editMenuItem(restaurant_id, menu_id): # not working yet
    editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        if request.form['name'] or request.form['description'] or request.form['price']:
            editedItem.name = request.form['name']
            editedItem.description = request.form['description']
            editedItem.price = request.form['price']
            editedItem.id = menu_id
            editedItem.restaurant_id = restaurant_id
            session.add(editedItem)
            session.commit()
            flash("Edited item")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, i = editedItem)
    

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        if request.form['delete'] == 'delete':
            session.delete(deleteItem)
            session.commit()
            flash("Item deleted")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, deleteItem = deleteItem)

if __name__ == '__main__':  # This is used only run the following if its being directly initiated and 
    app.secret_key = 'super_secret_key'
    app.debug = True        # not if the app was imported as a module but the rest of the content can
    app.run(host = '0.0.0.0', port = 5000)  # still be imported
    