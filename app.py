from flask import Flask, render_template, request

app = Flask(__name__, static_folder='public', template_folder='views')

@app.route("/")
def index():
    return render_template("index.html")
  
@app.route("/par_mums")
def par_mums():
    return render_template("par_mums.html")
  
@app.route("/konvertors")
def konvertors():
    return render_template("konvertors.html")

@app.route("/kontakti")
def kontakti():
    return render_template("kontakti.html")
  
@app.route("/pamati_sintakse")
def pamati_sintakse():
    return render_template("pamati_sintakse.html")
   
@app.route("/sveiciens")
def sveiciens():
    return render_template("sveiciens.html")
  
@app.route("/mainigie")
def mainigie():
  vards = "Zzzzzz"
  vecums = 121
  skaitlis1 = 4
  skaitlis2 = 7
  summa = skaitlis1 + skaitlis2
  return render_template("mainigie.html", vards=vards, vecums=vecums, summa=summa)

@app.route("/datu_tipi")
def datu_tipi():
  teksts = "Sveika pasaule! Sis ir teksts!"
  skaitlis = 100
  decimals = 10.5
  saraksts = ["vards", 2, 3, 4, 5]
  mans_dict = {"vards": "Anna", "vecums": 20}
  return render_template("datu_tipi.html", teksts = teksts, skaitlis = skaitlis, decimals = decimals, saraksts = saraksts, mans_dict = mans_dict, mans_kopa = mans_kopa)
  
@app.route("/operatori")
def operatori():
  a = 10
  b = 6
  summa = a + b
  starpiba = a - b
  reizinajums = a * b
  dalijums = a / b
  atlikums = a % b
  vienads = (a == b)
  return render_template("operatori.html", summa = summa, starpiba = starpiba, reizinajums = reizinajums, dalijums = dalijums, atlikums = atlikums, vienads = vienads)

@app.route("/kontroles_strukturas")
def kontroles_strukturas():
  x = 13
  if x >= 5:
    rezultats = "x ir lielaks par 5"
  else:
    rezultats = "x ir mazaks par 5"
    
  for_cikla_rezultats = [i for i in range(1, 11)]
  
  while_cikla_rezultats = []
  
  y = 0
  while y <= 5:
    while_cikla_rezultats.append(y)
    y+=1
    
  return render_template("kontroles_strukturas.html", rezultats = rezultats, for_cikla_rezultats = for_cikla_rezultats, while_cikla_rezultats = while_cikla_rezultats)

@app.route("/funkcijas")
def funkcijas():
  def sveiciens(vards="Pasaule"):
    return "Sveiki, " + vards + "!"
  noklusetais_sveiciens = sveiciens()
  pasutitais_sveiciens = sveiciens("Andris")
  return render_template("funkcijas.html", noklusetais_sveiciens = noklusetais_sveiciens, pasutitais_sveiciens = pasutitais_sveiciens)

@app.route("/ievade_izvade", methods=['GET', 'POST'])
def ievade_izvade():
  if request.method == 'POST':
    vards = request.form['vards']
    return render_template("ievade_izvade.html", vards = vards)
  return render_template("ievade_izvade.html", vards = None)

@app.route("/failu_apstrade")
def failu_apstrade():
  saturs = ""
    
  try:
    with open('piemers.txt', 'r') as fails:
      saturs = fails.read()
  except IOError:
        saturs = "Fails nav atrasts!"
  return render_template("failu_apstrade.html", saturs = saturs)

@app.route("/oop")
def oop():
  class Persona:
    def __init__ (self, vards, vecums):
      self.vards = vards
      self.vecums = vecums
      
    def sveiciens(self):
      return "Sveiki, mani sauc " + self.vards + " un man ir " + str(self.vecums) + " gadi."
    
  persona = Persona("Janis", 30)
  sveiciens = persona.sveiciens()
    
  return render_template("oop.html", sveiciens = sveiciens)

@app.route("/moduli")
def moduli():
  import math
  sqrt_rezultats = math.sqrt(16) + math.sqrt(16)
  return render_template("moduli.html", sqrt_rezultats = sqrt_rezultats)

@app.route("/aptauja")
def aptauja():
  return render_template("aptauja.html")

@app.route("/iesniegt", methods=[ 'POST' ])
def iesniegt():
    if request.method ==  'POST':
      vards = request.form[ 'vards' ]
      dzimums = request.form[ 'vards' ]
      hobiji = request.form[ 'vards' ]
      return render_template("ievade_izvade.html", vards = vards)
    return render_template("ievade_izvade.html", vards = None)
  
        


if __name__ == "__main__":
  app.run()