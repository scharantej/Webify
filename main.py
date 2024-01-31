
# Import necessary modules
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def homepage():
    """
    Renders the homepage of the website.

    Returns:
        The rendered homepage HTML template.
    """
    return render_template('index.html')

# Define the route for the basics page
@app.route('/basics')
def basics():
    """
    Renders the basics page of the website.

    Returns:
        The rendered basics HTML template.
    """
    return render_template('basics.html')

# Define the route for the design page
@app.route('/design')
def design():
    """
    Renders the design page of the website.

    Returns:
        The rendered design HTML template.
    """
    return render_template('design.html')

# Define the route for the development page
@app.route('/development')
def development():
    """
    Renders the development page of the website.

    Returns:
        The rendered development HTML template.
    """
    return render_template('development.html')

# Define the route for the deployment page
@app.route('/deployment')
def deployment():
    """
    Renders the deployment page of the website.

    Returns:
        The rendered deployment HTML template.
    """
    return render_template('deployment.html')

# Define the route for the resources page
@app.route('/resources')
def resources():
    """
    Renders the resources page of the website.

    Returns:
        The rendered resources HTML template.
    """
    return render_template('resources.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
