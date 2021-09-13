import csv

def normalize(value, range):
    return (value - range[0]) / (range[1] - range[0])


def denormalize(value, range):
    return (value * (range[1] - range[0])) + range[0]


def read_data(x, y):
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                x.append(int(row[0]))
                y.append(int(row[1]))
                line_count += 1