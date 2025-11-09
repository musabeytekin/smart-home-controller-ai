from agents.supervisor.agent import supervisor_agent
from container import container

def test_supervisor_agent():

    while True:

        query = input("\nEnter a command for the supervisor agent (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break



        for step in supervisor_agent.stream(
            {"messages": [{"role": "user", "content": query}]}
        ):
            for update in step.values():
                for message in update.get("messages", []):
                    message.pretty_print()


        print(container.house.get_house_plan())


test_supervisor_agent()