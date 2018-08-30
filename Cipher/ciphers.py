'''
	Assignment name: ciphers.py
    
    A python command-line program to encrypt or deccrypt a text file.
    
    Usage: ciphers.py COMMAND [OPTIONS] [ARGS]...
    
    Commands:
        decrypt  Decrypt a file using selected algorithm:...
        dist     Calculate frequency distributions of symbols...
        encrypt  Encrypt a file using selected algorithm:...
        list     List the available ciphers
    
    Help for each command is avaible:
        ciphers.py COMMAND -h
          
    Example usage:
    
    $./ciphers.py encrypt -k none -c caesar ../test_text/midsummers_night.md temp
      caesar cipher encrypted text placed in file 'temp'
    
    @author Tao Guo
'''

import argparse
import click

""" 
    In the Caesar cipher, "each letter of the text is replaced
    by the letter which stands a certain number of places
    before or after it in the alphabet".
    Sources:
        "Manual of Cryptography", 1911, page 28
        http://practicalcryptography.com/ciphers/caesar-cipher/
        https://learncryptography.com/classical-encryption/caesar-cipher
        https://www.xarg.org/tools/caesar-cipher/
        http://crypto.interactive-maths.com/caesar-shift-cipher.html
"""
class Caesar_cipher(object):

	def __init__(self, key):
		self.key = key
		
	def caesar_cipher(text):

		while True:
			print("Please enter a key to start: ")
			key = int(input())
			if (key > 26 or key < 1):
				print("Invailad key, please try again")
			else:
				return key

	def encrypt(self, input_file, output_file):
		""" 
			Encrypt a simple substitution cipher.
		"""
		key = self.getKey()
		for l in input_file:
			result = l
			if l.isalpha():
				l = l.upper()
				result = chr(ord(l) + key)
			file.write(result)

	def decrypt(self, cipher_text):
		""" 
			Decrypt a simple substitution cipher.
		"""
		ct = self.preprocess(cipher_text)
		plain_text = []

		for symbol in ct:
			plain_text.append( self.decode_dict[ symbol ] )

		return ''.join(plain_text)

"""
	"In this cipher each letter of the message is replaced by 
	a fixed substitute, usually also a letter. Thus the message 
		M = m1 m2 m3 m4 ...
	becomes
		E = e1 e2 e3 e4
		= f(m1) f(m2) f(m3) f(m4)...
	where the function f(m) is function with an inverse. The key is
	a permutation of the alphabet(when the substitutes are letters."
	
	Sources:
		"The Mathamatical Theory of Cryptography", 1945, pages 31-32
		https://www.simonsingh.net/The_Black_Chamber/substitutioncrackingtool.html
		http://practicalcryptography.com/ciphers/simple-substitution-cipher/
		http://rumkin.com/tools/cipher/substitution.php
		https://www.britannica.com/topic/substitution-cipher

"""
class simple_substitution_cipher():

	key = 3

	def __init__(self, key):
		self.key = key

	def encrypt(self, input_file, output_file):
		""" 
			Encrypt a simple substitution cipher.
		"""
		key = self.getKey()
		for l in input_file:
			result = l
			if l.isalpha():
				l = l.upper()
				result = chr(ord(l) + key)
			file.write(result)

	def decrypt(self, cipher_text):
		""" 
			Decrypt a simple substitution cipher.
		"""
		ct = self.preprocess(cipher_text)
		plain_text = []

		for symbol in ct:
			plain_text.append( self.decode_dict[ symbol ] )

		return ''.join(plain_text)


"""
	Also called The Vigenère Cipher.
	"It consists of a set of twenty-six alphabets successively displaced 
	one letter per row, with the plaintext letters at the top of the square, 
	the key letters at the side, and the cipher letter inside."

	Sources:
	        "Friedman Lectures on Cryptography", 1965, page 29
	        https://inventwithpython.com/hacking/chapter19.html
	        https://www.geeksforgeeks.org/vigenere-cipher/
	        http://www.codingalpha.com/polyalphabetic-cipher-c-program/
	        https://www.khanacademy.org/computing/computer-science/cryptography/crypt/p/polyalphabetic-exploration

"""
class poly_alphabetic_cipher():

	def __init__(self):
        None

	def encrypt(self, plaintext, key):
		key = key.upper().replace(' ', '')
		plaintext = plaintext.upper().replace(' ', '')
		ciphertext = ''
		j = 0
		for i in range(len(plaintext)):
			ciphertext += chr((((ord(key[j]) - 65) + (ord(plaintext[i])) - 65) % 26) + 65)
			i += 1
			j += 1
			if j >= len(key):
				j = 0
		return ciphertext

	def decrypt(self, ciphertext, key):
		key = key.upper().replace(' ', '')
		plaintext = ''
		j = 0
		for i in range(len(ciphertext)):
			plaintext += chr((((ord(ciphertext[i]) - 65) - (ord(key[j]) - 65)) % 26) + 65)
			i += 1
			j += 1
			if j >= len(key):
				j = 0
		return plaintext


