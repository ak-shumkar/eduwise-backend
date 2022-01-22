from django import forms

from utils.data.iso_codes import ISO_CODES
from .models import Country, City


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        exclude = ['iso_code']

    def save(self, commit=True):
        obj = super(CountryForm, self).save(commit=False)
        if not obj.iso_code:
            obj.iso_code = ISO_CODES[obj.name]
        obj.save()
        return obj

    def clean(self):
        cleaned_data = super(CountryForm, self).clean()
        if not cleaned_data.get('iso_code'):
            cleaned_data['iso_code'] = ISO_CODES[cleaned_data.get('name')]
        if Country.objects.filter(iso_code=cleaned_data.get('iso_code')).exists():
            raise forms.ValidationError(f'Country {cleaned_data.get("name")} already exists')


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

    def clean(self):
        cleaned_data = super(CityForm, self).clean()
        country = cleaned_data.get('country')
        province = cleaned_data.get('province')
        name = cleaned_data.get('name')
        if City.objects.filter(country=country,
                               province=province,
                               name=name).exists():
            raise forms.ValidationError(f'Country {cleaned_data.get("name")} already exists')
