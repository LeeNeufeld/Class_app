from django.db import models


# model for storing all sentence pulled from Twitter
class Twitter(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    user_id = models.TextField(blank=True, null=True)
    status_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    screen_name = models.TextField(blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'twitter'

# model for storing sentences pulled from Party Press Releases


class PartyReleases(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    date = models.DateField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    urls = models.TextField(blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_releases'

# Model for the classified table in DB


class Classified(models.Model):
    sentenceid = models.IntegerField(blank=True, null=True)
    classification = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classified'

# Model for the in_progress table in DB


class InProgress(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    sentenceid = models.IntegerField(blank=True, null=True)
    sentence = models.TextField(null=True)
    questionid = models.IntegerField(blank=True, null=True)
    classification = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    educational_attainment = models.CharField(
        max_length=100, blank=True, null=True)
    ethncity = models.CharField(max_length=100, blank=True, null=True)
    income = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    urbanization = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'in_progress'

# Model for the not_started table in DB


class NotStarted(models.Model):
    sentenceid = models.IntegerField(blank=True, null=True)
    confidence_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'not_started'

# Model for the sentences table in DB


class Sentences(models.Model):
    sentence = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    confidence_score = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    source_id = models.TextField(blank=True, null=True)
    user_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sentences'

# Model for the undetermined table in DB


class Undetermined(models.Model):
    sentenceid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'undetermined'

# Model for the User Response table in the DB


class UserResponse(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    userid = models.IntegerField(blank=True, null=True)
    sentenceid = models.IntegerField(blank=True, null=True)
    classification = models.TextField(blank=True, null=True)
