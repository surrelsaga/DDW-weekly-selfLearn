def towerOfHanoi(numberOfDisks, start, middle, end):
    # Base case: when there's only 1 disk, we just move from the start (where the disk is at)
    # to the end and finish the game
    if numberOfDisks == 1:
        print(f"Move disk {numberOfDisks} from {start} to {end}")
    # Recursive case: 
    # move n - 1 disks from start to middle, 
    # move to the bottom from start to destination, 
    # move n - 1 disks left from middle to destination
    else:
        towerOfHanoi(numberOfDisks - 1, start, end, middle)
        print(f"Move disk {numberOfDisks} from {start} to {end}")
        towerOfHanoi(numberOfDisks - 1, middle, start, end)
        
towerOfHanoi(3, 'A', 'B', 'C')
