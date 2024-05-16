from textwrap import dedent
from crewai import Agent

class DemoAgents:
    def customer_agent(self):
        return Agent(
            role="Customer",
            goal='Request a booking at the restaurant',
            backstory=dedent("""\
                As a Customer, your goal is to make a booking request to the restaurant."""),
            verbose=True
        )
      
    def restaurant_agent(self):
        return Agent(
            role='Restaurant',
            goal='Process the booking request and respond',
            backstory=dedent("""\
                As a Restaurant, your goal is to process booking requests from customers and confirm or reject them based on availability."""),
            verbose=True
        )
      
    def notification_agent(self):
        return Agent(
            role='Notification',
            goal='Notify the customer about the booking status',
            backstory=dedent("""\
                As a Notification Agent, your role is to notify the customer about the status of their booking request."""),
            verbose=True
        )
