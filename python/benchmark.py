from dataset import DataGeneration


dataset = DataGeneration()


randomArray  = dataset["random_order"]
sortedArray = dataset["sorted_order"]
reversedArray = dataset["reverse_sorted"]
nearSortedArray = dataset["near_sorted"]
noDuplicateArray = dataset["no_duplicates"]
highDuplicateArray = dataset["high_duplicates"]


random_Array_small,random_Array_medium,random_Array_large  = randomArray[0] ,randomArray[1] ,randomArray[2]
sorted_Array_small,sorted_Array_medium,sorted_Array_large = sortedArray[0],sortedArray[1],sortedArray[2]
reversed_Array_small,reversed_Array_medium,reversed_Array_large =reversedArray[0],reversedArray[1],reversedArray[2]
nearsorted_Array_Small,nearsorted_Array_medium,nearsorted_Array_large=nearSortedArray[0],nearSortedArray[1],nearSortedArray[2]
noDuplicateArray_small,noDuplicateArray_medium,noDuplicateArray_large = noDuplicateArray[0],noDuplicateArray[1],noDuplicateArray[2]
high_Duplpicate_Array_small,high_Duplpicate_Array_medium,high_Duplpicate_Array_large = highDuplicateArray[0],highDuplicateArray[1],highDuplicateArray[2]