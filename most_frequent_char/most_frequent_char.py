from collections import Counter
​
def most_frequent_char(s):
  pass
  return Counter(s).most_common(1)[0][0]