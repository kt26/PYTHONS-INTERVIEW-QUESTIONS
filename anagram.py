def anagram_check():	
	a = input("Enter first string: ")
	b = input("Enter second string: ")


	count = {}

	a = a.replace(" ","").upper()
	b = b.replace(" ","").upper()

	if a==b:
		return True

	if len(a)!=len(b):
		return False


	for letter in a:
		if letter in count.keys():
			count[letter] +=1
		else:
			count[letter] = 1


	for letter in b:
		if letter in count.keys():
			count[letter] -=1
		else:
			count[letter] = 1

	for elements in count.value():
		if element != 0:
			return False

	return True


print(anagram_check())
