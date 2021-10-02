# PROGRAM : day7 assignment
# Programmed by : Bhavya Yasaswini Gadu
# Email-id : GaduBhavya.Yasaswini@Chubb.com
# Date : 24-sept-2021
# Python Version : 3.7.3
# Caveats : None
# License : None


from flask import Flask
from flask import render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABSE_URI'] = 'mysql+pymysql://root:19jg1A0538@localhost/students'
app.config['SECRET_KEY'] = ''

db = SQLAlchemy(app)

class APIUserModel(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))

@app.route('/write', methods = ['POST'])
def write():
    name = request.get_json()['name']
    id = request.get_json()['id']
    email = request.get_json()['email']
    api_user_model = APIUserModel(name=name,email=email,id=id)
    save_to_database = db.session()
    try:
        save_to_database.add(api_user_model)
        save_to_database.commit()
    except:
        save_to_database.rollback()
        save_to_database.flush()
    return jsonify({"message":"success"})


@app.route('/', methods = ['GET'])
def fetch():
    data = APIUserModel.query.all()
    data_all = []
    for data in data:
        data_all.append({"id":data.id, "name":data.name, "email":data.email})
    return jsonify(data_all)


@app.route('/update/<int:id>', methods = ['PATCH'])
def update(id):
    name = request.get_json()['name']
    email = request.get_json()['email']
    save_to_database = db.session()
    try:
        api_user_model = APIUserModel.query.filter_by(id=id).first()
        n,e = api_user_model.name, api_user_model.email
        api_user_model.name = name
        api_user_model.email = email
        save_to_database.commit()
    except:
        return jsonify({"message":"error in update"})
    data = APIUserModel.query.filter_by(id=id).first()
    return jsonify([{"name":n,"id":data.id,"email":e},{"name":data.name,"id":data.id,"email":data.email}])

@app.route('/delete/<int:id>',methods = ['DELETE'])
def delete(id):
    try:
        save_to_database = db.session()
        data = APIUserModel.query.filter_by(id=id).first()
        APIUserModel.query.filter_by(id=id).delete()
        save_to_database.commit()
    except:
        return jsonify({"message":"error in delete"})
    return jsonify({"id":data.id,"name":data.name,"email":data.email})

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True, port = 5000)