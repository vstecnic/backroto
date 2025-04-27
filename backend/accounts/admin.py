from django.contrib import admin
from .models import Profile
from .models import Destinos
from .models import Categorias
from .models import MetodoPago
from .models import Nosotros
from .models import Carrito



# PROFILE DETALLADO
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mail','address', 'location', 'telephone','user_group')
    search_fields = ('user__username', 'location', 'user__groups__name')
    list_filter = ('user__groups', 'location')


    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])
    user_group.short_description = 'Grupo'



class DestinosAdmin(admin.ModelAdmin):
    list_display = ('id_destino', 'nombre_Destino', 'descripcion', 'image', 'precio_Destino', 'fecha_salida', 'cantidad_Disponible')
    search_fields = ('nombre_Destino', 'descripcion')
    list_filter = ('fecha_salida', 'cantidad_Disponible', 'id_categoria')
    ordering = ('fecha_salida',)
    fields = ('nombre_Destino', 'descripcion', 'image', 'precio_Destino', 'fecha_salida','cantidad_Disponible', 'id_metodoPago', 'id_categoria')


class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id_categoria','nombreCategoria',)




class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('id_metodoPago','nombrePago',)


class NosotrosAdmin(admin.ModelAdmin):
    list_display = ('id_nosotros', 'nombre_apellido', 'github', 'linkedin', 'imagen')
    search_fields = ('nombre_apellido', 'github', 'linkedin')




class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id_compra','cantidad','id_metodoPago', 'id_destino','user')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Destinos, DestinosAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(MetodoPago, MetodoPagoAdmin)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(Carrito,CarritoAdmin)
