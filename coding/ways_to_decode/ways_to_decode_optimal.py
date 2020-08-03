ALPHABET_SIZE = 26

def decode(data, k, memo):
  if k == 0:
    return 1

  s = len(data) - k
  if data[s] == '0':
    return 0

  if memo[k] != null:
    return memo[k]

  result = decode(data, k - 1, memo)
  if k >= 2 and int(data[s:s+2]) <= ALPHABET_SIZE:
    result += decode(data, k - 2, memo)
  
  memo[k] = result
  return result

def ways_to_decode(data):
  memo = new int[len(data) + 1]
  return decode(data, len(data), memo)
