#import all your dependencies
from flask import Flask, render_template

#set Flask method to a variable
app = Flask(__name__)

@app.route("/")
def index():
    return 'ella is home'

#route to render html file
@app.route("/bellybutton")
def bellybutton():
    return render_template('Index.html')


#Start server if everything needed is set up
if __name__ == "__main__":
	#debug true will display errors
    #app.run(debug=True)
    #another way
    app.run(debug=True, port=300)