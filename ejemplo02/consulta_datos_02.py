from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Sacar las matriculas con su estudiante y módulo
#matriculas = session.query(Matricula).join(Estudiante).\
 #           filter(Estudiante.nombre.like("%tony%")).all()


#for m in matriculas:
#    print(m.periodo, m.estudiante, m.modulo)

#for m in matriculas:
 #   print("Periodo: ",m.periodo)
 #   print("Estudiante: ",m.estudiante.nombre, m.estudiante.apellido)
 #   print("Modulo: ",m.modulo.nombre)

matriculas = session.query(Matricula).join(Estudiante).join(Modulo).\
    filter(Estudiante.nombre.like("%tony%")).all()

for m in matriculas:
    print("Estudiante:", m.estudiante.nombre, m.estudiante.apellido)
    print("Módulo:", m.modulo.nombre)
    print("Periodo:", m.periodo)
    print("------")

