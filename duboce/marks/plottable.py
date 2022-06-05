def in_jupyter():
    try:
        ip = get_ipython()  # noqa

        return ip.has_trait("kernel")
    except NameError:
        return False



# TODO bundle javascript
output_template = jinja2.Template(
  '''
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
  '''
)

# https://github.com/visgl/deck.gl/blob/017d960d95160c456204f781dceac41eafd49579/bindings/pydeck/pydeck/io/html.py
class Plottable():
    def __init__(self, data, **kwargs) -> dict:
        self.data = data
        for k, v in kwargs.items():
            self[k] = v

    def plot():
        rendered_html = output_template.render(data=self.data)
        if in_jupyter():
            return HTML(rendered_html)
        # Render to HTML
        else:
            return rendered_html
