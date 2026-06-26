from flask import Flask, render_template, request

from models.db import cursor, conn
from models.analyzer import analyze_language
from models.regex_generator import generate_regex
from models.validator import validate_string
from models.dfa_generator import create_dfa
from models.explainer import explain_regex
from models.testcase_generator import generate_test_cases
app = Flask(__name__)
current_regex = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generator', methods=['GET', 'POST'])
def generator():

    global current_regex

    regex = ""
    pattern_type = ""
    regex_explanation = []
    valid_examples = []
    invalid_examples = []

    if request.method == 'POST':

        language = request.form['language']

        analysis = analyze_language(language)

        regex = generate_regex(analysis)
        valid_examples = []
        invalid_examples = []
   
        if analysis.get("type"):
            valid_examples, invalid_examples = generate_test_cases(
                analysis["type"]
            )
            regex_explanation = explain_regex(regex)

        if analysis.get("type"):
            pattern_type = analysis["type"]

        elif "start" in analysis and "end" in analysis:
            pattern_type = "starts with and ends with"

        elif "start" in analysis:
            pattern_type = "starts with"

        elif "end" in analysis:
            pattern_type = "ends with"

        elif "substring" in analysis:
            pattern_type = "substring"

        current_regex = regex

        cursor.execute("""
            INSERT INTO history(language_rule, generated_regex)
            VALUES(?,?)
            """,
            (
                language,
                regex
            ))

        conn.commit()

    return render_template(
        'generator.html',
        regex=regex,
        pattern_type=pattern_type,
        regex_explanation=regex_explanation,
        valid_examples=valid_examples,
        invalid_examples=invalid_examples
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
        VALUES(?,?,?)
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
@app.route('/dashboard')
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

@app.route('/dfa')
def dfa():

    image = create_dfa(current_regex)

    return render_template(
        'dfa.html',
        image=image
    )
    
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
