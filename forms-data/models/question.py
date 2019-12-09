from models import *

from orator.orm import belongs_to

class Question(Model):
  
  __table__ = "form_question"
  __fillable__ = ["text", "form_id"]
  __primary_key__ = "id"
  __incrementing__ = True

  @belongs_to("form_question_id", "id")
  def forms(self):
        from models import Form

        return Form