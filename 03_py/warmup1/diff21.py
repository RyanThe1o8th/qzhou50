def diff21(n):
  returnable = 21 - n
  if n > 21:
    return abs(returnable * 2)
  return abs(returnable)