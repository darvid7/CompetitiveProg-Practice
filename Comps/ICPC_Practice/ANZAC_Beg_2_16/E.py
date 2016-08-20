"""
@author: David Lei
@since: 13/08/2016
@modified:

"""


def main():

    data = [13, 2, 1, 3, 4]
    #[100, 2, 1, 1, 0]

        #100, 2, 1, 1, 0] #10,1,10,2,1]#list(map(int, input().split()))

    floors = data[0]
    starting_floor = data[1]
    final_goal_floor = data[2]
    up_once = data[3]
    down_once = data[4]

    current_floor = starting_floor

    pressed = 0

    if True:
        goal_floor = final_goal_floor-current_floor
        if goal_floor > 0:  # want to go up
            if up_once == 0:
                print("Use the stairs")
                return False
            go_up_times = goal_floor//up_once
            go_up_rem = goal_floor%up_once
            current_floor += go_up_times * up_once
            pressed += go_up_times

            go_down_times = go_up_rem//down_once
            go_down_rem = go_up_rem % down_once

            current_floor += go_down_times * -(down_once)
            pressed += go_down_times

            if ((final_goal_floor-current_floor) % up_once) != 0:
                print("Use the stairs")
                return False
            else:
                go_up_times = (final_goal_floor - current_floor)//up_once
                current_floor += go_up_times * up_once
                pressed += go_up_times

        elif goal_floor < 0: # want to go down
            if down_once == 0:
                print("Use the stairs")
                return False

            go_down_times = goal_floor//down_once
            go_down_rem = goal_floor%down_once

            current_floor += go_down_times * down_once
            pressed += go_down_times

            go_up_times = go_down_rem//up_once
            go_up_rem = go_down_rem % up_once

            current_floor += go_up_times * up_once
            pressed += go_up_times

            if final_goal_floor-current_floor % down_once != 0:
                print("Use the stairs")
                return False
            else:
                go_down_times = (final_goal_floor - current_floor)//down_once
                current_floor += go_down_times * down_once
                pressed += go_down_times

        else:   # at goal floor
            pass
    print(pressed)
main()