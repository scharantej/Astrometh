
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Define the root route
@app.route('/')
def home():
    # Render the home page
    return render_template('home.html')

# Define the route for concept 1
@app.route('/concept1')
def concept1():
    # Render the concept1 page
    return render_template('concept1.html')

# Define the route for concept 2
@app.route('/concept2')
def concept2():
    # Render the concept2 page
    return render_template('concept2.html')

# Define the route for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Process the form data (e.g., send an email)

        # Display a success message
        return render_template('contact.html', success=True)
    else:
        # Display the contact form
        return render_template('contact.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
