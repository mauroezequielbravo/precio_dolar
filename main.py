import schedule
from os import path, getenv
from os.path import join
from dotenv import dotenv_values
from functions import get_dolar, agregar_precios_dolar


dotenv_path = join('.env')
vars = dotenv_values(dotenv_path)


def job():
    mep = get_dolar(vars['URL'], vars['XPATH_MEP'])
    ccl = get_dolar(vars['URL'], vars['XPATH_CCL'])
    cripto = get_dolar(vars['URL'], vars['XPATH_CRIPTO'])
    tarjeta = get_dolar(vars['URL'], vars['XPATH_TARJETA'])
    blue = get_dolar(vars['URL'], vars['XPATH_BLUE'])
    oficial = get_dolar(vars['URL'], vars['XPATH_OFICIAL'])
    agregar_precios_dolar(mep, ccl, cripto, tarjeta, blue, oficial)


# schedule.every(2).minutes.do(job)
# Programar el trabajo para que se ejecute de lunes a viernes a las 19h
schedule.every().monday.at("19:00").do(job)
schedule.every().tuesday.at("19:00").do(job)
schedule.every().wednesday.at("19:00").do(job)
schedule.every().thursday.at("19:00").do(job)
schedule.every().friday.at("19:00").do(job)

# schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()


