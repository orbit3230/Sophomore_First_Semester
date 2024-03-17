class Person() :
    def __init__(self, name, sex, job) :
        self.name = name
        self.sex = sex
        self.job = job
    def __str__(self) :
        if self.sex == 0 :
            return "His name is %s, His job is %s - str" % (self.name, self.job)
        else :
            return "Her name is %s, Her job is %s - str" % (self.name, self.job)
    def __repr__(self) :
        if self.sex == 0 :
            return "His name is %s, His job is %s - repr" % (self.name, self.job)
        else :
            return "Her name is %s, Her job is %s - repr" % (self.name, self.job)
        
person = Person("Kim Seong-Hyeon", 0, "Master of CS")
print(person)
print(repr(person))
print(str(person))
person = Person("Kim Su-Hyeon", 1, "My mom")
print(person)
print(repr(person))
print(str(person))