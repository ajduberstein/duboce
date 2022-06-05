import jinja2
import json


def in_jupyter():
    try:
        ip = get_ipython()  # noqa

        return ip.has_trait("kernel")
    except NameError:
        return False


# TODO bundle javascript
output_template = jinja2.Template(
    """
  <!DOCTYPE html>
  <html>
    <head>
      <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
      <title>Duboce</title>
      <script>{{js_bundle}}</script>
      <script>
        const chart = JSONConverter.convert({{config}});
        document.body.append(chart.plot());
      </script>
    </head>
    <body>
    </body>
  </html>
  """
)


def get_class_name(cls):
    cls = cls.replace("<class ", "")
    cls = cls.replace("'>", "")
    class_name = cls.split(".")[-1]
    return class_name


# https://github.com/visgl/deck.gl/blob/017d960d95160c456204f781dceac41eafd49579/bindings/pydeck/pydeck/io/html.py
class Plottable:
    def __init__(self, data, **kwargs) -> dict:
        self.data = data
        self.__dict__["options"] = {}
        for k, v in kwargs.items():
            self.__dict__["options"][k] = v
        self.__dict__["@@type"] = get_class_name(str(self.__class__))

    def plot(self):
        RELPATH_TO_BUNDLE = "../static/bundle.js"
        rendered_html = output_template.render(
            data=self.data, js_bundle=RELPATH_TO_BUNDLE
        )
        if in_jupyter():
            from IPython import HTML

            return HTML(rendered_html)
        # Render to HTML
        else:
            return rendered_html

    def __repr__(self):
        return json.dumps(self.__dict__, sort_keys=True)
