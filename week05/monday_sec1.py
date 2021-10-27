###############################################################################
# Language issues
###############################################################################

# foreign language text can be included into `str`s

english = 'Computer programming is the best!!!'
chinese = '计算机编程是最好的！！！'
korean = '컴퓨터 프로그래밍이 최고입니다 !!!'
vietnamese = 'lập trình máy tính là tốt nhất !!!'
arabic = '!‏برمجة الكمبيوتر هي الأفضل!‏!‏'

# you can have the same string with multiple languages inside

combined = 'Computer 计算机 هي الأفضل tốt nhất !!!'

# variables can be named using any language

컴퓨터 = 'this is a variable'

# emojis work fine

emoji1 = '😊'
emoji2 = '💩'

# some things are weird

german = 'Strauß'

numbers = '৪৭' # In Tamil ৪ = 4 , ৭ = 7

url1 = 'https://www.BankOfAmerica.com'
url2 = 'https://www.ΒankΟfΑmerica.com'
url3 = 'https://www.BankOf​America.com'

greek = 'αβγδεζηθικλμνξοπρςστυφχψ'

empty = '​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​'

###############################################################################
# Code points
###############################################################################

# Background:
# - a "grapheme" is what Unicode calls an individual "unit" of text being displayed;
#   it's what most people would call a "letter"/"symbol"/"character"
# - a "font" is a set of pictures associated with each grapheme

# Graphemes can be composed of one or more "characters",
# and the same grapheme can be written in different ways

accents_1 = 'á'
accents_2 = 'á'
#len() funtctions displays the number of characters not the number of graphemes
#len(accents_1)==len(accents_2) is false because it is 1 == 2 respectively


# Equality in python (and all programming languages) is not based on grapheme-equivalence;
# it is based on character-equivalence

# Every character has a Unicode "code point" that represents the character.
# ord() converts from `str` to the code point
# chr() converts from the code point to `str`

accents_1a = '\xe1' # \x has range from 0-255
accents_1b = '\u00e1' #\u has range from 0-65535
accents_1c = '\U000000e1' #\U has range from 0-anything
accents_2b = 'a\u0301'
accents_2c = 'a\U00000301' # two characaters in this are: the "a" charcter and then the "add an accent mark to it" character
#the character and grapheme are the same above, but the notation is different
# the accent 1a 1b 1c have the same len 
# accents 2 b and c are the same, have the same len and character and grapheme
# accetns 1 and 2 are differnet length, but should be equal to each toehr, so use normalization

#anything that can be represented by u or x can be respresented by U

# NOTE:
# We cannot use the `\x` notation to write the character '\u0301'.
# \x only supports code points from 0-255 (1 byte);
# \u supports code points from 0-65335 (2 bytes);
# \U supports all code points (4 bytes);


# character normalization = represent the graphemes in a standard way
# normal form composed (NFC) groups graphemes into as few characters as possible
# normal form decomposed (NFD) ungroups graphemes into as many characters as possible

import unicodedata
accents_3 = unicodedata.normalize('NFC', accents_1) #converts accents 1 in to NFC form, and returns a new string, doesnt change the old string, shortens the amount of characters that represents the string
# accents 2 are in NFD form, which means decompose or enlargen the code, can have both normalized forms of strings, to then compare the multiple strings


# Example: Vietnamese

vietnamese_NFKD = 'lập trình máy tính là tốt nhất !!!'
vietnamese_NFKC = 'lập trình máy tính là tốt nhất !!!'
#length of two veitnamese things are different by 10 character length
# if you normalize the two strings, then you convert both to NFC form and then they will have the same length and grapheme quality (already have the same grapheme quality)
# Example: Arabic
# Arabic has lots of special characters, see: https://en.wikipedia.org/wiki/Arabic_script_in_Unicode

pbuh = 'ﷺ'       # "Peace be upon him"
basmala = '﷽'   # "In the name of Allah"


# PRINCIPLE 1:
# You must normalize your strings if you want to compare them. !!!!!!!!!!!!!!!

