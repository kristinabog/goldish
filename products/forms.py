from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ReviewForm(forms.ModelForm):
    """
    Form to add a new review to a product
    """

    class Meta:
        """
        Class to exclude certain fields
        """
        model = Review
        fields = (
            'review_text',
        )


class ProductForm(forms.ModelForm):
    """
    Form to add a new product to store
    """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = display_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border border-dark rounded-0'
