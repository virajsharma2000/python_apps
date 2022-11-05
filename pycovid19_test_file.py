import pycovid19

country = input('Enter your country name: ')

covid = pycovid19.covid_data(country)

print()

print('cases:',covid.cases())
print('todayCases:',covid.todayCases())
print('deaths:',covid.deaths())
print('todayDeaths:',covid.todayDeaths())
print('recovered:',covid.recovered())
print('active:',covid.active())
print('critical:',covid.critical())
print('casesPerOneMillion:',covid.critical())
print('deathsPerOneMillion:',covid.deathsPerOneMillion())
print('totalTests:',covid.totalTests())
print('testsPerOneMillion:',covid.testsPerOneMillion())
