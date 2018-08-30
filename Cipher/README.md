Ciphers homework

This is a program that can use command to encrypt or decrypt a file
Option flags to select the algorithm to use for encryption or decryption
Implement at least a total of 5 different cipher types:
    
    Caesar cipher
    Simple substitution cipher
    Poly-alphabetic cipher
    Transposition cipher
    Zigzag cipher

Command line tool that take flags and input file and output file
Different flag will use different cipher and encrypt a file

Developing on Python 3.6.3

Libraries:
  1. argparse: use for parse argument on command line
  2. click: a quick way to parse argument on command line
  
'--cipher', '-c', 'cipher_name', for different cipher
'--key', '-k', for different keys
'--dtype', '-d', 'dist_name', for different dist
'-h', a good way to look at the help and usage message

References:
  "Manual of Cryptography", 1911, page 28
  
  http://practicalcryptography.com/ciphers/caesar-cipher/
  
  https://learncryptography.com/classical-encryption/caesar-cipher
  
  https://www.xarg.org/tools/caesar-cipher/
  
  http://crypto.interactive-maths.com/caesar-shift-cipher.html
  
  "The Mathamatical Theory of Cryptography", 1945, pages 31-32
  
  https://www.simonsingh.net/The_Black_Chamber/substitutioncrackingtool.html
  
  http://practicalcryptography.com/ciphers/simple-substitution-cipher/
  
  http://rumkin.com/tools/cipher/substitution.php
  
  https://www.britannica.com/topic/substitution-cipher
  
  "Friedman Lectures on Cryptography", 1965, page 29
  
  https://inventwithpython.com/hacking/chapter19.html
  
  https://www.geeksforgeeks.org/vigenere-cipher/
  
  
  http://www.codingalpha.com/polyalphabetic-cipher-c-program/
  
  https://www.khanacademy.org/computing/computer-science/cryptography/crypt/p/polyalphabetic-exploration
  
  "Manual of Cryptography", 1911, page 21.
  
  http://crypto.interactive-maths.com/simple-transposition-ciphers.html
  
  https://www.dcode.fr/transposition-cipher
  
  https://inventwithpython.com/hacking/chapter8.html
  
  https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_transposition_cipher.htm
  
  "Manual of Cryptography", 1911, page 21-22.
  
  http://marshallfoundation.org/library/wp-content/uploads/sites/16/2014/09/WFFvol05watermark.pdf
  
  http://crypto.interactive-maths.com/rail-fence-cipher.html
  
  https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/
  
  https://www.daniweb.com/programming/software-development/threads/78106/how-to-create-a-zig-zag-encryption
