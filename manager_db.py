from arg_parser import ArgParser
from database import HostelDatabase
from file_handlers import JSONHandler, XMLWriter


class DatabaseManager:

    def __init__(self):
        self.arg_parser = ArgParser()
        self.json_handler = JSONHandler()
        self.xml_handler = XMLWriter()

        students_file_path, rooms_file_path, self.output_format = self.arg_parser.get_args()
        self.students_list = self.json_handler.convert_json_to_obj(students_file_path)
        self.rooms_list = self.json_handler.convert_json_to_obj(rooms_file_path)

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

    def write_queries_result_to_xml(self):
        students_amount_query, average_age_query, age_difference_query, common_rooms_query = self.run_queries()
        self.xml_handler.students_amount_query_to_xml(students_amount_query, 'query_1')
        self.xml_handler.average_age_query_to_xml(average_age_query, 'query_2')
        self.xml_handler.age_difference_query_to_xml(age_difference_query, 'query_3')
        self.xml_handler.common_rooms_query_to_xml(common_rooms_query, 'query_4')

    def write_queries_result_to_json(self):
        students_amount_query, average_age_query, age_difference_query, common_rooms_query = self.run_queries()
        self.json_handler.write_rooms_list_to_json(students_amount_query[1:], 'query_1')
        self.json_handler.write_rooms_list_to_json(average_age_query[1:], 'query_2')
        self.json_handler.write_rooms_list_to_json(age_difference_query[1:], 'query_3')
        self.json_handler.write_rooms_list_to_json(common_rooms_query[1:], 'query_4')

    def write_queries_results(self):
        if self.output_format == 'xml':
            self.write_queries_result_to_xml()
        elif self.output_format == 'json':
            self.write_queries_result_to_json()
        else:
            print(f'There are no functionality for {self.output_format} format. Sorry :c\n'
                  f'But you can choose json/xml c:')


if __name__ == '__main__':
    manager_db = DatabaseManager()
    manager_db.write_queries_results()
    manager_db.database.database.close()
