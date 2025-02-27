def tong(lst):
    sum = 0
    for num in lst: 
        if num % 2 == 0 : 
            sum += num
    return sum 
input_list = input("Nhap ds cac so, cach bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
sum_chan = tong(numbers)
print("Tong cac so chan trong list: ", sum_chan)