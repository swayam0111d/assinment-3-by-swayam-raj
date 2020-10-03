a = int(input( "please enter 1st side of triangle " ))
b = int(input( "please enter 2nd side of triangle " ))
c = int(input( "please enter 3rd side of triangle " ))
d = a**2
e = b**2
f = c**2
if a == b and a == c and b==c :
 print " it is a equilateral triangle "
if a ==b!=c or a==c!=b or c==b!=a:
    print "it is isosceles triangle "
if a!=b!=c :
    print "it is a scalen triangle"
if d + e == f or e + f == d or f + d == e :
 print "and it is also a right angled triangle "


print "thanks"
print "team swayam"
