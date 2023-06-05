from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.hashers import check_password
from .models import Block



class BlockForm(forms.ModelForm):
    block_number = forms.CharField(
        required=True,
        label='Block Number',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Block Number'}),
        error_messages={
            'required': 'Block number is required'
        }
    )
    name_of_person = forms.CharField(
        required=True,
        label='Name of Person',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Person Name'}),
        error_messages={
            'required': 'Name of person is required'
        }
    )

    varient = forms.CharField(
        required=True,
        label='Verient',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Verient'}),
        error_messages={
            'required': 'Verient is required'
        }
    )
    VARIENT_CHOICES = (
        ("CARRARA WHITE", "CARRARA WHITE"),
        ("STATUARIETTO", "STATUARIETTO"),
        ("ARABESCATO BRECCIA", "ARABESCATO BRECCIA"),
        ("BIANCO LASA", "BIANCO LASA"),
        ("MACAEL WHITE", "MACAEL WHITE"),
        ("CALACATTA", "CALACATTA"),
    )
    varient = forms.ChoiceField(
        required=True,
        label='Verient',
        initial='',
        widget=forms.Select(
            attrs={'class': "form-control"}),
        choices=VARIENT_CHOICES,
        error_messages={
            'required': 'Verient is required'
        }
    )
    BENCH_NUMBER = (("1","Step No. 1"),("2","Step No. 2"),("3","Step No. 3"),("4","Step No. 4"),("5","Step No. 5"),("6","Step No. 6"),("7","Step No. 7"),("8","Step No. 8"),("9","Step No. 9"),("10","Step No. 10"))
    bench_number = forms.ChoiceField(
        required=True,
        label='Verient',
        initial='',
        widget=forms.Select(
            attrs={'class': "form-control"}),
        choices=BENCH_NUMBER,
        error_messages={
            'required': 'Bench nummber is required'
        }
    )

    block_length = forms.FloatField(
        required=True,
        label='Block Length',
        widget=forms.NumberInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Block length'}),
        error_messages={
            'required': 'Block length is required'
        }
    )

    block_height = forms.FloatField(
        required=True,
        label='Block Height',
        widget=forms.NumberInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Block height'}),
        error_messages={
            'required': 'Block height is required'
        }
    )

    block_width = forms.FloatField(
        required=True,
        label='Block Width',
        widget=forms.NumberInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Block Width'}),
        error_messages={
            'required': 'Block Width is required'
        }
    )

    block_picture = forms.ImageField(
        required=False,
        label='Block Picture',
        initial='',
        widget=forms.FileInput(
            attrs={'class': "form-control ", 'placeholder': ''}),
        
    )

    class Meta:
        model = Block
        fields= ['block_number','varient','bench_number','name_of_person','block_picture','block_length','block_height','block_width']

    def clean_block_number(self):
        data = self.cleaned_data
        block_number = data.get('block_number')
        if block_number == "" or block_number is None:
            raise ValidationError(self.fields['block_number'].error_messages['required'])
        return block_number


    def clean_varient(self):
        data = self.cleaned_data
        varient = data.get('varient')
        if varient == "" or varient is None:
            raise ValidationError(self.fields['varient'].error_messages['required'])
        return varient
    
    def clean_bench_number(self):
        data = self.cleaned_data
        bench_number = data.get('bench_number')
        if bench_number == "" or bench_number is None:
            raise ValidationError(self.fields['bench_number'].error_messages['required'])
        return int(bench_number)
    

    def clean_name_of_person(self):
        data = self.cleaned_data
        name_of_person = data.get('name_of_person')
        if name_of_person == "" or name_of_person is None:
            raise ValidationError(self.fields['name_of_person'].error_messages['required'])
        return name_of_person
    

    def clean_block_picture(self):
        data = self.cleaned_data
        block_picture = data.get('block_picture')
        print(block_picture,"<<<<<< data")

        return block_picture

    def clean_block_length(self):
        data = self.cleaned_data
        block_length = data.get('block_length')
        if block_length == "" or block_length is None:
            raise ValidationError(self.fields['block_length'].error_messages['required'])
        return block_length
    
    def clean_block_height(self):
        data = self.cleaned_data
        block_height = data.get('block_height')
        if block_height == "" or block_height is None:
            raise ValidationError(self.fields['block_height'].error_messages['required'])
        return block_height
    
    def clean_block_width(self):
        data = self.cleaned_data
        block_width = data.get('block_width')
        if block_width == "" or block_width is None:
            raise ValidationError(self.fields['block_width'].error_messages['required'])
        return block_width