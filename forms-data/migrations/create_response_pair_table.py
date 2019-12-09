from orator.migrations import Migration

class CreateResponsePairTable(Migration):
  
  def up(self):
    ''' 
    Run the migrations
    '''
    
    with self.schema.create("form_response_pair") as table:
      table.increments("id")
      table.string("text")
      table.foreign('form_response_id').references('id').on('form_response')
      table.foreign('form_question_id').references('id').on('form_question')
      table.foreign('form_choice_id').references('id').on('form_choice')

      
  def down(self):
    '''
    Revert migrations
    '''

    self.schema.drop('form')