import json
import xml.etree.ElementTree as ElemTree


class FileConverter:
    def open_and_convert_to_object(self, path_to_file):
        raise NotImplementedError


class FileWriter:
    def write(self, rooms_list, filename):
        raise NotImplementedError


class JSONConverter(FileConverter):
    def open_and_convert_to_object(self, path_to_file):
        try:
            with open(path_to_file, 'r', encoding='utf-8') as json_file:
                obj = json.load(json_file)
                return obj
        except FileNotFoundError:
            raise FileNotFoundError(f"Unfortunately, file with path '{path_to_file}' doesn't exist. "
                                    f"Please, check the path to each required file.")
        except IsADirectoryError:
            raise IsADirectoryError("Unfortunately, you didn't point the name of file. "
                                    "The program needs it to continue.")
        except PermissionError:
            raise PermissionError(f"Unfortunately, access to file with path {path_to_file} denied.")


class JSONWriter(FileWriter):
    def write(self, rooms_list, filename):
        with open(f'output_files/json/{filename}.json', 'w') as json_file:
            json.dump(rooms_list[1:], json_file)
        print(f'Result of query was added to output_files/json/{filename}.json successfully!')


class XMLParser:
    def parse_students_amount_query_to_xml(self, rooms_list):
        root = ElemTree.Element('query_1')
        goal = ElemTree.SubElement(root, 'goal')
        goal.text = rooms_list[0]
        rooms = ElemTree.Element('rooms')
        root.append(rooms)
        for room_dict in rooms_list[1:]:
            room = ElemTree.Element('room')
            rooms.append(room)
            room_id = ElemTree.SubElement(room, 'id')
            room_id.text = str(room_dict.get('id'))
            room_name = ElemTree.SubElement(room, 'name')
            room_name.text = room_dict.get('name')
            students_amount = ElemTree.SubElement(room, 'amount_of_students')
            students_amount.text = str(room_dict.get('students'))
        query_1_tree = ElemTree.ElementTree(root)
        return query_1_tree

    def parse_average_age_query_to_xml(self, rooms_list):
        root = ElemTree.Element('query_2')
        goal = ElemTree.SubElement(root, 'goal')
        goal.text = rooms_list[0]
        rooms = ElemTree.Element('rooms')
        root.append(rooms)
        for room_dict in rooms_list[1:]:
            room = ElemTree.Element('room')
            rooms.append(room)
            room_id = ElemTree.SubElement(room, 'id')
            room_id.text = str(room_dict.get('id'))
            room_name = ElemTree.SubElement(room, 'name')
            room_name.text = room_dict.get('name')
            average_age = ElemTree.SubElement(room, 'average_age')
            average_age.text = str(room_dict.get('average_age'))
        query_2_tree = ElemTree.ElementTree(root)
        return query_2_tree

    def parse_age_difference_query_to_xml(self, rooms_list):
        root = ElemTree.Element('query_3')
        goal = ElemTree.SubElement(root, 'goal')
        goal.text = rooms_list[0]
        rooms = ElemTree.Element('rooms')
        root.append(rooms)
        for room_dict in rooms_list[1:]:
            room = ElemTree.Element('room')
            rooms.append(room)
            room_id = ElemTree.SubElement(room, 'id')
            room_id.text = str(room_dict.get('id'))
            room_name = ElemTree.SubElement(room, 'name')
            room_name.text = room_dict.get('name')
            age_difference = ElemTree.SubElement(room, 'age_difference')
            age_difference.text = str(room_dict.get('age_difference'))
        query_3_tree = ElemTree.ElementTree(root)
        return query_3_tree

    def parse_common_rooms_query_to_xml(self, rooms_list):
        root = ElemTree.Element('query_4')
        goal = ElemTree.SubElement(root, 'goal')
        goal.text = rooms_list[0]
        rooms = ElemTree.Element('rooms')
        root.append(rooms)
        for room_dict in rooms_list[1:]:
            room = ElemTree.Element('room')
            rooms.append(room)
            room_id = ElemTree.SubElement(room, 'id')
            room_id.text = str(room_dict.get('id'))
            room_name = ElemTree.SubElement(room, 'name')
            room_name.text = room_dict.get('name')
        query_4_tree = ElemTree.ElementTree(root)
        return query_4_tree


class XMLWriter(FileWriter):

    def __init__(self):
        self.parser = XMLParser()

    def write(self, rooms_list, filename):
        if filename[-1] == '1':
            query_tree = self.parser.parse_students_amount_query_to_xml(rooms_list)
        elif filename[-1] == '2':
            query_tree = self.parser.parse_average_age_query_to_xml(rooms_list)
        elif filename[-1] == '3':
            query_tree = self.parser.parse_age_difference_query_to_xml(rooms_list)
        else:
            query_tree = self.parser.parse_common_rooms_query_to_xml(rooms_list)
        with open(f'output_files/xml/{filename}.xml', 'w') as xml_file:
            query_tree.write(xml_file, encoding='unicode')
            print(f'Result of query was added to output_files/xml/{filename}.json successfully!')


class QueriesWriter:

    def __init__(self, output_format):
        self.json_writer = JSONWriter()
        self.xml_writer = XMLWriter()
        self.format = output_format

    def write(self, rooms_list, filename):
        if self.format == 'json':
            self.json_writer.write(rooms_list, filename)
        elif self.format == 'xml':
            self.xml_writer.write(rooms_list, filename)
        else:
            print(f'There are no functionality for {self.format} format. Sorry :c\n'
                  f'But you can choose json/xml c:')
