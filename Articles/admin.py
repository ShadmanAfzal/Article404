from django.contrib import admin
from Articles.models import CustomUser,Post,Comments,contact
 
admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(contact)

