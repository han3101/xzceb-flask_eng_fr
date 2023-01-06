from machinetranslation import translator
from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask("Web Translator")

@app.route("/englishToFrench/<textToTranslate>")
def englishToFrench(textToTranslate):
    # textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    # return translator.english_to_french(textToTranslate)
    return render_template("index.html", result = translator.english_to_french(textToTranslate))

@app.route("/frenchToEnglish/<textToTranslate>")
def frenchToEnglish(textToTranslate):
    # textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return render_template("index.html", result = translator.french_to_english(textToTranslate))

@app.route("/englishToHebrew/<textToTranslate>")
def englishToHebrew(textToTranslate):
    # textToTranslate = request.args.get('textToTranslate')
    return render_template("index.html", result = translator.eng_to_hebrew(textToTranslate))

@app.route("/englishToSpanish/<textToTranslate>")
def englishToSpanish(textToTranslate):
    # textToTranslate = request.args.get('textToTranslate')
    return render_template("index.html", result = translator.eng_to_spanish(textToTranslate))

@app.route("/englishToChinese/<textToTranslate>")
def englishToChinese(textToTranslate):
    # textToTranslate = request.args.get('textToTranslate')
    return render_template("index.html", result = translator.eng_to_chinese(textToTranslate))

@app.route("/select", methods=('POST', 'GET'))
def select():
    textToTranslate = request.form.get('textToTranslate')
    language = request.form.get('language')
    # if not textToTranslate:
    #     flash('Please enter a text to be translated')
    # redirectRoute = str(language) + "/" + str(textToTranslate)
    return redirect(url_for(language, textToTranslate = textToTranslate))

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
