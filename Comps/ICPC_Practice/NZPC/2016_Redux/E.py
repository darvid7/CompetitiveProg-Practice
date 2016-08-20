# correct :D

key = int(input())

string = input()

output = ""

upper_lim = 25

cipher_value = key

for char in string:
	if ord(char) >= 97 and ord(char) <= 122:
		rep = ord(char)
		# to decrypt it - chiper_value
		decrypted_rep = rep - cipher_value

		if decrypted_rep > 122:
			decrypted_rep = (decrypted_rep % 122) + 97

		elif decrypted_rep < 97:
			"""
			explanation of the +1 part
			if I want to represent 'z' I need decrypted_rep = 122
			to get this wlithout the +1 you need 97 - ? =
			97 - 97 = 0, but that is for 'a' and the condition is < 97
			so if decrypted_rep = 96, then you want to loop around and represent 'z' which is 122
			which is 122 +1 -1 or 123 - 1 which is 123 - (97-decrypted)
			if we get here we know that the result has to have the chance to be 122 (so can't be 122 -x) thus
			123 - x will give the chance to be 'z'
			"""
			while(decrypted_rep < 97):
				decrypted_rep = 122 +1 - ( 97 - decrypted_rep )
				#decrypted_rep = decrypted_rep % 97

		#print(str(char) + " to " + str(decrypted_rep) + ": " + chr(decrypted_rep) + " -- " + str(cipher_value))
		decrypted_char = chr(decrypted_rep)

		output += decrypted_char

		cipher_value += 1

		if cipher_value > 25:
			cipher_value = cipher_value % 25
	else:
		output += char
print(output)