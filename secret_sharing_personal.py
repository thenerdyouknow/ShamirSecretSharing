import random

class ShamirSecret:
	def __init__(self,secret,threshold,total_shares):
		self.threshold = threshold
		self.secret = secret
		self.first_zero_bit = False
		self.total_shares = total_shares

	def converting_to_ascii(self):
		complete_ascii_string = ''
		for each_letter in self.secret:
			padded_number = str(ord(each_letter)).zfill(3)
			complete_ascii_string += padded_number
		if(complete_ascii_string[0]=='0'):
			self.first_zero_bit = True
			self.secret = int(complete_ascii_string[1:])
		else:
			self.secret = int(complete_ascii_string)

	def constructing_polynomial(self):
		polynomial_list = []
		for i in range(self.threshold-1):
			random_number = random.randint(10,100)
			polynomial_list.append(random_number)
		polynomial_list.append(self.secret)
		return polynomial_list

	def compute_shares(self):
		self.converting_to_ascii()
		share_polynomial = self.constructing_polynomial()
		all_shares = []
		for i in range(1,self.total_shares+1):
			exponent = self.threshold - 1
			temporary_share = 0
			for each_coeff in share_polynomial:
				temporary_share += each_coeff * (i**exponent)
				exponent -= 1
			all_shares.append((i,temporary_share))
		return all_shares

	def lagrange_interpolation(self,x_values,y_values):
		k = self.threshold
		outer_sum = 0
		for j in range(0,k): #Using the formula from Wikipedia(the computationally efficient approach):https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing
			fx_for_j = y_values[j] 
			inner_sum = 1
			for m in range(0,k):
				if(m != j):
					inner_sum *= (x_values[m])/(x_values[m]-x_values[j])
			outer_sum += fx_for_j * inner_sum
		return int(outer_sum)

	def reconstructing_secret(self,shares_provided):
		if(len(shares_provided)<self.threshold):
			return 'Not enough shares to reconstruct the secret!'
		x_values = [each_tuple[0] for each_tuple in shares_provided]
		y_values = [each_tuple[1] for each_tuple in shares_provided]
		reconstructed_secret = self.lagrange_interpolation(x_values,y_values)
		return reconstructed_secret

threshold_shares = 3
total_shares = 6
plaintext_secret = input('Secret to be encoded :')
finding_shares = ShamirSecret(plaintext_secret,3,6)
shares = finding_shares.compute_shares()
recovered_secret = finding_shares.reconstructing_secret(shares[0:3])
