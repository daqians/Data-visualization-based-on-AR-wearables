from flask import Flask, jsonify, request
app = Flask(__name__)
data = {
}
@app.route('/get', methods=['GET'])
def get():
    return jsonify(data)
@app.route('/post', methods=['POST'])
def post():
    result = {}
    json = request.json
    if not json:
        result['isSuccess'] = False
        return jsonify(result)
    data['data'] = json
    result['isSuccess'] = True
    return jsonify(result)
if __name__ == '__main__':
 app.run(host='0.0.0.0',port=80,debug=True)#开放服务器
