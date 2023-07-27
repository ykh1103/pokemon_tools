from django.shortcuts import render
from django.shortcuts import redirect
from .execute import get_deck_pokemon_by_deck_id
from .repostitory import save_deck_sets
from .repostitory import delete_deck_sets


# DeckSetsにポケモンを登録
def register_deck(request):
    requests = {
        "pokemon_id": None,
        "deck_id": None,
        "criteria": None,
    }
    # Requestの処理/分岐の削除
    for k in requests:
        requests[k] = request.POST.get(key=k)
    if not requests["pokemon_id"]:
        return render(request, 'web/error.html')
    if not requests["deck_id"]:
        return render(request, 'web/error.html')
    if len(get_deck_pokemon_by_deck_id(requests["deck_id"])) >= 6:
        msg = "デッキは６匹までです"
        return redirect(f"/?deck_id={requests['deck_id']}&criteria={requests['criteria']}&msg={msg}")
    # 登録
    save_deck_sets(requests["deck_id"], requests["pokemon_id"])
    print(f"id：{requests['pokemon_id']}が登録されました")
    return redirect(f"/?deck_id={requests['deck_id']}&criteria={requests['criteria']}")


# DeckSetsのポケモンを削除
def delete_deck(request):
    requests = {
        "deck_id": None,
        "deck_set_id": None,
        "criteria": None,
    }
    # Requestの処理/分岐の削除
    for k in requests:
        requests[k] = request.POST.get(key=k)
    if not requests["deck_set_id"]:
        return render(request, 'web/error.html')
    if not requests["deck_id"]:
        return render(request, 'web/error.html')
    if len(get_deck_pokemon_by_deck_id(requests["deck_id"])) == 0:
        msg = "デッキにポケモンがいません"
        return redirect(f"/?deck_id={requests['deck_id']}&criteria={requests['criteria']}&msg={msg}")
    # 削除
    delete_deck_sets(requests["deck_set_id"])
    print(f"id：{requests['deck_set_id']}が削除されました")
    return redirect(f"/?deck_id={requests['deck_id']}&criteria={requests['criteria']}")
