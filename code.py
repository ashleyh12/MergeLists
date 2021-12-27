def Mergetwolists(list1, list2):
  empty_list = []
  length = len(list1)
  length1 = len(list2)
  for i in range(length):
    empty_list.append(list1[i])
  for i in range(length1):
    empty_list.append(list2[i])
  empty_list.sort()
  return empty_list

# print(Mergetwolists([1, 2, 4], [1, 3, 4])) .... example input



