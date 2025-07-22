import mysql.connector
from werkzeug.security import generate_password_hash

import json
class user_model():

    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="147.93.152.216",user="shinewel_lms_api",database="shinewel_lms_api",password="shinewel_lms_api")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connected Sucessfully..")
        except:
            print("Not connected")
    
    # Inserting the data in db
    def user_addone_model(self,data):
        # Encryption the password
        hashed_password=generate_password_hash(data['password'])
        self.cur.execute(f"""
        INSERT INTO users(name, mobile, email, usertype_id, password, status, created_at) 
        VALUES ('{data['name']}', '{data['mobile']}', '{data['email']}', 
                {data['usertype_id']}, '{hashed_password}', {data['status']}, NOW())""")

        return "insert sucessfully"
    
    #Get the alldata in interface
    def user_getall_model(self):
        self.cur.execute("select u.*,ut.name as 'user_role' from users u JOIN user_type ut ON u.usertype_id = ut.id ")
        result=self.cur.fetchall()
        if len(result)>0:
            return result
        else:
            return{"message":"No data retrieved"}
       
    
    #Get the data through id in interface
    def user_getbyid_model(self,id):
        self.cur.execute("select *from users where id= %s",(id,))
        result=self.cur.fetchone()
        if result:
            return json.dumps(result)
        else:
            return "No data found"
    
    #Update the data 
    def user_updatebyid_model(self,id,data):
        hashed_password=generate_password_hash(data['password'])
        self.cur.execute(f"update users set name='{data['name']}',mobile='{data['mobile']}',email='{data['email']}',usertype_id={data['usertype_id']},password='{hashed_password}',status={data['status']},updated_at=NOW() where id={id}")
        return "Update sucessfully.."
    
    #Delete by ID
    def user_deletebyid_model(self,id):
        self.cur.execute(f"delete from users where id={id}")
        if self.cur.rowcount>0:
            return "User Deleted Sucessfully.."
        else:
            return "User to Delete"


