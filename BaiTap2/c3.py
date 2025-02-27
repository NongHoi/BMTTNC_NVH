def tao_tuple_list(lst):
    return tuple(lst)
input_list = input("Nhap ds cac so , cach bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_list(numbers)
print("list: ", numbers)
print("tuple tu list: ", my_tuple)