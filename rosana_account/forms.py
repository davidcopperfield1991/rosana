from django import forms
from django.contrib.auth.models import User
from django.core import validators

class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"لطفا نام خود را وارد کنید", "class" : "form-control"}),
        label="نام"
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"لطفا نام خانوادگی خود را وارد کنید", "class" : "form-control"}),
        label="نام خانوادگی"
    )

class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"لطفا نام خود را وارد کنید"}),
        label="نام کاربری"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"لطفا رمز خود را وارد کنید"}),
        label="کلمه ی عبور "
    )


    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        is_exists_user = User.objects.filter(username=user_name).exists()
        if not is_exists_user:
            raise forms.ValidationError("کاربری با مشخصات فوق ثبت نام نکرده است")

        return user_name


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام خود را وارد کنید"}),
        label="نام کاربری"
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل',
        validators=[
            # validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا رمز خود را وارد کنید"}),
        label="کلمه ی عبور "
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا رمز خود را دوباره وارد کنید"}),
        label="تکرار کلمه ی عبور "
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError("این ایمیل قبلا ثبت نام کرده است")

        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError("داداش تو قبلا ثبت نام کردی")

        return user_name


    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if password != re_password:
            raise forms.ValidationError("کلمه عبور مغایرت دارد")

        return re_password


