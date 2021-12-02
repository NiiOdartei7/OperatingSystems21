from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Mini Project 4: Docker Based Web Application"

@app.route("/permissions", methods = ['GET'] )
def getPermissions():
    permissions_dict = {
        "0": "None",
        "1": "Execute",
        "2": "Write",
        "3": "Execute, Write",
        "4": "Read",
        "5": "Read, Execute",
        "6": "Read, Write",
        "7": "Read, Write, Execute",
    }

    a = request.args['code']
    owner = a[0]
    group = a[1]
    other = a[2]

    return jsonify("Owner: ["+ permissions_dict.get(owner)+"] ", " Group: ["+permissions_dict.get(group)+"] " ," Other: ["+permissions_dict.get(other)+
          "]")

@app.route("/parity", methods = ['GET'])
def parity():
    b1 = request.args["b1"]
    b2 = request.args["b2"]
    b3 = request.args["b3"]
    b4 = request.args["b4"]

    int_a = int(b1) ^ int(b2)
    int_b = int(b3) ^ int(b4)
    ans = int_a ^ int_b

    return jsonify(ans)

if __name__ == "__main__":
    app.run(debug=True)
