import matplotlib.pyplot as cross
import math


class Vertex:
    def __init__(self, x_pos, y_pos, cost, found):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.cost = cost
        self.found = found

    def __str__(self):
        return str(self.x_pos) + "," + str(self.y_pos) + "," + str(self.cost) + "," + str(self.found)

def motion_mode():
    move_cost = [[1, 0, 1], #d(x), d(y), cost
            [0, 1, 1],
            [-1, 0, 1],
            [0, -1, 1],
            [-1, -1, math.sqrt(2)],
            [-1, 1, math.sqrt(2)],
            [1, -1, math.sqrt(2)],
            [1, 1, math.sqrt(2)]]
    return move_cost

def get_map_obs(obs_xpos, obs_ypos, resol, ver):
    x_min = round(min(obs_xpos))
    y_min = round(min(obs_ypos))
    x_max = round(max(obs_xpos))
    y_max = round(max(obs_ypos))
    width_x = round(x_max - x_min)
    width_y = round(y_max - y_min)
    # obstacles on the map
    obs_map = [[False for i in range(width_y)] for i in range(width_x)]
    for i_x in range(width_x):
        x_pos = i_x + x_min
        for iy in range(width_y):
            y_pos = iy + y_min
            #  print(x_pos, y_pos)
            for iox, ioy in zip(obs_xpos, obs_ypos):
                dis = math.sqrt((iox - x_pos)**2 + (ioy - y_pos)**2)
                if dis <= ver / resol:
                    obs_map[i_x][iy] = True
                    break
    return obs_map, x_min, y_min, x_max, y_max, width_x, width_y

def vert_valid(vertex, obs_map, x_min, y_min, x_max, y_max):
    if vertex.x_pos < x_min:
        return False
    elif vertex.y_pos < y_min:
        return False
    elif vertex.x_pos >= x_max:
        return False
    elif vertex.y_pos >= y_max:
        return False
    if obs_map[vertex.x_pos][vertex.y_pos]:
        return False
    return True

def get_index(vertex, width_x, min_x, min_y):
    return (vertex.y_pos - min_y) * width_x + (vertex.x_pos - min_x)

def ret_heuristic(node_1, node_2):
    unit = 1.0  # unit cost of heuristic
    dis = unit * math.sqrt((node_1.x_pos - node_2.x_pos)**2 + (node_1.y_pos - node_2.y_pos)**2)
    return dis

def final_path_calc(goal_n, closed_set, resol):
    # calculates the final path
    rob_x_pos, rob_y_pos = [goal_n.x_pos * resol], [goal_n.y_pos * resol]
    found = goal_n.found
    while found != -1:
        n = closed_set[found]
        rob_x_pos.append(n.x_pos * resol)
        rob_y_pos.append(n.y_pos * resol)
        found = n.found
    return rob_x_pos, rob_y_pos

#start_xpos:  x coordinate of the start point.
#start_ypos:  y coordinate of the start point.
#goal_xpos :  x coordinate of the goal point.
#goal_ypos :  x coordinate of the goal point.
#obs_xpos  :  list of Obstacles (x)
#obs_ypos  :  ist of Obstacles (y)
#resol     :  resolution of the grid
#rob_rad   :  robot radius

def a_star_alg(start_xpos, start_ypos, goal_xpos, goal_ypos, obs_xpos, obs_ypos, resol, rob_rad):

    start_n = Vertex(round(start_xpos / resol), round(start_ypos / resol), 0.0, -1)
    goal_n = Vertex(round(goal_xpos / resol), round(goal_ypos / resol), 0.0, -1)
    obs_xpos = [iox / resol for iox in obs_xpos]
    obs_ypos = [ioy / resol for ioy in obs_ypos]
    obs_map, x_min, y_min, x_max, y_max, x_w, y_w = get_map_obs(obs_xpos, obs_ypos, resol, rob_rad)
    move = motion_mode()
    open_set, closed_set = dict(), dict()
    open_set[get_index(start_n, x_w, x_min, y_min)] = start_n
    while True:
        c_num = min(
            open_set, key=lambda o: open_set[o].cost + ret_heuristic(goal_n, open_set[o]))
        current_node = open_set[c_num]
        # shows the animation

        if current_node.x_pos == goal_n.x_pos and current_node.y_pos == goal_n.y_pos:
            print("Find goal")
            goal_n.found = current_node.found
            goal_n.cost = current_node.cost
            break
        # Removes an item from the open_set
        del open_set[c_num]
        # The item is added to the closed_set
        closed_set[c_num] = current_node
        # expanding the search grid based off of motion_mode
        for i, _ in enumerate(move):
            vertex = Vertex(current_node.x_pos + move[i][0],
                        current_node.y_pos + move[i][1],
                        current_node.cost + move[i][2], c_num)
            node_num = get_index(vertex, x_w, x_min, y_min)
            if node_num in closed_set:
                continue
            if not vert_valid(vertex, obs_map, x_min, y_min, x_max, y_max):
                continue
            if node_num not in open_set:
                open_set[node_num] = vertex  # check a new node
            else:
                if open_set[node_num].cost >= vertex.cost:
                    # This route is the slected path so far
                    open_set[node_num] = vertex
    rob_x_pos, rob_y_pos = final_path_calc(goal_n, closed_set, resol)
    return rob_x_pos, rob_y_pos



















def main():
    print(__file__ + " start!!")

    # start and goal position
    start_xpos = 1.0  # [m]
    start_ypos = 1.0  # [m]
    goal_xpos = 6.0  # [m]
    goal_ypos = 6.0  # [m]
    grid_size = 1  # [m]
    robot_size = 0.0  # [m]

    obs_xpos, obs_ypos = [], []





if __name__ == '__main__':
    main()
