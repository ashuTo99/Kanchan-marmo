from django.urls import path
from .import views


urlpatterns = [
    #category
    path("",views.index,name="block.index"),
    path("add-block/",views.addBlock,name="block.add"),
    # path("edit-category/<int:id>/<str:slug>/",views.editCategory,name="category.edit"),
    path("delete-block/<int:id>/",views.deleteBlock,name="block.delete"),
    path("generate-report",views.export_block_xls,name="block.report"),







]
