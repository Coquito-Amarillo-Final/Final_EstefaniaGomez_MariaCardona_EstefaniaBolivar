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

clientes = []
productos = []
pedidos = []

class Cliente(Resource):
    def get(self):
        return {"clientes": clientes}
    def post(self):
        nuevo = {"id": len(clientes)+1, "nombre": f"Cliente{len(clientes)+1}"}
        clientes.append(nuevo)
        return nuevo, 201

api.add_resource(Cliente, "/clientes")

class Producto(Resource):
    def get(self):
        return {"productos": productos}
    def post(self):
        nuevo = {"id": len(productos)+1, "nombre": f"Producto{len(productos)+1}"}
        productos.append(nuevo)
        return nuevo, 201

api.add_resource(Producto, "/productos")

class Pedido(Resource):
    def get(self):
        return {"pedidos": pedidos}
    def post(self):
        nuevo = {"id": len(pedidos)+1, "detalle": f"Pedido{len(pedidos)+1}"}
        pedidos.append(nuevo)
        return nuevo, 201

api.add_resource(Pedido, "/pedidos")



if __name__ == "__main__":
    app.run(debug=True)