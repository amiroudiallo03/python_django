from django.db import models
from faicon.fields import FAIconField
from colorfield.fields import ColorField



# Create your models here.
class Banner(models.Model):
    titre = models.CharField(max_length= 200)
    image = models.ImageField(upload_to = 'Banner')
    description = models.CharField(max_length= 500)
    
    
    def __str__(self):
        return self.titre

class About(models.Model):
    image = models.ImageField(upload_to = 'Abouts')
    titre = models.CharField(max_length= 200)
    sous_titre = models.TextField(max_length= 500)


class Prestation(models.Model):
    titre = models.CharField(max_length= 200)
    description = models.TextField(max_length= 500)
    image = models.ImageField(upload_to = 'Banner')
    
    def __str__(self):
        return self.titre

class Card(models.Model):
    icone = FAIconField()
    titre = models.CharField(max_length= 200)
    description = models.CharField(max_length= 500)
    color = ColorField(default='#009cea')


class Categorie(models.Model):
    nom = models.CharField(max_length= 200, null= False, blank= True)

    def __str__(self):
        return self.nom

class Image(models.Model):
    categorie = models.ForeignKey(Categorie, null= True, on_delete= models.SET_NULL, blank= False)
    image = models.ImageField()
    titre = models.CharField(max_length= 200)
    details = models.TextField(max_length= 500)
    titre_details = models.CharField(max_length=200)

    def __str__(self):
        return self.titre



class Testimonial(models.Model):
    description = models.TextField(max_length= 500)
    image = models.ImageField()
    nom = models.CharField(max_length= 200)
    travail = models.CharField(max_length= 200)

class Team(models.Model):
    image = models.ImageField()
    nom = models.CharField(max_length= 200)
    poste = models.TextField(max_length= 200)
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()

class Partenaire(models.Model):
    logo = models.ImageField()
    nom = models.CharField


class Pack(models.Model):
    nom = models.CharField(max_length= 200, null= False, blank= False)
    prix = models.FloatField()
    periode = models.DateField()
    etiquettes = models.BooleanField(default= False)
    couleur = ColorField(default= '#009cea')

    def __str__(self):
        return self.nom

class Avantage(models.Model):
    libele = models.CharField(max_length= 200)
    libele_barre = models.BooleanField(default= False)
    pack = models.ForeignKey(Pack, on_delete = models.SET_NULL, null= True)


    def __str__(self):
        return self.libele

class Faq(models.Model):
    question = models.TextField(max_length= 1000)
    reponse = models.TextField(max_length=1000)

    def __str__(self):
        return self.question


class Contact(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    sujet = models.TextField(max_length= 1000)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.nom

    
class Newsletter(models.Model):
    email = models.EmailField()

class Website(models.Model):
    nom_site = models.CharField(max_length= 200)
    description_service = models.CharField(max_length=200)
    description_partenaire = models.CharField(max_length=200)
    description_Portofolio = models.CharField(max_length= 200)
    description_temoignage = models.CharField(max_length= 200)
    description_team = models.CharField(max_length=200)
    description_partenaire = models.CharField(max_length= 200)
    email = models.EmailField()
    call = models.CharField(max_length=200)
    location = models.TextField()

    
    
    