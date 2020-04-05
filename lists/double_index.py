# Create a function named double_index that has two parameters:
# a list named lst and a single number named index.
# The function should return a new list where all elements are the same
# as in lst except for the element at index. The element at index should
# be double the value of the element at index of the original lst.
# If index is not a valid index, the function should return the original list.
# For example, the following code should return [1,2,6,4]
# because the element at index 2 has been doubled:


def double_index(lst, index):
    try:
        d_index = lst[index] * 2
        lst[index] = d_index
        return lst
    except IndexError:
        return lst


print(double_index([3, 8, -10, 12], 20))