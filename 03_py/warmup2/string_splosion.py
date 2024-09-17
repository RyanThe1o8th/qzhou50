def string_splosion(str):
  returnable = "";
  for i in range(len(str) + 1):
    returnable = returnable + str[:i]
  return returnable
