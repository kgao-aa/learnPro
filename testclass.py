# i define a class as a base class to be extended by chinese_student 
class student(object) :
    def __init__(self,name,subname):
        self.name = name           
	self.subname = subname 
        print 'this is the base class instance of a student'
    def study(self):
        print 'I want to study, study makes me happy'
   #  play = 'blizard' # define a attribute for the class and it will be used as  a class member
# another class that need to be extended by chinese_student 
class boy(object):
    def __init__(self,name,sex):
	self.name = name 
	self.sex = sex
    def play(self):   # I define this for the instance of chinese_student to use without having it in the chinese_student
	print 'I like to play overwatch'
class chinese_student(student,boy):
    def __init__(self,name,subname):
	self.name = name 
	self.subname = subname
	print 'I am a chinese student and I hate studying'
    def study(self):  # I overide the study func inheritance from student 
	print 'I don\'t want to study'
    keyword = 'entrance examination of collage'
student1 = student ('gao','keqing')
boy1 = boy('gaopp','male')
gaokeqing = chinese_student('gao','keqing')
print student1.name 
student1.study()
#print student1.play
print boy1.name
boy1.play()
gaokeqing.play()      # a surprise finding when I call this func without unable the attribute in the student class it will
# cause a exception you can try I think it's the unperfect part of python
gaokeqing.study()     
print chinese_student.keyword

