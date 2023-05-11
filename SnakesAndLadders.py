# Ignacio Hernández de la Fuente
# Proyecto: Juego de Serpientes y Escaleras
import random

#Esta función CREA el tablero que será utilizado durante el resto de la partida, a partir de una matriz.
#Cuando se crea una partida nueva, se crea un tablero nuevo.
#Todas las posiciones y números son aleatorios, respetando ciertas reglas que deben de seguirse para no provocar
#error en el programa, además de para seguir las instrucciones dadas.
def tablero(tamano):
    
#escaleras renglon
    loc1=random.randrange(5,10)
    loc2=random.randrange(5,10)
    loc3=random.randrange(5,10)
    loc4=random.randrange(5,10)

#escaleras columna

    loc10=random.randrange(0,10)
    if loc1==9 and loc10==0:
        loc10=random.randrange(1,10)
    
    loc20=random.randrange(0,10)
    if loc2==9 and loc20==0:
        loc20=random.randrange(1,10)
    while loc2==loc1 and loc20==loc10:
        loc2=random.randrange(5,10)
        loc20=random.randrange(0,10)
        
    loc30=random.randrange(0,10)
    if loc3==9 and loc30==0:
        loc30=random.randrange(1,10)
    while loc3==loc1 and loc30==loc10 or loc3==loc2 and loc30==loc20:
        loc3=random.randrange(5,10)
        loc30=random.randrange(0,10)
        
    loc40=random.randrange(0,10)
    if loc4==9 and loc40==0:
        loc40=random.randrange(1,10)
    while loc4==loc1 and loc40==loc10 or loc4==loc2 and loc4==loc20 or loc4==loc3 and loc40==loc30:
        loc4=random.randrange(5,10)
        loc40=random.randrange(0,10)
    
#serpientes renglon    
    loc5=random.randrange(0,5)
    loc6=random.randrange(0,5)
    loc7=random.randrange(0,5)
    loc8=random.randrange(0,5)

