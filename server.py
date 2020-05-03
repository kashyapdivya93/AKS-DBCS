import flask
import json
from flask import render_template
from connection import res_set, column_keys

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/get_dbdata', methods=['GET'])
def get_dbdata():
    res_array = []
    for i in res_set: 
        temp_dict={} 
        for j,key in zip(i,column_keys): 
            temp_dict[key]=j 
        res_array.append(temp_dict)
    return json.dumps(res_array)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
