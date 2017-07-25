import MySQLdb

db = MySQLdb.connect(host="10.5.18.101", user="14CS10037", passwd="btech14", db="14CS10037")
cursor = db.cursor()
sql = """select coursename from teacher,teaches where teacher.teachername="PPC" and teacher.teacherid=teaches.teacherid"""
tweets = open("output.txt", "w")
cursor.execute(sql)
print>>tweets, "Query 1:"
print>>tweets, "List all the Courses taught by the teacher - PPC "
print>>tweets, "**********************************************"
for row in cursor:
   print>>tweets, row[0]
print>>tweets, "**********************************************"
print>>tweets, "\n\n"
tweets.close()

sql = """select name,course.coursename from student,enrolls,course,teaches,teacher where
 student.studentid=enrolls.studentid AND  enrolls.coursename=course.coursename AND 
 course.coursename=teaches.coursename AND teacher.teachername="PPC" AND
teacher.teacherid=teaches.teacherid"""
tweets = open("output.txt", "a")
cursor.execute(sql)
print>>tweets, "Query 2:"
print>>tweets, "List all students registered in the courses taught by PPC "
print>>tweets, "**********************************************"
for row in cursor:
   print>>tweets, row[0]
print>>tweets, "**********************************************"
print>>tweets, "\n\n"
tweets.close()


sql = """select starttime,endtime,date from timings,timetable,course,willbein,classroom where
timings.timeid=timetable.timeid AND
timetable.coursename=course.coursename AND
course.coursename=willbein.coursename AND
classroom.roomnumber=willbein.roomnumber AND classroom.roomnumber="NC142" """
tweets = open("output.txt", "a")
cursor.execute(sql)
print>>tweets, "Query 3:"
print>>tweets, "List the timings of all courses in Class-Room NC142."
print>>tweets, "**********************************************"
for row in cursor:
   print>>tweets, row[0]
print>>tweets, "**********************************************"
print>>tweets, "\n\n"
tweets.close()


sql = """(select student.name,student.studentid from student,(select marks.marksid,max(marks.marks),
	course.coursename from marks,have,course,teaches,teacher where marks.marksid=have.marksid AND
	 have.coursename=course.coursename and course.coursename=teaches.coursename and teaches.teacherid=teacher.teacherid
	  and teacher.teachername="PPC" group by marks.marksid,course.coursename) as x where x.marksid=student.studentid ) """
tweets = open("output.txt", "a")
cursor.execute(sql)
print>>tweets, "Query 4:"
print>>tweets, "List the name of the students who received the highest marks in the courses taught by PPC "
print>>tweets, "**********************************************"
for row in cursor:
   print>>tweets, row[0]
print>>tweets, "**********************************************"
print>>tweets, "\n\n"
tweets.close()


sql = """select q.name from (select name,p,count(*) as EX1 from student,gradecard,  (select max(EXcount) as p from (select student.name, count(*) as EXcount from student,gradecard where  grade="EX" and studentid=gradeid group by gradeid ) as x )as z where grade="EX" and studentid=gradeid group by gradeid )as q where q. p=q.EX1 
"""
tweets = open("output.txt", "a")
cursor.execute(sql)
print>>tweets, "Query 5:"
print>>tweets, "List the students who have received a grade of EX in the largest number of courses."
print>>tweets, "**********************************************"
for row in cursor:
   print>>tweets, row[0]
print>>tweets, "**********************************************"
print>>tweets, "\n\n"
tweets.close()


db.close()









