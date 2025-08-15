dict_original=dict(Name="Kartik",Age=19,Height="6 feet")

dict_copy=dict_original.copy()

dict_copy.popitem()
print(dict_copy)
print(dict_original)