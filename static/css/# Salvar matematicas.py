# OPERACION SALVAR TODOS LOS RAMOS 

# Operacion Salvar matematicas 

c1  = 46 # 20%
c2  = 36 # 25%
c3  = 83 # 30%
co1 = 15
co2 = 20 
co3 = 56
promedio_co = (co1+co2+co3)/3
eta = ((((85+98)/2)*0.6+ 100*0.1 +(95+65)/2 *0.3)/450)+(79/90)
print(eta)

ponderacion = ((promedio_co * 0.25)+ c1*0.20 + c2*0.25 + c3*0.30)
print("Promedio Matematicas sin eta si me saco un 83", ponderacion)
ponderacion_eta = ponderacion*eta
print("Promedio Matematicas con eta si me saco un 83 con lab", ponderacion_eta)
ponderacion = ((promedio_co * 0.25)+ c1*0.20 + c2*0.25 + c3*0.60)

# Operacion Salvar fisica

ce1  = 42 
ce2  = 57 
ce3  = 52
coG  = 50
promedio_certamenes = (ce1+ce2+ce3)/3 #75%
Controles_fis = (70+80+90+50+30)/5
tareas_fis =(100+90+95+100+100)/5
promedio_fis = ((tareas_fis*0.3333)+(Controles_fis*0.6666))
nose = (promedio_fis*0.25+promedio_certamenes*0.75)
print("promedio fisica sin eta",nose)
noseeta = nose*1.03
print("promedio fisica con eta",noseeta)
global_fis = (noseeta*0.6+coG*0.4)
print("promedio fisica con global si me saco un 50",global_fis)

# Operacion Salvar quimica

c1  = 33 # 20%
c2  = 33 # 20%
c3  = 33 # 25%
co = (75+80+80+100+100+60+80)/8 #20
Ag = (94+92+100+100+100+100)/6#15
promedio_qui = co*0.2 + Ag*0.15 + c1*0.2 + c2*0.2 + c3*0.25 #60
glob = 60 # 40%
print("promedio de quimica",promedio_qui)
print("Promedio de quimica con global (nota:60)",promedio_qui*0.6+glob*0.4)