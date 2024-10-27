# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers...
"""


def bubble(int_list):
    """
    bubble docstring
    1. Outer loop iterates through the list n times
    2. Inner loop compares adjacent elements
    3. Swap elements if they are in the wrong order
    """
    for n in range(len(int_list) - 1, 0, -1):
        for i in range(n):
            if int_list[i] > int_list[i + 1]:
                swapped = True
                int_list[i], int_list[i + 1] = int_list[i + 1], int_list[i]
    print("bubble sort")
    return int_list


def quick(int_list):
    """
    qsort docstring
    1.If the input array has length 0 or 1, return the array as it is already sorted.
    2.Choose the first element of the array as the pivot element.
    3.Create two empty lists, left and right.
    4.For each element in the array except for the pivot:
    a. If the element is smaller than the pivot, add it to the left list.
    b. If the element is greater than or equal to the pivot, add it to the right list.
    5.Recursively call quicksort on the left and right lists.
    6.Concatenate the sorted left list, the pivot element, and the sorted right list.
    7.Return the concatenated list.
    """
    print("quick sort")
    if len(int_list) <= 1:
        return int_list
    else:
        pivot = int_list[0]
        left = [x for x in int_list[1:] if x < pivot]
        right = [x for x in int_list[1:] if x >= pivot]
        return quick(left) + [pivot] + quick(right)
    

def insertion(int_list):
    """
    insertion docstring
    1. Get the length of the array
    a. If the array has 0 or 1 element, it is already sorted, so return
    b. Iterate over the array starting from the second element
    2. Store the current element as the key to be inserted in the right position
    3. Move elements greater than key one position ahead
    4. Shift elements to the right
    5. Insert the key in the correct position
    """
    n = len(int_list) 
    if n <= 1:
        return
    for i in range(1, n):
        key = int_list[i]  
        j = i - 1  
        while j >= 0 and key < int_list[j]:
            int_list[j + 1] = int_list[j]
            j -= 1
        int_list[j + 1] = key
    print("insertion sort")
    return int_list
