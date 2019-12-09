from orator.migrations import Migration

class CreateChoiceTable(Migration):
  
  def up(self):
    '''
    Run the migrations
    '''
    
    with self.schema.cretea("form_choice") as table:
      table.increments("id")
      table.string("text")
      table.foreign('form_question_id').references('id').on('form_question')
      
  def down(self):
    '''
    Revert the migrations
    '''
    
    self.schema.drop("form_choice")