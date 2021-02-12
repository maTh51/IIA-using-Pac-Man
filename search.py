# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    node =  { 'state': problem.getStartState(), 'cost': 0, 'direction': []}
    if(problem.isGoalState(node['state'])):
        return []

    frontier = util.Stack()
    frontier.push(node)
    explored = []

    while(True):
        if(frontier.isEmpty()):
            raise Exception('DFS failed')
        
        node = frontier.pop()
        
        explored.append(node['state'])

        if(problem.isGoalState(node['state'])):
            return node['direction']

        successors = problem.getSuccessors(node['state'])
        for elem in successors:
            child = { 
                'state': elem[0], 
                'direction': (node['direction']+[elem[1]]), 
                'cost': elem[2],
                }
            if(child['state'] not in explored):
                frontier.push(child)
    
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

def breadthFirstSearch(problem):

    node =  { 'state': problem.getStartState(), 'cost': 0, 'direction': []}
    if(problem.isGoalState(node['state'])):
        return []

    frontier = util.Queue()
    frontier.push(node)
    explored = []

    while(True):
        if(frontier.isEmpty()):
            raise Exception('BFS failed')
        
        node = frontier.pop()
        
        explored.append(node['state'])

        if(problem.isGoalState(node['state'])):
            return node['direction']

        successors = problem.getSuccessors(node['state'])
        for elem in successors:
            child = { 
                'state': elem[0], 
                'direction': (node['direction']+[elem[1]]), 
                'cost': elem[2]
                }
            if(child['state'] not in explored and not(any(aux['state'] == child['state'] for aux in frontier.list))):
                frontier.push(child)


    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    node =  { 'state': problem.getStartState(),'direction': [], 'cost': 0}
    if(problem.isGoalState(node['state'])):
        return []

    frontier = util.PriorityQueue()
    frontier.push(node, node['cost'])
    explored = []

    while(True):
        if(frontier.isEmpty()):
            raise Exception('UCS failed')
        
        node = frontier.pop()

        if(problem.isGoalState(node['state'])):
            return node['direction']

        # tentar mudar isso pra ficar igual o pseudo do livro
        if node['state'] not in explored:
            successors = problem.getSuccessors(node['state'])
            for elem in successors:
                child = { 
                    'state': elem[0], 
                    'direction': (node['direction']+[elem[1]]), 
                    'cost': (elem[2] + node['cost'])
                    }
                
                # frontier.update(child, child['cost'])
                # print(explored)
                # for aux in frontier.heap:
                #     print(aux[2])
                if(child['state'] not in explored and not(any(aux[2]['state'] == child['state'] for aux in frontier.heap))):
                    frontier.push(child, child['cost'])
                elif(any(aux[2]['state'] == child['state'] for aux in frontier.heap)):
                    frontier.update(child, child['cost'])
            
        explored.append(node['state'])

    
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def greedySearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest heuristic first."""
    "*** YOUR CODE HERE ***"
    node =  { 'state': problem.getStartState(),'direction': [], 'cost': heuristic(problem.getStartState(), problem)}
    if(problem.isGoalState(node['state'])):
        return []

    frontier = util.PriorityQueue()
    frontier.push(node, node['cost'])
    explored = []
    old_path = []

    while True:
        if(frontier.isEmpty()):
            print("Solution not found wiht greed search. Last path:")
            return old_path
        
        node = frontier.pop()

        if(problem.isGoalState(node['state'])):
            return node['direction']

        aux = heuristic(node['state'], problem)

        if node['state'] not in explored:
            successors = problem.getSuccessors(node['state'])
            for elem in successors:
                child = { 
                    'state': elem[0], 
                    'direction': (node['direction']+[elem[1]]), 
                    'cost': heuristic(elem[0], problem)
                    }
                    
                if(child['state'] not in explored and not(any(aux[2]['state'] == child['state'] for aux in frontier.heap))):
                    frontier.push(child, child['cost'])
                elif(any(aux[2]['state'] == child['state'] for aux in frontier.heap)):
                    frontier.update(child, child['cost'])

        explored.append(node['state'])
        old_path = node['direction']
    # util.raiseNotDefined()


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    node =  { 
        'state': problem.getStartState(),
        'direction': [], 
        'r_cost': 0,
        'h_cost': heuristic(problem.getStartState(), problem)
        }
    
    if(problem.isGoalState(node['state'])):
        return []

    frontier = util.PriorityQueue()
    frontier.push(node, (node['r_cost']+node['h_cost']))
    explored = []

    while True:
        if(frontier.isEmpty()):
            raise Exception('A* failed')
        
        node = frontier.pop()

        if(problem.isGoalState(node['state'])):
            return node['direction']

        aux = heuristic(node['state'], problem)

        if node['state'] not in explored:
            successors = problem.getSuccessors(node['state'])
            for elem in successors:
                if elem[0] not in explored:
                    child = { 
                        'state': elem[0], 
                        'direction': (node['direction']+[elem[1]]), 
                        'r_cost': (elem[2] + node['r_cost']),
                        'h_cost': heuristic(elem[0], problem)
                        }
                        
                    if(not(any(aux[2]['state'] == child['state'] for aux in frontier.heap))):
                        frontier.push(child, (child['r_cost']+child['h_cost']))
                    elif(any(aux[2]['state'] == child['state'] for aux in frontier.heap)):
                        frontier.update(child, (child['r_cost']+child['h_cost']))

        explored.append(node['state'])    
    
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()


def foodHeuristic(state, problem):
    """
    Your heuristic for the FoodSearchProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come
    up with an admissible heuristic; almost all admissible heuristics will be
    consistent as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the
    other hand, inadmissible or inconsistent heuristics may find optimal
    solutions, so be careful.

    The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a Grid
    (see game.py) of either True or False. You can call foodGrid.asList() to get
    a list of food coordinates instead.

    If you want access to info like walls, capsules, etc., you can query the
    problem.  For example, problem.walls gives you a Grid of where the walls
    are.

    If you want to *store* information to be reused in other calls to the
    heuristic, there is a dictionary called problem.heuristicInfo that you can
    use. For example, if you only want to count the walls once and store that
    value, try: problem.heuristicInfo['wallCount'] = problem.walls.count()
    Subsequent calls to this heuristic can access
    problem.heuristicInfo['wallCount']
    """
    
    # def find_cicle(path, beg, fin):
    #         for item in path:
    #             if item[0] == beg:
    #                 if item[1] == fin:
    #                     return True
    #                 else:
    #                     return find_cicle(path, item[1], fin)
            
    #         return False

    # def biuld_simple_path(path, way, start, ind):
    #     for i in path:
    #         if i[((ind) % 2)] == start:
    #             way.append(start)
    #             biuld_simple_path(path, way, i[((ind+1) % 2)], ind)
            
    #     return way

    position, foodGrid = state

    # if problem.heuristicInfo == {}:
    #     print("Oh shit, here we go again...")

    #     dist_start = []
    #     savings = util.PriorityQueue()
    #     path = []

    #     for food in foodGrid.asList():
    #         dist_start.append((food, util.manhattanDistance(position, food)))

    #     for i in range(0, len(dist_start)):
    #         for j in range((i+1), len(dist_start)):
    #             # print("q poha é essa: {} {}".format(i,j))
    #             sav = dist_start[i][1] + dist_start[j][1] - util.manhattanDistance(dist_start[i][0], dist_start[j][0])
    #             savings.update((dist_start[i][0], dist_start[j][0], sav), -sav)

    #     # print(position)

    #     # print(dist_start)
    #     rec_ar = []
    #     send_ar = []
    #     for k in range(len(savings.heap)):
    #         elem = savings.pop()
    #         # print("-> {} {} {} \n".format(elem[0], elem[1], elem[2]))
    #         if(
    #             (elem[0] in send_ar) == False and 
    #             (elem[1] in rec_ar) == False and
    #             find_cicle(path, elem[1], elem[0]) == False
    #         ):
    #             send_ar.append(elem[0])
    #             rec_ar.append(elem[1])
    #             path.append((elem[0], elem[1]))
                    
    #         elif(
    #             (elem[0] in rec_ar) == False and 
    #             (elem[1] in send_ar) == False and
    #             find_cicle(path, elem[0], elem[1]) == False
    #         ):
    #             send_ar.append((elem[1]))
    #             rec_ar.append(elem[0])
    #             path.append((elem[1], elem[0]))

                
    #         if(len(rec_ar) == (len(dist_start)-1)):
    #             flag = True
    #             break
                
    #     aux = []
    #     for node in dist_start:
    #         if node[0] not in send_ar or node[0] not in rec_ar:
    #             aux.append(node)

    #     # print("la vai o aux:")
    #     # print(aux)
    #     inv = 0
    #     if aux[0][1] < aux[1][1]:
    #         if(aux[0][0] not in send_ar):
    #             path.append((aux[0][0], position))
    #             inv + 1
    #         else:
    #             path.append((position, aux[0][0]))
    #         aux.remove(aux[0])
    #     else:
    #         if(aux[1][0] not in send_ar):
    #             path.append((aux[1][0], position))
    #             inv + 1
    #         else:
    #             path.append((position, aux[1][0]))
    #             aux.remove(aux[1])

    #     # print("o grande e poderoso path:")
    #     # print(path)

    #     way = []
    #     way = biuld_simple_path(path, way, path[-1][((inv + 1) % 2)], inv)

    #     last = aux.pop()
    #     way.append(last[0])

    #     problem.heuristicInfo['way'] = way

    # # print("\nTaraaaaan:")
    # # print(problem.heuristicInfo['way'])            
    # # print(way)

    # if problem.heuristicInfo['way'] != []:
    #     if(position not in problem.heuristicInfo['way']):
            
    #         # print("cabeççç: {}".format(problem.heuristicInfo['way'][0]))
    #         return util.manhattanDistance(position, problem.heuristicInfo['way'][0])

    #     elif position == problem.heuristicInfo['way'][0]:
    #         print(foodGrid.asList())
    #         return util.manhattanDistance(position, problem.heuristicInfo['way'][0])
    #         problem.heuristicInfo['way'].pop(x)
        
    #     else:
    #         for x in range(len(problem.heuristicInfo['way'])):
    #             if position == problem.heuristicInfo['way'][x]:
    #                 print(foodGrid.asList())
    #                 del problem.heuristicInfo['way']
    #                 return 0
                      
    # return 0

    dist_pac_to_food = []
    dist_food_to_food = [0]

    for food in foodGrid.asList():
        dist_pac_to_food.append(util.manhattanDistance(position, food))
    
    for food1 in foodGrid.asList():
        for food2 in foodGrid.asList():
            if food1 != food2:
                dist_food_to_food.append(util.manhattanDistance(food1, food2))

    if len(dist_pac_to_food) > 0:
        return( min(dist_pac_to_food)+max(dist_food_to_food) ) 
    else:
        return( max(dist_food_to_food) )

    
    raise Exception("teste")


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
gs = greedySearch
astar = aStarSearch
