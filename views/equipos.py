from flask import Blueprint, request, make_response,jsonify
from flask_jwt_extended import (
    get_jwt,
    jwt_required
)
from app import db
from models import Fabricante, Caracteristica, Proveedor, Categoria, Accesorio, Marca, Modelo, Equipo, Deposito

from schemas import FabricanteSchema,CaracteristicaSchema,ProveedorSchema,CategoriaSchema,AccesorioSchema,MarcaSchema,ModeloSchema,EquipoSchema,DepositoSchema

equipo_bp = Blueprint('equipos',__name__)

@equipo_bp.route('/fabricantes',methods=['GET','POST'])
def fabricante():
    if request.method == 'POST':
      @jwt_required()
      def fabricante_post():
        additional_data = get_jwt()
        administrador = additional_data.get('administrador')
        if administrador is True:
                data = request.get_json()

                errors = FabricanteSchema().validate(data)
                if errors:
                    return make_response(jsonify(errors))

                nuevo_fabricante = Fabricante(
                    nombre = data.get('nombre'),
                    pais_origen = data.get('pais_origen')
                )
                db.session.add(nuevo_fabricante)
                db.session.commit()
                return FabricanteSchema().dump(nuevo_fabricante)

        
        else:
            return jsonify(Mensaje="El usuario no es administrador")    
      return fabricante_post()   

    return FabricanteSchema().dump(Fabricante.query.all(), many=True)


@equipo_bp.route('/caracteristicas', methods=['GET', 'POST'])
def caracteristica():
    if request.method == 'POST':
      @jwt_required()
      def caracteristica_post():
        additional_data = get_jwt()
        administrador = additional_data.get('administrador')
        if administrador is True:
            data = request.get_json()
            errors = CaracteristicaSchema().validate(data)
            if errors:
                return make_response(jsonify(errors))
            nueva_caracteristica = Caracteristica(
                tipo=data.get('tipo'),
                descripcion=data.get('descripcion')
            )
            db.session.add(nueva_caracteristica)
            db.session.commit()
            return CaracteristicaSchema().dump(nueva_caracteristica)
        else:
            return jsonify({"Mensaje": "El usuario no es administrador"})
      return caracteristica_post()
        
    return CaracteristicaSchema().dump(Caracteristica.query.all(),many=True)

@equipo_bp.route('/proveedores', methods=['GET', 'POST'])
def proveedor():
    if request.method == 'POST':
     @jwt_required()
     def proveedor_post():
        additional_data = get_jwt()
        administrador = additional_data.get('administrador')
        if administrador:
            data = request.get_json()
            errors = ProveedorSchema().validate(data)
            if errors:
                return jsonify(errors)

            nuevo_proveedor = Proveedor(
                nombre=data.get('nombre'),
                correo=data.get('correo'),
                celular=data.get('celular')
            )
            db.session.add(nuevo_proveedor)
            db.session.commit()
            return ProveedorSchema().dump(nuevo_proveedor)
        else:
            return jsonify({"Mensaje": "El usuario no es administrador"})
     return proveedor_post()

    return ProveedorSchema().dump(Proveedor.query.all(),many=True)


@equipo_bp.route('/categorias', methods=['GET', 'POST'])
def categoria():
    if request.method == 'POST':
     @jwt_required()
     def categoria_post():
        additional_data = get_jwt()
        administrador = additional_data.get('administrador')
        if administrador:
            data = request.get_json()
            errors = CategoriaSchema().validate(data)
            if errors:
                return jsonify(errors)

            nueva_categoria = Categoria(
                tipo=data.get('tipo')
            )
            db.session.add(nueva_categoria)
            db.session.commit()
            return CategoriaSchema().dump(nueva_categoria)
        else:
            return jsonify({"Mensaje": "El usuario no es administrador"})
     return categoria_post()
    return CategoriaSchema().dump(Categoria.query.all(), many=True)


@equipo_bp.route('/accesorios', methods=['GET', 'POST'])
def accesorio():
    if request.method == 'POST':
     @jwt_required()
     def accesorio_post():
        additional_data = get_jwt()
        administrador = additional_data.get('administrador')
        if administrador:
            data = request.get_json()
            errors = AccesorioSchema().validate(data)
            if errors:
                return jsonify(errors)

            nuevo_accesorio = Accesorio(
                tipo=data.get('tipo'),
                descripcion=data.get('descripcion'),
                proveedor_id=data.get('proveedor_id')
            )
            db.session.add(nuevo_accesorio)
            db.session.commit()
            return AccesorioSchema().dump(nuevo_accesorio)
        else:
            return jsonify({"Mensaje": "El usuario no es administrador"})
     return accesorio_post()
    return AccesorioSchema().dump(Accesorio.query.all(), many=True)


