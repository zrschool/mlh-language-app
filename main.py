import os
import logging
import webapp2
import jinja2


jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)


class MainPage(webapp2.RequestHandler):
    def get(self):

        template_vars = {
            # "<html_variable_name>" : <python_variable_name>
        }

        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))

    def post(self):
        pass


app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)
