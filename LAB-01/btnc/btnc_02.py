import re

def sum_positive_negative(numbers):
    positive_sum = 0
    negative_sum = 0

    for number in numbers:
        if number > 0:
            positive_sum += number
        elif number < 0:
            negative_sum += number

    return positive_sum, negative_sum

def main():
    input_string = input("Nhập chuỗi các số nguyên: ")
    number_strings = re.findall(r'-?\d+', input_string)
    
    numbers = [int(num_str) for num_str in number_strings]

    positive_sum, negative_sum = sum_positive_negative(numbers)

    print(f"Tổng các số nguyên dương: {positive_sum}")
    print(f"Tổng các số nguyên âm: {negative_sum}")

if __name__ == "__main__":
    main()
