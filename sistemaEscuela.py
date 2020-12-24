from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
Base = declarative_base(engine)


class Teacher(Base):
    """ Class for Teacher
    """
    __tablename__ = 'teacher'
    id = Column(Integer, Sequence('teacher_seq_id'), primary_key=True)
    nameTeacher = Column(String)
    lastTeacher = Column(String)
    teacher_course = relationship("Time", back_populates='course_teacher')

    def __repr__(self):
        return'{}{}'.format(self.nameTeacher, self.lastTeacher)


class Course(Base):
    """ Class for Course
    """
    __tablename__ = 'course'
    id = Column(Integer, Sequence('curso_seq_id'), primary_key=True)
    nameCourse = Column(String)
    stud = relationship("Student", back_populates='courses')
    time_course = relationship("Time", back_populates='curso_hora')

    def __repr__(self):
        return'{}'.format(self.nameCourse)


class Student(Base):
    """ Class for Student
    """
    __tablename__ = "student"
    id = Column(Integer, Sequence('student_seq_id'), primary_key=True)
    nameStudent = Column(String)
    lastStudent = Column(String)
    courseIdStudent = Column(Integer, ForeignKey('course.id'))
    courses = relationship("Course", back_populates='stud')

    def __repr__(self):
        return'{}{}'.format(self.nameStudent, self.lastStudent)


class Time(Base):
    """ Class for Schedule
    """
    __tablename__ = 'schedule'
    id = Column(Integer, Sequence('horario_seq_id'), primary_key=True)
    day = Column(String)
    time_start = Column(String)
    time_end = Column(String)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    curso_hora = relationship("Course", back_populates='time_course')
    course_teacher = relationship("Teacher", back_populates='teacher_course')

    def __repr__(self):
        return'{}{}{}'.format(self.day, self.time_start, self.time_end)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# ********************************************************************
# FIRST STUDENT
# ********************************************************************
print()
print()
print('*' * 50)
stud_01 = Student(nameStudent='Marlon', lastStudent='  GARCIA')
print('* Information first student')
print('*' * 50)
print('* NAME: ', stud_01)
session.add(stud_01)
stud_01.cursos = Course(nameCourse='PROGRAMACIÓN')
print('* ASSIGNMENT: ', stud_01.cursos)

shed_01 = Time(day='Monday: ', time_start="10:00 am ", time_end='- 5:00 pm')
session.add(shed_01)
shed_01.curso_hora = Course(nameCourse='ALGORITMOS')
shed_01.course_teacher = Teacher(nameTeacher='Pedro', lastTeacher=' CARRERO')

print('* TEACHER: ', shed_01.course_teacher)
print('* ASSIGNMENTS: ',
      session.query(Course).filter(Teacher.teacher_course.any()).all())
print('* SCHEDULES: ', session.query(Time).filter(Teacher.teacher_course.any()).all())


# ********************************************************************
# SECOND STUDENT
# ********************************************************************
print()
print()
print('*' * 50)
stud_02 = Student(nameStudent='Leidy', lastStudent=' GANDICA')
print('* Information second student')
print('*' * 50)
print('* NAME: ', stud_02)
session.add(stud_02)
stud_02.cursos = Course(nameCourse='CONTABILIDAD')
print('* ASSIGNMENT: ', stud_02.cursos)

shed_02 = Time(day='Thursday: ', time_start="2:00 am ", time_end='- 7:00 pm')
session.add(shed_02)
shed_02.curso_hora = Course(nameCourse='TRUBUTACION')
shed_02.course_teacher = Teacher(nameTeacher='Hermes', lastTeacher=' CORREA')

print('* TEACHER: ', shed_02.course_teacher)
print('* ASSIGNMENTS: ',
      session.query(Course).filter(Teacher.teacher_course.any()).all())
print('* SCHEDULES: ', session.query(Time).filter(Teacher.teacher_course.any()).all())

session.commit()
