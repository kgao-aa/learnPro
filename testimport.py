# this is a test for usage of 'the __name__ == "__main__"'  ,in python we can just excute the func without put it in the 
# main func so and the python provide a simliar way to act like the C and C++ ,we can define the func upside the setance 
#'if __name__ == '__main__' :' and put the calling logic under it , it will act as the main func. remember that the calls
#of a func will excute anyway whether you put it under the 'if __name__ == "__main__" :' or above it but when you import 
#a moduel the only the code that is above the 'if __name__ == "__main__" :' will be included. 
import testmainmoduel
import testmoduelwithoutmain
print testmainmoduel.compute(4)
def main():
    print 'you are too simple'
if __name__ == "__main__" :
    print 'dadadadddddaa'
    main()
