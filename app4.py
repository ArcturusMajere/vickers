from flask import Flask, send_from_directory

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Flask App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                display: flex;
                background-image: url('/static/lol.webp');
                background-size: cover;
                background-position: center;
                color: white;
            }
            .sidebar {
                width: 200px;
                background-color: rgba(0, 0, 0, 0.7);
                color: white;
                height: 100vh;
                padding: 20px;
                box-sizing: border-box;
            }
            .sidebar a {
                display: block;
                color: white;
                text-decoration: none;
                margin: 10px 0;
                padding: 10px;
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 5px;
                text-align: center;
            }
            .sidebar a:hover {
                background-color: rgba(255, 255, 255, 0.4);
            }
            .content {
                flex: 1;
                padding: 20px;
                background-color: rgba(0, 0, 0, 0.5);
                height: 100vh;
                overflow-y: auto;
            }
            h1 {
                color: #ffdf00;
            }
            p {
                font-size: 18px;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <div class="sidebar">
            <h3>Navigation</h3>
            <a href="/">Home</a>
            <a href="/resume">Resume</a>
            <a href="/diploma1">Diploma 1</a>
            <a href="/diploma2">Diploma 2</a>
            <a href="/diploma3">Diploma 3</a>
            <a href="/paper">Sample Paper</a>
        </div>
        <div class="content">
            <h1>Johnny's Web</h1>
            <p>johnnystuto@live.com</p>
        </div>
    </body>
    </html>
    '''

# Resume Route
@app.route("/resume")
def resume():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resume</title>
    </head>
    <body>
        <h1>Resume</h1>
        <iframe src="/static/jms_y1.pdf" width="95%" height="1200px" style="border: none;"></iframe>
        <p><a href="/">Back to Home</a></p>
    </body>
    </html>
    '''

# Diploma 1 Route
@app.route("/diploma1")
def diploma1():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Diploma 1</title>
    </head>
    <body>
        <h1>Diploma 1</h1>
        <iframe src="/static/diploma1.pdf" width="95%" height="1200px" style="border: none;"></iframe>
        <p><a href="/">Back to Home</a></p>
    </body>
    </html>
    '''

# Diploma 2 Route
@app.route("/diploma2")
def diploma2():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Diploma 2</title>
    </head>
    <body>
        <h1>Diploma 2</h1>
        <iframe src="/static/diploma2.pdf" width="95%" height="1200px" style="border: none;"></iframe>
        <p><a href="/">Back to Home</a></p>
    </body>
    </html>
    '''

# Diploma 3 Route
@app.route("/diploma3")
def diploma3():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Diploma 3</title>
    </head>
    <body>
        <h1>Diploma 3</h1>
        <iframe src="/static/diploma3.pdf" width="95%" height="1200px" style="border: none;"></iframe>
        <p><a href="/">Back to Home</a></p>
    </body>
    </html>
    '''

# Sample Paper Route
@app.route("/paper")
def paper():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sample Paper</title>
    </head>
    <body>
        <h1>Sample Paper</h1>
        <iframe src="/static/sample_paper.pdf" width="95%" height="1200px" style="border: none;"></iframe>
        <p><a href="/">Back to Home</a></p>
    </body>
    </html>
    '''

# Serve Static Files
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)
