data = [1,2,3]
structure = ['name',data,'subname']
print isinstance(data,list)
print all(isinstance(item,list) for item in structure)
