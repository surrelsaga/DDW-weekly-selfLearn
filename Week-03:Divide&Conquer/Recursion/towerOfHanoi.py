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
