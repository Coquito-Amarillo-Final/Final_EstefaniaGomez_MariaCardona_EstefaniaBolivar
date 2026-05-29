from datetime import datetime

#Clientes
class ClienteModel:
    """Representa a un usuario registrado en la tienda de Coquito Amarillo."""

    def __init__(self, id_cliente: int, nombre: str, correo: str, contrasena_hash: str, numero_telefono: str, fecha_registro: datetime):
        self.id_cliente: int        = id_cliente
        self.nombre: str            = nombre
        self.correo: str            = correo
        self.contrasena_hash: str   = contrasena_hash
        self.activo: bool           = True
        self.numero_telefono: str   = numero_telefono
        self.fecha_registro: datetime = fecha_registro

    def to_dict(self):
        return{
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "correo": self.correo,
            "activo": self.activo,
            "numero_telefono": self.numero_telefono,
            "fecha_registro": self.fecha_registro.isoformat()
        }
    

#Productos
class ProductoModel:
    """Representa un producto artesanal disponible en el catálogo."""

    def __init__(self, id_producto: int, nombre: str, precio: float, stock: int, descripcion: str, categoria: str, precio_envio: float):
        self.id_producto: int  = id_producto
        self.nombre: str       = nombre
        self.precio: float     = precio
        self.stock: int        = stock
        self.descripcion: str  = descripcion
        self.categoria: str    = categoria
        self.precio_envio: float = precio_envio

    def to_dict(self):
        return{
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "descripcion": self.descripcion,
            "categoria": self.categoria,
            "precio_envio": self.precio_envio
        }
    

#Pedidos
class PedidoModel:
    """Representa una orden de compra confirmada por el cliente."""

    ESTADOS = ["pendiente", "pagado", "en_preparacion", "enviado", "entregado", "cancelado"]

    def __init__(self, id_pedido: int, cliente: ClienteModel, items: list, total: float, direccion_entrega: str):
        self.id_pedido: int       = id_pedido
        self.cliente: ClienteModel     = cliente
        self.items: list    = items
        self.total: float         = total
        self.estado: str          = "pendiente"
        self.fecha: datetime      = datetime.now()
        self.direccion_entrega: str = direccion_entrega

    def to_dict(self):
        return{
            "id_pedido": self.id_pedido,
            "cliente": self.cliente.to_dict(),
            "items": self.items,
            "total": self.total,
            "estado": self.estado,
            "fecha": self.fecha.isoformat(),
            "direccion_entrega": self.direccion_entrega
        }