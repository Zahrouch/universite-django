from django.urls import path
from .views import liste_cours, accueil, ajouter_cours, modifier_cours, supprimer_cours, liste_enseignant, ajouter_enseignant, modifier_enseignant, supprimer_enseignant,connexion_utilisateur, deconnexion_utilisateur

urlpatterns = [
    
    path('',accueil, name='accueil'),
    path('cours/', liste_cours, name='liste_cours'),
    path('ajouter/', ajouter_cours, name= 'ajouter_cours'),
    path('modifier/<int:id>/', modifier_cours, name='modifier_cours'),
    path('supprimer/<int:id>/', supprimer_cours, name='supprimer_cours'),
    path('enseignant/', liste_enseignant, name='liste_enseignant'),
    path('ajouter/', ajouter_enseignant, name= 'ajouter_enseignant'),
    path('modifier/<int:id>/', modifier_enseignant, name='modifier_enseignant'),
    path('supprimer/<int:id>/', supprimer_enseignant, name='supprimer_enseignant'),
    path('connexion/',connexion_utilisateur, name='connexion'),
    path('deconnexion/',deconnexion_utilisateur, name='deconnexion'),
]
