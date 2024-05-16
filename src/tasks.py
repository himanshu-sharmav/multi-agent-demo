from textwrap import dedent
from crewai import Task

class DemoTasks:
    def booking_task(self, customer_agent, restaurant_agent, task_description):
        return Task(
            description=dedent(f"""\
                The Customer will make a booking request for the following details:
                {task_description}"""),
            expected_output=dedent("""\
                A booking confirmation or rejection based on the restaurant's availability."""),
            agent=customer_agent,
            follow_up_tasks=[self.process_booking_task(restaurant_agent, task_description)]
        )

    def process_booking_task(self, restaurant_agent, task_description):
        return Task(
            description=dedent(f"""\
                The Restaurant will process the booking request and respond with a confirmation or rejection:
                {task_description}"""),
            expected_output=dedent("""\
                A booking confirmation or rejection message."""),
            agent=restaurant_agent
        )
