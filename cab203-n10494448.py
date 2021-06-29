
# test data Tuple index values: [0] = robot, [1] = part robot attaches, [2] = part/parts attached to, [3] = part/parts blocked by
testData = ({
    ("Johnny-V", "chasis", frozenset({}), frozenset()),
    ("TARS", "gadget", frozenset({"whatsit"}), frozenset({"whatchamacallit"})),
    ("Marvin", "doodad", frozenset({"gadget", "doohickey"}), frozenset()),
    ("Gerty", "whatsit", frozenset({"thingamabob"}), frozenset()),
    ("Ava", "whatchamacallit", frozenset({"doodad", "whatsit"}), frozenset()),
    ("Lore", "doohickey", frozenset({"chasis"}), frozenset({"whatsit"})),
    ("T800", "thingamabob", frozenset({"chasis"}), frozenset({"doohickey", "doodad"}))
})

# Modified from graphys.py obtained from CAB203 Blackboard
# vertices connected by an edge to u (returns list of vertices which points to u)
def N_in(V, E, u):
   return { v for v in V if (v,u) in E }

# checks the length of the set returned by N_in, if the length == 0 there are no vertices going in
def hasInEdge(V, E, v):
    return len(N_in(V, E, v)) != 0

# khan's algorithm
def topOrdering(V, E):
    return topOrderingR(E, set(), V, [])    # G0 = {}, V0 = V

def topOrderingR(E, Q, V, ordering):
    # puts into a set all vertices which have no edges coming into the 
    Qnew = {v for v in V if not hasInEdge(V, E, v)}
    if len(Qnew) == 0: 
        return False # this indicates a directed cycle and not a DAG
    ordering = ordering + [u for u in Qnew] # insert into the order the elements with no edges going in
    Vnew = V - Qnew # update the remaining vertices to be selected
    if len(Vnew) == 0: return ordering # no more vertices - this is the end
    return topOrderingR(E, Qnew, Vnew, ordering) # recurse the function

# return a topological ordering given an instance (testdata)
def solve(instance):
    (P) = instance
    V = {u[0] for u in P}
    # where uj is the robot that must come somewhere before uk in the assembly line
    E = {(uj[0], uk[0]) for uj in P for uk in P if uj[1] in uk[2] or uk[1] in uj[3]}   
    return (topOrdering(V, E)) 

# print the solution in an easy to read format
def printSolution(solution):
    if (solution == False):
        print ("No ordering for the robots could be found")
    else:
        message = "The ordering of robots in the assembly line from first to last is: "
        solutionLength = len(solution)
        for robot in solution:
            solutionLength -= 1
            message += robot
            if (solutionLength != 0):
                message += ", "
        print(message)

printSolution(solve(testData))

    
