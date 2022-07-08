swap = [1, 2, 'four', 3]

# swapping easily in python
# order things are = order the way we want it to be
swap[2], swap[3] = swap[3], swap[2]

# print(swap)

li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]

sorted = [0, 1, 2, 3, 9, 10, 100]
# check if a list is sorted or not
def is_sorted(li):
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            return False

    return True

iterations = 0
# print(is_sorted(li))
# print(is_sorted(sorted))

def bubble_sort(li):
    # flag that tells us if the list is sorted
    has_swapped = True

    while has_swapped:
        # assume that no swap will be made
        has_swapped = False
        for i in range(len(li) - 1):
            # check the neighbors balues -- if current is greater than on to the right -- make swap
            if  li[i] > li[i + 1]:
                # wrong order -- need to swap
                li[i], li[i+1] = li[i+1], li[i]
                has_swapped = True

bubble_sort(li)
print(is_sorted(li))
print(li)

# def bubbleSort(li):
#     n = len(li)
#     swapped = False
#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if li[j] > li[j + 1]:
#                 swapped = True
#                 li[j], li[j + 1] = li[j + 1], li[j]
#         if not swapped:
#             return

# bubbleSort(li)

# print("Sorted array is:")
# for i in range(len(li)):
#     print("% d" % li[i], end=" ")