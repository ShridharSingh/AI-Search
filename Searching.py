from Utils import *


class Problem:

    def __init__(self, initial,boolean_set, goal):

        self.boolean_set = boolean_set #possible moves
        self.initial = initial #many initial states
        self.goal = goal #many goal states

        initialState = []

        """Takes initial state in form of matrix to be processed"""

        for i in self.initial:
            rows = i[0]
            cols = i[1]
            maxcols = len(self.boolean_set[0])
            pn = 1 + cols + (rows * maxcols)
            initialState.append(pn)

        self.initial = initialState

        goalState = []

        """Takes goal state in form of matrix to be processed"""

        for g in self.goal:
            rows = g[0]
            cols = g[1]
            maxcols = len(self.boolean_set[0])
            pn = 1 + cols + (rows * maxcols)
            goalState.append(pn)

        self.goal = goalState


    def actions(self, state):


        """Moves are calcualed and presented and apllicable locations are given in
        single row-col matrix form representation"""

        maxcols = len(self.boolean_set[0])
        r = (state-1) // maxcols
        c = (state-1) % maxcols

        action_string = []

        if r == 0:

            """Moves applicable at the top of the maze - first row"""

            '''moves to the right'''

            if self.boolean_set[r][c + 1] == False:
                action_string.append(1)

            '''moves diagonally down to the right'''

            if self.boolean_set[r + 1][c + 1] == False:
                action_string.append(2)
                print(action_string)

            return action_string


        elif r == (len(self.boolean_set) - 1):

            """Moves applicable at the bottom of the maze - last row"""

            '''moves to the right'''

            if self.boolean_set[r - 1][c + 1] == False:
                action_string.append(0)

            '''moves diagonally up to the right'''

            if self.boolean_set[r][c + 1] == False:
                action_string.append(1)

            return action_string


        else:

            """Moves applicable "inside body" of the maze - !fist and !last row"""

            '''moves to the right'''

            if self.boolean_set[r - 1][c + 1] == False:
                action_string.append(0)

            '''moves diagonally up to the right'''

            if self.boolean_set[r][c + 1] == False:
                action_string.append(1)

            '''moves diagonally down to the right'''

            if self.boolean_set[r + 1][c + 1] == False:
                action_string.append(2)

            return action_string


    def result(self, state, action):

        maxcols = len(self.boolean_set[0])
        r = (state - 1) // maxcols
        c = (state - 1) % maxcols
        if action == 0:

            rows = r-1
            cols = c+1
            n = 1 + cols + (rows * maxcols)

            return n

        elif action == 1:

            rows = r
            cols = c + 1
            n = 1 + cols + (rows * maxcols)

            return n

        elif action == 2:

            rows = r + 1
            cols = c + 1
            n = 1 + cols + (rows * maxcols)

            return n



    def goal_test(self, state):

        goalState = False

        for gt in self.goal:
            if state == gt:

                goalState = True

                break
            else:
                continue

        return goalState


    def path_cost(self, c, state1, action, state2):

        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError

#-----------------------------------------------------------------------------------------------------------------------

class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1


    '''Nodes are printed one at a time in the form: '''

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # We want for a queue of nodes in breadth_first_graph_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def Heuritics(self, problem):

        maxCols = len(problem.boolean_set[0])

        row_dx = (self.state-1) // maxCols
        col_dy = (self.state-1) % maxCols

        h = 0

        for x in problem.goal:

            node_dx = (x-1) // maxCols
            node_dy = (x-1) % maxCols

            dx = abs((node_dx - row_dx))
            dy = abs(node_dy - col_dy)

            h_val_cost = dx + dy


            if (h == 0):
                h = h_val_cost
            elif (h < h_val_cost):
                h = h
            elif (h_val_cost<h):
                h = h_val_cost

        return h

#-----------------------------------------------------------------------------------------------------------------------

def breadth_first_graph_search(problem):

    node = []

    for row in problem.initial:
        node.append(Node(row))
    for col in node:
        if problem.goal_test(col.state):
            return col

        frontier = []

        frontier.append(col)

        explored_arr = []
        bfs_arr = []

        while frontier:

            node = frontier.pop(0)
            temp_arr = []

            maxCols = len(problem.boolean_set[0])

            rows = (node.state - 1) // maxCols
            cols = (node.state - 1) % maxCols

            temp_arr.append(rows)
            temp_arr.append(cols)

            bfs_arr.append(temp_arr)
            explored_arr.append(node.state)

            for child in node.expand(problem):
                if child.state not in explored_arr and child not in frontier:
                    if problem.goal_test(child.state):

                        temp_arr = []

                        maxCols = len(problem.boolean_set[0])

                        ch_row = (child.state - 1) // maxCols
                        ch_col = (child.state - 1) % maxCols

                        temp_arr.append(ch_row)
                        temp_arr.append(ch_col)

                        bfs_arr.append(temp_arr)

                        explored_arr.append(child.state)
                        return bfs_arr

                    frontier.append(child)
    return None


def depth_first_graph_search(problem):


    #frontier = [(Node(problem.initial))]  # Stack

    frontier = []
    for row in problem.initial:
        frontier.append(Node(row))

        explored = []
        dfs_arr = []

        while frontier:

            node = frontier.pop()

            if problem.goal_test(node.state):
                explored.append(node.state)

                temp_arr = []

                maxCols = len(problem.boolean_set[0])

                rows = (node.state-1) // maxCols
                cols = (node.state-1) % maxCols

                temp_arr.append(rows)
                temp_arr.append(cols)

                dfs_arr.append(temp_arr)

                return dfs_arr

            temp_arr = []


            maxCols = len(problem.boolean_set[0])

            rows = (node.state - 1) // maxCols
            cols = (node.state - 1) % maxCols


            temp_arr.append(rows)
            temp_arr.append(cols)

            dfs_arr.append(temp_arr)

            explored.append(node.state)
            frontier.extend(child for child in node.expand(problem)

                            if child.state not in explored and child not in frontier)

    return None



def best_first_graph_search(problem, f, display=False):


    if(display=='g'):
        f = memoize(f, problem,'g')
    else:
        f = memoize(f, problem, 'f')

    for row in problem.initial:

        node = Node(row)
        frontier = PriorityQueue('min', f)
        frontier.append(node)

        explored_arr = []
        bstfs_arr = []

        while frontier:
            node = frontier.pop()

            if problem.goal_test(node.state):
                if display:

                    print("paths expanded: ", len(explored_arr), "\n",
                          "paths remaining in frontier :", len(frontier))

                explored_arr.append(node.state)

                for row in explored_arr:
                    temp_arr = []

                    maxCols = len(problem.boolean_set[0])


                    rows = (row - 1) // maxCols
                    cols = (row - 1) % maxCols

                    temp_arr.append(rows)
                    temp_arr.append(cols)

                    bstfs_arr.append(temp_arr)

                return bstfs_arr


            explored_arr.append(node.state)

            for child in node.expand(problem):

                if child.state not in explored_arr and child not in frontier:
                    frontier.append(child)

                elif child in frontier:
                    if f(child) < frontier[child]:

                        del frontier[child]
                        frontier.append(child)
    return None

def astar_search(problem, h=None):

    h = memoize(h or problem.h, 'h')

    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), 'g')

