import requests
from jinja2 import Environment, FileSystemLoader

def data():
  api='https://aves.ninjas.cl/api/birds'
  res= requests.get(api)
  if res.status_code == 200:
    return res.json()
  else:
    print(f"Error en la llamada de al API")
    return None
  

def html(birds_data):
  environment = Environment(loader=FileSystemLoader('.'))
  template = environment.get_template('index.html')
  content = template.render(birds=birds_data)
  with open ('index2.html', 'w', encoding='utf-8') as f:
    f.write(content)


def main():
  birds_data = data()
  if birds_data:
    html(birds_data)
    print("Sitio web creado correctamente como 'aves_de_chile.html'.")

if __name__ == "__main__":
  main()