from flask import Flask, redirect, url_for, render_template ,request ,jsonify ,make_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/findaddress', methods=['GET','POST'])
def findaddress():
    req = request.get_json()
    print(req)
    #res = make_response(jsonify({"message": "OK"}), 200)
    res = make_response(jsonify(req), 200)
    return res

if __name__ == "__main__":
    app.run(debug=True)
