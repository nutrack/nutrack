from django.forms import ModelForm
from food_rec.models import Food


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'protein', 'fat', 'carbs', 'rating', 'rater']