# This program will fail in test cases where the ascii value of words in the given list are same, need to try another solution

def group_anagrams(arr):
  holder = []
  for i in arr:
    holder.append("".join(sorted(i)))

  print(holder)
  for i in holder: 
  
arr = ['mohit','acre','rohit', 'kalyan', 'megha',  'race', 'care']

print(group_anagrams(arr))
# **********************************************************************************************************
# Second Method - Using a new function as key, this function calculates the total aschii value of each words
# **********************************************************************************************************
def count_ascii(word):
    total = 0
    for ch in word:
        total += ord(ch)
    print(total)   
    return total

def group_anagrams(arr):
  return sorted(arr, key = count_ascii)
  
arr = ['mohit', 'acre', 'rohit', 'kalyan', 'race', 'megha',  'care']

print(group_anagrams(arr))
