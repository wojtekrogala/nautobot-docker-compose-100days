from nautobot.apps.jobs import MultiChoiceVar, Job, ObjectVar, register_jobs, TextVar, IntegerVar

name = "Day 6 Variables"

class HelloVariables(Job):

    message = TextVar()
    days = IntegerVar(
        default="10"
    )

    class Meta:

        name = "Hello Variables"
        description = "Jobs Variable Examples"

    def run(self, message, days):
        self.logger.debug(f"Please give the message: {message} in {days} days")

register_jobs(
    HelloVariables,
)