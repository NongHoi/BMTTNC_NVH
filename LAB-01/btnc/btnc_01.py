from itertools import permutations

def list_permutations(lst):
    return list(permutations(lst))

# Example usage
if __name__ == "__main__":
    sample_list = [1, 2, 3]
    perms = list_permutations(sample_list)
    print("danh sách đầu vào: ", sample_list)
    print("các hoán vị của danh sách: ")
    for perm in perms:
        print(perm)