import csv

def real_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for line in reader:
            iterable = zip(header, line)
            country_dict = { key: value for key, value in iterable }
            data.append(country_dict)
        return data
            
if __name__ == '__main__':
    data = real_csv('/Users/hdgarcia/Documents/Python/Clases_Tareas/platzi/app/data.csv')
    print(data[0])