from collections import deque
from queue import PriorityQueue

#answer list
answer = []
# Print the path in BFS,UCS 
def printPath(parent,goal):
    answerList = []
    key = goal
    while parent[key] != None:
        answerList.append((key[1],key[0]))
        key = parent[key]
    answerList.append((key[1],key[0]))
    answerList = answerList[::-1]
    #addition
    answer.append(answerList)
    #addition done
    # with open('output.txt', 'a') as file:
    #     file.write(' '.join(str(x) + ',' + str(y) for x, y in answerList))
    #     file.write('\n')

# Check point if the cell is reachable for BFS ans UCS
def isReachable(ski_map,stamina,current,to):
    #value of current cell
    currentE = abs(ski_map[current[0]][current[1]])
    #value of next cell
    nextE = ski_map[to[0]][to[1]]
    if (nextE < 0 and abs(nextE) > currentE):
        return False
    nextE = abs(nextE)

    if(currentE >= nextE):
        return True
    elif(stamina >= nextE-currentE):
        return True
    else:
        return False

############################################ BFS ###################################################

# Expansion of children nodes in BFS algorithm
def ExpandBFS(current,ski_map):
    childrenList = []
    x = current[0]
    y = current[1]
    #North
    if(x-1 >= 0):
        childrenList.append((x-1,y))
    #NorthEast
    if(x-1 >=0 and y+1 <len(ski_map[0])):
        childrenList.append((x-1,y+1))
    #East
    if(y+1 < len(ski_map[0])):
        childrenList.append((x,y+1))
    #SouthEast    
    if(x+1 < len(ski_map) and y+1 < len(ski_map[0])):
        childrenList.append((x+1,y+1))
    #South    
    if(x+1 < len(ski_map)):
        childrenList.append((x+1,y))
    #SouthWest    
    if(x+1 < len(ski_map) and y-1 >=0):
        childrenList.append((x+1,y-1))
    #West
    if(y-1 >= 0):
        childrenList.append((x,y-1))
    #NorthWest
    if(x-1 >=0 and y-1 >=0):
        childrenList.append((x-1,y-1))
    return childrenList

# BFS algorithm
def BFS(ski_map,stamina,start_cordinate,goal_point):
    #Queue
    q = deque()
    #Parent Dictionary
    parent = {}
    #visited list
    visited = []
    #Start coordinate has no parents
    parent[start_cordinate] = None
    #marked the start coordinate as visited
    visited.append(start_cordinate)
    #append the start coordinate to the queue
    q.append(start_cordinate)

    #while queue is not empty
    while q:
        #pop the front of the queue
        current = q.popleft()
        if(current == goal_point):
            printPath(parent,goal_point)
            return
        #make a list of its neighbours and iterate on each coordinate
        children = ExpandBFS(current,ski_map)
        for child in children:
            #check if the coordinate is reachable
            if(isReachable(ski_map,stamina,current,child)):
                #if reachable then check if that coordinate is a goal if yes then print the path
                if child == goal_point:
                    parent[child] = current
                    printPath(parent,goal_point)
                    return
                #if not goal and the child is not visited. Add it to visited and set its parent and add that child to queue
                if child not in visited:
                    visited.append(child)
                    parent[child] = current
                    q.append(child)
    #if whole map is exhausted then print fail
    #addition
    answer.append("FAIL")
    #addition done
    # with open('output.txt', 'a') as file:
    #     file.write("FAIL")
    #     file.write('\n')
    return

############################################ UCS ###################################################

# Expansion of children nodes in UCS algorithm
def ExpandUCS(current,ski_map):
    childrenList = []
    x = current[1][0]
    y = current[1][1]
    current_cost = current[0]
    #North
    if(x-1 >= 0):
        childrenList.append((current_cost+10,(x-1,y)))
    #NorthEast
    if(x-1 >=0 and y+1 <len(ski_map[0])):
        childrenList.append((current_cost+14,(x-1,y+1)))
    #East
    if(y+1 < len(ski_map[0])):
        childrenList.append((current_cost+10,(x,y+1)))
    #SouthEast    
    if(x+1 < len(ski_map) and y+1 < len(ski_map[0])):
        childrenList.append((current_cost+14,(x+1,y+1)))
    #South    
    if(x+1 < len(ski_map)):
        childrenList.append((current_cost+10,(x+1,y)))
    #SouthWest    
    if(x+1 < len(ski_map) and y-1 >=0):
        childrenList.append((current_cost+14,(x+1,y-1)))
    #West
    if(y-1 >= 0):
        childrenList.append((current_cost+10,(x,y-1)))
    #NorthWest
    if(x-1 >=0 and y-1 >=0):
        childrenList.append((current_cost+14,(x-1,y-1)))
    return childrenList

