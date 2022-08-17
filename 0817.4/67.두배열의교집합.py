nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
inter = []
if len(nums1) <=  len(nums2):
    short_n = nums1
    long_n = nums2
else:
    short_n = nums2
    long_n = nums1

for i in short_n:
    if i in long_n and i not in inter:
        inter.append(i)

print(inter)
