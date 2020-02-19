import pymysql


class HostelDatabase:

    def __init__(self, students_list, rooms_list):
        self.students_list = students_list
        self.rooms_list = rooms_list

        self.database = pymysql.connect(host='localhost',
                                        user='tonystark',
                                        password='morgan3000',
                                        db='LX_TASK4')
        self.cursor = self.database.cursor()

    def create_rooms_table(self):
        rooms_table = """
        CREATE TABLE IF NOT EXISTS ROOMS (
        ID INT,
        NAME CHAR(10) NOT NULL,
        PRIMARY KEY (ID)
        )"""
        self.cursor.execute(rooms_table)
        self.database.commit()

    def create_students_table(self):
        students_table = """
        CREATE TABLE IF NOT EXISTS STUDENTS (
        ID INT,
        NAME CHAR(40) NOT NULL,
        BIRTHDAY DATETIME,
        ROOM_ID INT,
        SEX CHAR(1) NOT NULL,
        PRIMARY KEY (ID),
        FOREIGN KEY (ROOM_ID) REFERENCES ROOMS (ID)
        )"""
        self.cursor.execute(students_table)
        self.database.commit()

    def fill_students_table(self):
        for student in self.students_list:
            student_info_insertion = f"""
                        INSERT INTO STUDENTS (ID, NAME, BIRTHDAY, ROOM_ID, SEX)
                        VALUES (
                        {student.get('id')}, 
                        %s, 
                        %s, 
                        {student.get('room')}, 
                        %s
                        )"""
            try:
                self.cursor.execute(student_info_insertion,
                                    (student.get('name'),
                                    student.get('birthday'),
                                    student.get('sex')))
            except pymysql.IntegrityError:
                continue
        self.database.commit()

    def fill_rooms_table(self):
        for room in self.rooms_list:
            room_info = f"""
            INSERT INTO ROOMS (ID, NAME)
            VALUES ({room.get('id')}, %s)"""
            try:
                self.cursor.execute(room_info, room.get('name'))
            except pymysql.IntegrityError:
                continue
        self.database.commit()

    def create_sex_index_to_students(self):
        query = """CREATE INDEX SEX_INDEX ON STUDENTS(SEX)"""
        try:
            self.cursor.execute(query)
        except pymysql.InternalError:
            print("Index with name 'sex_index' already exists. New index wasn't created.")
        self.database.commit()

    def get_amount_of_students_in_room(self):  # 1
        aim = 'Get list of rooms with amount of students for each room'
        query = """
        SELECT ROOMS.ID, ROOMS.NAME, COUNT(STUDENTS.ID) AS AMOUNT_OF_STUDENTS 
        FROM ROOMS JOIN STUDENTS ON ROOMS.ID = STUDENTS.ROOM_ID 
        GROUP BY ROOMS.ID 
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        rooms = [aim]
        for room in data:
            rooms.append({'id': room[0], 'name': room[1], 'students': room[2]})
        return rooms

    def get_students_average_age(self):  # 2
        aim = 'Get top-5 rooms where students have the youngest average age'
        query = """
        SELECT ROOMS.ID, ROOMS.NAME, AVG(AGE) AS AVERAGE_AGE 
        FROM ROOMS JOIN (
        SELECT STUDENTS.ID, TIMESTAMPDIFF(YEAR, STUDENTS.BIRTHDAY, NOW()) AS AGE, STUDENTS.ROOM_ID AS ROOM_ID 
        FROM STUDENTS
        ) AS AGE_TABLE 
        ON ROOMS.ID = AGE_TABLE.ROOM_ID 
        GROUP BY ROOMS.ID 
        ORDER BY AVERAGE_AGE ASC LIMIT 5;
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        rooms = [aim]
        for room in data:
            rooms.append({'id': room[0], 'name': room[1], 'average_age': float(room[2])})
        return rooms

    def get_largest_difference_in_stud_age(self):  # 3
        aim = 'Get top-5 rooms there students have the biggest age difference'
        query = """
        SELECT ROOMS.ID, ROOMS.NAME, MAX(AGE) - MIN(AGE) AS DIFF_AGE
        FROM ROOMS JOIN ( 
        SELECT STUDENTS.ID, TIMESTAMPDIFF(YEAR, STUDENTS.BIRTHDAY, NOW()) AS AGE, STUDENTS.ROOM_ID AS ROOM_ID 
        FROM STUDENTS
        ) AS AGE_TABLE ON ROOMS.ID = AGE_TABLE.ROOM_ID 
        GROUP BY ROOMS.ID 
        ORDER BY DIFF_AGE DESC LIMIT 5;
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        rooms = [aim]
        for room in data:
            rooms.append({'id': room[0], 'name': room[1], 'age_difference': room[2]})
        return rooms

    def get_common_rooms(self):  # 4
        aim = 'Get rooms where women and men live together'
        query = """
        SELECT DISTINCT WOMEN_ROOMS.ID, WOMEN_ROOMS.NAME 
        FROM (
        SELECT ROOMS.ID AS ID, ROOMS.NAME AS NAME FROM ROOMS JOIN STUDENTS ON STUDENTS.ROOM_ID = ROOMS.ID WHERE SEX='F'
        ) AS WOMEN_ROOMS 
        JOIN (
        SELECT ROOMS.ID AS ID FROM ROOMS JOIN STUDENTS ON STUDENTS.ROOM_ID = ROOMS.ID WHERE SEX = 'M'
        ) AS MEN_ROOMS ON MEN_ROOMS.ID = WOMEN_ROOMS.ID 
        ORDER BY WOMEN_ROOMS.ID ASC;
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        rooms = [aim]
        for room in data:
            rooms.append({'id': room[0], 'name': room[1]})
        return rooms
