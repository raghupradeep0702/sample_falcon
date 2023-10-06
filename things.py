# examples/things.py
from wsgiref.simple_server import make_server

import falcon



class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200 
        resp.content_type = falcon.MEDIA_TEXT  
        resp.text = (
            '\nTwo things awe me most, the starry sky '
            'above me and the moral law within me.\n'
            '\n'
            '    ~ Immanuel Kant\n\n'
        )

    def on_post(self, req, resp):
        """Handles POST requests"""
        try:
            data = req.media
            number = data['number']
            prediction = "even" if number % 2 == 0 else "odd"
            resp.status = falcon.HTTP_200
            # resp.text = 'Data received successfully'
            resp.media = {"prediction": prediction}
        except Exception as e:
            resp.status = falcon.HTTP_400
            resp.text = f'Error: {str(e)}'

# falcon.App instances are callable WSGI apps
app = falcon.App()

things = ThingsResource()

app.add_route('/things', things)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        httpd.serve_forever()