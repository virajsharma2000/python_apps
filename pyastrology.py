import pyaztro

def get_astrological_sign(day,month):
    if month == 'december':
        if day >= 22 and not day > 31:
            return 'Capricorn'

        if day <= 21 and not day < 1:
            return 'Sagittarius'

    elif month == 'january':
        if day <= 19 and not day < 1:
            return 'Capricorn'

        if day >= 20 and not day > 31:
            return 'Aquarius'

    elif month == 'march':
        if day <= 20 and not day < 1:
            return 'Pisces'

        if day >= 21 and not day > 31:
            return 'Aries'

    elif month == 'february':
       if day <= 18 and not day < 1:
           return 'Aquarius'

       if day >= 19 and not day > 30:
           return 'Pisces'

    elif month == 'april':
        if day >= 20 and not day > 30:
            return 'Taurus'

        if day <= 19 and not day < 1:
            return 'Aries'

    elif month == 'may':
        if day >= 21 and not day > 31:
            return 'Gemini'
        if day <= 20 and not day < 1:
            return 'Taurus'

    elif month == 'june':
       if day <= 20 and not day < 1:
           return 'Gemini'

       if day >= 21 and not day > 30:
           return 'Cancer'

    elif month == 'july':
        if day <= 22 and not day < 1:
            return 'Cancer'
        if day >= 23 and not day > 30:
            return 'Leo'

    elif month == 'august':
        if day <= 22 and not day < 1:
            return 'Leo'
        if day >= 23 and not day > 31:
            return 'Virgo'

    elif month == 'september':
        if day <= 22 and not day < 1:
            return 'Virgo'
        if day >= 23 and not day > 30:
            return 'Libra'

    elif month == 'october':
        if day <= 22 and not day < 1:
            return 'Libra'
        if day >= 23 and not day > 31:
            return 'Scorpio'

    elif month == 'november':
        if day <= 21 and not day < 1:
            return 'Scorpio'
        if day >= 22 and not day > 30:
            return 'Sagittarius'


def get_symbol_of_sunsign(sunsign):
    if sunsign == 'Capricorn':
        return 'Goat'

    elif sunsign == 'Aquarius':
        return 'Water Bearer'

    elif sunsign == 'Pisces':
        return 'Fish'

    elif sunsign == 'Aries':
        return 'Deer'

    elif sunsign == 'Taurus':
        return 'Bull'

    elif sunsign == 'Gemini':
        return 'Twins'

    elif sunsign == 'Cancer':
        return 'Crab'

    elif sunsign == 'Leo':
        return 'Lion'

    elif sunsign == 'Virgo':
        return 'Girl'

    elif sunsign == 'Libra':
        return 'Balance'

    elif sunsign == 'Scorpio':
        return 'Scorpion'

    elif sunsign == 'Sagittarius':
        return 'Archer'


def print_sunsign_chart():
    sunsign_chart_list = ['Aries (March 21 – April 19)',
                         'Taurus (April 20 – May 20)',
                         'Gemini (May 21 – June 20)',
                         'Cancer (June 21 – July 22)',
                         'Leo (July 23 – August 22)',
                         'Virgo (August 23 – September 22)',
                         'Libra (September 23 – October 22)',
                         'Scorpio (October 23 – November 21)',
                         'Sagittarius (November 22 – December 21)',
                         'Capricorn (December 22 – January 19)',
                         'Aquarius (January 20 – February 18) ',
                         'Pisces (February 19 – March 20)',
                          ]

    for chart_list in sunsign_chart_list:
        print(chart_list)


def get_day_prediction(day,month,day_to_predict):
 return pyaztro.Aztro(sign = get_astrological_sign(day,month),day = day_to_predict).description