"""
	"In this cipher lines containing a certain number of letters 
	are agreed upon, and the message is then wrriten out in lines 
	of this lines."

	Sources:
        "Manual of Cryptography", 1911, page 21.
        http://crypto.interactive-maths.com/simple-transposition-ciphers.html
        https://www.dcode.fr/transposition-cipher
        https://inventwithpython.com/hacking/chapter8.html
        https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_transposition_cipher.htm

"""
class transposition_cipher():
	def split_len(seq, length):
		return [seq[i:i + length] for i in range(0, len(seq), length)]
	def encode(key, plaintext):
		order = {
			int(val): num for num, val in enumerate(key)
			}
	ciphertext = ''

	for index in sorted(order.keys()):
		for part in split_len(plaintext, len(key)):
			try:ciphertext += part[order[index]]
				except IndexError:
					continue
		return ciphertext



""" 
	The Zigzag cipher transposes symbols in the plaintext
        by first writing the characters down the first column,
        then up the next column, then down the third and
        so forth filling out a grid. The plaintext is made by reading
        the grid rows left-to-right/top-to-bottom.
        
        Cipher taken from:
          "Manual of Cryptography", 1911, page 21-22.
          http://marshallfoundation.org/library/wp-content/uploads/sites/16/2014/09/WFFvol05watermark.pdf
          http://crypto.interactive-maths.com/rail-fence-cipher.html
          https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/
          https://www.daniweb.com/programming/software-development/threads/78106/how-to-create-a-zig-zag-encryption
"""
class zigzag_cipher():

	def __init__(self, key):
		try:
			h, w = key.split('x')
			height, width = int(h), int(w)
		except:
			raise ValueError( "Illegal key of of {} for Zigzag transposition cipher".format(key) )

		self.transposition_permutation = range(width * height)
		for x in range(width):
			for y in range(height):
				if x % 2:           # x odd, zig up
					y_ = height - y - 1
				else:
					y_ = y          # x even, zig down
				index = y_*width + x
				self.transposition_permutation[index] = x*height + y

cipher_list = (Caesar, Stencil, Zigzag) # explicit list of supported ciphers
cipher_name_list = [ Cipher.__name__.lower() for Cipher in cipher_list]
# dictionary of lower case name to Cipher using name introspection of class
cipher_dict = { Cipher.__name__.lower() : Cipher for Cipher in cipher_list }

# collect all distribution routines for cli usage
dist_dict = {'mono':Monograph, 'di':Digraph, 'tri':Trigraph, 'ng':Ngraph}
dist_name_list =[ key for key in dist_dict]

@click.version_option(0.1)

@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.pass_context     # ctx
def cli(ctx):
    """ A tool to encrypt or decrypt a file using simple ciphers. """
    pass

@cli.command()
@click.option('--cipher', '-c', 'cipher_name', type=click.Choice( cipher_name_list ) )
@click.password_option('--key', '-k')
@click.argument('input_file', type=click.File('rb'))
@click.argument('output_file', type=click.File('wb'))
def encrypt(cipher_name, key, input_file, output_file):
    """ Encrypt a file using selected algorithm:
            crypt [OPTIONS] encrypt <in_file> <out_file>
    """
    Cipher = cipher_dict[cipher_name] # instantiate class from dictionary
    cipher = Cipher(key)
    plain_text = input_file.read()

    cipher_text = cipher.encrypt( plain_text )

    output_file.write( cipher_text )
    output_file.write("\n")

@cli.command()
@click.option('--cipher', '-c', 'cipher_name', type=click.Choice( cipher_name_list ) )
@click.password_option('--key', '-k')
@click.argument('input_file', type=click.File('rb'))
@click.argument('output_file', type=click.File('wb'))
def decrypt(cipher_name, key, input_file, output_file):
    """ Decrypt a file using selected algorithm:
            crypt decrypt [OPTIONS] <in_file> <out_file>
             -k   key
             -c   cipher name
    """
    Cipher = cipher_dict[ cipher_name ] # instantiate class from dictionary
    cipher = Cipher( key )
    cipher_text = input_file.read()

    plain_text = cipher.decrypt( cipher_text )

    output_file.write( plain_text )
    output_file.write("\n")

@cli.command()
def list():
    """ List the available ciphers that may be invoked with the -c option.
    """
    click.echo( "The following {} ciphers are supported:".format( len(cipher_list)))
    for cipher in cipher_list:
        base_class_name = cipher.__bases__[0].__name__.replace("_", " ")
        click.echo( "    {} - {}".format( cipher.__name__.lower(),
                                          base_class_name ))

@cli.command()
@click.option('--dtype', '-d', 'dist_name', type=click.Choice( dist_name_list ) )
@click.argument('input_file', type=click.File('rb'))
@click.argument('output_file', type=click.File('wb'))
def Dist(dist_name, input_file, output_file):
    """ Calculate frequency distributions of symbols in files.
    """
    D = dist_dict[dist_name]
    dist = D()
    text = input_file.read()

    dist.analyze(text)

	output_file.write(dist.to_readable())

if __name__ == '__main__':
	
	# parser = argparse.ArgumentParser()
	# parser.add_argument('-h', help='help')
	# args = parser.parse_args()

	# parser = argparse.ArgumentParser(prog='ciphers')
	# parser.add_argument('-encrypt', '-decrypt', help='Encrypt or decrypt mode')
	# parser.add_argument('-caesar', '-substitution', '-poly', help='foo2 of the %(prog)s program')
	# args = parser.parse_args()

	cli()