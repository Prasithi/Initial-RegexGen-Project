from flask import Flask, render_template, request

from models.db import cursor, conn
from models.analyzer import analyze_language
from models.regex_generator import generate_regex
from models.validator import validate_string

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generator', methods=['GET', 'POST'])
def generator():

    regex = ""

    if request.method == 'POST':

        language = request.form['language']

        analysis = analyze_language(language)

        regex = generate_regex(analysis)

        cursor.execute("""
        INSERT INTO history(language_rule, generated_regex)
        VALUES(%s,%s)
        """, (language, regex))

        conn.commit()

    return render_template(
        'generator.html',
        regex=regex
    )

@app.route('/validator', methods=['GET', 'POST'])
def validator():

    result = ""

    if request.method == 'POST':

        regex = request.form['regex']
        test_string = request.form['test_string']

        result = validate_string(
            regex,
            test_string
        )

        cursor.execute("""
        INSERT INTO history(
            generated_regex,
            test_string,
            result
        )
        VALUES(%s,%s,%s)
        """,
        (
            regex,
            test_string,
            result
        ))

        conn.commit()

    return render_template(
        'validator.html',
        result=result
    )

@app.route('/history')
def history():

    cursor.execute("""
    SELECT * FROM history
    ORDER BY id DESC
    """)

    records = cursor.fetchall()

    return render_template(
        'history.html',
        records=records
    )
   # Dashboard@app.route('/dashboard')
def dashboard():

    cursor.execute("SELECT COUNT(*) FROM history")
    total_records = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM history WHERE result='VALID'"
    )
    valid_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM history WHERE result='INVALID'"
    )
    invalid_count = cursor.fetchone()[0]

    return render_template(
        'dashboard.html',
        total_records=total_records,
        valid_count=valid_count,
        invalid_count=invalid_count
    )

    from models.dfa_generator import create_dfa
    from flask import Flask, render_template, request

from models.db import cursor, conn
from models.analyzer import analyze_language
from models.regex_generator import generate_regex
from models.validator import validate_string

from models.dfa_generator import create_dfa

@app.route('/dfa')
def dfa():

    image = create_dfa()

    return render_template(
        'dfa.html',
        image=image
    )

if __name__ == '__main__':
    app.run(debug=True)
