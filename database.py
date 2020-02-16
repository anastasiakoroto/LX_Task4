import pymysql

from file_handlers import JSONHandler


class Database:

    def __init__(self, students_list, rooms_list):
        self.json_handler = JSONHandler()
        self.students_list = students_list
        self.rooms_list = rooms_list

        self.database = pymysql.connect('localhost', 'tonystark', 'morgan3000', 'LX_TASK4')
        self.cursor = self.database.cursor()
    #

    def create_students_table(self):
        students_table = """
        CREATE TABLE IF NOT EXISTS STUDENTS (
        ID INT PRIMARY KEY,
        NAME CHAR(40) NOT NULL,
        BIRTHDAY DATETIME,
        ROOM_ID INT,
        SEX CHAR(1)
        )"""
        self.cursor.execute(students_table)
        self.database.commit()

    def create_rooms_table(self):
        rooms_table = """
        CREATE TABLE IF NOT EXISTS ROOMS (
        ID INT primary key,
        NAME CHAR(10)
        )"""
        self.cursor.execute(rooms_table)
        self.database.commit()

    def fill_students_table(self):
        for student in self.students_list:
            student_info_insertion = f"""
            INSERT INTO STUDENTS (ID, NAME, BIRTHDAY, ROOM_ID, SEX)
            VALUES (
            {student.get('id')}, 
            '{student.get('name')}', 
            '{student.get('birthday')}', 
            {student.get('room')}, 
            '{student.get('sex')}'
            )"""
            self.cursor.execute(student_info_insertion)
        self.database.commit()

    def fill_rooms_table(self):
        for room in self.rooms_list:
            room_info = f"""
            INSERT INTO ROOMS (ID, NAME)
            VALUES ({room.get('id')}, '{room.get('name')}')"""
            self.cursor.execute(room_info)
        self.database.commit()

    def get_amount_of_students_in_room(self):  # 1
        aim = 'Get list of rooms with amount of students for each room'
        query = """
        select rooms.id, rooms.name, count(students.id) as amount_of_students 
        from rooms join students on rooms.id=students.room_id 
        group by rooms.id 
        order by rooms.id asc;
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)
        rooms = [aim]
        for room in data:
            rooms.append({'id': room[0], 'name': room[1], 'students': room[2]})
        print('Rooms list:', rooms, sep='\n')
        return rooms

    def get_min_avg(self):  # 2
        aim = 'Get top-5 rooms where students have the youngest average age'
        query = """
        select rooms.id, rooms.name, avg(age) as average_age 
        from rooms join (
        select students.id, TIMESTAMPDIFF(year,students.birthday,now()) as age, students.room_id as room_id 
        from students
        ) as age_table 
        on rooms.id=age_table.room_id 
        group by rooms.id 
        order by average_age asc limit 5;
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)
        rooms = [aim]
        for room in data:
            rooms.append({'id': room[0], 'name': room[1], 'average_age': float(room[2])})
        print('Rooms list #2:', rooms, sep='\n')
        return rooms

    def get_largest_difference_in_stud_age(self):  # 3
        aim = 'Get top-5 rooms there students have the biggest age difference'
        query = """
        select rooms.id, rooms.name, max(age)-min(age) as diff_age 
        from rooms join (
        select students.id, TIMESTAMPDIFF(year,students.birthday,now()) as age, students.room_id as room_id 
        from students
        ) as age_table on rooms.id=age_table.room_id 
        group by rooms.id 
        order by diff_age desc limit 5;
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)
        rooms = [aim]
        for room in data:
            rooms.append({'id': room[0], 'name': room[1], 'age_difference': room[2]})
        print('Rooms list #3:', rooms, sep='\n')
        return rooms

    def get_common_rooms(self):  # 4
        aim = 'Get rooms where women and men live together'
        query = """
        select distinct women_rooms.id, women_rooms.name 
        from (
        select rooms.id as id, rooms.name as name from rooms join students on students.room_id=rooms.id where sex='F'
        ) as women_rooms 
        join (
        select rooms.id as id from rooms join students on students.room_id=rooms.id where sex='M'
        ) as men_rooms on men_rooms.id=women_rooms.id 
        order by women_rooms.id asc;
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)
        rooms = [aim]
        for room in data:
            rooms.append({'id': room[0], 'name': room[1]})
        print('Rooms list #4:', rooms, sep='\n')
        return rooms
