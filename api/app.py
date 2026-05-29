from flask import Flask
from flask_restful import Api, Resource
from datetime import datetime
from models import ClienteModel, ProductoModel, PedidoModel

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"message": "Bienvenido a Coquito Amarillo API"}

api.add_resource(HelloWorld, "/")

#Datos
clientes = []
productos = []
pedidos = []


class Cliente(Resource):

    def get(self, id_cliente = None):
        
        if id_cliente is None:
            return {"clientes": [cliente.to_dict() for cliente in clientes]}

        for cliente in clientes:
            if cliente.id_cliente == id_cliente:
                return cliente.to_dict(), 200
        
        return{"error": f"Cliente con id '{id_cliente}' no encontrado"}, 404

    def post(self):
        datos = request.get_json()

        campos_requeridos = ["nombre", "correo", "contrasena_hash", "numero_telefono"]

        for campo in campos_requeridos:
            if campo not in datos:
                return {"error": f"Campo requerido: '{campo}'"}, 400


        nuevo_cliente = ClienteModel(
            id_cliente = len(clientes) + 1,
            nombre = datos["nombre"],
            correo = datos["correo"],
            contrasena_hash = datos["contrasena_hash"],
            numero_telefono = datos["numero_telefono"],
            fecha_registro = datetime.now() 

        )

        clientes.append(nuevo_cliente)
        return nuevo_cliente.to_dict(), 201
    
    def put(self, id_cliente = None):

        if id_cliente is None:
             return {"error": "Se requiere el ID del cliente para realizar cambios"}, 400

        datos = request.get_json()

        for cliente in clientes:

            if cliente.id_cliente == id_cliente:

                if "nombre" in datos: cliente.nombre = datos["nombre"]
                if "correo" in datos: cliente.correo = datos["correo"]
                if "numero_telefono" in datos: cliente.numero_telefono = datos["numero_telefono"]
                

                return cliente.to_dict(), 200
            
        return {"error": f"cliente con id '{id_cliente}' no encontrado"}, 404
    
    def delete(self, id_cliente = None):

        if id_cliente is None:
             return {"error": "Se requiere el ID del cliente para eliminar"}, 400

        for cliente in clientes:

            if cliente.id_cliente == id_cliente:

                clientes.remove(cliente)
                return {"mensaje": f"El cliente con el id '{id_cliente}' fue eliminado exitosamente"}, 200

        return {"error": f"cliente con id '{id_cliente}' no encontrado"}, 404



class Producto(Resource):
    def get(self):
        return {"productos": productos}
    def post(self):
        nuevo = {"id": len(productos)+1, "nombre": f"Producto{len(productos)+1}"}
        productos.append(nuevo)
        return nuevo, 201



class Pedido(Resource):

    def get(self, id_pedido = None):
        
        if id_pedido is None:
            return {"pedidos": [pedido.to_dict() for pedido in pedidos]}

        for pedido in pedidos:
            if pedido.id_pedido == id_pedido:
                return pedido.to_dict(), 200
 
        return{"error": f"Pedido con id '{id_pedido}' no encontrado"}, 404

    def post(self):
        nuevo = {"id": len(pedidos)+1, "detalle": f"Pedido{len(pedidos)+1}"}
        pedidos.append(nuevo)
        return nuevo, 201




#Rutas
api.add_resource(Cliente, "/clientes", "/clientes/<int:id_cliente>")
api.add_resource(Producto, "/productos", "/productos/<int:id_producto>")
api.add_resource(Pedido, "/pedidos")


if __name__ == "__main__":
    app.run(debug=True)