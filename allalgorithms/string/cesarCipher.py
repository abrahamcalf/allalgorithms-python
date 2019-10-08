# String Algorithms
# Contributed by: JordaoA
#Cesar Cipher implemented in python

class cipher():
	#Constructor method
	def __init__(self,posCipher,jump):
		self.letters = ["A","B","C","D","E",
			"F","G","H","I","J","K","L",
			"M","N","O","P","Q","R","S",
			"T","U","V","W","X","Y","Z"] #Alphabet in UPPERCASE
		self.posCipher = posCipher #encrypted word
		self.jump = jump #jump between the letters

	#Method responsible for ignore the case of all letters of the word  
	def ignoreCase(self):
		newPosCipher = ""

		for i in range(len(self.posCipher)):
			newPosCipher += self.posCipher[i].upper()
		
		self.posCipher = newPosCipher #transforming the old word 

	#Method responsible for search index of each letter of the word in the alphabet
	def returnIndex(self,element, listOfLetters):
		index = 0 #letter index
		
		for i in range(len(listOfLetters)):
			if element == listOfLetters[i]:
				index = i
				break

		return index
	
	#Method responsible for deciphering the word given by the user according to the letter jump
	def cipherC(self):

		self.ignoreCase()
		preCipher = "" #decipher word
		
		for j in range(len(self.posCipher)):
			index = self.returnIndex(self.posCipher[j], self.letters)

			if (index - self.jump) > 25:
				preCipher += self.letters[(index - self.jump) % 26]
			
			else:
				preCipher += self.letters[(index - self.jump)]
		
		return preCipher
