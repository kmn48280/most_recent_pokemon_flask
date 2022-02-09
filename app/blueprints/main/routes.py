from .import bp as main
from flask import request, flash, render_template, url_for, redirect
import requests
from .forms import SearchForm
from flask_login import login_required, current_user
from app.models import Pokemon, User, PokemonUser

@main.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@main.route('/pokedex', methods=['GET','POST'])
@login_required
def pokedex():
    form = SearchForm()
    poke_name = request.form.get('poke_name')
    if request.method == 'POST' and form.validate_on_submit():
        url=f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
        response = requests.get(url)
        if response.ok:
            data = response.json()
            if poke_name in data['forms'][0]['name']:
                poke_dict={
                    "name": data['forms'][0]['name'],

                    "abilities": data['abilities'][0]['ability']['name'],
                                    # data['abilities'][1]['ability']['name']},
        
                    "stats_hp": data['stats'][0]['base_stat'],
                                    
                    
                    "stats_defense": data['stats'][2]['base_stat'],
                                    # data['stats'][2]['base_stat']},

                    "stats_attack": data['stats'][1]['base_stat'],
                                        # data['stats'][1]['base_stat']},

                    "sprite_URL": data['sprites']['front_shiny']
            }
            if poke_name != Pokemon.query.filter_by(name=poke_name):
                new_poke_object = Pokemon()
                new_poke_object.from_poke_dict(poke_dict)
                new_poke_object.add_poke()
                return render_template('pokedex.html.j2', poke = new_poke_object, form = form)
            else:
                flash('You already have this pokemon in your pokedex or you have too many pokemon.','danger')
                #Error Return
                return render_template('pokedex.html.j2', form = form)
    flash('That is not a name of a pokemon', 'danger')
    return render_template('pokedex.html.j2', form=form)


@main.route('/add_to_pokemon_bank/<int:id>', methods=['GET'])
@login_required
def add_to_pokemon_bank(id):
    pokemon = Pokemon.query.get(id)
    if pokemon in current_user.pokemon_bank:
        flash(f'You already have {pokemon.name} in your collection', 'danger')
        return redirect(url_for('main.pokedex'))
    else:
        flash('added', 'success')
        current_user.add_pokemon(pokemon)
        current_user.current_poke()
    return redirect(url_for('main.pokedex'))

@main.route('/del_pokemon_from_bank/<int:id>', methods = ['GET'])
@login_required
def del_pokemon_from_bank(id):
    pokemon = Pokemon.query.get(id)
    if pokemon in current_user.pokemon_bank:
        current_user.delete_poke()
    flash(f'You have deleted {pokemon.name} from your collection', 'warning')
    return redirect(url_for('main.pokedex'))






    



