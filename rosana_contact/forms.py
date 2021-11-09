from django import forms
from django.core import validators

class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام و نام خانوادگی خود را وارد کنید", "class" : "form-control"}),
        label=" نام و نام خانوادگی",
        validators=[
            validators.MaxLengthValidator(150,"زیاد نوشتی")
                    ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "لطفا ایمیل خود را وارد کنید","class" : "form-control"}),
        label=" ایمیل",
        validators=[
            validators.MaxLengthValidator(150, "زیاد نوشتی")
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا عنوان خود را وارد کنید","class" : "form-control"}),
        label="عنوان ",
        validators=[
            validators.MaxLengthValidator(150, "زیاد نوشتی")
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "لطفا متن خود را وارد کنید" , "class" : "form-control" , "rows" :8}),
        label="متن"

    )