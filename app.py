from flask import Flask, request, render_template
from Model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell', methods=['POST'])
def spell():
    text = request.form['text']
    corrected_text = spell_checker_module.correct_spell(text)
    corrected_grammar, _ = spell_checker_module.correct_grammar(text)
    return {
        'corrected_text': corrected_text,
        'corrected_grammar': corrected_grammar
    }

@app.route('/grammar', methods=['POST'])
def grammar():
    file = request.files['file']
    readable_file = file.read().decode('utf-8', errors='ignore')
    corrected_file_text = spell_checker_module.correct_spell(readable_file)
    corrected_file_grammar, _ = spell_checker_module.correct_grammar(readable_file)
    return {
        'corrected_file_text': corrected_file_text,
        'corrected_file_grammar': corrected_file_grammar
    }

# python main
if __name__ == "__main__":
    app.run(debug=True)
