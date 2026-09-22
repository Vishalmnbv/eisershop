from django import forms
from .models import Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review', 'image', 'size', 'color', 'country']
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Apna review yahan likhein...'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }