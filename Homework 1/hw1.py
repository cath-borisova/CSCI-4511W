'''
Adapted from Professor Watters' code

Complete the homework by changing the code in the HW1 class.

'''

import sys 
sys.path.append('aima-python')
from agents import *

class HW1:

    def problem_a(self):
        '''
        Call the run() method with the reflex agent and the trivial vac environment 
        and return the environment status
        '''
        agent = TraceAgent(ReflexVacuumAgent())
        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15) #steps?
        # environment.status == {(1,0):'Clean' , (0,0) : 'Clean'}
        return environment.status

    def problem_b(self):
        '''
        Call the run() method with the model based agent and the trivial vac environment
        and return the environment status
        '''
        agent = TraceAgent(ModelBasedVacuumAgent())
        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        # environment.status == {(1,0):'Clean' , (0,0) : 'Clean'}
        return environment.status 

    def problem_c(self):
        '''
        Call the run() method with the random agent and the trivial vac environment
        and return the environment status
        '''
        agent = TraceAgent(RandomVacuumAgent())
        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        return environment.status 

    def problem_d(self):
        '''
        Compare the performance of the reflex agent, the model based agent, and random agent in the trivial vac environment.
        You will have to pass the agents and the environment to the comparison function, 
        this will require reviewing the documentation because the process is a little different.
        '''
        environment = TrivialVacuumEnvironment
        agents = [ModelBasedVacuumAgent, ReflexVacuumAgent, RandomVacuumAgent]
        result = compare_agents(environment, agents)
        performance_ModelBasedVacuumAgent = result[0][1]
        performance_ReflexVacuumAgent = result[1][1]
        performance_RandomVacuumAgent = result[2][1]
        print("Model Based Vacuum Agent: " + str(performance_ModelBasedVacuumAgent))
        print("Reflex Vacuum Agent: " + str(performance_ReflexVacuumAgent))
        print("Random Vacuum Agent: " + str(performance_RandomVacuumAgent))
        return result
         


def main():
    hw1 = HW1()
    print("Problem a:", hw1.problem_a())
    print("Problem b:", hw1.problem_b())
    print("Problem c:", hw1.problem_c())
    print("Problem d:", hw1.problem_d())

if __name__ == '__main__':
    main()
