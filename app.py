from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
library = []

@app.route('/books', methods=['GET'])
def index():
    return render_template('index.html', library=library)

@app.route('/books/new', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        category = request.form['category']
        book_id = len(library) + 1
        book = {
            'id': book_id,
            'title': title,
            'author': author,
            'year': year,
            'category': category,
            'cover': 'images/book_cover_default.jpg'
        }
        library.append(book)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/books/<int:book_id>', methods=['GET'])
def book_details(book_id):
    book = next((b for b in library if b['id'] == book_id), None)
    return render_template('book_details.html', book=book)

@app.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    global library
    library = [book for book in library if book['id'] != book_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
