from arg_parser import ArgParser
from database import HostelDatabase
from file_handlers import JSONConverter, QueriesWriter


class DatabaseManager:

    def __init__(self):
        self.arg_parser = ArgParser()
        students_file_path, rooms_file_path, output_format = self.arg_parser.get_args()

        self.json_converter = JSONConverter()
        self.students_list = self.json_converter.open_and_convert_to_object(students_file_path)
        self.rooms_list = self.json_converter.open_and_convert_to_object(rooms_file_path)

        self.query_result_writer = QueriesWriter(output_format)
        self.database = HostelDatabase(self.students_list, self.rooms_list)

    def fill_database_by_rooms_students(self):
        self.database.create_rooms_table()
        self.database.create_students_table()
        self.database.fill_rooms_table()
        self.database.fill_students_table()

    def run_queries(self):
        self.fill_database_by_rooms_students()
        self.database.create_sex_index_to_students()

        students_amount_query = self.database.get_amount_of_students_in_room()
        average_age_query = self.database.get_students_average_age()
        age_difference_query = self.database.get_largest_difference_in_stud_age()
        common_rooms_query = self.database.get_common_rooms()
        return students_amount_query, average_age_query, age_difference_query, common_rooms_query

    def write_queries_result_to_file(self):
        students_amount_query, average_age_query, age_difference_query, common_rooms_query = self.run_queries()
        self.query_result_writer.write(students_amount_query, 'query_1')
        self.query_result_writer.write(average_age_query, 'query_2')
        self.query_result_writer.write(age_difference_query, 'query_3')
        self.query_result_writer.write(common_rooms_query, 'query_4')


if __name__ == '__main__':
    manager_db = DatabaseManager()
    manager_db.write_queries_result_to_file()
    manager_db.database.database.close()
