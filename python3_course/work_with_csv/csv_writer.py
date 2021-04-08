import csv

# with open('students.csv', 'w') as file:
#     csv_writer = csv.writer(file,delimiter=';')
#     csv_writer.writerow(['First name', 'Last name', 'Age'])
#     csv_writer.writerow(['Jack', 'White', 25])
#     csv_writer.writerow(['Jane', 'White', 22])


# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     make_model_list = []
#     for car in csv_reader:
#         make_model = [car[1], car[2]]
#         make_model_list.append(make_model)
#     print(make_model_list)
#
# with open('cars_make_model.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     for row in make_model_list:
#         csv_writer.writerow(row)


# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#
#     with open('cars_make_model.csv', 'w') as file:
#         csv_writer = csv.writer(file)
#         for row in csv_reader:
#             csv_writer.writerow([row[1], row[2]])


with open('students1.csv', 'w') as file:
    headers_list = ['First name', 'Last name', 'Age']
    csv_writer = csv.DictWriter(file,fieldnames=headers_list)
    csv_writer.writeheader()
    csv_writer.writerow({'First name': 'Jack', 'Last name': 'White', 'Age': 25})
    csv_writer.writerow({'First name': 'Jane', 'Last name': 'White', 'Age': 22})
