ALPHABET_SIZE = 26

def decode(data, k):
  if k == 0:
    return 1

  s = len(data) - k
  if data[s] == '0':
    return 0

  result = decode(data, k - 1)
  if k >= 2 and int(data[s:s+2] <= ALPHABET_SIZE):
    result += decode(data, k - 2)
  
  return result

def ways_to_decode(data):
  return decode(data, len(data))
