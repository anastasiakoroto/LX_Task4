from database import Database
from file_handlers import JSONHandler, XMLWriter
from arg_parser import ArgParser


class DatabaseManager:

    def __init__(self):
        self.arg_parser = ArgParser()
        self.json_handler = JSONHandler()
        self.xml_handler = XMLWriter()

        students_file_path, rooms_file_path, self.output_format = self.arg_parser.get_args()
        self.students_list = self.json_handler.convert_json_to_obj(students_file_path)
        self.rooms_list = self.json_handler.convert_json_to_obj(rooms_file_path)

        self.database = Database(self.students_list, self.rooms_list)

    # def get_arguments_cmd_line(self):
    #     path_to_students, path_to_rooms, output_format = self.arg_parser.get_args()
    #     if self.arg_parser.is_valid_file(path_to_students) and self.arg_parser.is_valid_file(path_to_rooms):
    #         return path_to_students, path_to_rooms, output_format
    #     else:
    #         print("Unfortunately, file doesn't exist. Please, check the path to each required file.")
    #         raise FileExistsError

    # def get_lists_from_files(self, students_file_path, rooms_file_path):
    #     students_list = self.json_handler.convert_json_to_obj(students_file_path)
    #     rooms_list = self.json_handler.convert_json_to_obj(rooms_file_path)
    #     return students_list, rooms_list

    def fill_database(self):
        self.database.create_rooms_table()
        self.database.create_students_table()
        self.database.fill_rooms_table()
        self.database.fill_students_table()

    def run_queries(self):
        self.fill_database()

        result_of_query_1 = self.database.get_amount_of_students_in_room()
        result_of_query_2 = self.database.get_min_avg()
        result_of_query_3 = self.database.get_largest_difference_in_stud_age()
        result_of_query_4 = self.database.get_common_rooms()
        return result_of_query_1, result_of_query_2, result_of_query_3, result_of_query_4

    def write_queries_result_to_xml(self):
        result_1, result_2, result_3, result_4 = self.run_queries()
        self.xml_handler.write_query_1_to_xml(result_1)
        self.xml_handler.write_query_2_to_xml(result_2)
        self.xml_handler.write_query_3_to_xml(result_3)
        self.xml_handler.write_query_4_to_xml(result_4)

    def write_queries_result_to_json(self):
        result_1, result_2, result_3, result_4 = self.run_queries()
        self.json_handler.write_rooms_list_to_json(result_1[1:], 1)
        self.json_handler.write_rooms_list_to_json(result_2[1:], 2)
        self.json_handler.write_rooms_list_to_json(result_3[1:], 3)
        self.json_handler.write_rooms_list_to_json(result_4[1:], 4)

    def write_queries_results(self):
        if self.output_format == 'xml':
            self.write_queries_result_to_xml()
        elif self.output_format == 'json':
            self.write_queries_result_to_json()
        else:
            print(f'There are no functionality for {self.output_format} format. Sorry :c\n'
                  f'But you can choose json/xml c:')


if __name__ == '__main__':
    # arg_parser = ArgParser()
    # students_file_path, rooms_file_path, output_format = arg_parser.get_args()
    # print('Arguments got successfully.')

    manager_db = DatabaseManager()
    manager_db.write_queries_results()
    manager_db.database.database.close()
