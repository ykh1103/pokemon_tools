from django.shortcuts import render
from ..models import Types
from .execute import get_pokemons_like_name
from .execute import get_deck_pokemon_by_deck_id
from .execute import get_deck_pokemon_by_deck_set_id
from .execute import get_skills_in_ids
import requests as r


# 必要な情報を検索画面へ渡す
def index(request):
    requests = {
        "criteria": None,
        "deck_id": None,
        "msg": None
    }
    # Requestの処理/分岐の削除
    for k in requests:
        requests[k] = request.GET.get(key=k)
    if not requests["criteria"]:
        requests["criteria"] = "フシギダネ"
    if not requests["deck_id"]:
        return render(request, 'web/no_deck.html')
    context = {
        'pokemon_views': get_pokemons_like_name(requests["criteria"]),
        'deck_pokemons': get_deck_pokemon_by_deck_id(requests["deck_id"]),
        "deck_id": requests["deck_id"],
        "criteria": requests["criteria"],
        "msg": requests["msg"],
        "type_compatibility": type_compatibility(requests["deck_id"])
    }
    return render(request, 'web/search.html', context)


# Deck内のポケモンの覚える技一覧を表示
def select_skills(request):
    requests = {
        "deck_set_id": None,
        "msg": None
    }
    # Requestの処理/分岐の削除
    for k in requests:
        requests[k] = request.GET.get(key=k)
    if not requests["deck_set_id"]:
        return render(request, 'web/error.html')
    deck_pokemon = get_deck_pokemon_by_deck_set_id(requests["deck_set_id"])
    # 表示
    pokemons_url = f"https://pokeapi.co/api/v2/pokemon/{deck_pokemon.pokemon_view.id}/"
    pokemons_response = r.get(pokemons_url).json()
    skill_ids = list(map(lambda x: x["move"]["url"].split("/")[-2], pokemons_response["moves"]))
    skills = get_skills_in_ids(skill_ids)
    context = {
        "skills": skills,
        "deck_pokemon": deck_pokemon,
        "msg": requests["msg"],
    }
    return render(request, 'web/skills.html', context)


# 不足しているタイプの表示
def type_compatibility(deck_id):
    # デッキ内のわざ一覧を取得
    types_list = Types.objects.filter(id__lt=19)
    for deck_pokemon in get_deck_pokemon_by_deck_id(deck_id):
        for val in deck_pokemon.skill_views:
            # 「こうかはばつぐん」を返す
            match val.type_id:
                case 2:
                    types_list = [o for o in types_list if o.id not in [1, 6, 9, 15, 17]]
                case 3:
                    types_list = [o for o in types_list if o.id not in [2, 7, 12]]
                case 4:
                    types_list = [o for o in types_list if o.id not in [12, 18]]
                case 5:
                    types_list = [o for o in types_list if o.id not in [4, 6, 9, 10, 13]]
                case 6:
                    types_list = [o for o in types_list if o.id not in [3, 7, 10, 15]]
                case 7:
                    types_list = [o for o in types_list if o.id not in [12, 14, 17]]
                case 8:
                    types_list = [o for o in types_list if o.id not in [8, 14]]
                case 9:
                    types_list = [o for o in types_list if o.id not in [6, 15, 18]]
                case 10:
                    types_list = [o for o in types_list if o.id not in [7, 9, 12, 15]]
                case 11:
                    types_list = [o for o in types_list if o.id not in [5, 6, 10]]
                case 12:
                    types_list = [o for o in types_list if o.id not in [5, 6, 11]]
                case 13:
                    types_list = [o for o in types_list if o.id not in [3, 11]]
                case 14:
                    types_list = [o for o in types_list if o.id not in [4, 2]]
                case 15:
                    types_list = [o for o in types_list if o.id not in [3, 5, 12, 16]]
                case 16:
                    types_list = [o for o in types_list if o.id not in [16]]
                case 17:
                    types_list = [o for o in types_list if o.id not in [8, 14]]
                case 18:
                    types_list = [o for o in types_list if o.id not in [2, 16, 17]]
    # 表示
    for weakness_type in types_list:
        print(weakness_type.name + "タイプに有効なわざがありません")
    return types_list
