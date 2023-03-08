class Student:

    def __init__(self, id, code, firstName, lastName, dob, math, physics, chemistry):
        self.id = id
        self.code = code
        self.fistName = firstName
        self.lastName = lastName
        self.dob = dob
        self.math = math
        self.physics = physics
        self.chemistry = chemistry

    def getStudentInfor(self):
        print('Id: ' + self.id)
        print('Name: ' + self.fistName + " " + self.lastName)
        print('Dob: ' + self.dob)
        print('Toan: ' + str(self.math))
        print('Ly: ' + str(self.physics))
        print('Hoa: ' + str(self.chemistry))


def createTableStudents(mydb, cursor):
    mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS Students ( 
                                 id int(11) NOT NULL AUTO_INCREMENT,
                                 code varchar(250) NULL ,
                                 first_name varchar(250) NULL,
                                 last_name varchar(250) NULL,
                                 dob varchar(250) NULL,
                                 math float NULL,
                                 physics float NULL,
                                 chemistry float NULL,
                                 PRIMARY KEY (id)) """
    cursor.execute(mySql_Create_Table_Query)
    mydb.commit()
    print("Students created")