#serpientes columna
    loc50=random.randrange(0,10)
    if loc5==0 and loc50==0:
        loc50=random.randrange(1,10)
    
    loc60=random.randrange(0,10)
    if loc6==0 and loc60==0:
        loc60=random.randrange(1,10)
    while loc6==loc5 and loc60==loc50:
        loc6=random.randrange(0,5)
        loc60=random.randrange(0,10)
        
    loc70=random.randrange(0,10)
    if loc7==0 and loc70==0:
        loc70=random.randrange(1,10)
    while loc7==loc5 and loc70==loc50 or loc7==loc6 and loc70==loc60:
        loc7=random.randrange(0,5)
        loc70=random.randrange(0,10)
        
    loc80=random.randrange(0,10)
    if loc8==0 and loc80==0:
        loc80=random.randrange(1,10)
    while loc8==loc5 and loc80==loc50 or loc8==loc6 and loc80==loc60 or loc8==loc7 and loc80==loc70:
        loc8=random.randrange(0,5)
        loc80=random.randrange(0,10)  
    
    matriz = []
    for renglon in range(tamano):
        matriz.append([])
        for columna in range(tamano):
            if renglon==loc1 and columna==loc10:
                escalera1_renglon=str(random.randrange(0,loc1))
                escalera1_columna=str(random.randrange(1,10))
                escalera1='['+escalera1_renglon+','+escalera1_columna+']'
                matriz[renglon].append(escalera1)
                escalera1_renglon=int(escalera1_renglon)
                escalera1_columna=int(escalera1_columna)

            elif renglon==loc2 and columna==loc20:
                escalera2_renglon=str(random.randrange(0,loc2))
                escalera2_columna=str(random.randrange(1,10))
                escalera2='['+escalera2_renglon+','+escalera2_columna+']'
                matriz[renglon].append(escalera2)
                escalera2_renglon=int(escalera2_renglon)
                escalera2_columna=int(escalera2_columna)
                
            elif renglon==loc3 and columna==loc30:
                escalera3_renglon=str(random.randrange(0,loc3))
                escalera3_columna=str(random.randrange(1,10))
                escalera3='['+escalera3_renglon+','+escalera3_columna+']'
                matriz[renglon].append(escalera3)
                escalera3_renglon=int(escalera3_renglon)
                escalera3_columna=int(escalera3_columna)
                
            elif renglon==loc4 and columna==loc40:
                escalera4_renglon=str(random.randrange(0,loc4))
                escalera4_columna=str(random.randrange(1,10))
                escalera4='['+escalera4_renglon+','+escalera4_columna+']'
                matriz[renglon].append(escalera4)
                escalera4_renglon=int(escalera4_renglon)
                escalera4_columna=int(escalera4_columna)
                
                        
            elif renglon==loc5 and columna==loc50:
                serpiente5_renglon=str(random.randrange(loc5,9))
                serpiente5_columna=str(random.randrange(1,10))
                serpiente5='['+serpiente5_renglon+','+serpiente5_columna+']'
                matriz[renglon].append(serpiente5)
                serpiente5_renglon=int(serpiente5_renglon)
                serpiente5_columna=int(serpiente5_columna)
                
            elif renglon==loc6 and columna==loc60:
                serpiente6_renglon=str(random.randrange(loc6,9))
                serpiente6_columna=str(random.randrange(1,10))
                serpiente6='['+serpiente6_renglon+','+serpiente6_columna+']'
                matriz[renglon].append(serpiente6)
                serpiente6_renglon=int(serpiente6_renglon)
                serpiente6_columna=int(serpiente6_columna)
                
            elif renglon==loc7 and columna==loc70:
                serpiente7_renglon=str(random.randrange(loc7,9))
                serpiente7_columna=str(random.randrange(1,10))
                serpiente7='['+serpiente7_renglon+','+serpiente7_columna+']'
                matriz[renglon].append(serpiente7)
                serpiente7_renglon=int(serpiente7_renglon)
                serpiente7_columna=int(serpiente7_columna)
                
            elif renglon==loc8 and columna==loc80:
                serpiente8_renglon=str(random.randrange(loc8,9))
                serpiente8_columna=str(random.randrange(1,10))
                serpiente8='['+serpiente8_renglon+','+serpiente8_columna+']'
                matriz[renglon].append(serpiente8)
                serpiente8_renglon=int(serpiente8_renglon)
                serpiente8_columna=int(serpiente8_columna)

            else:
                matriz[renglon].append(0)
    return matriz,loc1,loc2,loc3,loc4,loc5,loc6,loc7,loc8,loc10,loc20,loc30,loc40,loc50,loc60,loc70,loc80,escalera1_renglon,escalera1_columna,escalera2_renglon,escalera2_columna,escalera3_renglon,escalera3_columna,escalera4_renglon,escalera4_columna,serpiente5_renglon,serpiente5_columna,serpiente6_renglon,serpiente6_columna,serpiente7_renglon,serpiente7_columna,serpiente8_renglon,serpiente8_columna

#Esta función MUESTRA (imprime) el tablero ya creado.
def muestra_tablero(matriz):
    for elrenglon in range (10):
        for lacolumna in range (10):
            print(str(matriz[elrenglon][lacolumna]).center(5),end="")
        print()

#Esta función DETERMINA e IMPRIME la dirección (izquierda/derecha) a la que se debe mover sobre el tablero.
#La dirección depende enteramente del renglón en el que se ubica la posición actual.
# nr = numero de renglon, nc = numero de columna
def determina_direccion(nr,nc):
    if int(nr)%2==1:
        direccion='derecha'
    if int(nr)%2==0 or (nr)==0:
        direccion='izquierda'
    print('Posición: (' + str(nr) +',' + str(nc) +')'+' Hacia la ' + direccion)

#Esta función representa la columna inicial y se utiliza para ir actualizando la posición actual (solo en columna).
def funcioncolumna():
    elcolumna=0
    return elcolumna