# UCS algorithm
def UCS(ski_map,stamina,start_cordinate,goal_point):
    #Queue
    pq = PriorityQueue()
    #Parent Dictionary
    parent = {}
    #visited list
    visited = {}
    #Start coordinate has no parents
    parent[start_cordinate] = None
    #marked the start coordinate as visited and cost of it is 0
    visited[start_cordinate] = 0
    #append the start coordinate to the queue
    pq.put((0,(start_cordinate)))

    #while queue is not empty
    while not pq.empty():
        #pop the front of the queue
        current = pq.get()
        if(current[1] == goal_point):
            printPath(parent,goal_point)
            return
        #make a list of its neighbours and iterate on each coordinate
        children = ExpandUCS(current,ski_map)
        for child in children:
            #check if the coordinate is reachable
            if(isReachable(ski_map,stamina,current[1],child[1])):
                if child[1] not in visited:
                    visited[child[1]] = child[0]
                    parent[child[1]] = current[1]
                    pq.put(child)
                elif child[1] in visited:
                    if(visited[child[1]] > child[0]):
                        visited[child[1]] = child[0]
                        parent[child[1]] = current[1]
                        pq.put(child)
    #if whole map is exhausted then print fail
    #addition
    answer.append("FAIL")
    #addition done
    # with open('output.txt', 'a') as file:
    #     file.write("FAIL")
    #     file.write('\n')
    return

############################################ A Star ###################################################

#Elevation change cost
def Elevation_Change_Cost(ski_map,to,current):
    return max(0,abs(ski_map[to[0]][to[1]]) - abs(ski_map[current[1][0]][current[1][1]])-current[2])

# Heuristic path cost
def Heuristic_cost(current, goal):
    # Using Manhattan Distance we will calculate the number of diagonal movements and number of adjacent movements
    diagonal_movement = min(abs(goal[0]-current[0]),abs(goal[1]-current[1]))
    # adjacent_movement = abs(goal[0]-current[0])+abs(goal[1]-current[1]) - 2*diagonal_movement
    return 10*diagonal_movement #+14*diagonal_movement

# Momentum   
def Momentum_Required(ski_map,previous,current,to):
    if previous[0] == None:
        return 0
    elif (abs(ski_map[to[1][0]][to[1][1]]) - abs(ski_map[current[1][0]][current[1][1]]))>0:
        return max(0,abs(ski_map[previous[0][0]][previous[0][1]]) - abs(ski_map[current[1][0]][current[1][1]]))
    else:
        return 0

# Expansion of children nodes in A*
def ExpandA_star(ski_map,current,goal):
    childrenList = []
    x = current[1][0]
    y = current[1][1]
    # h = Heuristic_cost(current[1],goal)
    #North
    if(x-1 >= 0):
        ECC =  Elevation_Change_Cost(ski_map,(x-1,y),current)
        h = Heuristic_cost((x-1,y),goal)
        cost = h + ECC + 10 + current[0]
        childrenList.append([cost,(x-1,y),-1])  
    #NorthEast
    if(x-1 >=0 and y+1 <len(ski_map[0])):
        ECC =  Elevation_Change_Cost(ski_map,(x-1,y+1),current)
        h = Heuristic_cost((x-1,y+1),goal)
        cost = h + ECC+ 14 + current[0]
        childrenList.append([cost,(x-1,y+1),-1])
    #East
    if(y+1 < len(ski_map[0])):
        ECC =  Elevation_Change_Cost(ski_map,(x,y+1),current)
        h = Heuristic_cost((x,y+1),goal)
        cost = h + ECC + 10 + current[0]
        childrenList.append([cost,(x,y+1),-1])
    #SouthEast    
    if(x+1 < len(ski_map) and y+1 < len(ski_map[0])):
        ECC =  Elevation_Change_Cost(ski_map,(x+1,y+1),current)
        h = Heuristic_cost((x+1,y+1),goal)
        cost = h + ECC +14 + current[0]
        childrenList.append([cost,(x+1,y+1),-1])
    #South    
    if(x+1 < len(ski_map)):
        ECC =  Elevation_Change_Cost(ski_map,(x+1,y),current)
        h = Heuristic_cost((x+1,y),goal)
        cost = h + ECC +10 + current[0]
        childrenList.append([cost,(x+1,y),-1])
    #SouthWest    
    if(x+1 < len(ski_map) and y-1 >=0):
        ECC =  Elevation_Change_Cost(ski_map,(x+1,y-1),current)
        h = Heuristic_cost((x+1,y-1),goal)
        cost = h + ECC +14 + current[0]
        childrenList.append([cost,(x+1,y-1),-1])
    #West
    if(y-1 >= 0):
        ECC =  Elevation_Change_Cost(ski_map,(x,y-1),current)
        h = Heuristic_cost((x,y-1),goal)
        cost = h + ECC +10 + current[0]
        childrenList.append([cost,(x,y-1),-1])
    #NorthWest
    if(x-1 >=0 and y-1 >=0):
        ECC =  Elevation_Change_Cost(ski_map,(x-1,y-1),current)
        h = Heuristic_cost((x-1,y-1),goal)
        cost = h + ECC +14 + current[0]
        childrenList.append([cost,(x-1,y-1),-1])
    return childrenList

