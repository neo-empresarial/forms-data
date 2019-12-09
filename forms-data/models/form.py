from models import *

class Form(Model):
  
  __table__ = "form"
  __fillable__ = ["name", "link"]
  __primary_key__ = "id"
  __incrementing__ = True

  
  
  
  
  
  