from orator.migrations import Migration

class CreateResponsePairTable(Migration):
  
  def up(self):
    ''' 
    Run the migrations
    '''
    
    with self.schema.create("form_response_pair") as table:
      table.increments("id")
      table.dateTime("created_at")
      table.foreign('form_id').references('id').on('form')

      
  def down(self):
    '''
    Revert migrations
    '''

    self.schema.drop('form')