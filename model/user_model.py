import mysql.connector
from werkzeug.security import generate_password_hash
import json

class user_model:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="147.93.152.216",
                user="shinewel_lms_api",
                password="shinewel_lms_api",
                database="shinewel_lms_api"
            )
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("✅ Connected Successfully")
        except Exception as e:
            print("❌ Connection Failed:", e)

    # Insert user
    def user_addone_model(self, data):
        hashed_password = generate_password_hash(data['password'])
        query = """
            INSERT INTO users (name, mobile, email, usertype_id, password, status, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, NOW())
        """
        values = (
            data['name'],
            data['mobile'],
            data['email'],
            data['usertype_id'],
            hashed_password,
            data['status']
        )
        self.cur.execute(query, values)
        return {"message": "Inserted successfully"}

    # Get all users
    def user_getall_model(self):
        query = """
            SELECT u.*, ut.name AS user_role
            FROM users u
            JOIN user_type ut ON u.usertype_id = ut.id
        """
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result if result else {"message": "No data retrieved"}

    # Get user by ID
    def user_getbyid_model(self, id):
        self.cur.execute("SELECT * FROM users WHERE id = %s", (id,))
        result = self.cur.fetchone()
        return result if result else {"message": "No data found"}

    # Update user by ID
    def user_updatebyid_model(self, id, data):
        hashed_password = generate_password_hash(data['password'])
        query = """
            UPDATE users SET
                name = %s,
                mobile = %s,
                email = %s,
                usertype_id = %s,
                password = %s,
                status = %s,
                updated_at = NOW()
            WHERE id = %s
        """
        values = (
            data['name'],
            data['mobile'],
            data['email'],
            data['usertype_id'],
            hashed_password,
            data['status'],
            id
        )
        self.cur.execute(query, values)
        return {"message": "Updated successfully"}

    # Delete user by ID
    def user_deletebyid_model(self, id):
        self.cur.execute("DELETE FROM users WHERE id = %s", (id,))
        if self.cur.rowcount > 0:
            return {"message": "User deleted successfully"}
        else:
            return {"message": "User not found to delete"}
