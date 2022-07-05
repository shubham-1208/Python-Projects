test_str = "Geeks"
  
# printing original string 
print("The original string is : " + str(test_str))
  
# Get all substrings of string
# Using list comprehension + string slicing
res = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]
  
# printing result 
print("All substrings of string are : " + str(res))


from itertools import combinations
  
# initializing string 
test_str = "Geeks"
  
# printing original string 
print("The original string is : " + str(test_str))
  
# Get all substrings of string
# Using itertools.combinations()
res = [test_str[x:y] for x, y in combinations(
            range(len(test_str) + 1), r = 2)]
  
# printing result 
print("All substrings of string are : " + str(res))