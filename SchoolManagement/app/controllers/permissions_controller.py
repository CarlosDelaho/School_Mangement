import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.permissions_model import Permissions
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class PermissionsController:
    def create_permission(self, permission: Permissions):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO permissions (role_id, module_id, can_view, can_edit, can_delete) VALUES (%s, %s, %s, %s, %s)", (permission.role_id, permission.module_id, permission.can_view, permission.can_edit, permission.can_delete))
            conn.commit()
            conn.close()
            return {"resultado": "Permisos asignados correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_permission(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM permissions WHERE id = %s", (id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'role_id':int(result[1]),
                    'module_id':int(result[2]),
                    'can_view':bool(result[3]),
                    'can_edit':bool(result[4]),
                    'can_delete':bool(result[5]),
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Info permission not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_permissions(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM permissions")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'role_id':data[1],
                    'module_id':data[2],
                    'can_view':data[3],
                    'can_edit':data[4],
                    'can_delete':data[5],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Info permissions not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def edit_permission(self, permission: Permissions):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE permissions SET role_id = %s, module_id = %s, can_view = %s, can_edit = %s, can_delete = %s", (permission.role_id, permission.module_id, permission.can_view, permission.can_edit, permission.can_delete))
            conn.commit()
            conn.close()
            return {"resultado": "Permiso editado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_permission(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            deleted_at = datetime.now()
            cursor.execute("UPDATE permissions SET deleted_at = %s WHERE id = %s", (deleted_at, id))
            conn.commit()
            return {"resultado": "Permiso eliminado exitosamente."}
        except mysql.connector.Error as err:
            conn.rollback()
            return {"error": str(err)}
        finally:
            conn.close()
       