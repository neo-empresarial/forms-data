from models import *

class ResponsePair(Model):
  
  __table__ = "response_pair"
  __fillable__ = ["form_reponse_id", "form_question_id", "form_choice_id", "text"]
  __primary_key__ = "id"
  __incrementing__ = True
  
    
  
  