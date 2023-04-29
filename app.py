from flask import Flask, render_template
from data import Hanime_Brain

app = Flask(__name__)
hanime_brain = Hanime_Brain()

@app.route('/')
def home():
    data = hanime_brain.main_page()
    return render_template('main-page.html', page_details=data)

@app.route('/g/<id>/')
def reading_page(id):
    reading_page_data = hanime_brain.reading_page(id)
    return render_template('reading-page.html', page_data=reading_page_data)

@app.route('/tags')
def tags_page():
    reading_page_data = hanime_brain.reading_page(id)
    return render_template('reading-page.html', page_data=reading_page_data)

if __name__ == '__main__':
    app.run(debug=True)