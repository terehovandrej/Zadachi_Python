# Write a function named append_sum that has one parameter — a list named named lst.
# The function should add the last two elements of lst together and append the result
# to lst. It should do this process three times and then return lst.
# For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].


def append_sum(lst):
    counter = 0
    while counter < 3:
        lst.append(sum(lst[-2:]))
        counter += 1
    return lst


print(append_sum([1, 1, 2]))
