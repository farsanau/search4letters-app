from flask import Flask, render_template, request

from vsearch import searcheletters

app = Flask(__name__)




@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results =str(searcheletters(phrase, letters))
    title = 'Here are your results'

    return render_template('results.html', the_title = title, the_phrase = phrase, the_letters = letters, the_results=results)

@app.route('/')
@app.route('/entry')
def display_index() -> 'html':

    return render_template('entry.html', the_title='Welcome to search for letters on Web!' )


if  __name__ == '__main__':
    app.run(debug=True)
