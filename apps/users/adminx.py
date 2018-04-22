import xadmin
from xadmin import views
from.models import EmailVerifyRecord, Banner


# 设置主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# 页头页脚配置
class GlobalSetting(object):
    site_title = '花时间 flower time'
    site_footer = '花时间 flower time'
    # 左侧导航栏收起
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
