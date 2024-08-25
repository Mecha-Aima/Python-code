# The final configuration with n disks piled up to the third rod in decreasing order can be obtained by moving:
# n - 1 disks from the source to the auxiliary rod
# the largest disk from the source to the target
# and then the n - 1 disks from the auxiliary rod to the target.
NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    
    # move the nth disk from source to target
    target.append(source.pop())
    
    # display our progress
    print(f'A: {A}, B: {B}, C: {C}', '\n')
    
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)