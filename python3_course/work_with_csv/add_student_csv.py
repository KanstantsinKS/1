import csv

def add_student(first_name, last_name, age):
    with open('students.csv', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first_name,last_name,age])

add_student('1','1',1)
add_student('2','2',2)


def print_student():
    with open('students.csv') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)


print_student()
