"""
@author: David Lei
@since: 27/07/2016
@modified: 

"""

first_row = [int(c) for c in input().split(' ')]
second_row = [int(c) for c in input().split(' ')]
third_row = [int(c) for c in input().split(' ')]

sum_first_row = sum(first_row)
sum_second_row = sum(second_row)
sum_third_row = sum(third_row)

sum_first_col = first_row[0]+second_row[0]+third_row[0]
sum_second_col = first_row[1]+second_row[1]+third_row[1]
sum_third_col = first_row[2]+second_row[2]+third_row[2]

sum_lr_diag = first_row[0]+second_row[1]+third_row[2]
sum_rl_diag = first_row[2] + second_row[1] + third_row[0]

print('q')