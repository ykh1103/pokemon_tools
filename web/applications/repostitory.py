from typing import List
from ..models import Types
from ..models import Skills
from ..models import Pokemons
from ..models import DeckSets
from ..models import SkillSets
import datetime


# 格納場所
# わざの情報の格納場所
class SkillView:
    id = None
    name = None
    type_id = None
    type_name = None

    def __init__(self, skills: Skills, type: Types):
        self.id = skills.id
        self.name = skills.name
        self.type_id = type.id
        self.type_name = type.name


# ポケモン情報の格納場所
class PokemonView:
    id = None
    name = None
    icon = None
    type1_id = None
    type1_name = None
    type2_id = None
    type2_name = None

    def __init__(self, pokemon: Pokemons, type1: Types, type2: Types):
        self.id = pokemon.id
        self.name = pokemon.name
        self.icon = pokemon.icon
        if type1:
            self.type1_id = type1.id
            self.type1_name = type1.name
        if type2:
            self.type2_id = type2.id
            self.type2_name = type2.name


# デッキ内ポケモンの情報の格納場所
class DeckPokemonView:
    deck_set_id = None
    deck_id = None
    pokemon_view = None
    skill_views = None

    def __init__(self, deckSet: DeckSets,
                 pokemon_view: PokemonView,
                 skill_views: List[SkillView]):
        self.deck_set_id = deckSet.id
        self.deck_id = deckSet.deck_id
        self.pokemon_view = pokemon_view
        self.skill_views = skill_views


# デッキ内ポケモンのわざの格納場所
class SkillPokemonView:
    deck_set_id = None
    skill_id = None
    skill_name = None
    pokemon_view = None

    def __init__(self, deckSet: DeckSets,
                 skillSet: SkillSets,
                 skills: Skills,
                 pokemon_view: PokemonView):
        self.deck_set_id = deckSet.id
        self.skill_id = skillSet.skill_id
        self.skill_name = skills.name
        self.pokemon_view = pokemon_view


# データベース操作
# DeckSetsへ保存
def save_deck_sets(deck_id, pokemon_id):
    return DeckSets(deck_id=deck_id, pokemon_id=pokemon_id,
                    created_date=datetime.datetime.now(), created_by="kawano").save()


# DeckSetから削除
def delete_deck_sets(deck_set_id):
    return DeckSets.objects.filter(id=deck_set_id).delete()


# SkillSetsへ保存
def save_skill_sets(deck_set_id, skill_id):
    SkillSets(deck_set_id=deck_set_id, skill_id=skill_id,
              created_date=datetime.datetime.now(), created_by="kawano").save()


# SkillSetsから削除
def delete_skill_sets(skill_id, deck_set_id):
    SkillSets.objects.filter(skill_id=skill_id, deck_set_id=deck_set_id).delete()

