import argparse
import os


class ArgParser:

    def create_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('path_to_students_file', help='Path to students file')
        parser.add_argument('path_to_rooms_file', help='Path to rooms file')
        parser.add_argument('format', help='Format of output file')
        return parser

    def is_valid_file(self, filepath):
        if os.path.exists(filepath):
            return True
        return False

    def get_args(self):
        parser = self.create_parser()
        args = parser.parse_args()
        students_file_path = args.path_to_students_file
        rooms_file_path = args.path_to_rooms_file
        output_format = args.format
        if self.is_valid_file(students_file_path) and self.is_valid_file(rooms_file_path):
            return students_file_path, rooms_file_path, output_format
        else:
            print("Unfortunately, file doesn't exist. Please, check the path to each required file.")
            raise FileExistsError

    # def run_command_line(self):
    #     parser = self.create_parser()
    #     args = parser.parse_args()
    #     students_file_path = args.path_to_students_file
    #     rooms_file_path = args.path_to_rooms_file
    #     output_format = args.format
    #     if self.is_valid_file(students_file_path) and self.is_valid_file(rooms_file_path):
    #         # db = Database(students_file_path, rooms_file_path, output_format)
    #         pass
    #         # helper = Helper(students_file_path, rooms_file_path, output_format)
    #         # helper.fill_database_by_files()
    #     else:
    #         print("Unfortunately, file doesn't exist. Please, check the path to each required file.")


# if __name__ == '__main__':
#     # students = '/Users/Anastasia/PycharmProjects/LeverX Course/task_4/input_files/students.json'
#     # rooms = '/Users/Anastasia/PycharmProjects/LeverX Course/task_4/input_files/rooms.json'
#
#     arg_parser = ArgParser()
#     arg_parser.run_command_line()
