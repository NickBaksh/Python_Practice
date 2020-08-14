z = [0, 1, 2, 3, 4, 2.3, 3.5, 5, 29, 34, 45, 66, 78, 89, 101, 145, 134] # input list
a = [a for a in z if a < (5)] # find numbers less then 5
for man in a: 
	print (man)
print ()	
print (a)
print ()
g = float (input ("Enter num: ", ))	
a = [a for a in z if a < (g)]
print (a) # print list less then ur num