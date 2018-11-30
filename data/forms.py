from django import forms
from .models import Review, Image
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.forms import inlineformset_factory


class ReviewForm(forms.ModelForm):
    rate = forms.FloatField(widget=forms.HiddenInput())
    
    class Meta:
        model = Review
        fields = ['content', 'rate']
        
    
class ImageForm(forms.ModelForm):
    image = ProcessedImageField(
                            processors=[ResizeToFill(716,537)],
                            format="JPEG",
                            options={'quality':90},
                                    )
                                    
    class Meta:
        model = Image
        fields = ['image']
        
        
ImageFormSet = inlineformset_factory(Review, Image, form=ImageForm, extra=3)