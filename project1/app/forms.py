import datetime

from django import forms

class CarSearchForm(forms.Form):
    min_price=forms.IntegerField(
        label="Мінімальна ціна",
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})  #input type & style
    )
    max_price = forms.IntegerField(
        label="Максимальна ціна",
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})  # input type & style
    )
    min_year=forms.IntegerField(
        label="Мінімальний рік",
        required=False,
        min_value=1900,
        widget=forms.NumberInput(attrs={'class':'form-control'})
    )
    max_year=forms.IntegerField(
        label="Максимальний рік",
        required=False,
        min_value=2025,
        widget=forms.NumberInput(attrs={'class':'form-control'})
    )
    model=forms.CharField(
        label="Модель",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mark = forms.CharField(
        label="Марка",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class AddCarForm(forms.Form):
    brand = forms.CharField(
        label="Марка",
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    model=forms.CharField(
        label="Модель",
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    year = forms.IntegerField(
        label="Рік",
        required=True,
        min_value=1900,
        max_value=datetime.datetime.now().year,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    price=forms.IntegerField(
        label="Ціна",
        required=True,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class DeleteCarForm(forms.Form):
    ID=forms.IntegerField(
        label="ID",
        required=True,
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class UpdateCarForm (forms.Form):
    brand = forms.CharField(
        label="Марка",
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    model = forms.CharField(
        label="Модель",
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    year = forms.IntegerField(
        label="Рік",
        required=False,
        min_value=1900,
        max_value=datetime.datetime.now().year,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    price = forms.IntegerField(
        label="Ціна",
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )