

class Coach
name = 'Johnson'
email = 'johnsonemail'
sport = 'football'

    def Login(self):
        entryName = input('Name here')
        entryFacultyEmail = input('email here')
        if entryName == self.email and entryFacultyEmail == self.email):
            print('welcome back []'.format(entryName))
        else :
            print('no')
        

class Athlete(Coach):
    GPA = 1.5
    Honors = False

     def Login(self):
        entryName = input('Name here')
        entryStudentEmail = input('email here')
        if entryName == self.email and entryStudentEmail == self.email):
            print('welcome back []'.format(entryName))
        else :
            print('no')

    
    
class Parent(Coach):
    mailing_list = True
    donated = True

     def Login(self):
        entryName = input('Name here')
        entryParentEmail = input('email here')
        if entryName == self.email and entryParentEmail == self.email):
            print('welcome back []'.format(entryName))
        else :
            print('no')
