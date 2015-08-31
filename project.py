from flask import Flask # Import the Flask class from class library
app = Flask(__name__)  # Creates instant of the class using the name of the running application 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')        # @app decorators are used to enclose a function. Genrally the one following them
@app.route('/hello')   # In this case the HelloWorld
def HelloWorld():
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem)
    output = ''
    for i in items:
        output += '<h3>'
        output += i.name
        output += '</h3>'
        output += i.description
        output += '</br>'
        output += i.price
        output += '</br>'
    return output

if __name__ == '__main__':  # This is used only run the following if its being directly initiated and 
    app.debug = True        # not if the app was imported as a module but the rest of the content can
    app.run(host = '0.0.0.0', port = 5000)  # still be imported
    