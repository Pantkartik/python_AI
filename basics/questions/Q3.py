# wap to enter the marks of 3 subjects from user and store them in dictionary
dict={}
marks_chem=int(input("Enter the marks of chem "))
marks_math=int(input("Enter the marks of math "))
marks_bio=int(input("Enter the marks of bio"))
dict.update({"CHEMISTRY":marks_chem })
dict.update({"MATHS":marks_math})
dict.update({"BIOLOGY":marks_bio})

print(dict)