from string import ascii_letters, digits
def uncompress(s, res=""):
  i = 0     # the number
  j = i + 1
  
  while s[j] in digits:
    j += 1
    
  number = int(s[i:j])
  letter = s[j]
  res += letter * number
  
  if len(s) - 1 == j:
    return res
  
  return uncompress(s[j+1:], res)
  
  
  
r = uncompress("2h5y1g2q")
print(r)