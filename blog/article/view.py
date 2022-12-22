from flask import Blueprint, render_template

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/')
def article_list():
    return render_template('articles/list.html',
                           articles=[1, 2, 3, 4, 5, 6, 7, 8, 9,]
                           )