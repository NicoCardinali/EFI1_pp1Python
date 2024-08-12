from app import db

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais_origen = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre
    
class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)

    def __str__(self) -> str:
        return self.tipo
    
class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    celular = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre
    

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    
    def __str__(self) -> str:
        return self.tipo


class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)

    proveedor = db.relationship('Proveedor', backref=db.backref('accesorios', lazy=True))

    def __str__(self) -> str:
        return self.tipo


class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)

    proveedor = db.relationship('Proveedor', backref=db.backref('marcas', lazy=True))
    fabricante = db.relationship('Fabricante', backref=db.backref('marcas', lazy=True))


    def __str__(self) -> str:
        return self.nombre


class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    caracteristica_id = db.Column(db.Integer, db.ForeignKey('caracteristica.id'), nullable=False)

    marca = db.relationship('Marca', backref=db.backref('modelos', lazy=True))
    categoria = db.relationship('Categoria', backref=db.backref('modelos', lazy=True))
    caracteristica = db.relationship('Caracteristica', backref=db.backref('modelos', lazy=True))

    def __str__(self) -> str:
        return self.nombre
    

    
class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    costo = db.Column(db.Integer, nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)

    modelo = db.relationship('Modelo', backref=db.backref('equipos', lazy=True))

    def __str__(self) -> str:
        return self.nombre
    
     
class Deposito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def __str__(self) -> str:
        return self.nombre
    

class Equipo_en_Deposito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad_equipo = db.Column(db.Integer, nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    deposito_id = db.Column(db.Integer, db.ForeignKey('deposito.id'), nullable=False)

    equipo = db.relationship('Equipo', backref=db.backref('equipos_en_deposito', lazy=True))
    deposito = db.relationship('Deposito', backref=db.backref('equipos_en_deposito', lazy=True))

