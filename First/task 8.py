A = [1, -6, 9, -3, 2, -3, 1, -7, 1, -8]
mark=bool()
for i in range(len(A)-2):
   if (A[i]>0)==(A[i+1]>0):
      mark=1
if mark:
   print('В этом массиве есть соседние числа с одинаковыми знаками')
else:
   print('В этом массиве нет соседних чисел с одинаковыми знаками')
