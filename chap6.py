# Enter your answrs for chapter 6 here
# Name: Aparna Sud 


# Ex. 6.6

def first(word): 
  return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]


# If you call a string with 2 letters, 1 letter, or a blank string '', you get '' as an output because it reads the middle letter as blank since it's not present 

def is_palindrome(word):
        if len(word) <=1:
                return "Palindrome"
        if first(word) == last(word):
               return is_palindrome(middle(word))
        else:
                return "Not palindrome"
# Ex. 6.8

def gcd(a,b):
        if b == 0:
                return a 
        else:
                r = a%b
                return gcd(b,r)
    



