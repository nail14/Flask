
from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

# USERS = ['Alice', 'Jon', 'Mike']
USERS = {
    1: 'Alice',
    2: 'Jon',
    3: 'Mike',
}

ARTICLES = {
    1: {
        'title': 'TIT1',
        'text': 'abc',
        'author': {
            'name': 'nnamee',
            'id': 1,
            }
        },
    2: {'title': 'TIT2',
        'text': 'abc2',
        'author': {
            'name': 'nnamee',
            'id': 1,
            }
        },
    3: {'title': 'TIT3',
        'text': 'abc3',
        'author': {
            'name': 'nnamee',
            'id': 1,
            }
        },
}


@user.route('/news/')
def article_list():
    return render_template('articles/list.html',
                           articles=ARTICLES,
                           )


@user.route('/news/<int:pk>')
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]
    except KeyError:
        # raise NotFound(f'User id {pk} not found')
        return redirect('/articles/')
    return render_template('articles/details.html',
                           article_name=article_name,
                           )


@user.route('/')
def user_list():
    return render_template('users/list.html',
                           users=USERS,
                           )


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        # raise NotFound(f'User id {pk} not found')
        return redirect('/users/')
    return render_template('users/details.html',
                           user_name=user_name,
                           )
