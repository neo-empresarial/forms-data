from models import *

from orator.orm import belongs_to

class Choice(Model):
  
  __table__ = "form_choice"
  __fillable__ = ["text", " form_question_id"]
  __primary_key__ = "id"
  __incrementing__ = True
  
  @belongs_to("form_question_id", "id")
  def questions(self):
        from models import Question

        return Question
  