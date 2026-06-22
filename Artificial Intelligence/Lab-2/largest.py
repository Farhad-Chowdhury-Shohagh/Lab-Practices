numbers=[2,3,5,6,6,8,9,9,10,1,4]

uniqueNum = set(numbers)

uniqueNum.remove(max(uniqueNum))
print(f"2nd Largest Unique number: {max(uniqueNum)}")