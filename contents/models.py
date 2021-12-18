from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from abstract.models import AbstractLocaleModel, AbstractDateModel


class Menu(AbstractDateModel):
    """ A dynamic menu in navbar """
    title = models.CharField(max_length=256, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'menu'
        ordering = ['order']

    def __str__(self):
        return f'{self.title}'


class MenuI18N(AbstractLocaleModel):
    menu = models.ForeignKey(Menu,
                             related_name='translations',
                             on_delete=models.PROTECT,
                             verbose_name='Original name')
    title = models.CharField(max_length=256, verbose_name='Translation')

    class Meta:
        db_table = 'menu_i18n'
        verbose_name = 'menu translation'


class SubMenu(AbstractDateModel):
    """ A dynamic submenu under specific menu in navbar """
    title = models.CharField(max_length=256)
    order = models.PositiveIntegerField(default=0)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name='submenus')

    class Meta:
        db_table = 'submenu'
        ordering = ['order']
        unique_together = ['menu', 'title']

    def __str__(self):
        return f"{self.title} [submenu of {self.menu.title}]"


class SubMenuI18N(AbstractLocaleModel):
    submenu = models.ForeignKey(SubMenu,
                                related_name='translations',
                                on_delete=models.PROTECT,
                                verbose_name='Original name')
    title = models.CharField(max_length=256, verbose_name='Translation')

    class Meta:
        db_table = 'submenu_i18n'
        verbose_name = 'submenu translation'


class TextBlock(AbstractDateModel):
    title = models.CharField(max_length=256, default="")
    content = RichTextUploadingField()
    submenu = models.ForeignKey(SubMenu, on_delete=models.PROTECT, null=True, related_name='posts')  # TODO remove null=True

    class Meta:
        db_table = 'text_block'
        verbose_name = 'post'

    def __str__(self):
        return f"Post [{self.submenu.title}]"


class TextBlockMenuI18N(AbstractLocaleModel):
    title = models.CharField(max_length=256, default="")
    text_block = models.ForeignKey(TextBlock,
                                   related_name='translations',
                                   on_delete=models.PROTECT,
                                   verbose_name='Original name')
    content = RichTextUploadingField(verbose_name='Translation')

    class Meta:
        db_table = 'text_block_i18n'
        verbose_name = 'post translation'
