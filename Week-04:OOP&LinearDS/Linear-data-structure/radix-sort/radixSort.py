# let's say we have a number abc. abc = a x 10^3 + b x 10^2 + c x 10^3.
# By putting in buckets from 0 to 9 (or RADIX QUEUE) -> this is techincally a comparision of a, b, c in a number

# WE HAVE TO START SORT BY ONEs -> then tens -> then hundreds
# intuitive reason: so we 100% sure the order inside one radix queue is correct
# e.g: 34 and 36. First round: sort by ones -> 34, 36. Second round: sort by tens -> both have 3 in tens 
# => just need to preserve the order from previous round


# WHY THE FIFO (first in first out) principle of Queue data structures match with this
# Reason: as long as a digit (e.g at ones, tens) pass -> it can go inside the room (by this, I mean we don't have to care about it any more)
# it's like whoever is at the top of the queue to visit museum, they can go in first.

# Implementation

# #1 task: build data structure queue
# Queue
# Attributes:
# 1. items

# Methods:
# 1. Enqueue
# 2. Dequeue
# 3. Peek
class Queue:
    def __init__(self):
        self._items = []
    
    # method getter for item list
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, value):
        self._items = value
    
    # Enqueue
    def enqueue(self, value):
        self.items.append(value)
        
    # Dequeue: This will be optimized by splitting the queue into 2 stacks. O(n) -> O(1)
    def dequeue(self):
        return self.items.pop(0)
    
    # Peek
    def peek(self):
        return self.items[-1]
    
    
#2 task: implement radix sort
# input: a list of int
# output: a ascendingly sorted list of int

# pseudo
#1: find max (number of digits) -> know how many times to loop
#2: set up 1 main queue and 10 radix queues (all are called "bin")
#3: loop through every integer inside the main queue, extract the digits by ones, tens, hundreds,.. 

# find maximum number of digits of a number inside the list
def get_max_digits(array):
    max_digits = 0
    
    for number in array:
        # convert number to string first
        number = str( abs(number) )
        
        # get the number of digits
        digits = len(number)
        
        # update maximum digits
        if digits > max_digits:
            max_digits = digits
    
    return max_digits


# The Radix sort operation can be described as follows:

# First, put all items into the Main bin queue.
# The next step is to start with the lowest digit. In this case, it is the ones digit. We take out all the items from the Main bin and put it into the respective radix bins. If the ones is 0, we put into radix bin 0. If the ones is 1, we put into the radix bin 1. If the ones is 2, we put into the radix bin 2, and so on until 9.
# Once we finish putting all the items into the respective radix bins, we empty out the radix bin queue and put the items back into the Main bin queue. We start from radix 0 and continue until radix bin 9.
# We repeat this step until we reach the highest digits.

def radixSort(array):
    # find the max number of digits
    max_digits = get_max_digits(array)
    
    # set up the bins (main queue + radix queue)
    main_queue = Queue()
    
    # set up 10 radix queues
    radix_queues = [Queue() for _ in range(10)]
    
    # put all numbers into the main bin queue
    for number in array:
        main_queue.enqueue(number)
    
    # outer loop: digit pass
    for i in range(max_digits):
            
        # take each number out inside the main queue and extract the digit(first digit is ones, second is tens, third is hundreds)
        # the formula is that (number // 10^i) % 10
        while len(main_queue.items) != 0:
            # current number that we are targeting in the main queue, starting from the very first number
            current_number = main_queue.dequeue()
            
            # the extracted digits should only be from 0 to 9
            extracted_digit = ( current_number // pow(10, i) ) % 10
            
            # we will put the numbers in their corresponding bins
            # e.g: 34 -> by ones, digit is 4 -> put in bin 4. Bin ranges from 0 to 9
            radix_queues[extracted_digit].enqueue( current_number )
            
        # After the numbers are put in their correct bins, we take them out
        # starting with bin 0, put back to the main queue
        
        main_queue.items = [] #reset the main queue to receive newly sorted by ones array
        for radix_queue in radix_queues:
            
            # put all the items inside a bin in the main queue
            # while putting all items inside a radix bin to the main queue, we also need to remove them from the radix bins
            # so it's more like MOVING the items from radix bins to the main bin
            
            while len(radix_queue.items) != 0:
                # current number inside the radix queue that is targeted, starting from the very first number
                current_number = radix_queue.dequeue()
                
                main_queue.enqueue(current_number)
                
    
    # After we're done with the outer loop, the main queue will contain the sorted ascendingly array
    return main_queue.items


arr = [101, 21, 4000, 7]
print( radixSort(arr) )
