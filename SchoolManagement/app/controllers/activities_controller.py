import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.activities_model import Activities
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class ActivitiesController:
        
    def create_activity(self, activity: Activities):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO activities (title, description, start_date, end_date, type_activity_id, school_id, state) VALUES (%s, %s, %s, %s, %s, %s, %s)", (activity.title, activity.description, activity.start_date, activity.end_date, activity.type_activity_id, activity.school_id, activity.state))
            conn.commit()
            conn.close()
            return {"resultado": "Actividad creado exitosamente."}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_activity(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM activities WHERE id = %s", (id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'title':result[1],
                    'description':result[2],
                    'start_date':datetime(result[3]),
                    'end_date':datetime(result[4]),
                    'type_activity_id':result[5],
                    'school_id':result[6],
                    'state':bool(result[7])
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                raise HTTPException(status_code=404, detail="Activities not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

            

    def get_activities(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            SELECT a.id, a.title, a.description, a.start_date, a.end_date, s.name AS school_name, pv.name AS type_activity_name
            FROM activities a
            JOIN parameters_values pv ON a.type_activity_id = pv.id 
            JOIN schools s ON a.school_id = s.id          
            WHERE a.deleted_at IS NULL AND s.deleted_at IS NULL
            """)
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'title': data[1],
                    'description': data[2],
                    'start_date': data[3],
                    'end_date': data[4],
                    'type_activity_id': data[5],
                    'school_id': data[6],
                    'state': data[7],
                }
                payload.append(content)

            json_data = jsonable_encoder(payload)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Activities not found")  
                    
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail="Database error")
        finally:
            conn.close()

    
    def edit_activity(self, activity: Activities):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE activities SET title = %s, description = %s, start_date = %s, end_date = %s, type_activity_id = %s, school_id = %s, state = %s WHERE id =%s", (activity.title, activity.description, activity.start_date, activity.end_date, activity.type_activity_id, activity.school_id, activity.state))
            conn.commit()
            conn.close()
            return {"resultado": "Actividad editada exitosamente."}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_activity(self, id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            deleted_at = datetime.now()
            cursor.execute("UPDATE activities SET deleted_at = %s WHERE id = %s", (deleted_at, id))
            conn.commit()
            return {"resultado": "Actividad eliminada exitosamente."}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_parameter_values(self, parameter_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name FROM parameters_values WHERE parameter_id = %s
            """, (parameter_id,))
            result = cursor.fetchall()
            payload = [{'id': data[0], 'name': data[1]} for data in result]
            json_data = jsonable_encoder(payload)
            return {"resultado": json_data}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
