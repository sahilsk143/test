s=0
n=input("enter the no")
m=n
while n >0:
     s=s*10+n%10
     n=n / 10
if m==s:
 print'no is palindrome'
else:
 print'no is not apalindrome'


