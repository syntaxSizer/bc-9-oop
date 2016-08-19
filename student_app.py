from student import Student

#students objects
s1=Student('Emmanuel','Ouday','SD')
s2=Student('Kelvin','Luai')
s3=Student('Karen','Dry')
s4=Student('Judith','Salh')
s5=Student('blessing','Mummy')
s6=Student('sam','Kantara')
s7=Student('George','Intiga')
s8=Student('morena','sarah')
s9=Student('vigur','athis')
s10=Student('Grace','John')
s11=Student('Titus','kayla')
    
# students who attended class
s1.attend_class(date='Thu Aug 17 22:54:52 2016')
s2.attend_class(date='Thu Aug 18 22:54:52 2016')
s3.attend_class(date='Thu Aug 18 22:54:52 2016', teacher='Ozil')
s4.attend_class(date='Thu Aug 18 22:54:52 2016', teacher="Samer")
s5.attend_class(date='Thu Aug 18 22:54:52 2016', teacher='Tutti')
    
print(s1.specific_day_attendees(date='Thu Aug 17 22:54:52 2016'))
print(s2.specific_day_attendees(date='Thu Aug 17 22:54:52 2016'))
