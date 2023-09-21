import utils
import leer_csv
import graficas
import pandas as pd

def run():  
  df = pd.read_csv('./data.csv')
  df = df[df['Continent'] == 'Asia']
  
  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  graficas.generate_pie_chart(countries, percentages)
  
  
  data = leer_csv.real_csv('./data.csv')
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    graficas.generate_bar_chart(country['Country'], labels, values)
  else:
    print('No encontrado.')

if __name__ == '__main__':
  run()