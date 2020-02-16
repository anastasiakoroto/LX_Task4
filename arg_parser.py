import argparse


class ArgParser:

    def create_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('path_to_students_file', help='Path to students file')
        parser.add_argument('path_to_rooms_file', help='Path to rooms file')
        parser.add_argument('format', help='Format of output file')
        return parser

    def get_args(self):
        parser = self.create_parser()
        args = parser.parse_args()
        students_file_path = args.path_to_students_file
        rooms_file_path = args.path_to_rooms_file
        output_format = args.format
        return students_file_path, rooms_file_path, output_format
