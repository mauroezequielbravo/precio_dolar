# Precio del Dolar

## Ejecutar y crear la imagen
docker-compose up -d --build

## Archivo .env
URL = 'https://dolarhoy.com/'

XPATH_BLUE = '//*[@id="home_0"]/div[2]/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/text()'
XPATH_OFICIAL = '//*[@id="home_0"]/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/text()'
XPATH_MEP = '//*[@id="home_0"]/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div[3]/div[1]/div[2]/text()'
XPATH_CCL = '//*[@id="home_0"]/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[4]/div/div[3]/div[1]/div[2]/text()'
XPATH_CRIPTO = '//*[@id="home_0"]/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[5]/div/div[3]/div[1]/div[2]/text()'
XPATH_TARJETA = '//*[@id="home_0"]/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[6]/div/div[3]/div[1]/div[2]/text()'

SUPABASE_URL = 'url'
SUPABASE_KEY = 'anon public'
