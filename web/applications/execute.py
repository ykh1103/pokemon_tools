from ..models import Types
from ..models import Skills
from ..models import Pokemons
from ..models import DeckSets
from ..models import SkillSets
from .repostitory import PokemonView
from .repostitory import SkillView
from .repostitory import DeckPokemonView


# ポケモンの情報をPokemonViewへ格納
def build_pokemon_view_by_pokemon(pokemon):
    type1s = Types.objects.filter(id=pokemon.type_id1)
    type2s = Types.objects.filter(id=pokemon.type_id2)
    return PokemonView(
        pokemon,
        None if len(type1s) == 0 else type1s[0],
        None if len(type2s) == 0 else type2s[0],
    )


# idからポケモンを取得してbuild_pokemon_view_by_pokemonへ渡す
def get_pokemon_by_id(id):
    pokemons = Pokemons.objects.filter(id=id)
    if len(pokemons) != 1:
        return None
    return build_pokemon_view_by_pokemon(pokemons[0])


# ポケモンの名前を部分一致検索
def get_pokemons_like_name(name):
    pokemons = Pokemons.objects.filter(name__contains=name)
    return list(map(lambda pokemon: build_pokemon_view_by_pokemon(pokemon), pokemons))


# わざの情報をSkillViewへ格納
def build_skill_view_by_skill(skill: Skills):
    type = Types.objects.filter(id=skill.type_id)
    return SkillView(skill, None if len(type) == 0 else type[0])


# deck_idからデッキ内のポケモンを取得
def get_deck_pokemon_by_deck_id(deck_id):
    deck_sets = DeckSets.objects.filter(deck_id=deck_id)
    return list(map(lambda deck_set: get_deck_pokemon_by_deck_set_id(deck_set.id), deck_sets))


# デッキ内のポケモンの情報をDeckPokemonViewへ格納
def get_deck_pokemon_by_deck_set_id(deck_set_id):
    deck_sets = DeckSets.objects.filter(id=deck_set_id)
    if len(deck_sets) != 1:
        return None
    skill_ids = list(map(lambda skill_set: skill_set.skill_id, SkillSets.objects.filter(deck_set_id=deck_set_id)))
    skills = Skills.objects.filter(id__in=skill_ids)
    skill_views = list(map(lambda skill: build_skill_view_by_skill(skill), skills))
    return DeckPokemonView(deck_sets[0], get_pokemon_by_id(deck_sets[0].pokemon_id), skill_views)


# idからわざを取得
def get_skills_in_ids(ids):
    return list(map(lambda x: build_skill_view_by_skill(x), Skills.objects.filter(id__in=ids)))
