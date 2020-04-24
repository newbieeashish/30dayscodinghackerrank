"""
In this challenge, we're going to learn about the difference between a class and an instance;
because this is an Object Oriented concept, it's only enabled in certain languages.
Task
Write a Person class with an instance variable, age, and a constructor that takes an integer, initial_age, as a parameter.
The constructor must assign initial_age to _age after confirming the argument passed as _initial_age is not negative.
If a negative argument is passed as initial_age, the constructor should set to and print "Age is not valid, setting age to 0."
In addition, you must write the following instance methods:
	age_1_year() should increase the instance variable _age by 1.
	is_old() should perform the following conditional actions:
		If age < 13, print "You are young.".
		If age >= 13 and age < 18, print "You are a teenager.".
		Otherwise, print "You are old.".
"""


class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self._age = 0
        else:
            self._age = initialAge
        # Add some more code to run some checks on initialAge

    def amIOld(self):
        if self._age < 13:
            print('You are young.')
        elif ((13 <= self._age) and (self._age < 18)):
            print('You are a teenager.')

        else:
            print('You are old.')
        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        # Increment the age of the person in here
        self._age += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")


"""
Objective
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.
Task
Given an integer, N, print its first 10 multiples.
Each multiple N * i (where 1 <= i <= 10) should be printed on a new line in the form:
N x i = result.
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    for i in range(1,11):
        print('{0} x {1} = {2}'.format(n,i,n*i))


'''
"""
Objective
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops.
Task
Given a string, S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters
as 2 space-separated strings on a single line.
Note: 0 is considered to be an even index.
"""
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input().strip())

for i in range(0,T):
    S = input()
    even,odd = S[::2],S[1::2]
    print(even+' '+odd)

"""
Objective
Today, we're learning about the Array data structure.
Task
Given an array, A, of N integers, print A's elements in reverse order
as a single line of space-separated numbers.
"""

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    rarr = map(str, arr[::-1])
    print(" ".join(rarr))

"""
Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure.
Task
Given N names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers. You will then be given an unknown number of names
to query your phone book for; for each name queried, print the associated entry from
your phone book (in the form name=number) or Not found if there is no entry for name.
Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""
import sys
inputList=[]

for line in sys.stdin:
    inputList.append(line)

n = int(inputList[0])
entries = inputList[1:n+1]
queries = inputList[n+1:]

phoneBook = {}

for entry in entries:
    name, id = entry.split()
    phoneBook[name] = id

for query in queries:
    stripQuery = query.rstrip() #Eliminates the newline character
    if stripQuery in phoneBook:
        print(stripQuery + "=" + str(phoneBook[stripQuery]))
    else:
        print("Not found")

'''factorial rec'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()


''''Given a base- integer,10 , convert it to binary (base-2). 
Then find and print the base-10 integer denoting the maximum 
number of consecutive 1's '
in n's binary representation.'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

max_one_count = 0
one_count = 0

while n!=0:
    factor = n//2
    remainder = n-2 * factor
    n = factor
    if remainder == 1:
        one_count += 1
        max_one_count = max(max_one_count,one_count)
    else:
        one_count = 0
print(max_one_count)


'''2D array Hourglass max sum'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

smax = -9 * 7

for row in range(len(arr) - 2):
    for column in range(len(arr[row]) - 2):
        tl = arr[row][column]
        tc = arr[row][column + 1]
        tr = arr[row][column + 2]
        mc = arr[row + 1][column + 1]
        bl = arr[row + 2][column]
        bc = arr[row + 2][column + 1]
        br = arr[row + 2][column + 2]
        s = tl + tc + tr + mc + bl + bc + br
        smax = max(s, smax)

print(smax)

'''inheritance '''

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName, idNumber,scores):
        super().__init__(firstName,lastName,idNumber)
        self.scores = scores

    def calculate(self):
        a = sum(self.scores)/len(self.scores)
        if a<40:
            return 'T'
        elif (40 <= a) and (a < 55):
            return "D"
        elif (55 <= a) and (a < 70):
            return "P"
        elif (70 <= a) and (a < 80):
            return "A"
        elif (80 <= a) and (a < 90):
            return "E"
        elif (90 <= a) and (a <= 100):
            return "O"
        else:
            return ""

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())


'''abstract class'''

from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(): pass


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()


'''Scope'''

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        l = len(a)
        for i in range(0, l):
            for j in range(i + 1, l):
                difference = abs(a[i] - a[j])
                self.maximumDifference = max(difference, self.maximumDifference)


'''linkedlist'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):

        if head is None:
            head = Node(data)

        else:
            current = head
            while (current.next is not None):
                current = current.next
            current.next = Node(data)
        return head
    # Complete this method


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);

