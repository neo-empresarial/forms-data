from orator.migrations import Migration


class CreateChoiceTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('form_choice') as table:
            table.increments('id')
            table.text("text")
            table.integer('form_question_id').unsigned()
            table.foreign('form_question_id').references('id').on('form_question')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('form_choice')
