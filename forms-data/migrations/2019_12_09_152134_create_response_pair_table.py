from orator.migrations import Migration


class CreateResponsePairTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('form_response_pair') as table:
            table.increments('id')
            table.text("text")
            table.integer('form_question_id').unsigned()
            table.foreign('form_question_id').references('id').on('form_question')
            table.integer('form_choice_id').unsigned()
            table.foreign('form_choice_id').references('id').on('form_choice')
            table.integer('form_response_id').unsigned()
            table.foreign('form_response_id').references('id').on('form_response')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('form_response_pair')