@equipo_bp.route('/marcas',methods=['GET','POST'])
def marca():
    if request.method == 'POST':
     @jwt_required()
     def marca_post():
        additional_data = get_jwt()
        administrador = additional_data.get('administrador')
        if administrador:
            data = request.get_json()
            errors = MarcaSchema().validate(data)
            if errors:
                return make_response(jsonify(errors))

            nueva_marca = Marca(
                nombre = data.get('nombre'),
                fabricante_id = data.get('fabricante_id'),
                proveedor_id = data.get('proveedor_id')
            )
            db.session.add(nueva_marca)
            db.session.commit()
            return MarcaSchema().dump(nueva_marca)
        else:
            return jsonify({"Mensaje": "El usuario no es administrador"})
     return marca_post()
    return MarcaSchema().dump(Marca.query.all(),many=True)

@equipo_bp.route('/modelos',methods=['GET','POST'])
def modelo():
    if request.method == 'POST':
     @jwt_required()
     def modelo_post():
        additional_data = get_jwt()
        administrador = additional_data.get('administrador')
        if administrador:
            data = request.get_json()
            errors = ModeloSchema().validate(data)
            if errors:
                return make_response(jsonify(errors))
            nuevo_modelo = Modelo(
                nombre = data.get('nombre'),
                marca_id = data.get('marca_id'),
                categoria_id = data.get('categoria_id'),
                caracteristica_id = data.get('caracteristica_id')
            )
            db.session.add(nuevo_modelo)
            db.session.commit()
            return ModeloSchema().dump(nuevo_modelo)
        else:
            return jsonify({"Mensaje": "El usuario no es administrador"})
     return modelo_post()
    return ModeloSchema().dump(Modelo.query.all(), many=True)


@equipo_bp.route('/depositos',methods=['GET','POST'])
def deposito():
    if request.method == 'POST':
     @jwt_required()
     def deposito_post():
      additional_data = get_jwt()
      administrador = additional_data.get('administrador')
      if administrador:
            data = request.get_json()
            errors = DepositoSchema().validate(data)
            if errors:
                return make_response(jsonify(errors))

            nuevo_deposito = Deposito(
                nombre = data.get('nombre'),
            )
            db.session.add(nuevo_deposito)
            db.session.commit()
            return DepositoSchema().dump(nuevo_deposito)
      
      else:
        return jsonify(Mensaje="El usuario no es administrador")       
     return deposito_post()
    return DepositoSchema().dump(Deposito.query.all(), many=True)


@equipo_bp.route('/equipos',methods=['GET','POST'])
def equipo():
    if request.method == 'POST':
     @jwt_required()
     def equipo_post():
      additional_data = get_jwt()
      administrador = additional_data.get('administrador')
      if administrador is True:
            data = request.get_json()
            errors = EquipoSchema().validate(data)
            if errors:
                return make_response(jsonify(errors))

            nuevo_equipo = Equipo(
                nombre = data.get('nombre'),
                anio = data.get('anio'),
                costo = data.get('costo'),
                modelo_id = data.get('modelo_id')
            )
            db.session.add(nuevo_equipo)
            db.session.commit()
            return EquipoSchema().dump(nuevo_equipo)
      
      else:
        return jsonify(Mensaje="El usuario no es administrador")   
     return equipo_post()    
    return EquipoSchema().dump(Equipo.query.all(),many=True)

@equipo_bp.route('/editar_equipo/<int:id>', methods=['POST'])
@jwt_required()
def editar_equipo(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')
    if not administrador:
        return jsonify({"Mensaje": "El usuario no es administrador"})

    equipo = Equipo.query.get(id)
    if not equipo:
        return jsonify({"error": "Equipo no encontrado"})

    data = request.get_json()
    errors = EquipoSchema().validate(data)
    if errors:
        return make_response(jsonify(errors))

    equipo.nombre = data.get('nombre')
    equipo.anio = data.get('anio')
    equipo.costo = data.get('costo')
    equipo.modelo_id = data.get('modelo_id')
    
    db.session.commit()
    return jsonify({"Mensaje": "Equipo actualizado con éxito"})

@equipo_bp.route('/borrar_equipo/<int:id>', methods=['POST'])
@jwt_required()
def borrar_equipo(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')
    if not administrador:
        return jsonify({"Mensaje": "El usuario no es administrador"})

    equipo = Equipo.query.get(id)
    if not equipo:
        return jsonify({"error": "Equipo no encontrado"})

    db.session.delete(equipo)
    db.session.commit()
    
    return jsonify({"Mensaje": "Equipo eliminado con éxito"})
