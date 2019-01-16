import random

books = ["The waling dead", "Entourage", "THe Sopranos", "The Vampire Diaries"]

for index, book in enumerate(books):
	print(book)
	print(index)

num1 = random.randrange(10)
num2 = random.randrange(10)
ans = int(num1 * num2)
your = input("{} * {} = ".format(num1,num2))
yourans = int(your)
if yourans != ans:
	print("you're wrong. Do it again")

else:
	print("Congrats")

nums1 = [8, 19, 148, 4]
nums2 = [9, 1, 33, 83]
list = []
for x in nums1:
	for y in nums2:
		list.append(x * y)

print(list)
