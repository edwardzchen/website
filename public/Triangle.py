#  File: Triangle.py

#  Description: Find the greatest sum in a num triangle

#  Student Name: Zhihao Chen

#  Student UT EID: zc4284

#   Partner's Name: Neil Pareddy

#   Partner's UT EID: nsp632

#   Course Name: CS 313E

#   Unique Number: 50205

#   Date Created: 12/09/19

#   Date Last Modified: 12/09/19

import time
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
    b = []
    exhaustive_helper(grid, 0, 0, 0, b)
    return max(b)
def exhaustive_helper(grid, current_list, index, sum, b):
    if current_list == len(grid):
        b.append(sum)
    else:
        number = int(grid[current_list][index])
        return exhaustive_helper(grid, current_list + 1, index, sum + number, b) or exhaustive_helper(grid, current_list + 1, index + 1, sum + number, b)

# returns the greatest path sum using greedy approach
def greedy (grid):
    current_list = 0
    index = 0
    number = int(grid[current_list][index])
    sum = 0
    while current_list < len(grid) - 1:
      sum += int(number)
      num1 = int(grid[current_list + 1][index])
      num2 = int(grid[current_list + 1][index + 1])
      if num1 > num2:
          number = num1
          current_list += 1
      else:
          number = num2
          current_list += 1
          index += 1

    return sum


# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
    sum = 0
    b = []
    helper_rec_search(grid, sum, b)
    return max(b)


def helper_rec_search(grid, sum, b):
    if (len(grid) == 1):
        return b.append(sum + int(grid[0][0]))
    else:
        grid1 = []
        grid2 = []
        for line in grid[1:]:
            grid1.append(line[1:])
            grid2.append(line[:-1])
        sum += int(grid[0][0])
        return helper_rec_search(grid1, sum, b) or helper_rec_search(grid2, sum, b)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    return dynamic_prog_helper(0, 0, grid)

def dynamic_prog_helper(a, b, grid):
    if a >= len(grid):
        return 0
    else:
        number = int(grid[a][b])
        i = int(number) + dynamic_prog_helper(a + 1, b, grid)
        j = int(number) + dynamic_prog_helper(a + 1, b + 1, grid)
        return max(i, j)

def dyn_helper (grid, i, j):
  # base case -- we've reached the bottom of the triangle
  if i >= len(grid):
    return 0
  else:
    a = int(grid[i][j]) + dyn_helper (grid, i + 1, j)
    b = int(grid[i][j]) + dyn_helper (grid, i + 1, j + 1)
    return max(a,b)



# reads the file and returns a 2-D list that represents the triangle
def read_file ():
    f = open("triangle.txt", "r")
    num_rows = int((f.readline()).strip())
    grid = []
    for i in range(num_rows):
        row = (f.readline()).strip()
        row = row.split()
        for i in row:
            i = int(i)
        grid.append(row)

    f.close()
    return grid

def main ():


  # read triangular grid from file
  grid = read_file()

  ti = time.time()
  # output greates path from exhaustive search
  print("The greatest path sum through exhaustive search is", str(exhaustive_search(grid)) + ".")
  tf = time.time()
  del_t = tf - ti
  print("The time taken for exhaustive search is", del_t, "seconds.")
  # print time taken using exhaustive search
  print("")

  ti = time.time()
  # output greates path from greedy approach
  print("The greatest path sum through greedy search is", str(greedy(grid)) + ".")
  tf = time.time()
  del_t = tf - ti
  print("The time taken for recursive search is", del_t, "seconds.")
  # print time taken using greedy approach
  print("")
  ti = time.time()
  # output greates path from divide-and-conquer approach
  print("The greatest path sum through recursive search is", str(rec_search(grid)) + ".")
  tf = time.time()
  del_t = tf - ti
  print("The time taken for recursive search is", del_t, "seconds.")
  # print time taken using divide-and-conquer approach
  print("")
  ti = time.time()
  # output greates path from dynamic programming
  print("The greatest path sum through dynamic programming is", str(dynamic_prog(grid)) + ".")
  tf = time.time()
  del_t = tf - ti
  print('The time taken for dynamic programming is ', del_t, "seconds.")
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()
