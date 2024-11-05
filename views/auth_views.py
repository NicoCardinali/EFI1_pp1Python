from datetime import timedelta

from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required
)
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)
from app import db
from models import User
from schemas import UserSchema, UserMinimalSchema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
   data = request.authorization
   username = data.username
   password = data.password

   usuario = User.query.filter_by(username = username).first()


   if usuario and check_password_hash(
      pwhash=usuario.password,
      password=password
   ): 
      access_token = create_access_token(
         identity=username,
         expires_delta=timedelta(minutes=120),
         additional_claims=dict(
            administrador = usuario.is_admin
         )
      )

      return jsonify({'Token': f'{access_token}'})

   return jsonify(Mensaje = 'Usuario o contraseño incorrectos')

@auth_bp.route('/users', methods=['GET','POST'])
@jwt_required()
def users():
   additional_data = get_jwt()
   administrador = additional_data.get('administrador')
   if request.method == 'POST':
      if administrador is True:
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        errors = UserSchema().validate(data)
        if errors:
           return make_response(jsonify(errors))

        try:
            nuevo_usuario = User(
                    username = username,
                    password = generate_password_hash(password),
                is_admin = False,
                )
            db.session.add(nuevo_usuario)
            db.session.commit()
            return jsonify(
            {
                "Mensaje": "usuario creado",
                "usuario":nuevo_usuario.to_dict()
                }
                )
        except:
            return jsonify(
                {
                "Mensaje":"No se pudo crear usuario"
                }
            )
      else:
        return jsonify(Mensaje="El usuario no es administrador") 
          
   usuarios = User.query.all()
   if administrador is True:
       return UserSchema().dump(obj=usuarios, many=True)
   else:
      return UserMinimalSchema().dump(obj=usuarios, many=True)