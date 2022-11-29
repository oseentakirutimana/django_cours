from django.forms import ModelForm
from app.models import Order

class CustomerForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'