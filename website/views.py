from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):

    #check to see if logging in

    if  request.method == 'POST':
        username=request.POST['user_name']
        password=request.POST['password']
        #Authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'you have been Logged In !')
            return redirect('home')
        else:
            messages.success(request,"There Was an Error Logging In , Please Try Again...")
            return redirect('home')
    else:
        return render(request,'home.html',{})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    return render(request,'register.html',{})
 







# """
# from django.shortcuts import render, redirect
# ➡️ Importe :

# render : pour afficher une page HTML.

# redirect : pour rediriger quelqu’un vers une autre page (après login par exemple).


# from django.contrib.auth import authenticate, login, logout
# ➡️ Importe des fonctions toutes prêtes pour :

# authenticate : vérifie si l'utilisateur existe et si le mot de passe est correct.

# login : connecte l'utilisateur (le garde en session).

# logout : déconnecte un utilisateur (pas encore utilisé dans ton code).


# from django.contrib import messages
# ➡️ Importe le système de messages (genre « Bravo, vous êtes connecté ! »).


# def home(request):
# ➡️ Tu crées une fonction appelée home, qui reçoit request :

# request contient tout ce que l’utilisateur envoie (clics, formulaires, etc.).


#     if request.method == 'POST':
# ➡️ Si l’utilisateur a soumis un formulaire (POST) :

# Tu veux vérifier son nom d’utilisateur et son mot de passe.

#         username = request.POST['user_name']
#         password = request.POST['password']
# ➡️ Tu récupères ce que l’utilisateur a écrit dans les champs du formulaire :

# user_name → dans le <input name="user_name">

# password → dans le <input name="password">

# Donc :

# Ce que l’utilisateur tape	Est récupéré ici
# Nom d’utilisateur	request.POST['user_name']
# Mot de passe	request.POST['password']

#     user = authenticate(request, username=username, password=password)
# ➡️ Django vérifie dans la base de données :

# Si un utilisateur existe avec ce nom et mot de passe.

# Si oui, user sera un objet utilisateur.

# Sinon, user sera None.


#     if user is not None:
# ➡️ Si l’utilisateur existe (c’est pas None) :


#     login(request, user)
# ➡️ Django connecte cet utilisateur :

# Il crée une session (le user reste connecté sur tout le site).


#     messages.success(request, 'you have been logged in !')
# ➡️ Il envoie un petit message qu’on pourra afficher sur la page.

# Par exemple : ✅ "You have been logged in!"


#     return redirect('home')
# ➡️ Redirige vers la page d’accueil (home).

# Cela réinitialise le formulaire et affiche que l’utilisateur est connecté.


#     return render(request, 'home.html', {})
# ➡️ Sinon (si ce n’est pas un formulaire POST, donc juste quelqu’un qui ouvre la page),
# on affiche simplement home.html.

# Résumé rapide 🔥
# Action de l’utilisateur	Ce que Django fait
# Il ouvre la page	Il montre le formulaire.
# Il remplit et envoie	Django vérifie username/password.
# Si ok	Il connecte et redirige vers home.
# Si pas ok	Il reste sur la même page (pas de login).



# 📚 Voici les choses essentielles que tu dois comprendre pour ton projet :

#         Fonction	                                Sert à quoi	                            Important de savoir...

        
#         render(request, template, context)      	Affiche une page HTML.      	        Oui, c’est tout le temps utilisé.

#         redirect('url_name')    	                Redirige vers une autre page.       	Oui, très utile.

#         authenticate(request, username, password)   Vérifie si l’utilisateur existe.        Oui, surtout pour login.

#         login(request, user)	                    Connecte l’utilisateur.     	        Oui, pour gérer les sessions.

#         logout(request)	                            Déconnecte l’utilisateur.           	Oui, très simple à utiliser.

#         messages.success(request, 'message')	    Affiche un message temporaire.      	Non obligatoire, mais joli.

#         request.POST[...]       	                Récupère ce que l’utilisateur a envoyé dans un formulaire.      	Oui, essentiel pour tous les formulaires.

# 🧠 Comment apprendre efficacement ?

# Regarde ton tuto → mais fais en même temps sur ton PC.

# Quand un mot ou une fonction ne te parle pas ➔ demande-moi ou cherche vite ce que ça fait.

# Pas besoin d’apprendre par cœur. ➔ Utiliser > mémoriser naturellement.

# Avec la pratique, tu vas voir que tu vas te souvenir naturellement des choses. 🔥




# """
