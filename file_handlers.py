import json
import xml.etree.ElementTree as ElemTree


class JSONHandler:

    def convert_json_to_obj(self, path_to_file):
        with open(path_to_file, 'r', encoding='utf-8') as json_file:
            obj = json.load(json_file)
            return obj

    def write_rooms_list_to_json(self, rooms_list, filename):
        with open(f'output_files/json/{filename}.json', 'w') as json_file:
            json.dump(rooms_list, json_file)
        print(f'Updated list of rooms was added to output_files/json/{filename}.json successfully!')


class XMLWriter:

    def _parse_students_amount_query_to_xml(self, rooms_list):
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

    def _parse_average_age_query_to_xml(self, rooms_list):
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

    def _parse_age_difference_query_to_xml(self, rooms_list):
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

    def _parse_common_rooms_query_to_xml(self, rooms_list):
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

    def students_amount_query_to_xml(self, room_list, filename):
        queries_tree = self._parse_students_amount_query_to_xml(room_list)
        with open(f'output_files/xml/{filename}.xml', 'w') as xml_file:
            queries_tree.write(xml_file, encoding='unicode')

    def average_age_query_to_xml(self, room_list, filename):
        queries_tree = self._parse_average_age_query_to_xml(room_list)
        with open(f'output_files/xml/{filename}.xml', 'w') as xml_file:
            queries_tree.write(xml_file, encoding='unicode')

    def age_difference_query_to_xml(self, room_list, filename):
        queries_tree = self._parse_age_difference_query_to_xml(room_list)
        with open(f'output_files/xml/{filename}.xml', 'w') as xml_file:
            queries_tree.write(xml_file, encoding='unicode')

    def common_rooms_query_to_xml(self, room_list, filename):
        queries_tree = self._parse_common_rooms_query_to_xml(room_list)
        with open(f'output_files/xml/{filename}.xml', 'w') as xml_file:
            queries_tree.write(xml_file, encoding='unicode')
