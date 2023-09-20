import utils

data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

def run():
  key, value = utils.get_population()
  print(key, value)

  country = input('Ingrese el país: ')
  result = utils.population_by_conuntry(data, country)
  print(result)

if __name__ == '__main__':
    run()