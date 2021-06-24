import datetime

from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
from django.forms import widgets


class Client(models.Model):
    user = models.OneToOneField(User, related_name="ClientUser", verbose_name='Utilisateur', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, default='')
    civilite = models.CharField(verbose_name='Civilite', max_length=10, default='')
    tele = models.TextField(verbose_name='Telephone', max_length=14, default='')
    adresse1 = models.TextField(verbose_name='Adresse 1', max_length=100, default='')
    adresse2 = models.TextField(verbose_name='Adresse 2', max_length=150, default='')
    codepostal = models.TextField(verbose_name='Zip', max_length=150, default='')
    city = models.TextField(verbose_name='Ville', max_length=100, default='')
    country = models.TextField(verbose_name='Pays', max_length=100, default='')

    class Meta:
        verbose_name = 'Client'


class Message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tele = models.TextField(null=True, max_length=100)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Message'


class Category(models.Model):
    name = models.CharField(verbose_name='Nom', max_length=100, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categorie'


class ChildCategory(models.Model):
    Category = models.ForeignKey(Category, verbose_name='Categorie', related_name='ChildCategory',
                                 on_delete=models.CASCADE)
    name = models.CharField(verbose_name='nom', max_length=100, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sous categorie'


class CategoryHistory(models.Model):
    childcategory = models.ForeignKey(ChildCategory, verbose_name='Sous categorie', related_name='ChildCategoryHistory',
                                      on_delete=models.CASCADE, )
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.childcategory.name

    class Meta:
        verbose_name = 'Categories historique'


class Article(models.Model):
    title = models.CharField(verbose_name='Titre', max_length=100)
    childcategory = models.ForeignKey(ChildCategory, verbose_name='Sous categorie', related_name='ArticleChildCategory',
                                      on_delete=models.CASCADE, max_length=50)
    info = models.TextField(verbose_name='Infos produit', null=True)
    options = models.TextField(verbose_name='Options - Finitions', null=True)
    conseil = models.TextField(verbose_name='Conseils Techniques', null=True)
    complementes = models.TextField(verbose_name='Produits complémentaires', null=True)
    pdf = models.FileField(verbose_name='Specification Pdf', null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'

    def images(self):
        return ArticleImage.objects.filter(article=self.id)


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, verbose_name='Article', related_name="articleimages", on_delete=models.CASCADE)
    name = models.FileField(verbose_name='Nom', upload_to='static/product_images')
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'Article image'


class Size1(models.Model):
    width = models.FloatField(verbose_name='Longeur', null=True)
    height = models.FloatField(verbose_name='Largeur', null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.width) + '-' + str(self.height)

    class Meta:
        verbose_name = 'Size'


class PaperType(models.Model):
    name = models.CharField(verbose_name='Nom', max_length=100, null=True)
    price = models.FloatField(verbose_name='Prix', null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Papier type'


class PaperColor(models.Model):
    name = models.CharField(verbose_name='Nom', max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Papier coleur'


class FontColor(models.Model):
    name = models.CharField(verbose_name='Nom', max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Font coleur'


class Side(models.Model):
    name = models.CharField(verbose_name='Nom', max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name


class Orientation(models.Model):
    name = models.CharField(verbose_name='Nom', max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Orientation'


class Finition(models.Model):
    name = models.CharField(verbose_name='Nom', max_length=100, null=True)
    price = models.FloatField(verbose_name='Prix', null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Finition'


class Quantity(models.Model):
    nb = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.nb)


class FormatType(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.name)


class Specification(models.Model):
    article = models.OneToOneField(Article, related_name='SpecificationArticle', verbose_name='Article',
                                   on_delete=models.CASCADE)
    customSize = models.BooleanField(verbose_name='client choisi longeur et largeur', null=True, blank=True)
    customQuantite = models.BooleanField(verbose_name='client choisi Quantite', null=True, blank=True)
    customDesign = models.BooleanField(verbose_name='client Charger un design', null=True, blank=True)
    size = models.ManyToManyField(Size1, verbose_name='Size', related_name="SizeSpecification", blank=True)
    formattype = models.ManyToManyField(FormatType, verbose_name='FromaTypeSpecification',
                                        related_name="FormaTypeSpecification", blank=True)
    paperType = models.ManyToManyField(PaperType, verbose_name='Papier type', related_name="PaperSpecification",
                                       blank=True)
    paperColor = models.ManyToManyField(PaperColor, verbose_name='Papier coleur',
                                        related_name="PaperColorSpecification", blank=True)
    fontColor = models.ManyToManyField(FontColor, verbose_name='Font coleur', related_name="FontColorSpecification",
                                       blank=True)
    side = models.ManyToManyField(Side, verbose_name='direction', related_name="SideSpecification", blank=True)
    orientation = models.ManyToManyField(Orientation, verbose_name='Orientation',
                                         related_name="OrientationSpecification", blank=True)
    finition = models.ManyToManyField(Finition, verbose_name='Finition', related_name="FinitionSpecification",
                                      blank=True)
    Quantity = models.ManyToManyField(Quantity, related_name='QuantitySpecification', verbose_name='Quantite',
                                      blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        quanity = self.Quantity.first().nb
        if self.finition is None:
            finition = 1
        else:
            finition = self.finition.first().price
        if self.paperType is None:
            paperType = 1
        else:
            paperType = self.paperType.first().price

        return (quanity * finition * paperType)
        # return self.article.title

    class Meta:
        verbose_name = 'Specification'

    @property
    def minprice(self):
        quanity = self.Quantity.first().nb
        if self.finition is None:
            finition = 1
        else:
            finition = self.finition.first().price
        if self.paperType is None:
            paperType = 1
        else:
            paperType = self.paperType.first().price

        return (quanity*finition*paperType)


class Bestarticle(models.Model):
    article = models.OneToOneField(Article, related_name="bestarticle",
                                   on_delete=models.CASCADE, verbose_name='Article')
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'Top article'


class Search(models.Model):
    user = models.ForeignKey(User, related_name='search_user', on_delete=models.CASCADE, null=True, default='')
    title = models.TextField(null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name = 'Recherche'


class PromoCode(models.Model):
    price = models.FloatField(null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)


class Delivery(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')
    price = models.FloatField(verbose_name='Prix')
    mindays = models.IntegerField(verbose_name='Minimun de nb de jours')
    maxdays = models.IntegerField(verbose_name='Maximun de nb de jours')
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name


class FileControle(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')
    price = models.FloatField(verbose_name='Prix')
    creatd_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name


class Pane(models.Model):
    article = models.ForeignKey(Article, related_name='ArticlePane', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='UserPane', on_delete=models.CASCADE)
    FileControle = models.ForeignKey(FileControle, related_name='FileControlePane', on_delete=models.CASCADE)
    delevery = models.ForeignKey(Delivery, related_name='DeleveryPane', on_delete=models.CASCADE)
    ArticleDesign = models.FileField(verbose_name='Nom', upload_to='static/pane_images', null=True)
    size = models.ForeignKey(Size1, verbose_name='Size', related_name="SizePane", null=True, blank=True,
                             on_delete=models.CASCADE)
    formattype = models.ForeignKey(FormatType, verbose_name='Forma type',
                                   related_name="FormaTypePane", null=True, blank=True, on_delete=models.CASCADE)
    paperType = models.ForeignKey(PaperType, verbose_name='Papier type', related_name="PaperPane",
                                  null=True, blank=True, on_delete=models.CASCADE)
    paperColor = models.ForeignKey(PaperColor, verbose_name='Papier coleur',
                                   related_name="PaperColorPane", null=True, blank=True, on_delete=models.CASCADE)
    fontColor = models.ForeignKey(FontColor, verbose_name='Font coleur', related_name="FontColorPane",
                                  null=True, blank=True, on_delete=models.CASCADE)
    side = models.ForeignKey(Side, verbose_name='direction', related_name="SidePane", null=True, blank=True,
                             on_delete=models.CASCADE)
    orientation = models.ForeignKey(Orientation, verbose_name='Orientation',
                                    related_name="OrientationPane", null=True, blank=True, on_delete=models.CASCADE)
    finition = models.ForeignKey(Finition, verbose_name='Finition', related_name="FinitionPane",
                                 null=True, blank=True, on_delete=models.CASCADE)
    Quantity = models.ForeignKey(Quantity, related_name='QuantityPane', verbose_name='Quantite',
                                 null=True, blank=True, on_delete=models.CASCADE)
    CostumQuantity = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.article)

    @property
    def total(self):
        if self.Quantity is not None:
            quanity = self.Quantity
        elif self.CostumQuantity is not None:
            quanity = self.CostumQuantity
        else:
            quanity=1
        if self.finition is None:
            finition = 1
        else:
            finition = self.finition.price
        if self.paperType is None:
            paperType = 1
        else:
            paperType = self.paperType.price
        FileControle = float(self.FileControle.price)
        price = float(self.delevery.price)
        return (finition * quanity * paperType) + FileControle


class Commande(models.Model):
    Pane = models.ManyToManyField(Pane, related_name='panes')
    User = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    total = models.FloatField()
    delevery = models.ForeignKey(Delivery, related_name='Deleverycommande', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['-created_at']
