import json
import xml.etree.ElementTree as ElemTree


class JSONHandler:

    def convert_json_to_obj(self, path_to_file):
        with open(path_to_file, 'r', encoding='utf-8') as json_file:
            obj = json.load(json_file)
            return obj

    def write_rooms_list_to_json(self, rooms_list, flag):
        with open(f'output_files/json/rooms_{flag}.json', 'w') as json_file:
            json.dump(rooms_list, json_file)
        print(f'Updated list of rooms was added to output_files/json/updated_rooms_{flag}.json successfully!')


class XMLWriter:

    # def _parse_rooms_to_xml_1(self, rooms_list):
    #     root = ElemTree.Element('rooms')
    #     for room_dict in rooms_list:
    #         room = ElemTree.Element('room')
    #         root.append(room)
    #         room_id = ElemTree.SubElement(room, 'id')
    #         room_id.text = str(room_dict.get('id'))
    #         room_name = ElemTree.SubElement(room, 'name')
    #         room_name.text = room_dict.get('name')
    #         students_amount = ElemTree.SubElement(room, 'amount_of_students')
    #         students_amount.text = str(room_dict.get('students'))
    #     room_tree = ElemTree.ElementTree(root)
    #     return room_tree
    #
    # def write_rooms_list_to_xml_1(self, rooms_list):
    #     rooms_tree = self._parse_rooms_to_xml_1(rooms_list)
    #     with open('output_files/xml/rooms_1', 'w') as xml_file:
    #         rooms_tree.write(xml_file, encoding='unicode')
    #     print('Updated list of rooms was added to output_files/xml/rooms_1.xml successfully!')

    def _parse_rooms_to_xml_query_1(self, rooms_list):
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

    def _parse_rooms_to_xml_query_2(self, rooms_list):
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

    def _parse_rooms_to_xml_query_3(self, rooms_list):
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

    def _parse_rooms_to_xml_query_4(self, rooms_list):
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

    # def unite_queries(self, room_list_1, room_list_2, room_list_3, room_list_4):
    #     root = ElemTree.Element('queries')
    #     query_1_info = self._parse_rooms_to_xml_query_1(room_list_1)
    #     query_2_info = self._parse_rooms_to_xml_query_2(room_list_2)
    #     query_3_info = self._parse_rooms_to_xml_query_3(room_list_3)
    #     query_4_info = self._parse_rooms_to_xml_query_4(room_list_4)
    #     data = query_1_info.getroot()
    #     root.append(query_1_info)
    #     root.append(query_2_info)
    #     root.append(query_3_info)
    #     root.append(query_4_info)
    #     queries_tree = ElemTree.ElementTree(root)
    #     return queries_tree
    #
    # def write_queries_to_xml(self, room_list_1, room_list_2, room_list_3, room_list_4):
    #     queries_tree = self.unite_queries(room_list_1, room_list_2, room_list_3, room_list_4)
    #     with open('queries_result.xml', 'w') as xml_file:
    #         queries_tree.write(xml_file, encoding='unicode')

    def write_query_1_to_xml(self, room_list):
        queries_tree = self._parse_rooms_to_xml_query_1(room_list)
        with open('output_files/xml/query_1_result.xml', 'w') as xml_file:
            queries_tree.write(xml_file, encoding='unicode')

    def write_query_2_to_xml(self, room_list):
        queries_tree = self._parse_rooms_to_xml_query_2(room_list)
        with open('output_files/xml/query_2_result.xml', 'w') as xml_file:
            queries_tree.write(xml_file, encoding='unicode')

    def write_query_3_to_xml(self, room_list):
        queries_tree = self._parse_rooms_to_xml_query_3(room_list)
        with open('output_files/xml/query_3_result.xml', 'w') as xml_file:
            queries_tree.write(xml_file, encoding='unicode')

    def write_query_4_to_xml(self, room_list):
        queries_tree = self._parse_rooms_to_xml_query_4(room_list)
        with open('output_files/xml/query_4_result.xml', 'w') as xml_file:
            queries_tree.write(xml_file, encoding='unicode')
