from bottle import Bottle, template, static_file


class Bootle_test(Bottle):

    def __init__(self):
        super(Bootle_test, self).__init__()
        self.route('/', callback=self.index)
        self.route('/static/<picture>',  callback=self.serve_picture)

    def index(self):
        picture_name = 'hahaha.jpg'
        return template('index', picture=picture_name)

    def serve_picture(self, picture):
            return static_file(picture, root='./imgs')

if __name__ == '__main__':
    app = Bootle_test()
    app.run(host='localhost', port='8080')