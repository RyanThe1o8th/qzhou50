def string_bits(str):
  returnable = ""
  for i in range(len(str)):
    if(i%2 == 0):
      returnable += str[i]
  return returnable
