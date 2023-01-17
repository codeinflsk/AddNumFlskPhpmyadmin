from flask import Flask, request, jsonify
app = Flask(__name__)
from models.model import *

@app.post('/post_numbers')
def add_num():
    # try:
        data={}
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        # sum = (num1 + num2)
        org = Addition(num1=num1,num2=num2)
        db.session.add(org)
        db.session.commit()
        return jsonify({'result': num1+num2})
    # except:
    #     return jsonify({'result': 0})
    
@app.get('/get_num')
def getNum():
    getNum = Addition.query.all()
    output = []
    for org in getNum:
       num_data = {}
       num_data['num1'] = org.num1
       num_data['num2'] = org.num2
       output.append(num_data)
    return jsonify({'GetNum': output})

@app.delete("/deleteNum/<id>")
def deleteNum(id):
        deleteNum = Addition.query.get(id)
        db.session.delete(deleteNum)
        db.session.commit()
        return jsonify({"message":'The user has been deleted'})

if __name__ == '__main__':
    app.run(debug=True)