# It doesn't matter which normal form you use in your application,
# but you must pick one and use it consistently.
# Python will not normalize text for you automatically.


# Example: Korean
# Recall that sorting in python is done ASCII-betically for English text
# For non-English text, we sort "Unicode"-betically, or by the Unicode code points of text
# 
# 
# how to sort in none-english langauges: unicodebetically (THRU UNICODE)
# we can findthe unicode code point for the letters in korean using the function ord()
# for various regions: problem of sorting doesnt order correctly depending on the ordering

korean_alphabet_ROK = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ']
korean_alphabet_DPRK = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄲ', 'ㄸ']

# PRINCIPLE 2:
# It is impossible to sort text "correctly" in any programming language
# unless you know "meta" information about the user (e.g. their country).


###############################################################################
# Encoding
###############################################################################

# WHAT WE HAVE BEEN TALKING ABOUT: code point is the abstract number that represents a character, how do we actually store the information physically on the computer

# The `str` type in python is "syntactic sugar" for a list of code points.
# But how are these code points actually stored physically on the computer?

# Background:
# - a bit is a 0 or a 1
# - one byte is 8 bits
# - a byte is the fundamental unit of information in computer science
# - 8 bits is large enough to store ASCII values (end hence english values, but nothing more)

# The `byte` type looks like strings but starts with a `b`
# 8 bits = to byte to store ascii values, and became the standard
# a document with 1000 english characters, means 1000 ASCII values => 1000 BYTES

#normal strings just have quotes and raw strings that start with r outside of it
#you can compare the normal to raw strings and can be compared
#bytes are totally different from strings, even tho they look alike
# a byte actually has a sequence of 8 bits, every time you load a file in python, you are always reading bytes
#       stored as bytes on the hard drive
# bytes cant store non ascii characters, b is only for english, 
# .endcode converts the string into bytes and decode converts it back

example = b'this is a `byte`'

# NOTE:
# The type `byte` in python stores more than one byte!
# 
# The `byte` type represents a container of many bytes,
# and so is similar to a string.
# But because the `byte` type can only store 8bits,
# it cannot store non-ASCII (i.e. non-English) characters.

# >>> korean = b'컴퓨터 프로그래밍이 최고입니다 !!!'
#  File "<stdin>", line 1
# SyntaxError: bytes can only contain ASCII literal characters.

# In order to store non-English text, we need an "encoding" which maps bytes to characters
# .encode() converts from `str` to `byte`
# .decode() converts from `byte` to `str`

# The most popular encoding is UTF-8
# This is a "variable-length" encoding, which means it uses a different number of bytes for each character
# UTF-8 is popular because it "agrees" with ASCII

bytes1 = 'hello world'.encode('utf-8')
bytes2 = 'hello world'.encode('utf-16')
bytes3 = 'hello world'.encode('utf-32')
bytes4 = 'hello world'.encode('iso-8859-1')
bytes5 = 'hello world'.encode('ascii')

# formulas for increasing the amount of bytes returned
# 

# PRINCIPLE 3:
# Whenever you are working with bytes, you must know "meta" information about the encoding. WHAT is the acutall encoding, what was it created with, all of these work with any language


# Unfortunately, not all encodings support all languages/characters.
# Any encoding that begins with "utf" is safe for unicode characters.

chinese_bytes1 = '计算机编程是最好的！！！'.encode('utf-8')
chinese_bytes2 = '计算机编程是最好的！！！'.encode('utf-16')
chinese_bytes3 = '计算机编程是最好的！！！'.encode('utf-32')
#chinese_bytes4 = '计算机编程是最好的！！！'.encode('iso-8859-1')
#chinese_bytes5 = '计算机编程是最好的！！！'.encode('ascii')

# The len() reports how many bytes a `byte` consumes.

len(chinese_bytes1)
len(chinese_bytes2)
len(chinese_bytes3)

# PRINCIPLE 4:
# Some encodings are better for some languages than others.

# UTF-8 prioritizes English, but it has become the default encoding for most languages.
# This makes a lot of Asians upset because they "waste" lots of disk space/bandwidth.