import requests
from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime
from supabase import create_client, Client
from supabase.client import ClientOptions
from os.path import join
from dotenv import dotenv_values

dotenv_path = join('.env')
vars = dotenv_values(dotenv_path)
# URL: str = getenv("SUPABASE_URL")
# KEY: str = getenv("SUPABASE_KEY")
URL: str = vars["SUPABASE_URL"]
KEY: str = vars["SUPABASE_KEY"]

supabase: Client = create_client(URL, KEY,
  options=ClientOptions(
    postgrest_client_timeout=100,
    storage_client_timeout=100,
    schema="public",
  ))

def get_dolar(url: str, path: str):
  req = requests.get(url)
  status_code = req.status_code
  if status_code == 200:
    soup = BeautifulSoup(req.text, 'lxml')

    dom = etree.HTML(str(soup))

    precio = dom.xpath(path)
    
    return precio[0].replace('$','').replace(',','.')
  else:
    print(status_code)
    return status_code

def listar(ticker: str):
    response = supabase.table("tickers").select("*").eq("nombre", ticker).execute()
    return response

def agregar_precio_instrumento(nombre: str, 
          precio: float, 
          precio_anterior: float, 
          precio_apertura: float, 
          precio_maximo: float, 
          precio_minimo: float, 
          volumen_nominal: float, 
          volumen_efectivo: float, 
          volumen_promedio: float, 
          volumen_porcentual: float):
    response = supabase.table("tickers").insert({
        "nombre": nombre,
        "precio": precio,
        "precio_anterior": precio_anterior,
        "precio_apertura": precio_apertura,
        "precio_maximo": precio_maximo,
        "precio_minimo": precio_minimo,
        "volumen_nominal": volumen_nominal,
        "volumen_efectivo": volumen_efectivo,
        "volumen_promedio": volumen_promedio,
        "volumen_porcentual": volumen_porcentual,
        "fecha": datetime.now().isoformat()
    }).execute()
    return response

def agregar_precios_dolar(
          mep: float, 
          ccl: float, 
          cripto: float, 
          tarjeta: float, 
          blue: float, 
          oficial: float):
    response = supabase.table("dolar_prices").insert({
        "date": datetime.now().isoformat(),
        "mep": mep,
        "ccl": ccl,
        "cripto": cripto,
        "tarjeta": tarjeta,
        "blue": blue,
        "oficial": oficial
    }).execute()
    return response
