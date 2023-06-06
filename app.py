from flask import Flask, render_template
from data import Hanime_Brain

app = Flask(__name__)
hanime_brain = Hanime_Brain()

@app.route('/')
def home():
    data = hanime_brain.main_page_pages(url="https://nhentai.to")
    return render_template('main-page.html', page_details=data)

@app.route('/page/<page>')
def home_new_page(page):
    url= f"https://nhentai.to/?{page}"
    data = hanime_brain.main_page_pages(url=url)
    return render_template('main-page.html', page_details=data)

@app.route('/g/<id>/')
def reading_page(id):
    reading_page_data = hanime_brain.reading_page(id)
    return render_template('reading-page.html', page_data=reading_page_data)

@app.route('/tag/<tag>')
def tags_search(tag):
    reading_page_data = hanime_brain.tags_page(tag)
    return render_template('reading-page.html', page_data=reading_page_data)

@app.route('/tags/<page>')
def tags_page(page):
    tags_page_data = hanime_brain.full_tags_pages(int(page))
    return render_template('tags-page.html', page_data=tags_page_data, current_page=page)

if __name__ == '__main__':
    # app.run(debug=True, host="192.168.29.146")
    app.run(host="0.0.0.0")
