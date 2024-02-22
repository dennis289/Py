porsche ={
    "model":'911 GT3',
    'engine' : 'straight six cylinder',
    'horsePower' : "475Hp",
    'torque': "750Nm",
    'year of manufacture': 2022,
    'mode': '7 speed dual clutch automatic gearbox'
}
# Adding a field
porsche['miles']= 4200
# updating
# porsche.update()
# deleting
# porsche.pop()
#    print (porsche.keys())
#    print (porsche.values())
#    print (porsche.items())
# looping through a dictionary for bboth the keys and values
# for x,y in porsche.items():
#     print(x,y)
# looping through keys
for x in porsche.keys():
    print(x)
# looping through values
for x in porsche.values():
    print(x)
