from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, Enum, DateTime, Numeric
from sqlalchemy.orm import relationship
from database import db

def current_time():
    return datetime.utcnow().isoformat()

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum('comprador', 'vendedor', name='user_roles'), nullable=False)
    nombre_empresa = Column(String, nullable=True)
    direccion = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    descripcion = Column(Text, nullable=True)
    nombre = Column(String, nullable=True)
    apellido = Column(String, nullable=True)
    direccion_envio = Column(String, nullable=True)
    created_at = Column(String, default=current_time)
    updated_at = Column(String, default=current_time, onupdate=current_time)

    productos = relationship('Producto', back_populates='vendedor')
    pedidos = relationship('Pedido', back_populates='comprador')
    comentarios = relationship('Comentario', back_populates='usuario')

class Producto(db.Model):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text, nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)
    categoria = Column(Enum('pescado', 'marisco', 'accesorios_nauticos', 'equipos_de_pesca', 'ropa_accesorios', name='product_categories'), nullable=False)
    stock = Column(Integer, nullable=False)
    vendedor_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    created_at = Column(String, default=current_time)
    updated_at = Column(String, default=current_time, onupdate=current_time)

    vendedor = relationship('Usuario', back_populates='productos')
    lineas_pedido = relationship('LineaPedido', back_populates='producto')
    comentarios = relationship('Comentario', back_populates='producto')

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True)
    comprador_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    total = Column(Numeric(10, 2), nullable=False)
    estado = Column(Enum('pendiente', 'en_proceso', 'completado', 'cancelado', name='order_status'), nullable=False)
    created_at = Column(String, default=current_time)
    updated_at = Column(String, default=current_time, onupdate=current_time)

    comprador = relationship('Usuario', back_populates='pedidos')
    lineas_pedido = relationship('LineaPedido', back_populates='pedido')

class LineaPedido(db.Model):
    __tablename__ = 'lineas_pedido'

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)
    created_at = Column(String, default=current_time)
    updated_at = Column(String, default=current_time, onupdate=current_time)

    pedido = relationship('Pedido', back_populates='lineas_pedido')
    producto = relationship('Producto', back_populates='lineas_pedido')

class Comentario(db.Model):
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    contenido = Column(Text, nullable=False)
    created_at = Column(String, default=current_time)
    updated_at = Column(String, default=current_time, onupdate=current_time)

    producto = relationship('Producto', back_populates='comentarios')
    usuario = relationship('Usuario', back_populates='comentarios')
