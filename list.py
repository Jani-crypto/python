my_list=[]
print('before append:', my_list)
my_list.append([10,20,30,40])
print('after append:', my_list)
my_list=[10,20,30,40]
my_list.insert(2,15)
print('after insert:', my_list)
my_list=[10,20,15,30,40]
list=[50,60,70]
my_list.extend(list)
print('after extend:', my_list)
del my_list[7]
print('after del:', my_list)
my_list.sort()
print('after sort(ascending):', my_list)
idx=my_list.index(30)
print('after index:', idx)