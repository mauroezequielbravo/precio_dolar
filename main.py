import schedule
from os import path, getenv
from os.path import join
from dotenv import dotenv_values
from functions import get_dolar

dotenv_path = join('.env')
vars = dotenv_values(dotenv_path)



blue = get_dolar(vars['URL'], vars['XPATH_BLUE'])
print(blue)

def job():
    pass

# schedule.every(2).minutes.do(job)
# Programar el trabajo para que se ejecute de lunes a viernes a las 19h
schedule.every().monday.at("19:00").do(job)
schedule.every().tuesday.at("19:00").do(job)
schedule.every().wednesday.at("19:00").do(job)
schedule.every().thursday.at("19:00").do(job)
schedule.every().friday.at("19:00").do(job)

while True:
    schedule.run_pending()


