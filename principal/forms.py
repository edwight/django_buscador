from django import forms
#from django import newforms as forms

class Buscar_Mapa(forms.Form):

    Busqueda = forms.CharField(widget= forms.TextInput())

"""
TOPIC_CHOICES = (
('general', 'General enquiry'),
('bug', 'Bug report'),
('suggestion', 'Suggestion'),
)
class ContactForm(forms.Form):

    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField()
    sender = forms.EmailField(required=False)
"""

