from sqlalchemy import create_engine, event
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.engine import Engine

#Conecccion a la Dase de datos
#Nombre del usuario
dataBaseName="gestionpd"


#Usuario de la base de datos
UserName="root"


#Contaseña del usuario
UserPassword=""

#PUERTO DE CONEXION
conexionPort="3306"

#Servidor de conexion
serverConnection="localhost"

#CREANDO LA CONEXION
conexionToDataBase=f"mysql+mysqlconnector://{UserName}:{UserPassword}@{serverConnection}:{conexionPort}/{dataBaseName}"

print(conexionToDataBase)

engine=create_engine(conexionToDataBase)
sessionLocal=sessionmaker.Session(autocommint=False, autoFlush=False, bind=engine)

