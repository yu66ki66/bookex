ex = "Camus"

print(ex[0])
print(ex[1])
print(ex[2])
print(ex[3])
print(ex[4])

#challenge 2

thing = input("what did you write?")
name = input("who did you write for?")

print("I wrote a {}. I sent it to {}!".format(thing,name))

print("aldous Huxley was born in 1894.".capitalize())

#challenge 4
ex4 = "where now? Who now? When now?"
print(ex4.split("?"))

#challenge 5
list = ["The","fox","jumped","over","the","fense","."]
sentence = " ".join(list)
print(sentence[0:-2] + ".")

#challenge 6
sentence6 = "A screaming comes across the sky"

print(sentence6.replace("s","$"))

#challenge 7

print("Hemingway".index("m"))

#challenge 10

quote = "It was a bright cold day in April, and the clocks were striking thirteen."

num = quote.index(",")
print(quote[:num+1])
print(quote[num+1:])