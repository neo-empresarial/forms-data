from orator.migrations import Migration


class CreateQuestionTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('form_question') as table:
            table.increments('id')
            table.text("text")
            table.integer('form_id').unsigned()
            table.foreign('form_id').references('id').on('form')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('form_question')
