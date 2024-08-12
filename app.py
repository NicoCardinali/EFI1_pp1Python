from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/celulares_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Fabricante, Caracteristica, Proveedor, Categoria, Accesorio, Marca, Modelo, Equipo, Equipo_en_Deposito, Deposito

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route("/fabricante", methods=['POST', 'GET'])
def fabricante():
    fabricantes = Fabricante.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        pais = request.form['pais']
        nuevo_fabricante = Fabricante(nombre=nombre,pais_origen=pais)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return redirect(url_for('fabricante'))
    
    return render_template("fabricante.html",fabricantes = fabricantes)

@app.route("/editar_fabricante", methods=['POST', 'GET'])
def editar_fabricante():
    fabricantes = Fabricante.query.all()

    if request.method == 'POST':
        fabricante_buscado = request.form['fabricante_buscado']
        nombre = request.form['nombre']
        pais = request.form['pais']
        fabricante = Fabricante.query.get_or_404(fabricante_buscado)
        fabricante.nombre = nombre
        fabricante.pais_origen = pais
        db.session.commit()
        return redirect(url_for('editar_fabricante'))

    return render_template("editar_fabricante.html",fabricantes=fabricantes)

@app.route("/borrar_fabricante", methods=['POST', 'GET'])
def borrar_fabricante():
    fabricantes = Fabricante.query.all()
    error_message = None

    if request.method == 'POST':
        fabricante_buscado = request.form['fabricante_buscado']
        fabricante = Fabricante.query.get_or_404(fabricante_buscado)
        try:
            db.session.delete(fabricante)
            db.session.commit()
            return redirect(url_for('borrar_fabricante'))
        except IntegrityError:
            db.session.rollback()
            error_message = 'No se puede eliminar el fabricante porque tiene marcas asociadas.'

    return render_template("borrar_fabricante.html",fabricantes=fabricantes,error_message=error_message)


@app.route("/deposito", methods=['POST', 'GET'])
def deposito():
    depositos = Deposito.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_deposito = Deposito(nombre=nombre)
        db.session.add(nuevo_deposito)
        db.session.commit()
        return redirect(url_for('deposito'))
    
    return render_template("deposito.html",depositos = depositos)

@app.route("/editar_deposito", methods=['POST', 'GET'])
def editar_deposito():
    depositos = Deposito.query.all()

    if request.method == 'POST':
        deposito_buscado = request.form['deposito_buscado']
        nombre = request.form['nombre']
        deposito = Deposito.query.get_or_404(deposito_buscado)
        deposito.nombre = nombre
        db.session.commit()
        return redirect(url_for('editar_deposito'))

    return render_template("editar_deposito.html",depositos=depositos)

@app.route("/borrar_deposito", methods=['POST', 'GET'])
def borrar_deposito():
    depositos = Deposito.query.all()
    error_message = None

    if request.method == 'POST':
        deposito_buscado = request.form['deposito_buscado']
        deposito = Deposito.query.get_or_404(deposito_buscado)
        try:
            db.session.delete(deposito)
            db.session.commit()
            return redirect(url_for('borrar_deposito'))
        except IntegrityError:
            db.session.rollback()
            error_message = 'No se puede eliminar el deposito porque tiene equipos asociados.'

    return render_template("borrar_deposito.html",depositos=depositos,error_message=error_message)


@app.route("/caracteristica", methods=['POST', 'GET'])
def caracteristica():
    caracteristicas = Caracteristica.query.all()

    if request.method == 'POST':
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        nueva_caracteristica = Caracteristica(tipo=tipo, descripcion=descripcion)
        db.session.add(nueva_caracteristica)
        db.session.commit()
        return redirect(url_for('caracteristica'))
    
    return render_template("caracteristica.html",caracteristicas = caracteristicas)


@app.route("/editar_caracteristica", methods=['POST', 'GET'])
def editar_caracteristica():
    caracteristicas = Caracteristica.query.all()

    if request.method == 'POST':
        caracteristica_buscada = request.form['caracteristica_buscada']
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        caracteristica = Caracteristica.query.get_or_404(caracteristica_buscada)
        caracteristica.tipo = tipo
        caracteristica.descripcion = descripcion
        db.session.commit()
        return redirect(url_for('editar_caracteristica'))

    return render_template("editar_caracteristica.html",caracteristicas=caracteristicas)

