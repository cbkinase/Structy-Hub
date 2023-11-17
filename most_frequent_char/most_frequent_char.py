from collections import Counter
import math
​
def most_frequent_char(s):
  return Counter(s).most_common(1)[0][0]