from django.db import models


class DeckSets(models.Model):
    deck_id = models.IntegerField()
    pokemon_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deck_sets'


class Decks(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decks'


class Pokemons(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=45)
    type_id1 = models.IntegerField()
    type_id2 = models.IntegerField(blank=True, null=True)
    icon = models.TextField()
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemons'


class SkillSets(models.Model):
    deck_set_id = models.IntegerField()
    skill_id = models.IntegerField()
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_sets'


class Skills(models.Model):

    name = models.CharField(max_length=45, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'


class Types(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class WeakTypes(models.Model):
    type_id = models.IntegerField(blank=True, null=True)
    weaktype_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weak_types'
