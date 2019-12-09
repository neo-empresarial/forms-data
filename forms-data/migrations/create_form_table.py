from orator.migrations import Migration

class CreateFormTable(Migration):
  
  def up(self):
    ''' 
    Run the migrations
    '''
    
    with self.schema.create("form") as table:
      table.increments("id")
      table.string("name")
      table.string("link")
      
  def down(self):
    '''
    Revert migrations
    '''

    self.schema.drop('form')