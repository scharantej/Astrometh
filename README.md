## Flask Application Design

### HTML Files

- **home.html**: The homepage of the website, providing an overview of the complex mathematical concepts being taught and navigation links to the individual concept pages.
- **concept1.html**: A page dedicated to the first complex mathematical concept, with detailed explanations, examples, and interactive demonstrations using JavaScript.
- **concept2.html**: Similar to concept1.html, but for the second complex mathematical concept.
- **contact.html**: A contact form for users to reach out to the website creators with questions or feedback.

### Routes

- **@app.route('/')**: The root route, displaying the home.html page.
- **@app.route('/concept1')**: Displays the concept1.html page.
- **@app.route('/concept2')**: Displays the concept2.html page.
- **@app.route('/contact', methods=['GET', 'POST'])**: Handles the contact form submission.
- **@app.route('/submit_contact', methods=['POST'])**: Receives the contact form data, processes it (e.g., sends an email), and displays a success message.