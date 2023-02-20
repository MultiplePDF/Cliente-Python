from zeep import Client
from zeep.transports import Transport
import logging

wsdl = 'https://ecs.syr.edu/faculty/fawcett/Handouts/cse775/code/calcWebService/Calc.asmx?WSDL'

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('zeep.transports').setLevel(logging.DEBUG)
logging.getLogger('zeep').setLevel(logging.DEBUG)

# Crear cliente del servicio web
transport = Transport()
client = Client(wsdl=wsdl, transport=transport)

# Invocar el método Add del servicio
result = client.service.Add(1, 2)

# Imprimir el resultado y las solicitudes y respuestas SOAP
print(result)
