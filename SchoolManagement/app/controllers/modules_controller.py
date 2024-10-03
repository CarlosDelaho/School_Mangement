import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.modules_model import Modules
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class ModulesController:
    def create_module(self, module: Modules):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO modules (name, description, state) VALUES (%s, %s, %s)", (module.name, module.description, module.state))
            conn.commit()
            conn.close()
            return {"resultado": "Modulo creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_module(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM modules WHERE id = %s", (id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'name':result[1],
                    'description':result[2],
                    'state':bool(result[3]),
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Info modules not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_modules(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM modules")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'name':data[1],
                    'description':data[2],
                    'state':bool(data[3]),
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Info modules not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def edit_module(self, module:Modules):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE modules SET name = %s, description = %s, state = %s", (module.name, module.description, module.state))
            conn.commit()
            conn.close()
            return {"resultado": "Modulo editado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_module(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            deleted_at = datetime.now()
            cursor.execute("UPDATE modules SET deleted_at = %s WHERE id = %s", (deleted_at, id))
            conn.commit()
            return {"resultado": "Módulo marcado como eliminado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            return {"error": str(err)}
        finally:
            conn.close()
       