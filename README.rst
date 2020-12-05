***********
Wagtail SVG
***********

.. image:: https://img.shields.io/pypi/v/wagtailsvg
    :target: https://pypi.org/project/wagtailsvg/

.. image:: https://img.shields.io/pypi/pyversions/wagtailsvg
    :target: https://pypi.org/project/wagtailsvg/

`Wagtail <https://github.com/wagtail/wagtail>`_ + `SVG <https://developer.mozilla.org/docs/Web/SVG>`_ = 🚀

**SVG** for **Wagtail** with :

- **Svg** : Model
- **SvgChooserPanel** : ChooserPanel for ForeignKey
- **SvgChooserBlock** : ChooserBlock for StreamField

Can be used like this :
::

    from wagtailsvg.models import Svg
    from wagtailsvg.blocks import SvgChooserBlock
    from wagtailsvg.edit_handlers import SvgChooserPanel


    class TestPage(Page):
        logo = models.ForeignKey(
            Svg,
            related_name='+',
            null=True,
            blank=True,
            on_delete=models.SET_NULL
        )
        body = StreamField([
            ('svg', SvgChooserBlock()),
        ], blank=True)

        content_panels = Page.content_panels + [
            SvgChooserPanel('logo'),
            StreamFieldPanel('body'),
        ]


Setup
#####

Install with pip :

``pip install wagtailsvg``

Add wagtailsvg to django apps installed :
::

    INSTALLED_APPS = [
        ...
        'wagtailsvg',
    ]


Development env
###############

::

    git clone git@github.com:Aleksi44/wagtailsvg.git
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py init
    python manage.py runserver 0.0.0.0:4243


Idea to contribute
##################

Let's help designers who use wagtail with :

- Improvements of Wagtail Admin of `wagtailsvg`
- Editing SVG files directly from `wagtailsvg/templates/modeladmin/wagtailsvg/edit.html`
- With versioning of SVG files (like Page model?)
- Import essential customizable SVG files easily ?
- Import SVG files with a global styles conf ?

Feel free to contact me at `hello@snoweb.fr`
