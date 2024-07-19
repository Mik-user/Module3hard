data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def summator(*x):
    global summ
    for j in range(len(x)):
        if (isinstance (x[j], str)):
            summ += len(x[j])
        elif isinstance(x[j],int) or isinstance(x[j],float):
            summ += x[j]
        else:
            if isinstance(x[j], dict):
                key = list(dict.keys(x[j]))
                summator (*key)
                value = list(dict.values(x[j]))
                summator(*value)
            else:
                summator(*x[j])
    return summ
summ = float()
rez1 = summator(*data_structure)
print('Результат:', rez1)



