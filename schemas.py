from app import ma
from marshmallow import validates, ValidationError

from models import User, Fabricante, Caracteristica, Proveedor, Categoria, Accesorio, Marca, Modelo, Equipo, Deposito

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    password = ma.auto_field()
    is_admin = ma.auto_field()

    @validates('username')
    def validate_username(self, value):
        user = User.query.filter_by(username=value).first()
        if user:
            raise ValidationError("Ya existe ese usuario")
        return value
    
class UserMinimalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()

class FabricanteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Fabricante

    id = ma.auto_field()
    nombre = ma.auto_field()
    pais_origen = ma.auto_field()

    @validates('nombre')
    def validate_username(self, value):
        fabricante = Fabricante.query.filter_by(nombre=value).first()
        if fabricante:
            raise ValidationError("Ya existe ese fabricante")
        return value
    
class CaracteristicaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Caracteristica

    id = ma.auto_field()
    tipo = ma.auto_field()
    descripcion = ma.auto_field()

    @validates('tipo')
    def validate_tipo(self, value):
        caracteristica = Caracteristica.query.filter_by(tipo=value).first()
        if caracteristica:
            raise ValidationError("Ya existe una característica con este tipo")
        return value
    
class ProveedorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Proveedor

    id = ma.auto_field()
    nombre = ma.auto_field()
    correo = ma.auto_field()
    celular = ma.auto_field()

    @validates('nombre')
    def validate_nombre(self, value):
        if Proveedor.query.filter_by(nombre=value).first():
            raise ValidationError("Ya existe un proveedor con ese nombre.")
        return value

class CategoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Categoria

    id = ma.auto_field()
    tipo = ma.auto_field()

    @validates('tipo')
    def validate_tipo(self, value):
        if Categoria.query.filter_by(tipo=value).first():
            raise ValidationError("Ya existe una categoría con ese tipo.")
        return value

class AccesorioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Accesorio
    
    id = ma.auto_field()
    tipo = ma.auto_field()
    descripcion = ma.auto_field()
    proveedor_id = ma.auto_field()
    proveedor = ma.Nested(ProveedorSchema)

    @validates('proveedor_id')
    def validate_proveedor_id(self, value):
        if not Proveedor.query.filter_by(id=value).first():
            raise ValidationError("No existe el proveedor.")
        return value

class MarcaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marca
    
    id = ma.auto_field()
    nombre = ma.auto_field()
    fabricante_id = ma.auto_field()
    fabricante = ma.Nested(FabricanteSchema)
    proveedor_id = ma.auto_field()
    proveedor = ma.Nested(ProveedorSchema)

    @validates('nombre')
    def validate_nombre(self, value):
        if Marca.query.filter_by(nombre=value).first():
            raise ValidationError("Ya existe una marca con ese nombre.")
        return value

    @validates('proveedor_id')
    def validate_proveedor_id(self, value):
        if not Proveedor.query.filter_by(id=value).first():
            raise ValidationError("No existe el proveedor.")
        return value

    @validates('fabricante_id')
    def validate_fabricante_id(self, value):
        if not Fabricante.query.filter_by(id=value).first():
            raise ValidationError("No existe el fabricante.")
        return value

class ModeloSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Modelo
    
    id = ma.auto_field()
    nombre = ma.auto_field()
    marca_id = ma.auto_field()
    marca = ma.Nested(MarcaSchema)
    categoria_id = ma.auto_field()
    categoria = ma.Nested(CategoriaSchema)
    caracteristica_id = ma.auto_field()
    caracteristica = ma.Nested(CaracteristicaSchema)

    @validates('categoria_id')
    def validate_categoria_id(self, value):
        if not Categoria.query.filter_by(id=value).first():
            raise ValidationError("No existe la categoria.")
        return value
    
    @validates('marca_id')
    def validate_marca_id(self, value):
        if not Marca.query.filter_by(id=value).first():
            raise ValidationError("No existe la marca.")
        return value
    
    @validates('caracteristica_id')
    def validate_caracteristica_id(self, value):
        if not Caracteristica.query.filter_by(id=value).first():
            raise ValidationError("No existe la caracteristica.")
        return value

class DepositoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Deposito
    
    id = ma.auto_field()
    nombre = ma.auto_field()

    @validates('nombre')
    def validate_nombre(self, value):
        if Deposito.query.filter_by(nombre=value).first():
            raise ValidationError("Ya existe un deposito con ese nombre.")
        return value


class EquipoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Equipo
    
    id = ma.auto_field()
    nombre = ma.auto_field()
    anio = ma.auto_field()
    costo = ma.auto_field()
    modelo_id = ma.auto_field()
    modelo = ma.Nested(ModeloSchema)

    @validates('anio')
    def validate_anio(self, value):
        if value > 2024:
            raise ValidationError("El año debe ser menor o igual a 2024.")
        return value

    @validates('costo')
    def validate_costo(self, value):
        if value <= 0:
            raise ValidationError("El costo debe ser mayor a 0.")
        return value

    @validates('modelo_id')
    def validate_modelo_id(self, value):
        if not Modelo.query.filter_by(id=value).first():
            raise ValidationError("No existe el modelo.")
        return value

