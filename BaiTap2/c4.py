def truy_cap(tuple_data):
    fist = tuple_data[0]
    last = tuple_data[-1]
    return fist, last
input_tuple = eval(input("Nhap tuple vd: 1,2,3: "))
fists, lasts =truy_cap(input_tuple)
print("Pt dau tien: ", fists)
print("Pt cuoi cung: ", lasts)