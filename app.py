from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
library = []

@app.route('/books', methods=['GET'])
def index():
    return render_template('index.html', library=library)

@app.route('/books/new', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        form = request.form
        library.append({
            'id': len(library) + 1,
            'title': form['title'],
            'author': form['author'],
            'year': form['year'],
            'category': form['category'],
            'cover': 'images/book_cover_default.jpg'
        })
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/books/<int:book_id>', methods=['GET'])
def book_details(book_id):
    book = next((b for b in library if b['id'] == book_id), None)
    return render_template('book_details.html', book=book)

@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = next((b for b in library if b['id'] == book_id), None)
    if request.method == 'POST' and book:
        form = request.form
        book.update({k: form[k] for k in ('title', 'author', 'year', 'category')})
        return redirect(url_for('book_details', book_id=book['id']))
    return render_template('edit_book.html', book=book)

@app.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    global library
    library = [book for book in library if book['id'] != book_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
