# create a class
from codecs import lookup


class pair_elements:


    def twoSum(self, num, target):
            # create an empty dictionary
            lookiup = {}


            # Iterate through the tuple
            for i, num in enumerate(nums):
                    if target - num in lookup:
                           return (lookup[target - num], i )
                    lookup[num] = i


# take input of dum form the user
value = int(input("Enter sum for which you want to make this search : "))
print("index1=%d, index2=%d" % pair_elements().twosum((10,20,30,40,50,60,70),value))