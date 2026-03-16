from flask import Flask, render_template, send_file
from generate_resume import generate_resume
import os

app = Flask(__name__, static_folder='src', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def serve_resume():
    """Serve the generated resume PDF"""
    pdf_path = 'optimized_resume_niraj_aryal.pdf'
    if not os.path.exists(pdf_path):
        generate_resume()
    return send_file(pdf_path, as_attachment=False, mimetype='application/pdf')

@app.route('/regenerate', methods=['POST'])
def regenerate_resume():
    """Regenerate the resume PDF"""
    generate_resume()
    return {'status': 'success', 'message': 'Resume regenerated successfully'}

if __name__ == '__main__':
    app.run(debug=True)
