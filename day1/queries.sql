CREATE DATABASE student;

USE student;

CREATE TABLE users(user_id INT primary key,uname varchar(20),email varchar(30),mid INT,foreign key(mid) references mentors(m_id));
CREATE TABLE problems(p_id INT primary key, p_desc varchar(40));
CREATE TABLE codekata(c_id INT primary key,uid INT,pid INT,foreign key(uid) references users(user_id),foreign key(pid) references problems(p_id));
CREATE TABLE companies(cid INT primary key,cname varchar(15));
CREATE TABLE company_drives(id INT primary key,uid INT,cid INT,foreign key(uid) references users(user_id),foreign key(cid) references companies(cid));
CREATE TABLE mentors(m_id INT primary key,mname varchar(20));
CREATE TABLE attendance(att_id INT primary key, uid INT, foreign key(uid) references users(user_id),datee date,attendance varchar(5));
CREATE TABLE courses(course_id INT primary key, course_name varchar(20));
CREATE TABLE student_activated_courses(id INT primary key,uid INT,course_id INT,foreign key(uid) references users(user_id),foreign key(course_id) references courses(course_id));
CREATE TABLE topics(topic_id INT primary key, topic_name varchar(20));
CREATE TABLE tasks(task_id INT primary key,task_name varchar(20),topic_id INT, foreign key(topic_id) references topics(topic_id));
CREATE TABLE course_ref_topic(id INT primary key,course_id INT,topic_id INT,foreign key(course_id) references courses(course_id),foreign key(topic_id) references topics(topic_id));

INSERT INTO mentors values (1,'Rahul'),(2,'Payal'),(3,'Deepthi'),(4,'Kiran'),(5,'Lahari');
INSERT INTO users values (1,'Arjun','arjun@gmail.om',1),(2,'Arha','arha@gmail.om',5),(3,'Priya','priya@gmail.om',1),(4,'Siri','siri@gmail.om',2),(5,'Ravi','ravi@gmail.om',1);
INSERT INTO users values (6,'Ria','ria@gmail.om',4),(7,'Tina','tina@gmail.om',3),(8,'Raj','raj@gmail.om',3),(9,'Madhu','madhu@gmail.om',2),(10,'Manas','manas@gmail.om',4);
INSERT INTO problems values (1,'P1'),(2,'P2'),(3,'P3'),(4,'P4'),(5,'P5'),(6,'P6'),(7,'P7'),(8,'P8'),(9,'P9'),(10,'P10');
INSERT INTO codekata values (1,1,2),(2,2,1),(3,2,2),(4,2,6),(5,4,1),(6,5,9),(7,5,10),(8,7,2),(9,9,3),(10,9,10);
INSERT INTO companies values (1,'Google'),(2,'Amazon'),(3,'Microsoft'),(4,'Adobe'),(5,'Walmart');
INSERT INTO company_drives values (1,1,1),(2,1,5),(3,2,2),(4,3,1),(5,3,2),(6,4,4),(7,4,3),(8,5,1),(9,6,3),(10,7,2),(11,7,1),(12,8,4),(13,9,5),(14,10,3);
INSERT INTO courses values (1,'Full Stack'),(2,'Frontend'),(3,'DBMS'),(4,'Data Science'),(5,'Machine Learning');
INSERT INTO student_activated_courses values (1,1,4),(2,1,1),(3,2,1),(4,2,5),(5,2,4),(6,3,2),(7,4,3),(8,5,1),(9,7,4),(10,7,5),(11,9,1);
INSERT INTO topics values (1,'Django'),(2,'Javascript'),(3,'Python'),(4,'.Net'),(5,'SQL'),(6,'MongoDB'),(7,'Keras'),(8,'Bootstrap'),(9,'Data Structures'),(10,'HTML/CSS');
INSERT INTO course_ref_topic values (1,1,2),(2,1,4),(3,1,5),(4,1,6),(5,1,10),(6,2,2),(7,2,10),(8,1,1),(9,3,5),(10,3,6),(11,4,3),(12,5,7),(13,5,9),(14,2,8);
INSERT INTO tasks values (1,'Task1',2),(2,'Task2',1),(3,'Task3',4),(4,'Task4',4),(5,'Task5',3),(6,'Task6',6),(7,'Task7',8),(8,'Task8',9),(10,'Task10',10);
INSERT INTO attendance values (2,1,'2021-09-15','A'),(3,3,'2021-09-14','P'),(4,4,'2021-09-14','P'),(5,6,'2021-09-14','A'),(6,8,'2021-09-15','P'),(7,8,'2021-09-14','A'),(8,10,'2021-09-14','P');

-- get no.of problems solved in codekata
select count(DISTINCT pid) from codekata;

-- display no of company drives attended by user
select uname,count(cid) from company_drives left join users on company_drives.uid=users.user_id group by uname;

-- combine and display student_activated_courses and courses for a specific user grouping them based on course
select course_name,count(uid) from courses left join student_activated_courses on courses.course_id=student_activated_courses.course_id group by course_name;

-- list all the mentors
select mname from mentors;

-- list the no. of students that are assigned for a mentor
select mname,count(user_id) from users left join mentors on users.mid=mentors.m_id group by mname;
