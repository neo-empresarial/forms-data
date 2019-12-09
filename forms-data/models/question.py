from models import *

class Question(Model):
  
  __table__ = "form_question"
  __fillable__ = ["text", "form_id"]
  __primary_key__ = "id"
  __incrementing__ = True