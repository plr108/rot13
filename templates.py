import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        text = self.request.get_all('text')
        self.render('base.html', text=text)

    def post(self):
        text = self.request.get_all('text')
        self.response.out.write('Thanks for clicking')


app = webapp2.WSGIApplication([('/', MainPage),
                               ],
                              debug=True)