@app.route("/borrar_caracteristica", methods=['POST', 'GET'])
def borrar_caracteristica():
    caracteristicas = Caracteristica.query.all()
    error_message = None

    if request.method == 'POST':
        caracteristica_buscada = request.form['caracteristica_buscada']
        caracteristica = Caracteristica.query.get_or_404(caracteristica_buscada)
        try:
            db.session.delete(caracteristica)
            db.session.commit()
            return redirect(url_for('borrar_caracteristica'))
        except IntegrityError:
            db.session.rollback()
            error_message = 'No se puede eliminar la caracteristica porque tiene modelos asociados.'

    return render_template("borrar_caracteristica.html",caracteristicas=caracteristicas,error_message=error_message)

@app.route("/proveedor", methods=['POST', 'GET'])
def proveedor():
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        celular = request.form['celular']
        nuevo_proveedor = Proveedor(nombre=nombre, correo=correo, celular=celular)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return redirect(url_for('proveedor'))

    return render_template("proveedor.html",proveedores = proveedores)

@app.route("/editar_proveedor", methods=['POST', 'GET'])
def editar_proveedor():
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        proveedor_buscado = request.form['proveedor_buscado']
        nombre = request.form['nombre']
        correo = request.form['correo']
        celular = request.form['celular']
        proveedor = Proveedor.query.get_or_404(proveedor_buscado)
        proveedor.nombre = nombre
        proveedor.correo = correo
        proveedor.celular = celular
        db.session.commit()
        return redirect(url_for('editar_proveedor'))

    return render_template("editar_proveedor.html",proveedores=proveedores)

@app.route("/borrar_proveedor", methods=['POST', 'GET'])
def borrar_proveedor():
    proveedores = Proveedor.query.all()
    error_message = None

    if request.method == 'POST':
        proveedor_buscado = request.form['proveedor_buscado']
        proveedor = Proveedor.query.get_or_404(proveedor_buscado)
        try:
            db.session.delete(proveedor)
            db.session.commit()
            return redirect(url_for('borrar_proveedor'))
        except IntegrityError:
            db.session.rollback()
            error_message = 'No se puede eliminar el proveedor porque tiene accesorios o marcar asociados.'

    return render_template("borrar_proveedor.html",proveedores=proveedores,error_message=error_message)

@app.route("/categoria", methods=['POST', 'GET'])
def categoria():
    categorias = Categoria.query.all()

    if request.method == 'POST':
        tipo = request.form['tipo']
        nueva_categoria = Categoria(tipo=tipo)
        db.session.add(nueva_categoria)
        db.session.commit()
        return redirect(url_for('categoria'))    

    return render_template("categoria.html",categorias = categorias)

@app.route("/editar_categoria", methods=['POST', 'GET'])
def editar_categoria():
    categorias = Categoria.query.all()

    if request.method == 'POST':
        categoria_buscada = request.form['categoria_buscada']
        tipo = request.form['tipo']
        categoria = Categoria.query.get_or_404(categoria_buscada)
        categoria.tipo = tipo
        db.session.commit()
        return redirect(url_for('editar_categoria'))

    return render_template("editar_categoria.html",categorias=categorias)

@app.route("/borrar_categoria", methods=['POST', 'GET'])
def borrar_categoria():
    categorias = Categoria.query.all()
    error_message = None

    if request.method == 'POST':
        categoria_buscada = request.form['categoria_buscada']
        categoria = Categoria.query.get_or_404(categoria_buscada)
        try:
            db.session.delete(categoria)
            db.session.commit()
            return redirect(url_for('borrar_categoria'))
        except IntegrityError:
            db.session.rollback()
            error_message = 'No se puede eliminar la categoria porque tiene modelos asociados.'

    return render_template("borrar_categoria.html",categorias=categorias,error_message=error_message)

@app.route("/accesorio", methods = ['POST', 'GET'])
def accesorio():
    accesorios = Accesorio.query.all()
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        proveedor = request.form['proveedor']
        nuevo_accesorio = Accesorio(tipo=tipo,descripcion=descripcion,proveedor_id=proveedor)
        db.session.add(nuevo_accesorio)
        db.session.commit()
        return redirect(url_for('accesorio'))

    return render_template("accesorio.html",accesorios = accesorios, proveedores = proveedores)

@app.route("/editar_accesorio", methods=['POST', 'GET'])
def editar_accesorio():
    accesorios = Accesorio.query.all()
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        accesorio_buscado = request.form['accesorio_buscado']
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        proveedor = request.form['proveedor']
        accesorio = Accesorio.query.get_or_404(accesorio_buscado)
        accesorio.tipo = tipo
        accesorio.descripcion = descripcion
        accesorio.proveedor_id = proveedor
        db.session.commit()
        return redirect(url_for('editar_accesorio'))

    return render_template("editar_accesorio.html", accesorios=accesorios, proveedores=proveedores)

