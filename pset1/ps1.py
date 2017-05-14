###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    start = time.time()    
    itemsCopy = cows.copy() #copy cows
    itemsValue = [] #items list place holder, to allow innumeration
    
    result = [] 
    totalWeight = 0.0
    trip = []   

    while itemsCopy: #as long as the dictionary copy has entries do...
        for value in itemsCopy.values(): #check which entries are still available
            itemsValue.append(value) 
        itemsValue = sorted(itemsValue, reverse=True) #after build a list, sort them by biggest to smallest
        
        for i in range(len(itemsValue)):
           if (totalWeight + itemsValue[i]) <= limit: #if total weight plus weight of the current cow is smaller than limit do
                trip.append((list(itemsCopy.keys())[list(itemsCopy.values()).index(itemsValue[i])])) #find the name of the cow and load it into the trip
                totalWeight += itemsValue[i] #add weight of current trip
                del(itemsCopy[((list(itemsCopy.keys())[list(itemsCopy.values()).index(itemsValue[i])]))]) #remove cow from available list
          
        result.append(trip) #make record of the trips that have been taken
        trip = [] #set everything up for the new trip and keep going
        itemsValue = []
        totalWeight = 0
    end = time.time()
    print(end - start)
    return result


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
#    start = time.time()    
    def addCowWeight(list, cows):
        """adds a list of cows, with value coming from dict"""
        sum = 0.0
        for key in list:
            sum += cows[key]
       
        return sum

    #list of cows
    cowName = (cows.keys())
    ##cowName = ['Maggie', 'Lola', 'Oreo']

    #list to store all partitions and useful ones
    allCowsTripsCombinations = []
    usePart = []
    
    for cowsTripsCombinations in get_partitions(cowName):
        allCowsTripsCombinations.append(cowsTripsCombinations)
       
    #make a test that checks each trip list if their sum <= limit
    #adds each partition that passes all tests to usePart
    for completeCowsTrips in allCowsTripsCombinations:
        test = []
        for individualCowTrip in completeCowsTrips:
           if addCowWeight(individualCowTrip, cows) <= limit:
               test.append(individualCowTrip)
    
        if len(test) == len(completeCowsTrips):
            usePart.append(completeCowsTrips)

    #find all the lengths of each option, and search for smallest
    lenIndex = []
    for part in usePart:
        lenIndex.append(len(part))
        print(lenIndex)
    find = min(lenIndex)

    for part in usePart:
        if len(part) == find:
#            end = time.time()
#            print(end - start)
            return part
            

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10


#print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))

#Oreo,6
#Moo Moo,3
#Milkshake,2
#Millie,5
#Lola,2
#Florence,2
#Henrietta,9
