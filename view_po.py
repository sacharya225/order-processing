import flask  
from flask import request, jsonify
import MySQLdb

app = flask.Flask(__name__)  ##Create a flask application object
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return "<h1>Home Page for PO Creation</h1>"

	
@app.route('/api/v1/users/all', methods=['GET'])
def api_getalluser():       
    db = MySQLdb.connect(host="172.30.42.188", user="root", passwd="root123", db="sfgdev")
    cursor = db.cursor()
    cursor.execute("select * from PURCHASE_ORDER")
    records=cursor.fetchall()
    return jsonify(records) 

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>resource could not be found.</p>", 404


if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True) 





