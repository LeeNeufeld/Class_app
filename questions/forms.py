from django.forms import ModelForm,widgets,NullBooleanSelect, NullBooleanField, modelformset_factory
from django import forms
from .models import Questions

QuestionsFormSet = modelformset_factory(Questions, fields=('id', 'question'))
formset = QuestionsFormSet(queryset=Questions.objects.order_by('?')[0:1])


        