@app.route("/borrar_accesorio", methods=['POST', 'GET'])
def borrar_accesorio():
    accesorios = Accesorio.query.all()
    error_message = None

    if request.method == 'POST':
        accesorio_buscado = request.form['accesorio_buscado']
        accesorio = Accesorio.query.get_or_404(accesorio_buscado)
        try:
            db.session.delete(accesorio)
            db.session.commit()
            return redirect(url_for('borrar_accesorio'))
        except IntegrityError:
            db.session.rollback()
            error_message = 'No se puede eliminar el accesorio porque tiene productos asociados.'

    return render_template("borrar_accesorio.html", accesorios=accesorios, error_message=error_message)

@app.route("/marca", methods = ['POST', 'GET'])
def marca():
    marcas = Marca.query.all()
    proveedores = Proveedor.query.all()
    fabricantes = Fabricante.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        proveedor = request.form['proveedor']
        fabricante = request.form['fabricante']
        nueva_marca = Marca(nombre=nombre,proveedor_id=proveedor,fabricante_id=fabricante)
        db.session.add(nueva_marca)
        db.session.commit()
        return redirect(url_for('marca'))

    return render_template("marca.html",marcas = marcas, proveedores = proveedores, fabricantes = fabricantes)

@app.route("/editar_marca", methods=['POST', 'GET'])
def editar_marca():
    marcas = Marca.query.all()
    proveedores = Proveedor.query.all()
    fabricantes = Fabricante.query.all()

    if request.method == 'POST':
        marca_buscada = request.form['marca_buscada']
        nombre = request.form['nombre']
        proveedor = request.form['proveedor']
        fabricante = request.form['fabricante']
        marca = Marca.query.get_or_404(marca_buscada)
        marca.nombre = nombre
        marca.proveedor_id = proveedor
        marca.fabricante_id = fabricante
        db.session.commit()
        return redirect(url_for('editar_marca'))

    return render_template("editar_marca.html", marcas=marcas, proveedores=proveedores, fabricantes=fabricantes)

@app.route("/borrar_marca", methods=['POST', 'GET'])
def borrar_marca():
    marcas = Marca.query.all()
    error_message = None

    if request.method == 'POST':
        marca_buscada = request.form['marca_buscada']
        marca = Marca.query.get_or_404(marca_buscada)
        try:
            db.session.delete(marca)
            db.session.commit()
            return redirect(url_for('borrar_marca'))
        except IntegrityError:
            db.session.rollback()
            error_message = 'No se puede eliminar la marca porque tiene modelos asociados.'

    return render_template("borrar_marca.html", marcas=marcas, error_message=error_message)


@app.route("/modelo", methods = ['POST', 'GET'])
def modelo():
    modelos = Modelo.query.all()
    marcas = Marca.query.all()
    categorias = Categoria.query.all()
    caracteristicas = Caracteristica.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        categoria = request.form['categoria']
        caracteristica = request.form['caracteristica']
        nuevo_modelo = Modelo(nombre=nombre,marca_id=marca,categoria_id=categoria,caracteristica_id=caracteristica)
        db.session.add(nuevo_modelo)
        db.session.commit()
        return redirect(url_for('modelo'))

    return render_template("modelo.html",modelos=modelos, marcas=marcas,categorias=categorias, caracteristicas=caracteristicas)

@app.route("/editar_modelo", methods=['POST', 'GET'])
def editar_modelo():
    modelos = Modelo.query.all()
    marcas = Marca.query.all()
    categorias = Categoria.query.all()
    caracteristicas = Caracteristica.query.all()

    if request.method == 'POST':
        modelo_buscado = request.form['modelo_buscado']
        nombre = request.form['nombre']
        marca = request.form['marca']
        categoria = request.form['categoria']
        caracteristica = request.form['caracteristica']
        modelo = Modelo.query.get_or_404(modelo_buscado)
        modelo.nombre = nombre
        modelo.marca_id = marca
        modelo.categoria_id = categoria
        modelo.caracteristica_id = caracteristica
        db.session.commit()
        return redirect(url_for('editar_modelo'))

    return render_template("editar_modelo.html", modelos=modelos, marcas=marcas, categorias=categorias, caracteristicas=caracteristicas)

@app.route("/borrar_modelo", methods=['POST', 'GET'])
def borrar_modelo():
    modelos = Modelo.query.all()
    error_message = None

    if request.method == 'POST':
        modelo_buscado = request.form['modelo_buscado']
        modelo = Modelo.query.get_or_404(modelo_buscado)
        try:
            db.session.delete(modelo)
            db.session.commit()
            return redirect(url_for('borrar_modelo'))
        except IntegrityError:
            db.session.rollback()
            error_message = 'No se puede eliminar el modelo porque tiene equipos asociados.'

    return render_template("borrar_modelo.html", modelos=modelos, error_message=error_message)

