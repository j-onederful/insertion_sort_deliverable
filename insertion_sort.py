li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]

sorted = [0, 1, 2, 3, 9, 10, 100]
# check if a list is sorted or not
def is_sorted(li):
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            return False

    return True

iterations = 0

def insertion_sort(li):
    global iterations
    # iterate over the entire list, loop downward when we find a value that is smaller than what is to the left
    for index in range(len(li)):
        # we need to know the current number for comparisons
        current_number = li[index]
        # the position sliding back down the list
        comparison_position = index - 1
        while comparison_position >= 0 and current_number < li[comparison_position]:
            # swap the values down while both conditions are met
            li[comparison_position], li[comparison_position + 1] = li[comparison_position + 1], li[comparison_position]
            comparison_position -= 1
            iterations += 1

insertion_sort(li)

print(is_sorted(li))
print(li)
print(iterations)