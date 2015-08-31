from flask import Flask # Import the Flask class from class library
app = Flask(__name__)  # Creates instant of the class using the name of the running application 

@app.route('/')        # @app decorators are used to enclose a function. Genrally the one following them
@app.route('/hello')   # In this case the HelloWorld
def HelloWorld():
    return "Hello World"
    
if __name__ == '__main__':  # This is used only run the following if its being directly initiated and 
    app.debug = True        # not if the app was imported as a module but the rest of the content can
    app.run(host = '0.0.0.0', port = 5000)  # still be imported
    