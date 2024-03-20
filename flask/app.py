from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        # Save the uploaded file with a specific name
        image_path = os.path.join(app.root_path, 'uploads', 'image.png')
        file.save(image_path)
        # Run the check.py script
        result = subprocess.run(['python', 'check.py', image_path], capture_output=True, text=True)
        output = result.stdout
        return render_template('result.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
