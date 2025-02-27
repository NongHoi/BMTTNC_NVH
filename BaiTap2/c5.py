def dem(lst):
    count = {}
    for item in lst:
        if item in count: 
            count[item] += 1
        else: 
            count[item] =1 
    return count
input_string = input("Nhap ds cac tu, cach nhau bang dau cach: ")
word_list = input_string.split()
sl_dem = dem(word_list)
print("Sl xuat hien: ", sl_dem)
