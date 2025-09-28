def check_palidrome(st_list):
    
    list_orginal=st_list.copy()
    rev_list=st_list[::-1]   
    if list_orginal==rev_list:
        print("Palndrome")
    
    
        
st_list=['n','a','m','a','n']
check_palidrome(st_list)

