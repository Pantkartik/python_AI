
# to check whether the string is palindrome or not 
    
def check_palidrome(st_list):
    
    list_orginal=st_list.copy()
    rev_list=st_list[::-1]   
    if list_orginal==rev_list:
        print("Palndrome")
    
    
        
st_list=['n','a','m','a','n']
check_palidrome(st_list)




#  to reverse the string 
st=str(input("Enter the string "))
st_list=list(st)

st_list.reverse()
print(st_list,type(st_list))