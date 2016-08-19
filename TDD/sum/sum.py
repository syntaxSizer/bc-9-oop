#/usr/bin/python
x =raw_input('Enter a number y ')
y =raw_input('Enter a number x ')
def my_sum(x,y):
    '''
    a method takes to number and return the sum
    '''
    n = x+y
    return n
print my_sum(x,y)
if __name__ == '__main__':
    print 'running'
else:
    print 'imported'
