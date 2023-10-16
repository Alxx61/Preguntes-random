import random

with open('log.txt', 'w', encoding='utf-8') as b:   # esborra els dos arxius si estan presents
    pass  
with open('respostes.txt', 'w', encoding='utf-8') as a:
    pass  

with open('log.txt', 'a', encoding='utf-8') as c:     #crea els 2 arxius si no estan
    pass
with open('respostes.txt', 'a', encoding='utf-8') as v:
    pass

file = open('preguntes.txt', 'r', encoding='utf-8')  # obrir arxiu
lines = file.readlines()                                # assignar lineas a la variable



def printandlog(s):           #la s es refereix a la variable random line mes endevant/ funció per guardar i per escriure
    print(s)
    with open('log.txt', 'a', encoding='utf-8') as f: #obrir document log per escriure tmb/ la n fica un espai extra??? 
        f.write(s + '\n') # / la s es torna a referir a la linea random de mes endevant, pertant escriu la linea random + el espai...........^^
    x = input('Resposta:')
    with open('respostes.txt', 'a', encoding='utf-8') as k:
        k.write(x + '\n')

while True:  #mentres quedin preguntes NO a log
    with open('log.txt', 'r', encoding='utf-8') as f:           # assigna el document a la variable logdoc per compararles
        logdoc = f.read()

    lines_not_in_logdoc = [line for line in lines if line not in logdoc]   # crea la funcio que compara les lines a logdoc amb les de preguntes

    if lines_not_in_logdoc:     #si no esta a log.txt pero si a pregutnes / Ho faig tot junt pq afora la variable random line no existeix, i es demanava un valor nul al repetirse tot el rato, ara només si son diferents 
        random_line = random.choice(lines_not_in_logdoc)       # tria la linea random
        if random_line not in logdoc:       #si la linea no esta a log.txt
            printandlog(random_line)    # preguntem
    
    if not lines_not_in_logdoc:      # si totes les lineas de log doc (log.txt) estan a preguntes.txt escriu JA ESTA   log = preguntes   
        print('No queden més preguntes')
        break
