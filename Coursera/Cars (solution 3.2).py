import os
import csv


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):

    body_length = 0.0
    body_width = 0.0
    body_height = 0.0

    def __init__(self, brand, photo_file_name, carrying, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_whl_split(body_whl)

    def body_whl_split(self, body_whl):
        list_whl = body_whl.split("x")
        try:
            list_whl2 = [float(a) for a in list_whl]
            if len(list_whl2) == 3:
                self.body_length = list_whl2[0]
                self.body_width = list_whl2[1]
                self.body_height = list_whl2[2]
        except ValueError:
            pass

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def valid_checking(row, list_car):
    if not row:
        return 0
    if row[1] == "":
        return 0
    if not row[5].replace(".", '', 1).isdigit():
        return 0
    path = os.path.splitext(row[3])
    if path[0] == "" or not path[1] in ['.jpeg', '.jpg', '.gif', '.png']:
        return 0
    if row[0] == "car" and row[2].isdigit():
        list_car.append(Car(row[1], row[3], row[5], row[2]))
    if row[0] == "truck":
        list_car.append(Truck(row[1], row[3], row[5], row[4]))
    if row[0] == "spec_machine" and row[6] != '':
        list_car.append(SpecMachine(row[1], row[3], row[5], row[6]))


def get_car_list(csv_filename):
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        list_car = []
        for row in reader:
            valid_checking(row, list_car)
    return list_car


