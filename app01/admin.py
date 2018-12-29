from django.contrib import admin
from app01.models import *

# Register your models here.

# admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publish)

# # 方式一
# @admin.register(Book)
# class Bookconfig(admin.ModelAdmin):
#     list_display = ['title','price']
#
# # 方式二
# class Bookconfig1(admin.ModelAdmin):
#     list_display = ['title','price']
#
# admin.site.register(Book,Bookconfig1)


@admin.register(Book)
class Bookconfig(admin.ModelAdmin):
    # 定制显示的列
    list_display = ['title','price']
    # 定制列可以点击跳转
    list_display_links = ['title']
    # 定制右侧快速筛选
    list_filter=['title']
    # 列表查询是否自动select_related
    list_select_related = ['publisher']
    # 列表显示时可以编辑的列
    list_editable = ['price']
    # 模糊搜索
    search_fields = ['title']
    # 对Date和DateTime类型进行搜索
    date_hierarchy = 'publishDate'

    # 定制action中的操作
    def patch_init(self,request,queryset):
        queryset.update(price=100)

    patch_init.short_description='批量初始化'
    actions=[patch_init]

    #详细页面，针对FK和M2M变成input框形式
    raw_id_fields = ('publisher',)

    #详细页面，定制显示的字段
    fields = ('title',)

    #详细页面，定制排除的字段
    exclude = ('price',)

    #详细页面时，定制只读的字段
    readonly_fields = ('title',)

    #详细页面时，使用fieldsets标签对数据进行分割显示
    fieldsets = (('基本数据',{'fields':('title',)}),('其他',{'classes':('collapse',),'fields':('price',)}),)

    # 详细页面时，M2M显示时，数据移动选择
    filter_vertical = ('authors',)

    #列表时，数据排序规则
    ordering = ('-id',)

    # 详细页面时，使用radio显示选项（FK默认使用select）
    radio_fields = {'publisher':admin.VERTICAL}


# 详细页面，如果有其他表和当前表做FK，那么详细页面可以进行动态增加和删除
class BookInline(admin.StackedInline):  # TabularInline
    extra = 0
    model = Book
class GroupAdminMode(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [BookInline, ]

#定制HTML模板
add_form_template = None
change_form_template = None
change_list_template = None
delete_confirmation_template = None
delete_selected_confirmation_template = None
object_history_template = None


# empty_value_display = "列数据为空时，显示默认值"
@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = "列数据为空时，默认显示"

    list_display = ('user', 'pwd', 'up')

    def up(self, obj):
        return obj.user

    up.empty_value_display = "指定列数据为空时，默认显示"


# form = ModelForm，用于定制用户请求时候表单验证
from django.forms import ModelForm
from django.forms import fields
class MyForm(ModelForm):
    others = fields.CharField()

    class Meta:
        model = models = Book
        fields = "__all__"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = MyForm






