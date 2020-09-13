
from flask import Flask, render_template, jsonify, after_this_request
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
import pandas as pd
import sqlalchemy
import sqlite3

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Automation_db.sqlite")
# db reflection 
Base = automap_base()
Base.prepare(engine, reflect = True)

# session from Python to db
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def api_call():

    return render_template('index.html')

################################################## 
#  tablename1 data
##################################################
# results of an inner merge of data on occupation code column

# Index(['Unnamed: 0', 'Occupation_Code', 'Occupation_Title', 'Total_Employees',
#        'Mean_Annual_Wage', 'Annual_10th_Percentile_Wage',
#        'Annual_25th_Percentile_Wage', 'Annual_Median_Wage',
#        'Annual_75th_Percentile_Wage', 'Annual_90th_Percentile_Wage',
#        'Probability of Automation', 'Alabama', 'Alaska', 'Arizona', 'Arkansas',
#        'California', 'Colorado', 'Connecticut', 'Delaware',
#        'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
#        'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
#        'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
#        'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
#        'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
#        'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
#        'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
#        'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
#        'West Virginia', 'Wisconsin', 'Wyoming'],
#       dtype='object')

@app.route ("/getData_tablename1")
def passer_endpoint():

    conn = sqlite3.connect('Automation_db.sqlite')
    c = conn.cursor()
    results = c.execute("SELECT * FROM tablename1")

    tablename1_data = []
    for r in results:
        tablename1_dict = {}

        tablename1_dict["Occupation_Code"] = r[1]
        tablename1_dict["Occupation_Title"] = r[2]
        tablename1_dict["Total_Employees"] = r[3]
        tablename1_dict["Mean_Annual_Wage"] = r[4]
        tablename1_dict["Annual_10th_Percentile_Wage"] = r[5]
        tablename1_dict["Annual_25th_Percentile_Wage"] = r[6]
        tablename1_dict["Annual_Median_Wage"] = r[7]
        tablename1_dict["Annual_75th_Percentile_Wage"] = r[8]
        tablename1_dict["Annual_90th_Percentile_Wage"] = r[9]
        tablename1_dict["Probability of Automation"] = r[10]
        tablename1_dict["Alabama"] = r[11]
        tablename1_dict["Alaska"] = r[12]
        tablename1_dict["Arizona"] = r[13]
        tablename1_dict["Arkansas"] = r[14]
        tablename1_dict["California"] = r[15]
        tablename1_dict["Colorado"] = r[16]
        tablename1_dict["Connecticut"] = r[17]
        tablename1_dict["Delaware"] = r[18]
        tablename1_dict["District of Columbia"] = r[19]
        tablename1_dict["Florida"] = r[20]
        tablename1_dict["Georgia"] = r[21]
        tablename1_dict["Hawaii"] = r[22]
        tablename1_dict["Idaho"] = r[23]
        tablename1_dict["Illinois"] = r[24]
        tablename1_dict["Indiana"] = r[25]
        tablename1_dict["Iowa"] = r[26]
        tablename1_dict["Kansas"] = r[27]
        tablename1_dict["Kentucky"] = r[28]
        tablename1_dict["Louisiana"] = r[29]
        tablename1_dict["Maine"] = r[30]
        tablename1_dict["Maryland"] = r[31]
        tablename1_dict["Massachusetts"] = r[32]
        tablename1_dict["Michigan"] = r[33]
        tablename1_dict["Minnesota"] = r[34]
        tablename1_dict["Mississippi"] = r[35]
        tablename1_dict["Missouri"] = r[36]
        tablename1_dict["Montana"] = r[37]
        tablename1_dict["Nebraska"] = r[38]
        tablename1_dict["Nevada"] = r[39]
        tablename1_dict["New Hampshire"] = r[40]
        tablename1_dict["New Jersey"] = r[41]
        tablename1_dict["New Mexico"] = r[42]
        tablename1_dict["New York"] = r[43]
        tablename1_dict["North Carolina"] = r[44]
        tablename1_dict["North Dakota"] = r[45]
        tablename1_dict["Ohio"] = r[46]
        tablename1_dict["Oklahoma"] = r[47]
        tablename1_dict["Oregon"] = r[48]
        tablename1_dict["Pennsylvania"] = r[49]
        tablename1_dict["Rhode Island"] = r[50]
        tablename1_dict["South Carolina"] = r[51]
        tablename1_dict["South Dakota"] = r[52]
        tablename1_dict["Tennessee"] = r[53]
        tablename1_dict["Texas"] = r[54]
        tablename1_dict["Utah"] = r[55]
        tablename1_dict["Vermont"] = r[56]
        tablename1_dict["Virginia"] = r[57]
        tablename1_dict["Washington"] = r[58]
        tablename1_dict["West Virginia"] = r[59]
        tablename1_dict["Wisconsin"] = r[60]
        tablename1_dict["Wyoming"] = r[61]
    

        tablename1_data.append(tablename1_dict)

    return jsonify(tablename1_data)


################################################# 
# tablename2 data
#################################################
# results of an outer merge of data (62col) on occupation code column

