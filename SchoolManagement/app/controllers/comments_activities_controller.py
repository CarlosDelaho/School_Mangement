import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.comments_activities_model import CommentsActivities
from fastapi.encoders import jsonable_encoder

class CommentsActivitiesController:
        
    def create_comment_activity(self, comment_activity: CommentsActivities):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO comments_activities (activity_id, user_id, comment) VALUES (%s, %s, %s)", (comment_activity.activity_id, comment_activity.user_id, comment_activity.comment))
            conn.commit()
            conn.close()
            return {"resultado": "comments created"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_comment_activity(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comments_activities WHERE id = %s", (id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'activity_id':result[1],
                    'user_id':result[2],
                    'comment':result[3]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
                return  json_data
            else:
                raise HTTPException(status_code=404, detail="Comments not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_comments_activities(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comments_activities")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'activity_id':data[1],
                    'user_id':data[2],
                    'comment':data[3],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Comments not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def edit_comment_activity(self, comment_activity: CommentsActivities):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE comments_activities SET activity_id = %s, user_id = %s, comment = %s WHERE id =%s", (comment_activity.activity_id, comment_activity.user_id, comment_activity.comment))
            conn.commit()
            conn.close()
            return {"resultado": "Comments edited"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def delete_comment_activity(self, id: int):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM comments_activities WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Comment eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()