@app.route("/equipo", methods = ['POST', 'GET'])
def equipo():
    equipos = Equipo.query.all()
    modelos = Modelo.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        anio = request.form['anio']
        costo = request.form['costo']
        modelo = request.form['modelo']
        nuevo_equipo = Equipo(nombre=nombre, anio=anio, costo=costo, modelo_id=modelo)
        db.session.add(nuevo_equipo)
        db.session.commit()
        return redirect(url_for('equipo'))

    return render_template("equipo.html", equipos = equipos, modelos = modelos)

@app.route("/editar_equipo", methods=['POST', 'GET'])
def editar_equipo():
    equipos = Equipo.query.all()
    modelos = Modelo.query.all()

    if request.method == 'POST':
        equipo_buscado = request.form['equipo_buscado']
        nombre = request.form['nombre']
        anio = request.form['anio']
        costo = request.form['costo']
        modelo = request.form['modelo']
        equipo = Equipo.query.get_or_404(equipo_buscado)
        equipo.nombre = nombre
        equipo.anio = anio
        equipo.costo = costo
        equipo.modelo_id = modelo
        db.session.commit()
        return redirect(url_for('editar_equipo'))

    return render_template("editar_equipo.html", equipos=equipos, modelos=modelos)

@app.route("/borrar_equipo", methods=['POST', 'GET'])
def borrar_equipo():
    equipos = Equipo.query.all()
    error_message = None

    if request.method == 'POST':
        equipo_buscado = request.form['equipo_buscado']
        equipo = Equipo.query.get_or_404(equipo_buscado)
        try:
            db.session.delete(equipo)
            db.session.commit()
            return redirect(url_for('borrar_equipo'))
        except IntegrityError:
            db.session.rollback()
            error_message = 'No se puede eliminar el equipo porque está asociado a un depósito.'

    return render_template("borrar_equipo.html", equipos=equipos, error_message=error_message)

@app.route("/mover_stock", methods=['POST', 'GET'])
def mover_stock():
    equipos = Equipo.query.all()
    depositos = Deposito.query.all()
    equipos_en_deposito = Equipo_en_Deposito.query.all()

    if request.method == 'POST':
        equipo_id = request.form['equipo']
        deposito_id = request.form['deposito']
        cantidad = int(request.form['cantidad'])

        movimiento_existente = Equipo_en_Deposito.query.filter_by(
            equipo_id=equipo_id,
            deposito_id=deposito_id
        ).first()

        if movimiento_existente:
            nueva_cantidad = movimiento_existente.cantidad_equipo + cantidad

            if nueva_cantidad < 0:
                if movimiento_existente.cantidad_equipo < abs(cantidad):
                    error_message = "La cantidad de salida es mayor que la existencia actual en el depósito."
                    return render_template("mover_stock.html", equipos=equipos, depositos=depositos, equipos_en_deposito=equipos_en_deposito, error_message=error_message)
                else:
                    movimiento_existente.cantidad_equipo = nueva_cantidad
            else:
                movimiento_existente.cantidad_equipo = nueva_cantidad
        else:
            if cantidad < 0:
                error_message = "No se puede registrar una salida sin existencia previa en el depósito."
                return render_template("mover_stock.html", equipos=equipos, depositos=depositos, equipos_en_deposito=equipos_en_deposito, error_message=error_message)
            else:
                nuevo_movimiento = Equipo_en_Deposito(
                    cantidad_equipo=cantidad,
                    equipo_id=equipo_id,
                    deposito_id=deposito_id
                )
                db.session.add(nuevo_movimiento)

        db.session.commit()
        return redirect(url_for('mover_stock'))

    return render_template("mover_stock.html", equipos=equipos, depositos=depositos, equipos_en_deposito=equipos_en_deposito)


@app.route("/consultar_stock", methods=['POST', 'GET'])
def consultar_stock():
    equipo_id = request.form.get('equipo')
    stock_total = 0
    equipo_nombre = None

    if equipo_id:
        equipos_en_deposito = Equipo_en_Deposito.query.filter_by(equipo_id=equipo_id).all()
        stock_total = sum(equipo.cantidad_equipo for equipo in equipos_en_deposito)
        equipo_nombre = Equipo.query.filter_by(id=equipo_id).first().nombre

    equipos = Equipo.query.all()
    depositos = Deposito.query.all()
    equipos_en_deposito = Equipo_en_Deposito.query.all()

    return render_template("consultar_stock.html", equipos=equipos,depositos=depositos,equipos_en_deposito=equipos_en_deposito,stock_total=stock_total,equipo_nombre=equipo_nombre)
