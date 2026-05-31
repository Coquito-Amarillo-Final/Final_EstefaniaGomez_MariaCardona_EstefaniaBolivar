from flask import Flask, request
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

    def post(self, id_cliente = None):
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

        campos_permitidos = {"nombre", "correo", "numero_telefono"}
        campos_invalidos = set(datos.keys()) - campos_permitidos

        if campos_invalidos:
            return{"error": f"Usted ingresó campos no permitidos: {list(campos_invalidos)}"}, 400

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


#Productos
class Producto(Resource):
    def get(self, id_producto = None):

        if id_producto is None:
            return {"productos": [producto.to_dict() for producto in productos]}

        for producto in productos:
            if producto.id_producto == id_producto:
                return producto.to_dict(), 200
        
        return{"error": f"Producto con id '{id_producto}' no encontrado"}, 404
        
    def post(self, id_producto = None):
        datos = request.get_json()

        campos_requeridos = ["nombre", "precio", "stock", "descripcion", "categoria", "precio_envio"]

        for campo in campos_requeridos:
            if campo not in datos:
                return {"error": f"Campo requerido: '{campo}'"}, 400


        nuevo_producto = ProductoModel(
            id_producto = len(productos) + 1,
            nombre = datos["nombre"],
            precio = datos["precio"],
            stock = datos["stock"],
            descripcion = datos["descripcion"],
            categoria = datos["categoria"],
            precio_envio =datos["precio_envio"] 

        )

        productos.append(nuevo_producto)
        return nuevo_producto.to_dict(), 201

    def put(self, id_producto = None):

        if id_producto is None:
             return {"error": "Se requiere el ID del producto para realizar cambios"}, 400
        
        datos = request.get_json()

        campos_permitidos = {"nombre", "precio", "stock", "descripcion", "categoria", "precio_envio"}
        campos_invalidos =  set(datos.keys()) - campos_permitidos

        if campos_invalidos:
            return{"error": f"Usted ingresó campos no permitidos: {list(campos_invalidos)}"}, 400

        for producto in productos:

            if producto.id_producto == id_producto:
                if "nombre" in datos: producto.nombre = datos["nombre"]
                if "precio" in datos: producto.precio = datos["precio"]
                if "stock" in datos: producto.stock = datos["stock"]
                if "descripcion" in datos: producto.descripcion = datos["descripcion"]
                if "categoria" in datos: producto.categoria = datos["categoria"]
                if "precio_envio" in datos: producto.precio_envio =datos["precio_envio"] 
      
                return producto.to_dict(), 200
            
        return {"error": f"producto con id '{id_producto}' no encontrado"}, 404

    def delete(self, id_producto = None):

        if id_producto is None:
             return {"error": "Se requiere el ID del producto para eliminar"}, 400
        

        for producto in productos:

            if producto.id_producto == id_producto:

                productos.remove(producto)
                return {"mensaje": f"El producto con el id '{id_producto}' fue eliminado exitosamente"}, 200

        return {"error": f"producto con id '{id_producto}' no encontrado"}, 404


class Pedido(Resource):

    def get(self, id_pedido = None):
        
        if id_pedido is None:
            return {"pedidos": [pedido.to_dict() for pedido in pedidos]}

        for pedido in pedidos:
            if pedido.id_pedido == id_pedido:
                return pedido.to_dict(), 200
 
        return{"error": f"Pedido con id '{id_pedido}' no encontrado"}, 404

    def post(self, id_pedido = None):
        datos = request.get_json()
    
        campos_requeridos = ["id_cliente", "items", "total", "direccion_entrega"]

        for campo in campos_requeridos:
            if campo not in datos:
                return {"error": f"Campo requerido: '{campo}'"}, 400
        

        cliente_pedido = None

        for cliente in clientes:
            if cliente.id_cliente == datos["id_cliente"]:
                cliente_pedido = cliente
                break
        
        if cliente_pedido is None:
            return {"error": "Cliente no encontrado"}, 404
        
        

        for item in datos["items"]:
           pedido__existente = False

           for producto in productos:
               
               if producto.id_producto == item["id_producto"]:
                   
                   pedido__existente = True
                   break
               
           if not pedido__existente:
            return {"error": f"Producto con id '{item['id_producto']}' no encontrado" }, 404

        nuevo_pedido = PedidoModel(
            id_pedido = len(pedidos) + 1,
            cliente = cliente_pedido,
            items = datos["items"],
            total = datos["total"],
            direccion_entrega = datos["direccion_entrega"]
        )

        pedidos.append(nuevo_pedido)
        return nuevo_pedido.to_dict(), 201
    
    def put(self, id_pedido = None):

        if id_pedido is None:
             return {"error": "Se requiere el ID del pedido para realizar cambios"}, 400
        
        datos = request.get_json()

        campos_permitidos = {"estado", "direccion_entrega"}
        campos_invalidos = set(datos.keys()) - campos_permitidos

        if campos_invalidos:
            return{"error": f"Usted ingresó campos no permitidos: {list(campos_invalidos)}"}, 400

        for pedido in pedidos:

            if pedido.id_pedido == id_pedido:
                
                if "estado" in datos:
                    if datos["estado"] not in PedidoModel.ESTADOS:
                        return {"error": f"Estado inválido. Opciones: {PedidoModel.ESTADOS}"}, 400 
                    
                    pedido.estado = datos["estado"]
                if "direccion_entrega" in datos: pedido.direccion_entrega = datos["direccion_entrega"] 
                return pedido.to_dict(), 200
            
        return {"error": f"pedido con id '{id_pedido}' no encontrado"}, 404
    
    def delete(self, id_pedido = None):
         
        if id_pedido is None:
             return {"error": "Se requiere el ID del pedido para eliminar"}, 400

        for pedido in pedidos:

            if pedido.id_pedido == id_pedido:
                pedidos.remove(pedido)
                return {"mensaje": f"El pedido con el id '{id_pedido}' fue eliminado exitosamente"}, 200

        return {"error": f"pedido con id '{id_pedido}' no encontrado"}, 404




#Rutas
api.add_resource(Cliente, "/clientes", "/clientes/<int:id_cliente>")
api.add_resource(Producto, "/productos", "/productos/<int:id_producto>")
api.add_resource(Pedido, "/pedidos", "/pedidos/<int:id_pedido>")

if __name__ == "__main__":
    app.run(debug=True)
