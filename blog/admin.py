from django.contrib import admin
from blog.models import Post,Miembros


#admin.site.register(Post)

@admin.register(Post)
class Administrador(admin.ModelAdmin):

    list_display=('titulo','evento_activo','capacidad')
    list_editable = ('titulo','capacidad','evento_activo')
    actions = ['guardado']

    def guardado(self,request , queryset):
        return queryset.update(evento_activo=False)
    guardado.short_description = 'Guardar cambios'

# Register your models here.
@admin.register(Miembros)
class Miembro(admin.ModelAdmin):
    list_display=('miembro_activo','cargo')
    list_editable = ('miembro_activo','cargo')
    actions = ['guardado']

    def guardado(self,request , queryset):
        return queryset.update(miembro_activo=False)
    guardado.short_description = 'Guardar cambios'


