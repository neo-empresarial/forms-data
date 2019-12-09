from orator.migrations import Migration


class CreateResponseTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('form_response') as table:
            table.increments('id')
            table.integer('form_id').unsigned()
            table.foreign('form_id').references('id').on('form')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('form_response')
