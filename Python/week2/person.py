class Person() :
    def __init__(self, name, sex, job) :
        self.name = name
        self.sex = sex
        self.job = job
    def __str__(self) :
        if self.sex == 0 :
            print("His name is %s, His job is %s" % (self.name, self.job))
        else :
            print("Her name is %s, Her job is %s" % (self.name, self.job))
        
person = Person("Kim Seong-Hyeon", 0, "Master of CS")
print(person)