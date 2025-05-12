"""A small frog wants to get to the other side of the road. 
The frog is currently located at position X and wants to get to a position 
greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to 
reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of 
jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y."""


#pseudo: 1. a loop that adds on D to X and adds to a counter every iteration 
# 2. compare new X to Y if X <= Y return count

def solution(X, Y, D):
    if X == Y:
        return 0
    else:
        count = 0
        jump = X + D
        while jump < Y:
            jump += D
            count += 1
            continue
        return count + 1

print(solution(10, 85, 30))
print(solution(0, 100, 10))
print(solution(10, 10, 10))

""" other sol:
def frog_jump(X, Y, D):
    distance = Y - X
    if distance % D == 0:
        return distance // D
    else:
        return distance // D + 1"""