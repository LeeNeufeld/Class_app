# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class ClassSentence(models.Model):
    id = models.FloatField(blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_sentence'


class Classified(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    sentenceid = models.IntegerField(blank=True, null=True)
    classification = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classified'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class InProgress(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    sentenceid = models.IntegerField(blank=True, null=True)
    questionid = models.IntegerField(blank=True, null=True)
    classification = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    educational_attainment = models.CharField(max_length=100, blank=True, null=True)
    ethncity = models.CharField(max_length=100, blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    urbanization = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'in_progress'


class NotStarted(models.Model):
    sentenceid = models.IntegerField(blank=True, null=True)
    confidence_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'not_started'


class PartyReleases(models.Model):
    date = models.DateField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    urls = models.TextField(blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_releases'


class QuestionsQuestions(models.Model):
    question = models.TextField()

    class Meta:
        managed = False
        db_table = 'questions_questions'


class ResponseAuthresponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'response_authresponses'


class ResponseCareresponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'response_careresponses'


class ResponseFairresponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'response_fairresponses'


class ResponseLibresponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'response_libresponses'


class ResponseLoyresponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'response_loyresponses'


class ResponseSanresponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'response_sanresponses'


class ResponseTotals(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    care_harm = models.IntegerField(blank=True, null=True)
    care_harm_yes = models.IntegerField(blank=True, null=True)
    care_harm_no = models.IntegerField(blank=True, null=True)
    fairness_cheating = models.IntegerField(blank=True, null=True)
    fairness_cheating_yes = models.IntegerField(blank=True, null=True)
    fairness_cheating_no = models.IntegerField(blank=True, null=True)
    loyalty_betrayal = models.IntegerField(blank=True, null=True)
    loyalty_betrayal_yes = models.IntegerField(blank=True, null=True)
    loyalty_betrayal_no = models.IntegerField(blank=True, null=True)
    authority_subversion = models.IntegerField(blank=True, null=True)
    authority_subversion_yes = models.IntegerField(blank=True, null=True)
    authority_subversion_no = models.IntegerField(blank=True, null=True)
    sanctity_degradation = models.IntegerField(blank=True, null=True)
    sanctity_degradation_yes = models.IntegerField(blank=True, null=True)
    sanctity_degradation_no = models.IntegerField(blank=True, null=True)
    liberty_oppression = models.IntegerField(blank=True, null=True)
    liberty_oppression_yes = models.IntegerField(blank=True, null=True)
    liberty_oppression_no = models.IntegerField(blank=True, null=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'response_totals'


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


class TutorialTutorial(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tutorial_tutorial'


class Twitter(models.Model):
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


class Undetermined(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    sentenceid = models.IntegerField(blank=True, null=True)
    classification = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'undetermined'


class UsersCustomuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    education_attainment = models.TextField(blank=True, null=True)
    ethnicity = models.TextField(blank=True, null=True)
    income = models.TextField(blank=True, null=True)
    nationality = models.CharField(max_length=2, blank=True, null=True)
    screen_name = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=100)
    urbanization = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_customuser'


class UsersCustomuserGroups(models.Model):
    customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_customuser_groups'
        unique_together = (('customuser', 'group'),)


class UsersCustomuserUserPermissions(models.Model):
    customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)
