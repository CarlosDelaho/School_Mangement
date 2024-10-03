import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.roles_model import Roles
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class RolesController:
        
    def create_rol(self, roles: Roles):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO roles (name, state) VALUES (%s, %s)", (roles.name, roles.state))
            conn.commit()
            conn.close()
            return {"resultado": "Rol creado exitosamente."}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_rol(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles WHERE id = %s", (id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'name':result[1],
                    'state':bool(result[2])
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                raise HTTPException(status_code=404, detail="Rol not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_roles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'name':data[1],
                    'state':data[2]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Rol not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_rol(self, id:int, roles: Roles):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE roles SET name = %s, state = %s WHERE id =%s", (roles.name, roles.state, id))
            conn.commit()
            conn.close()
            return {"resultado": "Rol edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_rol(self, id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            deleted_at = datetime.now()
            cursor.execute("UPDATE roles SET deleted_at = %s WHERE id = %s", (deleted_at, id))
            conn.commit()
            return {"resultado": "Rol eliminado exitosamente."}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()