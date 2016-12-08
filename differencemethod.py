class test:
    def local_method(self):
        print 'I am a local method'
    @classmethod
    def class_method(cls):
	print 'I am a class method'
    @staticmethod
    def static_method():
	print 'I am a static method'
test().local_method()
test().class_method()
test().static_method()

