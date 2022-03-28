from flaskly.globals import current_flaskly_app as _app
from flaskly.typing import AbstractWeakComponent, RenderReturnValue
from .state import form_json_state


def default_form_render(form: AbstractWeakComponent, /, **options) -> RenderReturnValue:
    if getattr(form, "flaskly_rendering_type", None) == 'stateful':
        return render_stateful(form, **options)
    return render_default(form, **options)


def render_default(form: AbstractWeakComponent, /, **options) -> RenderReturnValue:
    return _app.core_jinja_env.render_template("forms/default_form.html", form=form)


def render_stateful(form: AbstractWeakComponent, /, **options) -> RenderReturnValue:
    return _app.core_jinja_env.render_template("forms/stateful_form.html",
                                               form=form, form_state=form_json_state(form))
