def ln(n:int=0,text:str=''):
    if text!='':
        print(f"{text}{'\n' * n}")
    else:
        print(f"{'\n' * (n-1)}")
    
def main():

    testString='aaaaaaaaaaaaaaaaa'
    testNotString = [7,4,2]
    testDict = {'key':'val', 'key2':5}
    ln(text='test')# if you're doing this, you should be using print()
    print('...............')
    ln(5,'test')
    print('...............')
    ln()
    print('...............')
    ln(3)
    print('...............')
    ln(5,testString)
    print('...............')
    ln(5,testNotString)
    ln(3,testDict)
    
if __name__=="__main__":
    main()