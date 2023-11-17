from collections import Counter
​
pass
​
def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)