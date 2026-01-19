
#Bubble Sort
nums = [0, 1, 2, 2, 3, 0, 4, 2]
n = len(nums)

# Outer loop to traverse through all list elements
for i in range(n):
    # Inner loop for comparisons
    for j in range(0, n - 1):
        # Swap if the element found is greater than the next element
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
-----------------------------------------------------------
#Selection Sort
nums = [0,1,2,2,3,0,4,2]
n = len(nums)                             
                      
for i in range(n):
   # Assume the current position 'i' is the minimum
  min_pos=i    
  # Inner loop: look through the REST (right side) of the list (unsorted part)
    for x in range(i+1, n):         
  # If we find something smaller than our current minimum...
        if nums[x] < nums[min_pos]:      
  # Update the index of the minimum (don't swap yet!)
            min_pos=x   
  # After checking the whole unsorted section, swap the smallest found with nums[i]        
        nums[i], nums[min_pos] = nums[min_pos], nums[i]                  

print(nums)
---------------------------------------------------------
#Insertion Sort
nums = [0, 1, 2, 2, 3, 0, 4, 2]
n = len(nums)

for i in range(1, n):
    # j starts at the current number and looks back to the beginning
    for j in range(i, 0, -1):
        # If the number on the left is bigger, swap them
        if nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
        else:# If the left number is NOT bigger, it's already in the right spot
            break
print(nums)

----------------------------------------------
# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        # 1. Find the middle
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 2. Divide (Recursive calls)
        merge_sort(left_half)
        merge_sort(right_half)

        # 3. Merge (The sorting part)
        i = j = k = 0
        
        # Compare elements from both halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements were left over
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

nums = [0, 1, 2, 2, 3, 0, 4, 2]
merge_sort(nums)
print(nums)
            # If the left number is NOT bigger, it's already in the right spot
            break

print(nums)
