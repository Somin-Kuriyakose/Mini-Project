# from django import forms
# from .models import Profile

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ["age", "education_level", "interests", "allow_data_sharing"]
#         widgets = {
#             "interests": forms.CheckboxSelectMultiple,
#         }
from django import forms
from .models import Profile, Skill
from careers.models import Interest

class ProfileForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Profile
        fields = ["age", "education_level", "interests", "skills"]
