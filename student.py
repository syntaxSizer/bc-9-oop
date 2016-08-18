#/usr.bin.python
from datetime import datetime 
class Student(object):
    count =0
	def __init__(self, first_name, last_name,id_number, location = 'Hogwarts',date):
		count +=1
		self.first_name = first_name
		self.last_name = last_name
		self.__id_number = Student.count
		self.date = datetime.today()
		# generate unique id
	def attend_class(self, **kwargs):
		'''
	    default values:
	    loc = ''Hogwarts	
	    date = current_date
	    teacher = 'Alex'
	    '''
	    pass
s1 = Student('kevin','Chiteri','UG')
s1 = Student('Allan','M.','UG')
