from flask import Flask
from flask_restful import Resource, Api

# construct app application
app = Flask(__name__)

# create api object from Api class using app application
api = Api(app)

# create class BookModel with 3 attributes and 2 methods
class BookModel:

    def __init__(self, pk, title, author):
        self.pk = pk
        self.title = title
        self.author = author

    def __str__(self):
        return f'pk: {self.pk}, title: {self.title}, author: {self.author}'

    def to_dict(self):
        return {'pk': self.pk, 'title': self.title, 'author': self.author}

# create list that contain 5 object instantiated from class BookModel
books = [
    BookModel(num, f'title {num}', f'author {num}') for num in range(1, 6)
]

# create class BookResource that contain GET, POST, DELETE, UPDATE resources
class BookResource(Resource):
    def get(self):
        return [b.to_dict() for b in books]

# using api object from Api Class imported from flask_restful we create endpoint that point to some resources
api.add_resource(BookResource, '/books')

if __name__ == '__main__':
    app.run(debug=True)
