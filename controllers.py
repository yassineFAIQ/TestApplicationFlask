import pandas as pd
from utils.excel import Excel
from models import STUDENT,user_table, ROLE
from configuration import db

class TestApplication():
    @classmethod
    def check_identity(cls, username,password):
        query = user_table.query.filter(user_table.password==password,user_table.email == username).first()
        
        if query:
            if query.password == password:
                return True
            else:
                return False
        else:
            return False
    
    @classmethod
    def get_role(cls, username,password):
        query = ROLE.query.filter(user_table.password==password,user_table.email == username,ROLE.id_user == user_table.ID).first()
        
        if query:
            if query.role == 'user':
                return 'USER'
            else:
                return 'ADMIN'
        

    @classmethod
    def upload_file(cls, file):
        file_name = file.filename.split('.')[0]
        try:
            sheet = Excel.parse_to_pandas(file)
            sheet = sheet[['Name','Age','Level']]
            db.session.query(STUDENT).delete()
            db.session.commit()
            db.session.close_all()
            
            sheet.to_sql(
                'STUDENT',
                db.engine,
                if_exists="append",
                index=False
            )
        except Exception:
            message = 'File is not compatible !!'
            return message
        message = ''
        return message

    

    @classmethod
    def get_students(cls):
        a = STUDENT.query.all()
        liste = []
        for i in a:
            liste.append({'name':i.name,'age':int(i.age),'level':i.level})
        
        return liste