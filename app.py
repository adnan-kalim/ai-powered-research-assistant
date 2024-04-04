from flask import Flask,send_from_directory, render_template, request
import Scraper  # Assuming script.py is in the same directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=['POST'])
def search():
    query = request.form['query']  # Make sure this matches your form input's name attribute
    abstracts = Scraper.fetch_arxiv_abstracts(query)
    if abstracts:
        # Modify this to your needs; possibly return a confirmation or redirect
        Scraper.save_abstracts_to_pdf(abstracts, "research_abstracts.pdf")
        return render_template("result.html", abstracts=abstracts)
    else:
        return "No results found", 404  # Or redirect to an error page



if __name__ == "__main__":
    app.run(debug=True)
