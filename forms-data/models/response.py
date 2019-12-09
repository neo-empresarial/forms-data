from models import *

class Response(Model):
  
  __table__ = "form_response"
  __fillable__ = ["created_at", "form_question_id"]
  __primary_key__ = "id"
  __incrementing__ = True
  
