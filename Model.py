from textblob import TextBlob
from language_tool_python import LanguageTool
import enchant

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = LanguageTool('en-US')
        self.dictionary = enchant.Dict("en_US")

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            # Check if the word is spelled correctly using TextBlob first
            corrected_word = str(TextBlob(word).correct())
            # If TextBlob suggests a different word, check if it's valid with pyenchant
            if corrected_word != word and not self.dictionary.check(corrected_word):            
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(corrected_word)
        return " ".join(corrected_words)
    
    def correct_grammar(self, text):
        matches = self.grammar_check.check(text)

        found_mistakes = []
        for mistake in matches:
            found_mistakes.append({
                # 'message': mistake.message,
                'replacements': mistake.replacements,
                'context': mistake.context,
            })

        found_mistakes_count = len(found_mistakes)
        return found_mistakes, found_mistakes_count
