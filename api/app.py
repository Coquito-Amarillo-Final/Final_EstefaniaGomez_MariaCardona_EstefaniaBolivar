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
        nuevo = {"id": len(clientes)+1, "nombre": f"Cliente{len(clientes)+1}"}
        clientes.append(nuevo)
        return nuevo, 201



class Producto(Resource):
    def get(self):
        return {"productos": productos}
    def post(self):
        nuevo = {"id": len(productos)+1, "nombre": f"Producto{len(productos)+1}"}
        productos.append(nuevo)
        return nuevo, 201



class Pedido(Resource):
    def get(self):
        return {"pedidos": pedidos}
    def post(self):
        nuevo = {"id": len(pedidos)+1, "detalle": f"Pedido{len(pedidos)+1}"}
        pedidos.append(nuevo)
        return nuevo, 201




#Rutas
api.add_resource(Cliente, "/clientes", "/clientes/<int:id_cliente>")
api.add_resource(Producto, "/productos")
api.add_resource(Pedido, "/pedidos")


if __name__ == "__main__":
    app.run(debug=True)