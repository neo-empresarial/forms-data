from models import *

class Choice(Model):
  
  __table__ = "form_choice"
  __fillable__ = ["text", "form_question_id"]
  __primary_key__ = "id"
  __incrementing__ = True
  
    
  
  