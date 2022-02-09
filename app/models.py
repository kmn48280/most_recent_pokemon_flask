from app import db, login
from flask_login import UserMixin, current_user
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash


class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    abilities = db.Column(db.String(150))
    hp = db.Column(db.String(150))
    defense = db.Column(db.String(150))
    attack = db.Column(db.String(150))
    sprite = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Pokemon: {self.id}| {self.name}>'
    
    def from_poke_dict(self, poke_dict):
        self.name = poke_dict['name']
        self.abilities = poke_dict['abilities']
        self.hp = poke_dict['stats_hp']
        self.defense = poke_dict['stats_defense']
        self.attack = poke_dict['stats_attack']
    
    def add_poke(self):
        db.session.add(self)
        db.session.commit()
   
    def delete_poke(self):
        Pokemon.query.filter_by(id=Pokemon.id).delete()
        db.session.commit()

class PokemonUser(db.Model):
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(200))
    icon = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default = dt.utcnow)
    pokemon_bank = db.relationship(
        'Pokemon', 
        secondary = 'pokemon_user',
        backref='users', 
        lazy='dynamic')

    def current_poke():
        return list(User.pokemon_bank)

    def __repr__(self):
        return f"<User: {self.id} | {self.email}>"
    
    def add_pokemon(self, pokemon):
            self.pokemon_bank.append(pokemon)
            db.session.commit()

    def remove_pokemon(self, pokemon):
            self.pokemon_bank.remove(pokemon)
            db.session.commit()


    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    def check_hashed_password(self, login_password): 
        return check_password_hash(self.password, login_password)

    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = self.hash_password(data['password'])
        self.icon = data['icon']
        

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def get_icon(self):
        return f'/static/images/svg/{self.icon}.svg'
   

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


    



