# 堆的使用
# 如果量比较少的话，可使用nlargest、nsmallest
import heapq
nums = [1, 1, 0, 6, 9, 4, 8]
print(heapq.nlargest(3, nums))

# 否则的话，可以先吧list转化为堆
heap = list(nums)
heapq.heapify(heap)
print(heap)

# 更快的方式其实是先对集合排序，然后使用切片(sublist)
nums2 = [1, 1, 0, 6, 9, 4, 8]
ll = sorted(nums2)[:3]
print(ll)
print(ll[-3:])
