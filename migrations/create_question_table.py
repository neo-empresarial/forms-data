from orator.migrations import Migration

class CreateQuestionTable(Migration):
  
  def up(self):
    ''' 
    Run the migrations
    '''
    
    with self.schema.create("form_question") as table:
      table.increments("id")
      table.string("text")
      table.foreign('form_id').references('id').on('form')

      
  def down(self):
    '''
    Revert migrations
    '''

    self.schema.drop('form')