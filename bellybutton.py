#import all your dependencies

import os # joins path to the sqlite file 
import pandas as pd # will query the session(s)
import numpy as np 

import sqlalchemy
from sqlalchemy import create_engine # connects sqlite database via remote path of filename
from sqlalchemy.ext.automap import automap_base # generates quick rudimentary object from database
from sqlalchemy.orm import Session # reflects schema, and provides mapping
 
from flask import Flask, render_template # will route pages 

#############################################################

dbfile = os.path.join('db', 'belly_button_biodiversity.sqlite')
engine = create_engine(f"sqlite:///{dbfile}")

Base = automap_base()
Base.prepare(engine, reflect=True)

# Mapped classes are now created by names matching that of the table names
Samples_Metadata = Base.classes.samples_metadata
OTU = Base.classes.otu
Samples = Base.classes.samples

# Create our session (link) from Python to the DB
session = Session(engine)




#set Flask method to a variable
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('Index.html')

@app.route('/names')
def names():
    """Return a list of sample names."""

    stmt = session.query(Samples).statement
    df = pd.read_sql_query(stmt, session.bind)
    df.set_index('otu_id', inplace=True)

    # Return a list of the column names (sample names)
    return (list(df.columns))

#Start server if everything needed is set up
if __name__ == "__main__":
	#debug true will display errors
    #app.run(debug=True)
    #another way if need another port server 
    app.run(debug=True, port=300)
    