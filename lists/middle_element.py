# Create a function called middle_element that has one parameter named lst.
# If there are an odd number of elements in lst, the function should return the middle element.
# If there are an even number of elements,
# the function should return the average of the middle two elements.


def middle_element (lst):
    lst_length = int(len(lst))
    if lst_length % 2 > 0:
        middle_i = lst_length // 2
        middle_el = lst[middle_i]
        return middle_el
    elif lst_length % 2 == 0:
        middle_i_two = lst_length // 2
        middle_i_one = middle_i_two - 1
        avg = (int(lst[middle_i_one]) + int(lst[middle_i_two])) / 2
    return avg


print(middle_element([5, 2, -10, -4, 4, 5]))