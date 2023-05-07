import sys
sys.path.append('aima-python')
from search import *
import math
import time

class HW2:

    def __init__(self):
        pass

    def example_problem(self):
        #EightPuzzle example with A*
        # Default goal is (1, 2, 3, 4, 5, 6, 7, 8, 0)
        #   which represents:   1 2 3
        #                       4 5 6
        #                       7 8 _
        #

        # In this example, we'll construct a puzzle with initial state
        #               1 2 3
        #               4 5 6
        #               _ 7 8
        #
        init = (1, 2, 3, 4, 5, 6, 0, 7, 8)
        puzzle = EightPuzzle(init)
        print("Is the puzzle solvable from this initial state?")
        print(puzzle.check_solvability(init))
        # Checks whether the initialized configuration is solvable or not
        print("A* with default heuristic")
        return astar_search(puzzle).solution()

    def problem_1a(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem
            as described in the writeup
        2. return the solution from the A* search algorithm
        '''
        init = (1,6, 3, 4, 8, 5, 2, 7, 0)
        puzzle = EightPuzzle(init)
        return astar_search(puzzle).solution()
    
    def problem_1b(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem
            as described in the writeup
        2. return the solution from the A* search algorithm
        '''
        init = (1, 4, 2, 6, 7, 3, 8, 0, 5)
        goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)
        puzzle = EightPuzzle(init, goal)
        return astar_search(puzzle).solution()

    def problem_1c(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem
            as described in the writeup
        2. return the solution from the A* search algorithm
        '''
        init = (6, 0, 2, 1, 5, 3, 4, 8, 7)
        goal = (1, 2, 3, 8, 0, 4, 7, 6, 5) 
        puzzle = EightPuzzle(init, goal)
        return astar_search(puzzle).solution()

    def problem_1d(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem 
        2. write code that will create a different heuristic
        3. return the solution from the A* search algorithm
        '''
        init = (6, 0, 2, 1, 5, 3, 4, 8, 7)
        goal = (1, 2, 3, 8, 0, 4, 7, 6, 5) 
        puzzle = EightPuzzle(init, goal = goal)

        def mhd(node):
            '''Define your manhattan-distance heuristic for the 8-puzzle here
            '''
            dist = 0
            for i in range(len(goal)):
                x1 = i % 3
                y1 = i // 3
                actual_i = node.state.index(goal[i])
                x2 = actual_i % 3
                y2 = actual_i // 3
                dist = abs(x1 - x2) + abs(y1 - y2)
            return dist
        
        return astar_search(puzzle, h = mhd).solution()

    def problem_2(self, init, default):
        '''
        1. find initial states with optimal solutions of lengths 18, 20, 22 and 24
        2. for each of those, for each heuristic, measure the time it takes to find a solution
        Note: It is not required that your code for this be done specifically in this 
        function. It can be elsewhere in the file if you want to structure the code differently
        The autograder will not test this code, but we will look at it by hand, so if it
        is not all in this function, leave a comment letting us know where to look.
        '''
        st = time.time()
        goal = (1, 2, 3, 4, 5, 6, 7, 8, 0) #default goal
        puzzle = EightPuzzle(init)
        #not sure
        def mhd(node):
            '''Define your manhattan-distance heuristic for the 8-puzzle here
            '''
            dist = 0
            for i in range(len(goal)-1):
                x1 = i % 3
                y1 = i // 3
                actual_i = node.state.index(goal[i])
                x2 = actual_i % 3
                y2 = actual_i // 3
                dist += abs(x1 - x2) + abs(y1 - y2)
            return dist
        if default:
            sol = astar_search(puzzle).solution()
        else:
            sol = astar_search(puzzle, h = mhd).solution()
        print(sol)
        print("Length: ", len(sol))
        et = time.time()
        elapsed = et - st
        #I have more code in main
        return elapsed

    def example_problem_3(self):
        '''Use the InstrumentedProblem class to track stats about a breadth-first
        search on the Romania Map problem.
        '''
        g = InstrumentedProblem(GraphProblem('Timisoara', 'Zerind', romania_map))
        result = breadth_first_graph_search(g)
        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")
        print(g)
        return g.goal_tests

    def problem_3a(self):
        '''Use the InstrumentedProblem class to track stats about 
        different searches on the Romania Map problem.
        '''
        g_bf = InstrumentedProblem(GraphProblem('Bucharest', 'Zerind', romania_map))
        g_df = InstrumentedProblem(GraphProblem('Bucharest', 'Zerind', romania_map))
        g_id = InstrumentedProblem(GraphProblem('Bucharest', 'Zerind', romania_map))
        result_bf = breadth_first_graph_search(g_bf)
        result_df = depth_first_graph_search(g_df)
        result_id = iterative_deepening_search(g_id)

        # print("Su: Successor States created")
        # print("Go: Number of Goal State checks")
        # print("St: States created")
        # print("   Su   Go   St")
        # print(g)
        return (g_bf.goal_tests, g_df.goal_tests, g_id.goal_tests)

    def problem_3b(self):
        '''Use the InstrumentedProblem class to track stats about
        different searches on the Romania Map problem.
        '''
        g_bf = InstrumentedProblem(GraphProblem('Hirsova', 'Oradea', romania_map))
        g_df = InstrumentedProblem(GraphProblem('Hirsova', 'Oradea', romania_map))
        g_id = InstrumentedProblem(GraphProblem('Hirsova', 'Oradea', romania_map))
        result_bf = breadth_first_graph_search(g_bf)
        result_df = depth_first_graph_search(g_df)
        result_id = iterative_deepening_search(g_id)
        return (g_bf.goal_tests, g_df.goal_tests, g_id.goal_tests)


def main():
    
    # Create object, hw2, of datatype HW2.
    hw2 = HW2()
 
    #=======================
    # A* with 8-Puzzle 
    # An example for you to follow to get you started on the EightPuzzle
    print('Example Problem result:')
    print('=======================')
    print(hw2.example_problem())
    
    print('Problem 1a result:')
    print('==================')
    print(hw2.problem_1a())

    print('Problem 1b result:')
    print('==================')
    print(hw2.problem_1b())

    print('Problem 1c result:')
    print('==================')
    print(hw2.problem_1c())

    print('Problem 1d result:')
    print('==================')
    print(hw2.problem_1d())
    print("problem 2")
    print("Default:")
    print("Time: ", hw2.problem_2((1, 6, 3, 4, 8, 5, 0, 2, 7), True)) # length 18 using default h
    print("MHD:")
    print("Time: ",hw2.problem_2((1, 6, 3, 4, 8, 5, 0, 2, 7), False)) # length 18 usind mhd
    print("Default:")
    print("Time: ",hw2.problem_2((1, 4, 5, 2, 3, 6, 7, 8, 0), True)) # length 20 using default h
    print("MHD:")
    print("Time: ",hw2.problem_2((1, 4, 5, 2, 3, 6, 7, 8, 0), False)) # length 20 usind mhd
    print("Default:")
    print("Time: ",hw2.problem_2((0, 1, 2, 3, 4, 5, 6, 7, 8), True)) # length 22 using default h
    print("MHD:")
    print("Time: ",hw2.problem_2((0, 1, 2, 3, 4, 5, 6, 7, 8), False)) # length 22 usind mhd
    print("Default:")
    print("Time: ",hw2.problem_2((2, 1, 5, 3, 7, 8, 0, 6, 4), True)) # length 24 using default h
    print("MHD:")
    print("Time: ",hw2.problem_2((2, 1, 5, 3, 7, 8, 0, 6, 4), False)) # length 24 usind mhd

    print(hw2.example_problem_3())

    print('Problem 3a result:')
    print('==================')
    print(hw2.problem_3a())

    print('Problem 3b result:')
    print('==================')
    print(hw2.problem_3b())

    
if __name__ == '__main__':
    main()
