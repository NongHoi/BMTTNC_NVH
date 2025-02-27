def delete(dic , key): 
    if key in dic: 
        del dic[key]
        return True
    else: 
        return False
my_dic = {'a' : 1 , 'b': 2, 'c': 3, 'd': 4}
key_del = 'b'
result = delete(my_dic , key_del)
if result:
    print("Phan tyu dc xoa: ", my_dic)
else: 
    print("Ko co phan tu xoa") 