import random
import time 

# cách mà naive search hoạt động là nó sẽ đi vào từng phần tử, từ đầu cho đến cuối của list đó để check xem cái nào thoả mãn yêu cầu thì trả về. 
# cách này sẽ tốn nhiều thời gian, như ví dụ dưới này list này có tầm khoảng 3triệu phần tử thì cách này sẽ phải chạy 3 triệu lần để check


# với binary search, nó sẽ chạy thẳng vào chính giữa của dãy, và tìm xem nếu target lớn hơn hay nhỏ hơn phần tử nằm ở giữa, từ đây sẽ rút ngắn quá trình mà program chạy để tìm ra được đáp án
def binary_search(list_, low, high, target):
	#dòng này để chương trình biết được đâu là phần tử ở giữa 
	middle = round((high + low)/2)
	if high >= low : 
		if target == list_[middle]:
			return middle
		elif target < list_[middle]:
			return binary_search(list_, low, middle - 1, target)
		else:
			return binary_search(list_, middle + 1, high, target)
	else: 
		return -1

def naive_search(list_, target):
	index = []
	for i in list_:
		if i == target: 
			index.append(list_.index(i))
	return index[0] if len(index) > 0 else -1

array = []
length = 3000000
target = 220699
while len(array) < length:
	array.append(random.randint(-3*length, 3*length))

sorted_array = sorted(array)

start = time.time()
myFunc = naive_search(sorted_array, target)
print(f'Found {target} at index {myFunc} from naive search engine' if myFunc != -1 else 'Not found from naive search engine')
end = time.time()
print(end - start,'is how long naive search engine took')

start2 = time.time()
myFunc2 = binary_search(sorted_array, 0, len(sorted_array) -1 , target)
print(f'Found {target} at index {myFunc2} from binary search engine' if myFunc2 != -1 else 'Not found from binary search engine')
end2 = time.time()
print(end2 - start2, 'is how long naive search engine took')
