import os
import random
import logging
import webapp2
import jinja2
import chinese


jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)


class MainPage(webapp2.RequestHandler):
    def get(self):
        int_dict = {
            1: 'a',
            2: 'e',
            3: 'i',
            4: 'o',
            5: 'u',
        }

        a = u'\u3042'
        e = u'\u3048'
        i = u'\u3044'
        u = u'\u3046'
        o = u'\u3049'

        char_dict = {
            'a': a,
            'e': e,
            'i': i,
            'o': o,
            'u': u,
        }

        answer_choices = {

        }

        def multiple_choice():
            random_int = random.randint(1, 5)
            answer = char_dict.get(int_dict.get(random_int))
            answer_option = [int_dict.get(random_int)]
            answer_options = []
            x = 0
            while x < 4:
                z = random.randint(1,5)
                if answer_option.count(int_dict.get(z)) < 1:
                    answer_option.append(int_dict.get(z))
                    x += 1
            while len(answer_option) > 0:
                z = random.randint(0, len(answer_option) - 1)
                answer_options.append(answer_option[z])
                answer_option.pop(z)
            return (answer, answer_options)

        answer = multiple_choice()[0]
        answer_options = multiple_choice()[1]





        template_vars = {
            # "<html_variable_name>" : <python_variable_name>
            "answer_choices" : answer_choices,
            "answer" : answer,
            "answer_options" : answer_options,

        }

        template = jinja_env.get_template("templates/main.html")
        self.response.write(template.render(template_vars))

    def post(self):
        pass



app = webapp2.WSGIApplication([
    ("/", MainPage), ("/", ChinesePage)
], debug=True)
