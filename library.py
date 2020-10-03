b = "you are "
c = " days late so you have to pay "
d = "50 paise as fine "
e = "5 rupees as fine "
f = " days late so your regestration is cancelled "
print "welocome to the world of books "
a = int(input("enter no of days after you return the book :" ))
if a < 5 or a ==5 :
 print  str(b)+str(a)+str(c)+str(d)
if a == 6 or a < 30 and a > 6 :
  print str(b)+str(a)+str(c)+str(e)
if a > 30:
  print str(b)+str(a)+str(f)

  
print " thank you "
print " team swayam "
