class Solution(object):
    def reversePairs(self, nums):
        cnt = [0]  # Use a list to hold the count

        def count_arr(nums, left, mid, right):
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                cnt[0] += j - (mid + 1)

        def merge(nums, left, mid, right):
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
            for i in range(len(temp)):
                nums[left + i] = temp[i]

        def merge_sort(nums, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort(nums, left, mid)
                merge_sort(nums, mid + 1, right)
                count_arr(nums, left, mid, right)
                merge(nums, left, mid, right)

        merge_sort(nums, 0, len(nums) - 1)
        return cnt[0]