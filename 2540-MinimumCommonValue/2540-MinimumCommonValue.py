        
            return False
                else:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
        # Check which array is shorter for efficient searching
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Perform binary search on the shorter array
        for num in nums1:
            if binary_search(nums2, num):
                return num
        return -1  # If no common element found

[