#Esta función representa el renglón inicial y se utiliza para ir actualizando la posicion actual (solo en renglón).
def funcionrenglon():
    larenglon=9
    return larenglon

#Esta función imprime el dado creado por la función "tira_dado()".
def imprime_dado(dado):
    print('Dado: ' + str(dado))
    
#Esta función imprime el turno creado por la función "turno_inicial()".
def imprime_turno(turno):
    print('Turno: ' + str(turno))

#Esta función crea (tira) un dado, es decir, crea un número aleatorio entre 1 y 6.
def tira_dado():
    dado=(random.randrange(1,7))
    return dado

#Este número representa el número del turno, comienza en 1.
def turno_inicial():
    turno=1
    return turno

#Esta es la función principal donde incluí todas las instrucciones que no fui capaz de incorporar en otras funciones.
def main():
    matriz,loc1,loc2,loc3,loc4,loc5,loc6,loc7,loc8,loc10,loc20,loc30,loc40,loc50,loc60,loc70,loc80,escalera1_renglon,escalera1_columna,escalera2_renglon,escalera2_columna,escalera3_renglon,escalera3_columna,escalera4_renglon,escalera4_columna,serpiente5_renglon,serpiente5_columna,serpiente6_renglon,serpiente6_columna,serpiente7_renglon,serpiente7_columna,serpiente8_renglon,serpiente8_columna = tablero(10)
    turno=turno_inicial()
    dado=(tira_dado())
    enter=""
    numcolumna=(funcioncolumna())
    numrenglon=(funcionrenglon())
    while enter=="":
        imprime_turno(turno)
        turno=turno+1
        dado=tira_dado()
        determina_direccion(numrenglon,numcolumna)
        if int(numrenglon)%2==1:
            numcolumna+=dado
        if int(numrenglon%2)==0 or int(numrenglon)==0:
            numcolumna=numcolumna-dado
        if int(numcolumna)>9:
            numrenglon=numrenglon-1
            numerito=numcolumna-10
            numcolumna=9-numerito
        if int(numcolumna)<0:
            numrenglon=numrenglon-1
            exceso=numcolumna
            exceso=exceso+1
            exceso=exceso*-1
            numcolumna=exceso
        if numrenglon==-1 and numcolumna>=0:
            print('¡Llegaste a la meta!')
            exit()
        if numrenglon==0 and numcolumna==0:
            print('¡Llegaste a la meta!')
            exit()
        enter=input('[enter] para aventar el dado:')
        if enter=="":
            imprime_dado(dado)
#Cuando se pisa una escalera
        if loc1==numrenglon and loc10==numcolumna:
            print('¡Salto!')
            numrenglon=escalera1_renglon
            numcolumna=escalera1_columna
        if loc2==numrenglon and loc20==numcolumna:
            print('¡Salto!')
            numrenglon=escalera2_renglon
            numcolumna=escalera2_columna
        if loc3==numrenglon and loc30==numcolumna:
            print('¡Salto!')
            numrenglon=escalera3_renglon
            numcolumna=escalera3_columna
        if loc4==numrenglon and loc40==numcolumna:
            print('¡Salto!')
            numrenglon=escalera4_renglon
            numcolumna=escalera4_columna
#Cuando se pisa una serpiente
        if loc5==numrenglon and loc50==numcolumna:
            print('¡Salto!')
            numrenglon=serpiente5_renglon
            numcolumna=serpiente5_columna
        if loc6==numrenglon and loc60==numcolumna:
            print('¡Salto!')
            numrenglon=serpiente6_renglon
            numcolumna=serpiente6_columna
        if loc7==numrenglon and loc70==numcolumna:
            print('¡Salto!')
            numrenglon=serpiente7_renglon
            numcolumna=serpiente7_columna
        if loc8==numrenglon and loc80==numcolumna:
            print('¡Salto!')
            numrenglon=serpiente8_renglon
            numcolumna=serpiente8_columna
          
        print('')
        if enter=='m':
            muestra_tablero(matriz)
            print('')
            imprime_dado(dado)
            enter=input()
    
main()