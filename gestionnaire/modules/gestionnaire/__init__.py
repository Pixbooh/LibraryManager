from trytond.pool import Pool
import gestionnaire


def register():
    Pool.register(
        gestionnaire.category,
        gestionnaire.genre,
        gestionnaire.author,
        gestionnaire.book,
        gestionnaire.support,
        # gestionnaire.booksupportrelation,
        module='gestionnaire', type_='model')
