from trytond.model import ModelSQL, ModelView, fields


__all__ = [
    'Language',
    'Category',
    'Genre',
    'Author',
    'Book',
    'Support',
    # 'BookSupportRelation',
    ]


class Language(ModelSQL, ModelView):
    'Language'
    __name__ = 'gestionnaire.language'

    name = fields.Char('Name', required=True)

class Category(ModelSQL, ModelView):
    'Category'
    __name__ = 'gestionnaire.category'

    name = fields.Char('Name', required=True)


class Genre(ModelSQL, ModelView):
    'Genre'
    __name__ = 'gestionnaire.genre'

    name = fields.Char('Name', required=True)


class Author(ModelSQL, ModelView):
    'Author'
    __name__ = 'gestionnaire.author'

    name = fields.Char('Name', required=True)
    books = fields.One2Many('gestionnaire.book', 'author', 'Books')


class Book(ModelSQL, ModelView):
    'Book'
    __name__ = 'gestionnaire.book'

    title = fields.Char('Title', required=True)
    author = fields.Many2One('gestionnaire.author', 'Author', required=True,
                             ondelete='CASCADE')
    language = fields.Many2One('gestionnaire.language', 'Language',
                               required=True, ondelete='CASCADE')
    genre = fields.Many2One('gestionnaire.genre', 'Genre', required=False,
                            ondelette='CASCADE')
    category = fields.Many2One('gestionnaire.category', 'Category',
                               required=False, ondelete='CASCADE')
    # supports = fields.Many2Many('gestionnaire.book-gestionnaire.support',
    #                            'book', 'support', 'Supports')
    support = fields.Many2One('gestionnaire.support', 'Support', required=True,
                              ondelette='CASCADE')
    start_reading = fields.Date('Date started reading')
    stop_reading = fields.Date('Date stopped reading')

    is_reading = fields.Function(fields.Boolean('Is reading',
                                 'getter_is_reading',
                                 searcher='search_is_reading'))

    @classmethod
    def getter_is_reading(cls, books, name):
        return {x.id: None for x in books}

    @classmethod
    def search_is_reading(cls, name, clause):
        return[]


class Support(ModelSQL, ModelView):
    'Support'
    __name__ = 'gestionnaire.support'


#class BookSupportRelation(ModelSQL):
#    'Book - Support Relation'
#    __name__ = 'gestionnaire.book-gestionnaire.support'
#
#    book = fields.Many2One('gestionnaire.book', 'Book', required=True,
#                           ondelete='CASCADE')
#    support = fields.Many2One('gestionnaire.support', 'Support',
#                              required=True, ondelete='RESTRICT')
