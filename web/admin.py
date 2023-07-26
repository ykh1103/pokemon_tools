from django.contrib import admin

from .models import DeckSets
from .models import Decks
from .models import Pokemons
from .models import SkillSets
from .models import Skills
from .models import Types
from .models import WeakTypes


admin.site.register(DeckSets)
admin.site.register(Decks)
admin.site.register(Pokemons)
admin.site.register(SkillSets)
admin.site.register(Skills)
admin.site.register(Types)
admin.site.register(WeakTypes)

