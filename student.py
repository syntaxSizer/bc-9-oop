#/usr/bin/python
import time
class Student(object):
    country = {
        'KE': 'Kenya',
        'NG': 'Nigeria',
        'UG': 'Uganda',
        'TZ': 'Tanzania',
        'SD': 'Sudan'
        }
    class_list=[]
    Id=0
    def __init__(self,fName,lName,cc="KE"):
        Student.Id+=1
        self.id=Student.Id
        self.fName=fName
        self.lName=lName
        self.applcant_country = Student.country[cc]

    def attend_class(self, **kwargs):
        self.loc=kwargs.setdefault('loc','Hogwarts')
        self.date=kwargs.setdefault("date", time.strftime("%c"))
        self.teacher=kwargs.setdefault('teacher','alex')
        Student.class_list.append((self.date,self.fName,self.lName,self.id,self.loc,self.teacher,self.applcant_country))
      
   
    def specific_day_attendees(self, date=time.strftime("%c")):
        for item in Student.class_list:
            if item[0]==date:
                print(item)

