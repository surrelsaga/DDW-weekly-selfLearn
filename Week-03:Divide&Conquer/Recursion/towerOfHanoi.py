# PCDIT

# Problem statements: (check image in the doc)
# Give n disks and 3 towers (all n disks are at the first tower called 'source')
# so we have source, destination and auxiliary (tower to help with the moving in the algo)

# Cases: (visualization)

# DESIGN OF ALGO: 
# basic understanding: In each iteration, we take all the top disks (except for
# ONLY THE BOTTOM ONE) -> we move to the auxiliary
# then, the bottom one is moved to the destination tower.

# in the subsequent iteration, the empty tower (the old source tower) become
# the new auxiliary tower.
# So the pattern that happens in every recursion is
# "TOP DISKS ARE MOVED TO AUXILIARY, BOTTOM IS MOVED TO DESTINATION"

# Substeps in a step to move all top disks to auxiliary (we must keep the ascending order downward)
# reason?: is to have a pattern so we can use recursion
# Substeps: first disk always move to destination, until we only left with one disk
# above the actual bottom disk, then we move that disk to auxiliary and move all the
# previous top disks back to auxiliary
# These are all the substeps to form one step of move the first n - 1 disks from source to auxiliary

# ONE IMPORTANT NOTES: the disk stack is smallest on top, largest at bottom
# they are labelled with numbers from 1 to n.
# the smaller the disk number is, the smaller the its size is

# PSEUDOCODE
# Input:
#   - n, number of disks
#   - source tower
#   - destination tower
#   - auxiliary tower
# Output:
#   - sequence of steps to move n disks from source to destination tower using auxiliary tower
# Steps:
# 1. if n is 1 disk:
#     1.1 Move the one disk from source to destination tower
# 2. otherwise, if n is greater than 1:
#     2.1 Move the first n - 1 disks from source to auxiliary tower
#     2.2 Move the last disk n from source to destination tower
#     2.3 Move the first n - 1 disks from the auxiliary tower to the destination tower

def towerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    else:
        towerOfHanoi(n - 1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        towerOfHanoi(n - 1, auxiliary, destination, source)
        
towerOfHanoi(3, 'A', 'B', 'C')

# Imagine the execution process
# n = 3
# first the else block gets executed
# line 51 is executed and line 52 needs to wait for 51 to be done executing

# Execution of when n = 3 and line 51 is executed: towerOfHanoi(3, 'A', 'B', 'C')
    # Call towerOfHaNoi(2, 'A', 'C', 'B')
        # Then call towerOfHaNoi(1, 'A', 'B', 'C')
            # Then print "Move disk 1 from A to B"
            # towerOfHaNoi(1, 'A', 'B', 'C') is done executing, return nothing
        
        # print "Move disk 2 from A to C"
        
        # Then call towerOfHaNoi(1, 'B', 'C', 'A')
            # Print "Move disk 1 from B to C"
            # towerOfHaNoi(1, 'B', 'C', 'A') is done executing, return nothing
            
    # Print "Move disk 3 from A to B"
    
    # Call towerOfHaNoi(2, 'C', 'B', 'A')
        # Then call towerOfHaNoi(1, 'C', 'A', 'B')
            # Then print "Move disk 1 from C to A"
            # towerOfHaNoi(1, 'C', 'B', 'A') is done executing, return nothing
        
        # print "Move disk 2 from C to B"
        
        # Then call towerOfHaNoi(1, 'A', 'B', 'C')
            # Print "Move disk 1 from A to B"
            # towerOfHaNoi(1, 'A', 'B', 'C') is done executing, return nothing
            

# Final output:
# Move disk 1 from A to B
# Move disk 2 from A to C
# Move disk 1 from B to C
# Move disk 3 from A to B
# Move disk 1 from C to A
# Move disk 2 from C to B
# Move disk 1 from A to B
        

# FINALiZED PATTERN
# Base case: when there is one disk left, we move it from the source to destination
# Recursive:
# - Move top disks (except the bottom one) to the auxiliary
# - Move bottom disk to the destination

# - Repeat the 2 steps above with the top disks (mentioned in step 1)
        
        

