from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Adress'}))
    first_name= forms.CharField(label="",max_length=100 ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name= forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))


    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'




    
"""
🗂️ Ton fichier forms.py

from django.contrib.auth.forms import UserCreationForm
🔹 Ce que tu dois retenir :
Tu importes un formulaire prêt à l’emploi de Django pour créer un utilisateur (avec username, mot de passe, confirmation).


from django.contrib.auth.models import User
🔹 Tu importes le modèle utilisateur de Django.
👉 Ce modèle est lié à la base de données (utilisé pour enregistrer les utilisateurs).


from django import forms
🔹 Tu importes la base pour créer des champs personnalisés avec forms.CharField, forms.EmailField, etc.

📌 Création de ton formulaire personnalisé :

class SignUpForm(UserCreationForm):
🔹 Tu crées un formulaire qui hérite de UserCreationForm, donc tu récupères déjà :

username

password1

password2

Et tu vas ajouter des champs en plus (email, prénom, nom).

➕ Ajout de champs personnalisés

    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address'
    }))
✅ Tu ajoutes un champ email avec :

Aucun label (label = "")

Une classe CSS form-control (pour Bootstrap)

Un texte d’exemple (placeholder)


    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
✅ Tu ajoutes le prénom (first name) avec les mêmes améliorations.

    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
✅ Pareil pour le nom de famille.

🧬 Déclaration de la classe Meta

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
🔹 Meta dit à Django :

Le modèle à utiliser est User

Voici les champs à afficher dans le formulaire

✅ Cela dit : « Je veux un formulaire pour créer un utilisateur avec ces infos ».

🔧 Méthode __init__ : personnalisation
Tu ajoutes cette méthode :


def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
🔹 C’est juste la manière standard de surcharger un constructeur.
🔹 Tu récupères le formulaire de base, puis tu modifies certains champs.

Ensuite tu as :

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
    self.fields['username'].label = ''
    self.fields['username'].help_text = '<span class="form-text text-muted"><small>...texte explicatif...</small></span>'
✅ Tu personnalises le champ username pour :

Avoir du Bootstrap (form-control)

Un placeholder

Aucun label

Un texte d’aide (comme sur les sites d’inscription)

Pareil pour les mots de passe :


    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    ...
✅ Idem : style Bootstrap + texte explicatif.

✅ En résumé :
        Tu as fait un formulaire personnalisé qui :

        Hérite des champs de base (UserCreationForm)

        Ajoute des champs supplémentaires (email, first_name, last_name)

        Personnalise l’affichage Bootstrap

💡 À retenir pour ton projet :

        Tu n’as pas besoin de tout apprendre par cœur.

        Mais c’est bien de savoir que :

        UserCreationForm te simplifie la vie.

        __init__ sert à modifier l’apparence des champs.

Le formulaire va s'afficher dans ton HTML et s’occuper de la validation."""
    