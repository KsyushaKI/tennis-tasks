from django import forms


class SelectionOfParameters(forms.Form):

    FAVORITE_COLORS_CHOICES = [
    ('Белый', 'Белый'),
    ('Синий', 'Синий'),
    ('Желтый', 'Желтый'),
    ('Красный', 'Красный'),
    ('Оранжевый', 'Оранжевый'),
    ('Зеленый', 'Зеленый'),
    ]

    colors = forms.MultipleChoiceField(required=True, choices=FAVORITE_COLORS_CHOICES)
    colors_count = forms.IntegerField(required=True)
    pause_time = forms.IntegerField(required=True)
    full_time = forms.IntegerField(required=True)

#  initial='00:00:00'