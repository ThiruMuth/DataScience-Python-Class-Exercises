def human2dog(dogageinhumanyr):
    """This function returns dog's age in human years"""
    dogageindogyr=0.0
    if(dogageinhumanyr)<=2:
        dogageindogyr = dogageinhumanyr*10.5
    else:
        dogageindogyr = 2*10.5 + (dogageinhumanyr-2)*4
    return dogageindogyr

def maxof3num(input_number_array):
    """ This function returns the maximum of 3 numbers """
    max = input_number_array[0]
    for i in range(0,3):
        if (max < input_number_array[i]):
            max = input_number_array[i]
    return max
    
def countupperlower(input_string):
    """This function returns the number of capital and lower in a string"""
    capitalletters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallletters=capitalletters.lower()
    CapitalCount=0
    SmallCount=0
    for i in range(0,len(input_string)):
        if(capitalletters.find(input_string[i]) != -1):
            CapitalCount = CapitalCount+1
        elif(smallletters.find(input_string[i]) != -1):
            SmallCount = SmallCount+1
    return [CapitalCount,SmallCount]
