# IMPORTACIONES PARA PERFIL
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# IMPORTACIONES PARA EL RESTO DE LAS ENTIDADES
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError



# ENTIDADES

# 1 CATEGORIAS DE LOS VIAJES
class Categorias(models.Model):
        id_categoria = models.AutoField(primary_key=True)
        nombreCategoria = models.CharField(max_length=150)
class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
def __str__(self):
        return self.nombreCategoria
def __unicode__(self):
        return self.nombreCategoria


#2 METODO DE PAGO USUARIO
class MetodoPago(models.Model):
    id_metodoPago = models.AutoField(primary_key=True)
    nombrePago = models.CharField(max_length=100)

    class Meta:
        db_table = 'metodo_pago'
        verbose_name = 'Metodos De Pago'
        verbose_name_plural = 'Metodos de pagos'

    def __str__(self):
        return self.nombrePago

    def __unicode__(self):
        return self.nombrePago


#3  NOSOTROS
class Nosotros(models.Model):
    id_nosotros = models.AutoField(primary_key=True)
    nombre_apellido = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)

    class Meta:
        db_table = 'nosotros'
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        return self.nombre_apellido

#VALIDADORES PARA DESTINOS
#Agregamos un validador de precio
def positive_price_validator(value):
    if value < 0:
        raise ValidationError('El precio debe ser un valor positivo.')
#Agregamos un validador de stock de viajes
def positive_viaje_validator(value):
    if value < 0:
        raise ValidationError('El stock del viaje debe ser igual a 0, o un valor positivo.')





#4  DESTINOS
class Destinos(models.Model):
    id_destino = models.AutoField(primary_key=True)
    nombre_Destino = models.CharField(max_length=150)
    descripcion = models.TextField(default='descripcion', blank=False)
    image = models.URLField(max_length=200, blank=True)  # URLField para imágenes externas
    precio_Destino = models.DecimalField(max_digits=12, decimal_places=2, validators=[positive_price_validator])
    fecha_salida = models.DateTimeField(blank=False)
    cantidad_Disponible = models.IntegerField(default=12, validators=[positive_viaje_validator])
    id_metodoPago = models.ForeignKey('MetodoPago', db_column='id_metodoPago', on_delete=models.CASCADE)
    id_categoria = models.ForeignKey('Categorias',db_column='id_categoria', on_delete=models.CASCADE)

    class Meta:
        db_table = 'destinos'
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'

    def __str__(self):
        return self.nombre_Destino






#5 PERFIL DE USUARIO 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name='Imagen de perfil')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Localidad')
    mail = models.EmailField(max_length=150, null=True, blank=True, verbose_name='Email')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')
    dni = models.CharField(max_length=50, null=True, blank=True, verbose_name='DNI')
    
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


#6 CARRITO

class Carrito(models.Model):
    id_compra = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=3, decimal_places=0, validators=[positive_price_validator])
    id_metodoPago = models.ForeignKey(MetodoPago, db_column='id_metodoPago', on_delete=models.CASCADE)
    id_destino = models.ForeignKey(Destinos, db_column='id_destino', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'carrito'
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carrito'

    def __str__(self):
        return f"{self.user} - {self.id_destino} - {self.cantidad}"


    def __unicode__(self):
        return f'{self.user.username} - {self.id_destino.nombre_Destino}'