# Check if the child is reachable or not
def isReachable_Astar(ski_map,stamina,previous,current,to):
    #value of next cell
    nextE = ski_map[to[1][0]][to[1][1]]

    #value of current cell
    currentE = abs(ski_map[current[1][0]][current[1][1]])

    # if the next cell is a tree and it is a higher elevation then its false
    if (nextE < 0 and abs(nextE) > currentE):
        return False

    nextE = abs(nextE)

    # if the current elevation is more than next elevation then its true
    if(currentE >= nextE):
        return True
    # else if next elevation 
    elif(stamina+ Momentum_Required(ski_map,previous,current,to) >= nextE-currentE):
        return True
    else:
        return False

# Print Path in A*
def printPath_Astar(parent,goal):
    answerList = []
    key = goal
    answerList.append((key[0][1],key[0][0]))
    while key in parent and parent[key] != (None, 0):
        key = parent[key]
        answerList.append((key[0][1],key[0][0]))
    answerList = answerList[::-1]

    #addition
    answer.append(answerList)
    #addition done

    # with open('output.txt', 'a') as file:
    #     file.write(' '.join(str(x) + ',' + str(y) for x, y in answerList))
    #     file.write('\n')

# A* algorithm
def A_star(ski_map,stamina,start_cordinate,goal_point):
    #Queue
    pq = PriorityQueue()
    #Parent Dictionary
    parent = {}
    #visited list
    visited = {}
    #Start coordinate has no parents
    parent[(start_cordinate,0)] = (None,0) # (coord,momentum) 
    #marked the start coordinate as visited and cost of it is 0
    visited[(start_cordinate,0)] = Heuristic_cost(start_cordinate,goal_point)
    #append the start coordinate to the queue
    pq.put([Heuristic_cost(start_cordinate,goal_point),(start_cordinate),0])

    #while queue is not empty
    while not pq.empty():
        #pop the front of the queue
        current = pq.get()
        if(current[1] == goal_point):
            printPath_Astar(parent,(goal_point,current[2]))
            return
        #make a list of its neighbours and iterate on each coordinate
        children = ExpandA_star(ski_map,current,goal_point)
        for child in children:
            #check if the coordinate is reachable
            if(isReachable_Astar(ski_map,stamina,parent[(current[1],current[2])],current,child)):
                child[2] = max(0,abs(ski_map[current[1][0]][current[1][1]])-abs(ski_map[child[1][0]][child[1][1]]))
                key = (child[1],child[2]) # (coord, mom)
                if key not in visited:
                    parent[key] = (current[1],current[2])
                    visited[key] = child[0]
                    pq.put(child)
                elif key in visited:
                    if(visited[key] > child[0]):
                        parent[key] = (current[1],current[2])
                        visited[key] = child[0]
                        pq.put(child)
    #if whole map is exhausted then print fail
    #addition
    answer.append("FAIL")
    #addition done
    # with open('output.txt', 'a') as file:
    #     file.write("FAIL")
    #     file.write('\n')
    return

############################################ Main ###################################################
def main():
    # Making a list for first 5 lines
    l=[]

    # List of lodge points
    goal_points = []

    # Map of the ski
    ski_map = []

    # Accessing the file pointer
    fp = open("input.txt",'r')
    # Appending the first 5 lines to the list
    for i in range(5):
        l.append(fp.readline())
    
    # Name of the algorithm
    name = l[0].strip()

    # Width and Height of the map
    w_h = l[1].strip().split()
    width,height = int(w_h[0]),int(w_h[1])

    # Axis of the starting point
    x_y = l[2].strip().split()
    start_y,start_x = int(x_y[0]),int(x_y[1])
    # Stamina of the skier
    stamina = int(l[3].strip())

    # Number of lodges
    num_of_lodges = int(l[4].strip())

    # Appending the lodge points to the list
    for i in range(num_of_lodges):
        goal_points.append(list(map(lambda x : int(x),(fp.readline().strip().split()))))

    # Making the ski-map
    for i in range (height):
        ski_map.append(list(map(lambda x: int(x),(fp.readline()).strip().split())))
    
    fp.close()

    if(name == "BFS"):
        for i in goal_points:
            BFS(ski_map,stamina,(start_x,start_y),(i[1],i[0]))
    elif(name == "UCS"):
        for i in goal_points:
            UCS(ski_map,stamina,(start_x,start_y),(i[1],i[0]))
    elif(name == "A*"):
        for i in goal_points:
            A_star(ski_map,stamina,(start_x,start_y),(i[1],i[0]))
    
    with open('output.txt', 'w') as file:
        for ans in answer:
            if(ans == "FAIL"):
                file.write("FAIL")
                file.write('\n')
            else:
                file.write(' '.join(str(x) + ',' + str(y) for x, y in ans))
                file.write('\n')

if __name__ == '__main__':
  main()