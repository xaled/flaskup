from .render import default_form_render
from ..weak_component import AbstractWeakComponent


def wrap_form_cls(form_cls, /, *, form_id, rendering_type):
    for k in ('_renderer', 'render', 'get_renderer',):
        if not hasattr(form_cls, k):
            setattr(form_cls, k, getattr(AbstractWeakComponent, k))
    setattr(form_cls, 'find_renderer', classmethod(getattr(AbstractWeakComponent, 'find_renderer').__func__))
    setattr(form_cls, 'default_renderer', default_form_render)
    setattr(form_cls, 'rendered_type', 'Form')
    setattr(form_cls, 'flaskly_rendering_type', rendering_type)
    setattr(form_cls, 'flaskly_form_id', form_id)
