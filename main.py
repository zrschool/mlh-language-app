import os
import random as rand
import logging
import webapp2
import jinja2


jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)


class MainPage(webapp2.RequestHandler):
    def get(self):

        a = u'\u3042'
        b = u'\u3043'
        c = u'\u3044'
        d = u'\u3045'
        e = u'\u3046'

        hiragana = {
            1 : a,
            2 : b,
            3 : c,
            4 : d,
            5 : e,
        }


        answer_choices = {
            "A" : hiragana.get(rand.randrange(1,5)),
            "B" : hiragana.get(rand.randrange(1,5)),
            "C" : hiragana.get(rand.randrange(1,5)),
            "D" : hiragana.get(rand.randrange(1,5)),
            "E" : hiragana.get(rand.randrange(1,5)),
        }

        template_vars = {
            # "<html_variable_name>" : <python_variable_name>
            "answer_choices" : answer_choices,
        }

        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))

    def post(self):
        pass


app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)
