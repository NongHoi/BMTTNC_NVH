def dao_list(lst): 
    return lst[::-1]
input_list = input("Nhap ds cac so , cach bang dau phay: ")
numbers = list(map(int , input_list.split(',')))
list_dao = dao_list(numbers)
print("List da dao dc: ", list_dao)