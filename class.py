class Parent ():
	def __init__(self,age,name):
		self.name =name 
		self.age = age
		#size is a integer representing height 
	
		
	def birthday  (self,volume):
		# volume is a integer 
		#if volume is greater than 1 , print in all caps 
		if volume > 1:
			print ("MEOW MEOW")
		else:
			print ("meow meow")
class Baby (Parent):
	def __init__ (self,age,name,birthday):
		self.birthday= birthday 
		Parent.__init__ (self,age,name)
		
parent = Parent(25,"lilly")
baby = Baby (1,"clowe","aug.1")


print(parent.name)
print (parent.age)
print (baby.name)
print (baby.birthday)
print (baby.age)