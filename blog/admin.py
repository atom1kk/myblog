from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):  
	list_display = ('title', 'slug', 'author', 'publish', 'status')  # добавляем данные в интерфейс нашей админки для удобного управления постами
	list_filter = ('status', 'created', 'publish', 'author')  # добавляем фильтр для удобного поиска статей
	search_fields = ('title', 'body')  # добавляем поиск статей по заголовку или самому тексту в блоге
	prepopulated_fields = {'slug': ('title',)}  # добавили автозаполнение для SLUG по названию статьи (при добавлении нового поста)
	raw_id_fields = ('author',)  # добавляем поиск автора (при добавлении нового поста)
	date_hierarchy = 'publish'  # добавляем под поиском ссылку для навигации статей по датам 
	ordering = ('status', 'publish')  # сортируем по умолчанию по указанным полям

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('title', 'name', 'email', 'body')