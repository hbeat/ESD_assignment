import json
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello!"

@app.route("/display_data",methods=['GET'])
def display_data():
    jsonbody = {
        "products" : [],
    }
    with open('data.txt', 'r') as f:
        data = f.read()
        data = data.split('\n')
        for item in data:
            jsonbody["products"].append(item)
        return jsonify(jsonbody)

@app.route("/save_data")
def save_data():
    product = request.args.get("product")
    with open('data.txt', 'a') as f:
        f.write('\n'+product)
        f.close()
    jsonbody = {
        "product" : product,
    }
    return jsonify(jsonbody)

@app.route("/insert_data")
def insert_data():
    product = request.args.get("product")
    quantity = request.args.get("quantity")

    jsonbody = {
        "product" : product,
        "qunatity" : quantity,
    }

    return jsonify(jsonbody)
##http://127.0.0.1:5000/insert_data?product=<product_name>&quantity=<qty>

if __name__ == '__main__':
    app.run(port=5000)
