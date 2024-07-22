class Solution:
    def reversePairs(self, nums):
        if not nums:
            return 0
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid + 1, right)
        count += self.count_and_merge(nums, left, mid, right)
        return count

    def count_and_merge(self, nums, left, mid, right):
        count = 0
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)

        temp = []
        l, r = left, mid + 1
        while l <= mid and r <= right:
            if nums[l] <= nums[r]:
                temp.append(nums[l])
                l += 1
            else:
                temp.append(nums[r])
                r += 1
        while l <= mid:
            temp.append(nums[l])
            l += 1
        while r <= right:
            temp.append(nums[r])
            r += 1
        for i in range(len(temp)):
            nums[left + i] = temp[i]
        return count
