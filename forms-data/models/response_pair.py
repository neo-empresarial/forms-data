from models import *

from orator.orm import belongs_to

class ResponsePair(Model):
  
  __table__ = "response_pair"
  __fillable__ = ["form_reponse_id", "form_question_id", "form_choice_id", "text"]
  __primary_key__ = "id"
  __incrementing__ = True
  

  @belongs_to("form_response_id", "id")
    def responses(self):
      from models import Response

      return Question

  @belongs_to("form_question_id", "id")
    def questions(self):
      from models import Question

      return Question

  @belongs_to("form_choice_id", "id")
    def choices(self):
      from models import Choice

      return Choice

    
  
  