from collections import Counter
import math
​
def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)