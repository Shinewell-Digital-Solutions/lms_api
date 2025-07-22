from app import app
from model.user_model import user_model
from flask import request,jsonify
obj=user_model()

#route for insert
@app.route("/user/insert",methods=['POST'])
def user_addone_controller():
    return obj.user_addone_model(request.form)

#route for get all data
@app.route("/user/list",methods=['GET'])
def user_getall_controller():
    result = obj.user_getall_model()
    return jsonify(result)

#route for get data by id
@app.route("/user/list/<int:id>")
def user_getbyid_controller(id):
    return obj.user_getbyid_model(id)

#route for update through id
@app.route("/user/update/<int:id>",methods=['PUT'])
def user_updatebyid_controller(id):
    return obj.user_updatebyid_model(id,request.form)

@app.route("/user/delete/<int:id>",methods=['DELETE'])
def user_deletebyid_controller(id):
    return obj.user_deletebyid_model(id)



