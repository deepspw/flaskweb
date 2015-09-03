from flask import Flask, render_template, url_for # Import the Flask class from class library
app = Flask(__name__)  # Creates instant of the class using the name of the running application 

from sqlalchemy import create_engine, and_, asc, desc, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')        # @app decorators are used to enclose a function. Genrally the one following them
def homepage():
    return "Homepage"

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

@app.route('/restaurants/<int:restaurant_id>/add/')
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"
    
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"
    
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "Page to delete a menu item. Task 3 complete!"

@app.route('/restaurants/<int:restaurant_id>/add/')
def newRestaurantItem(restaurant_id):
    return "yay"
if __name__ == '__main__':  # This is used only run the following if its being directly initiated and 
    app.debug = True        # not if the app was imported as a module but the rest of the content can
    app.run(host = '0.0.0.0', port = 5000)  # still be imported
    