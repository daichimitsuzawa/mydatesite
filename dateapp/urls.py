from rest_framework import routers
from .views import Search_ViewSet, Table_Viewset,  FilterSearch_ViewSet, FilterTable_ViewSet

router = routers.DefaultRouter()
router.register('all_search/',Search_ViewSet)
router.register('all_table/',Table_Viewset)
router.register('search/',FilterSearch_ViewSet)
router.register('table/',FilterTable_ViewSet)
urlpatterns=router.urls