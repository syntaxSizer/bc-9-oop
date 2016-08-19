#/usr/bin/python
def my_sum(x,y):
    '''
    a method takes to number and return the sum
    '''
    if isinstance(x,int) and isinstance(y,int):
       n = x+y
       return n
    raise TypeError
print my_sum(2,8)
if __name__ == '__main__':
    print 'running'
else:
    print 'imported'
