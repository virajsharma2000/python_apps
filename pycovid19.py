import requests
import json

class covid_data:
    def __init__(self,country):
        self.country = country

        request = requests.get('https://corona-rest-api.herokuapp.com/Api/{}/'.format(self.country))

        if not 'error' in json.loads(request.text):
            response = json.loads(request.text)

            self.response = response

        else:
            error_response = json.loads(request.text)['error']
            raise Exception(error_response)

    def cases(self):
        return self.response['Success']['cases']

    def todayCases(self):
        return self.response['Success']['todayCases']

    def deaths(self):
        return self.response['Success']['deaths']

    def todayDeaths(self):
        return self.response['Success']['todayDeaths']

    def recovered(self):
        return self.response['Success']['recovered']

    def active(self):
        return self.response['Success']['active']

    def critical(self):
        return self.response['Success']['critical']

    def casesPerOneMillion(self):
        return self.response['Success']['casesPerOneMillion']

    def deathsPerOneMillion(self):
        return self.response['Success']['deathsPerOneMillion']

    def totalTests(self):
        return self.response['Success']['totalTests']

    def testsPerOneMillion(self):
        return self.response['Success']['testsPerOneMillion']
    


            