# Index(['Unnamed: 0', 'Occupation_Code', 'Occupation_Title', 'Total_Employees',
#        'Mean_Annual_Wage', 'Annual_10th_Percentile_Wage',
#        'Annual_25th_Percentile_Wage', 'Annual_Median_Wage',
#        'Annual_75th_Percentile_Wage', 'Annual_90th_Percentile_Wage',
#        'Probability of Automation', 'Alabama', 'Alaska', 'Arizona', 'Arkansas',
#        'California', 'Colorado', 'Connecticut', 'Delaware',
#        'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
#        'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
#        'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
#        'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
#        'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
#        'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
#        'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
#        'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
#        'West Virginia', 'Wisconsin', 'Wyoming'],
#       dtype='object')



@app.route ("/getData_tablename2")
def draft_endpoint():

    conn = sqlite3.connect('Automation_db.sqlite')
    c = conn.cursor()
    results = c.execute("SELECT * FROM tablename2")

    tablename2_data = []
    for r in results:
        tablename2_dict = {}
      
        tablename2_dict["Occupation_Code"] = r[1]
        tablename2_dict["Occupation_Title"] = r[2]
        tablename2_dict["Total_Employees"] = r[3]
        tablename2_dict["Mean_Annual_Wage"] = r[4]
        tablename2_dict["Annual_10th_Percentile_Wage"] = r[5]
        tablename2_dict["Annual_25th_Percentile_Wage"] = r[6]
        tablename2_dict["Annual_Median_Wage"] = r[7]
        tablename2_dict["Annual_75th_Percentile_Wage"] = r[8]
        tablename2_dict["Annual_90th_Percentile_Wage"] = r[9]
        tablename2_dict["Probability of Automation"] = r[10]
        tablename2_dict["Alabama"] = r[11]
        tablename2_dict["Alaska"] = r[12]
        tablename2_dict["Arizona"] = r[13]
        tablename2_dict["Arkansas"] = r[14]
        tablename2_dict["California"] = r[15]
        tablename2_dict["Colorado"] = r[16]
        tablename2_dict["Connecticut"] = r[17]
        tablename2_dict["Delaware"] = r[18]
        tablename2_dict["District of Columbia"] = r[19]
        tablename2_dict["Florida"] = r[20]
        tablename2_dict["Georgia"] = r[21]
        tablename2_dict["Hawaii"] = r[22]
        tablename2_dict["Idaho"] = r[23]
        tablename2_dict["Illinois"] = r[24]
        tablename2_dict["Indiana"] = r[25]
        tablename2_dict["Iowa"] = r[26]
        tablename2_dict["Kansas"] = r[27]
        tablename2_dict["Kentucky"] = r[28]
        tablename2_dict["Louisiana"] = r[29]
        tablename2_dict["Maine"] = r[30]
        tablename2_dict["Maryland"] = r[31]
        tablename2_dict["Massachusetts"] = r[32]
        tablename2_dict["Michigan"] = r[33]
        tablename2_dict["Minnesota"] = r[34]
        tablename2_dict["Mississippi"] = r[35]
        tablename2_dict["Missouri"] = r[36]
        tablename2_dict["Montana"] = r[37]
        tablename2_dict["Nebraska"] = r[38]
        tablename2_dict["Nevada"] = r[39]
        tablename2_dict["New Hampshire"] = r[40]
        tablename2_dict["New Jersey"] = r[41]
        tablename2_dict["New Mexico"] = r[42]
        tablename2_dict["New York"] = r[43]
        tablename2_dict["North Carolina"] = r[44]
        tablename2_dict["North Dakota"] = r[45]
        tablename2_dict["Ohio"] = r[46]
        tablename2_dict["Oklahoma"] = r[47]
        tablename2_dict["Oregon"] = r[48]
        tablename2_dict["Pennsylvania"] = r[49]
        tablename2_dict["Rhode Island"] = r[50]
        tablename2_dict["South Carolina"] = r[51]
        tablename2_dict["South Dakota"] = r[52]
        tablename2_dict["Tennessee"] = r[53]
        tablename2_dict["Texas"] = r[54]
        tablename2_dict["Utah"] = r[55]
        tablename2_dict["Vermont"] = r[56]
        tablename2_dict["Virginia"] = r[57]
        tablename2_dict["Washington"] = r[58]
        tablename2_dict["West Virginia"] = r[59]
        tablename2_dict["Wisconsin"] = r[60]
        tablename2_dict["Wyoming"] = r[61]
    

        tablename2_data.append(tablename2_dict)

    return jsonify(tablename2_data)


#######################################################
# tablename3 data
#######################################################
# an extra route if needed

# @app.route("/getData_salary_2019")
# def salary_endpoint():

#     conn = sqlite3.connect('Automation_db.sqlite')
#     c = conn.cursor()
#     results = c.execute("SELECT * FROM tablename3")

#     tablename3_data = []
#     for r in results:
#         tablename3_dict = {}

#         tablename3_dict["column name here"] = r[]
       


#         salary_data.append(tablename3_dict)
#     return jsonify(tablename3_data)


###########################################################
# visualizations
###########################################################
# 

@app.route("/visualization1")
def visualization1():

    return render_template('visualization1.html')
    
#  
@app.route("/visualization2")
def visualization2():

    return render_template('visualization2.html')

# 
@app.route("/visualization3")
def visualization3():

    return render_template('visualization3.html')
# 
@app.route("/visualization4")
def visualization4():

    return render_template('visualization4.html')

@app.route("/test")    
def test():

    return render_template('test.html')


if __name__ == "__main__":
    app.run(debug=True)
