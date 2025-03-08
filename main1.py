from crewai.flow.flow import Flow, start, listen
from project5.crews.crew.dev_crew import DevCrew

class DevFlow(Flow):
    
    @start()
    def run_dev_flow(self):
        output = DevCrew().crew().kickoff(
            inputs={
                "problem": "write a python code to calculate the sum of two numbers"
            }
        )
        return output.raw
    
    
def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result)
    
    