''':exception'''

#!/bin/python3

import sys


S = input().strip()

try:
    i = int(S)
    print(i)

except ValueError:
    print("Bad String")

'''more exceptions'''

#Write your code here
class Calculator:
    def power(self,n,p):
        if (n<0) or (p<0):
            raise Exception ("n and p should be non-negative")

        else:
            return n**p


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)


'''stack and queue'''

import sys


class Solution:

    def __init__(self):
        self.__stack = []
        self.__queue = []

    def pushCharacter(self, ch):
        self.__stack.append(ch)

    def enqueueCharacter(self, ch):
        self.__queue.insert(0, ch)

    def popCharacter(self):
        return self.__stack.pop()

    def dequeueCharacter(self):
        return self.__queue.pop()
    # Write your code here


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
import sys


class Solution:

    def __init__(self):
        self.__stack = []
        self.__queue = []

    def pushCharacter(self, ch):
        self.__stack.append(ch)

    def enqueueCharacter(self, ch):
        self.__queue.insert(0, ch)

    def popCharacter(self):
        return self.__stack.pop()

    def dequeueCharacter(self):
        return self.__queue.pop()
    # Write your code here


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")


'''interface'''

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        s = 0
        for i in range(1,n+1):
            if(n%i==0):
                s+=i
        return s


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)


'''no of swaps to sort'''

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
no_swaps = 0

for i in range(0,n):
    for j in range(0,n-1):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j]= a[j+1]
            a[j+1] = temp
            no_swaps +=1
    if (no_swaps == 0):
        break

print( "Array is sorted in " + str(no_swaps) + " swaps." )
print( "First Element: " + str(a[0]) )
print( "Last Element: " +  str(a[n-1]) )


'''max height of tree'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root is None or (root.left is None and root.right is None):
            return 0
        else:
            return max(self.getHeight(root.left),self.getHeight(root.right))+1
        #Write your code here

T=int(input())

'''BST level order traversal'''

import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        output = ''
        queue = [root]
        while queue:
            current = queue.pop(0)
            output += str(current.data) + " "
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        print(output[:-1])


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)


'''remove duplicates from linkedlist'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        current = head
        while (current.next):
            if (current.data == current.next.data):
                current.next = current.next.next

            else:
                current = current.next

        return head

        # Write your code here


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head);

'''Prime time complexity'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def check_prime(num):
    if num is 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x is 0:
            return "Not prime"
    return "Prime"

t = int(input())
for i in range(t):
    number = int(input())
    print(check_prime(number))


'''nested logic - fine'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
d, m, y = input().split(' ')
d = int(d)
m = int(m)
y = int(y)
de, me, ye = input().split(' ')
de = int(de)
me = int(me)
ye = int(ye)
fine = 0
if(ye==y):
    if(me < m):
        fine = (m - me) * 500
    elif((me == m) and (de < d)):
        fine = (d - de) * 15
elif(ye < y):
    fine = 10000

print( fine )

''''testing'''


def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx


class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        return []


class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        return [7, 4, 3, 8, 14]

    @staticmethod
    def get_expected_result():
        return 2


class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        return [7, 4, 3, 8, 3, 14]

    @staticmethod
    def get_expected_result():
        return 2


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")

'''regex'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        match = re.search(r'[\w\.-]+@gmail.com',emailID)

        if match:
            names.append(firstName)
    names.sort()
    for name in names:
        print(name)

'''Bitwise AND'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(k-1 if ((k-1) | k) <= n else k-2)


