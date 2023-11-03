from django.contrib import admin

from .models import Post,Comment
from django.utils.translation import gettext_lazy as _


class CommentAdminInLine(admin.TabularInline):
    model = Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','new','status']




class KindListFilter(admin.SimpleListFilter):
    title = _("KIND")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "kind"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            ("All", "All"),
            ("ACTIVE", "Active"),
            ("DRAFT", "Draft"),
            ("ARCHIVE", "Archive"),
        ]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == "All":
            return queryset
        return queryset.filter(kind = self.value())

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'time_create'
    fields = ['title','content','is_published','kind','price',]
    #exclude = ['kind']
    list_display = ['title','content','is_published','time_create','kind','price','byn_price']
    readonly_fields = ['kind']
    search_fields = ['title__startswith']
    ordering = ['-time_create']
    list_filter = [KindListFilter]
    inlines = [CommentAdminInLine]
    actions = ['activate_post']
    def byn_price(self,obj: Post):
        return str(obj.price*3.25)
    #get_price.short_description = 'BYN PRICE'




    @admin.action(description='Activate posts')
    def activate_post(modeladmin, request, queryset):
        queryset.update(kind=Post.ACTIVE)