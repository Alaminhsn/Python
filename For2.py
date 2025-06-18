nums=(1,2,3,7,8,5,9,5,6,2,7)
x=8
idx=0
for val in nums:
    if(val==x):
        print("number in found index:",idx)
        break
    idx += 1