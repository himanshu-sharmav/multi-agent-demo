from dotenv import load_dotenv
from crewai import Crew
from tasks import DemoTasks
from agents import DemoAgents

def main():
    load_dotenv()
    
    print("## Welcome to the Multi-Agent Demo")
    print('-------------------------------')
    task_description = input("Enter the details of the restaurant booking (time and date):\n")

    tasks = DemoTasks()
    agents = DemoAgents()

    # Create agents
    customer_agent = agents.customer_agent()
    restaurant_agent = agents.restaurant_agent()
    notification_agent = agents.notification_agent()

    # Create tasks
    booking_task = tasks.booking_task(customer_agent, restaurant_agent, task_description)

    crew = Crew(
        agents=[
            customer_agent,
            restaurant_agent,
            notification_agent
        ],
        tasks=[
            booking_task
        ]
    )

    result = crew.kickoff()

    print(result)

if __name__ == "__main__":
    main()
