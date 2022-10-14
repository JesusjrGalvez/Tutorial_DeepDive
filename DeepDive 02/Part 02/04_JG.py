from collections import namedtuple
cars = []


def cast(data_type, value):
    if data_type == 'DOUBLE':
        return float(value)
    elif data_type == 'INT':
        return int(value)
    else:
        return str(value)


def cast_row(data_types, data_row):
    new_data_row = []
    for data_type, value in zip(data_types, data_row):
        new_data = cast(data_type, value)
        new_data_row.append(new_data)
    return new_data_row


def main():
    cars = []
    with open('cars.csv') as file:
        row_index = 0
        for line in file:
            if row_index == 0:
                # header row
                headers = line.strip('\n').split(';')
                Car = namedtuple('Car', headers)
            elif row_index == 1:
                # data type row
                data_types = line.strip('\n').split(';')
                print(data_types)
            elif 2 <= row_index <= 5:
                # data rows
                data = line.strip('\n').split(';')
                data = cast_row(data_types, data)
                # how to create a name tuple:
                # namedTuple_name([list of values])
                # Car(['chevrolet', 18, 50, 'USA'])
                car = Car(*data)
                cars.append(car)
            else:
                pass
            row_index += 1


    for car in cars:
        for data_type, value in zip(data_types, car):
            cast(data_type, value)

    #for car in cars:
    #    print(car)
    print(cars[1])
    print(cars[1].MPG)
    print(type(cars[1].MPG))

def main2():
    print('hello world')

    cars = []

    with open('cars_01.csv') as file:
        file_iter = iter(file)
        headers = next(file_iter).strip('\n').split(';')
        data_types = next(file_iter).strip('\n').split(';')
        Car = namedtuple('Car', headers)
        for line in file_iter:
            data = line.strip('\n').split(';')
            data = cast_row(data_types, data)
            car = Car(*data)
            cars.append(car)

    for car in cars:
        print(car)
    print(cars[0].MPG)
    print(type(cars[0].MPG))

if __name__=="__main__":
    main2()