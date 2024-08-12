# Sistema de Gestión de Ventas

```Este proyecto es un sistema de gestión de ventas desarrollado con Flask, Flask-SQLAlchemy y Flask-Migrate. Está diseñado para gestionar información relacionada con celulares, incluyendo fabricantes, proveedores, características, marcas, modelos, equipos y depósitos. También permite mover stock entre depósitos y consultar el stock disponible.```

## Clonar el proyecto
- ```git clone https://github.com/NicoCardinali/EFI1_pp1Python```
##### Crear el entorno virtual
- ```python3 -m venv env```
##### Activar el entorno virtual
- ```source env/bin/activate```
##### Instalar requerimientos
- ``` pip install -r requirements.txt```
##### Correr el proyecto
- ```flask run --reload```


##### Navegar por la aplicación

- ```Inicio: Página principal del sistema```
- ```Fabricantes: Agregar, editar y eliminar fabricantes```
- ```Depositos: Agregar, editar y eliminar depósitos```
- ```Caracteristicas: Agregar, editar y eliminar características```
- ```Proveedores: Agregar, editar y eliminar proveedores```
- ```Categorías: Agregar, editar y eliminar categorías```
- ```Accesorios: Agregar, editar y eliminar accesorios```
- ```Marcas: Agregar, editar y eliminar marcas```
- ```Modelos: Agregar, editar y eliminar modelos```
- ```Equipos: Agregar, editar y eliminar equipos```
- ```Mover Stock: Mover stock entre depósitos```
- ```Consultar Stock: Consultar el stock disponible de un equipo```


##### Estructura de la Base de Datos
- ```Fabricante: id, nombre, pais_origen```
- ```Caracteristica: id, tipo, descripcion```
- ```Proveedor: id, nombre, correo, celular```
- ```Categoria: id, tipo```
- ```Accesorio: id, tipo, descripcion, proveedor_id```
- ```Marca: id, nombre, fabricante_id, proveedor_id```
- ```Modelo: id, nombre, marca_id, categoria_id, caracteristica_id```
- ```Equipo: id, nombre, anio, costo, modelo_id```
- ```Deposito: id, nombre```
- ```Equipo_en_Deposito: id, cantidad_equipo, equipo_id, deposito_id```