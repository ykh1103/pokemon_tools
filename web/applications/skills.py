from ..models import SkillSets
from django.shortcuts import render
from django.shortcuts import redirect
from .repostitory import save_skill_sets
from .repostitory import delete_skill_sets


# SkillSetsにわざを登録
def register_skill(request):
    requests = {
        "skill_id": None,
        "deck_set_id": None,
        "criteria": None,
    }
    # Requestの処理/分岐の削除
    for k in requests:
        requests[k] = request.POST.get(key=k)
    if not requests["skill_id"]:
        return render(request, 'web/error.html')
    if not requests["deck_set_id"]:
        return render(request, 'web/error.html')
    if len(SkillSets.objects.filter(deck_set_id=requests["deck_set_id"])) >= 4:
        msg = "登録できるわざは４つまでです"
        return redirect(f"/skills?deck_set_id={requests['deck_set_id']}&msg={msg}")
    if len(SkillSets.objects.filter(skill_id=requests["skill_id"], deck_set_id=requests["deck_set_id"])) >= 1:
        msg = "すでに覚えているわざは登録できません"
        return redirect(f"/skills?deck_set_id={requests['deck_set_id']}&msg={msg}")
    # 登録
    save_skill_sets(requests["deck_set_id"], skill_id=requests["skill_id"])
    print(f"id：{requests['skill_id']}が登録されました")
    return redirect(f"/skills?deck_set_id={requests['deck_set_id']}")


# SkillSetsのわざを削除
def delete_skill(request):
    requests = {
        "deck_set_id": None,
        "skill_id": None
    }
    # Requestの処理/分岐の削除
    for k in requests:
        requests[k] = request.POST.get(key=k)
    if not requests["skill_id"]:
        return render(request, 'web/error.html')
    if len(SkillSets.objects.filter(skill_id=requests["skill_id"], deck_set_id=requests["deck_set_id"])) == 0:
        msg = "デッキにわざがいません"
        return redirect(f"/skills?deck_set_id={requests['deck_set_id']}&msg={msg}")
    # 削除
    delete_skill_sets(requests["skill_id"], requests["deck_set_id"])
    print(f"skill_id={requests['skill_id']},deck_set_id={requests['deck_set_id']}が削除されました")
    return redirect(f"/skills?deck_set_id={requests['deck_set_id']}")
