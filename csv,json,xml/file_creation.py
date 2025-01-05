import csv
import json
import xml.etree.ElementTree as ET


def create_and_write_csv(file_name):
    data = [
        ["ID", "Name", "Age", "City"],
        [1, "Alice", 25, "New York"],
        [2, "Bob", 30, "Los Angeles"],
        [3, "Charlie", 35, "Chicago"],
    ]
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"CSV file '{file_name}' created and written successfully!")


def read_csv(file_name):
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data


def create_and_write_json(file_name):
    data = {
        "employees": [
            {"ID": 1, "Name": "Alice", "Age": 25, "City": "New York"},
            {"ID": 2, "Name": "Bob", "Age": 30, "City": "Los Angeles"},
            {"ID": 3, "Name": "Charlie", "Age": 35, "City": "Chicago"},
        ]
    }
    with open(file_name, mode="w") as file:
        json.dump(data, file, indent=4)
    print(f"JSON file '{file_name}' created and written successfully!")


def read_json(file_name):
    with open(file_name, mode="r") as file:
        data = json.load(file)
    return data


def create_and_write_xml(file_name):
    root = ET.Element("Employees")
    employees = [
        {"ID": "1", "Name": "Alice", "Age": "25", "City": "New York"},
        {"ID": "2", "Name": "Bob", "Age": "30", "City": "Los Angeles"},
        {"ID": "3", "Name": "Charlie", "Age": "35", "City": "Chicago"},
    ]
    for emp in employees:
        emp_element = ET.SubElement(root, "Employee")
        for key, value in emp.items():
            child = ET.SubElement(emp_element, key)
            child.text = value

    tree = ET.ElementTree(root)
    tree.write(file_name, encoding="utf-8", xml_declaration=True)
    print(f"XML file '{file_name}' created and written successfully!")


def read_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    data = []
    for emp in root.findall("Employee"):
        emp_data = {child.tag: child.text for child in emp}
        data.append(emp_data)
    return data


# Create files and write data
csv_file = "data.csv"
json_file = "data.json"
xml_file = "data.xml"

create_and_write_csv(csv_file)
create_and_write_json(json_file)
create_and_write_xml(xml_file)

# Read data from files
csv_data = read_csv(csv_file)
json_data = read_json(json_file)
xml_data = read_xml(xml_file)

# Print the collected data
print("\nData from CSV:")
for row in csv_data:
    print(row)

print("\nData from JSON:")
print(json_data)

print("\nData from XML:")
for emp in xml_data:
    print(emp)
