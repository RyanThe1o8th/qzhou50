def string_match(a, b):
  returnable = 0
  for i in range(len(a) - 1):
    if(a[i: i + 2] == b[i: i + 2]):
      returnable = returnable + 1
  return returnable
