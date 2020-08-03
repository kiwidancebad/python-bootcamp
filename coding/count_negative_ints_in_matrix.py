def count_negative_ints_in_matrix(M, n, m):
  count = 0
  i = 0
  j = m - 1

  while j >= 0 and i < n:
    if M[i][j] < 0:
      count += (j + 1)
      i += 1
    else:
      j -= 1
  
  return count
