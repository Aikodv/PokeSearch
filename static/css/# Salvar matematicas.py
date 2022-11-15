# OPERACION SALVAR TODOS LOS RAMOS 

 # Operacion Salvar matematicas 

c1  = 46 # 20%
c2  = 36 # 25%
c3  = 70 # 30%
co1 = 15
co2 = 20 
co3 = 35
promedio_co = (co1+co2+co3)/3
go = 69
eta = ((85*0.6+ 100*0.1 +95 *0.3)/450)+(79/90)
print(eta)

ponderacion = ((promedio_co * 0.25)+ c1*0.20 + c2*0.25 + c3*0.30)*eta
print("Promedio Matematicas", ponderacion)
print("Promedio Matematicas con global", ponderacion*0.70+go*0.30)

# Oparicion Salvar quimica

c1  = 33 # 20%
c2  = 33 # 20%
c3  = 40 # 25%
co = (75+80+80+100+100)/5 #20
Ag = (94+92+100+100+100+100)/6 #15
promedio_qui = co*0.2 + Ag*0.15 + c1*0.2 + c2*0.2 + c3*0.25
print("promedio de quimica",promedio_qui)

# Operacion Salvar fisica

ce1  = 42 
ce2  = 57 
ce3  = 60
coG  = 80
promedio_certamenes = (ce1+ce2+ce3)/3 #75%
Controles_fis = (70+80+60)/3
tareas_fis =(100+90+90)/3 
promedio_fis = (tareas_fis+Controles_fis)/2

print("promedio fisica",(((promedio_fis*0.25+promedio_certamenes*0.75)*1.05))*0.6+coG*0.4)
