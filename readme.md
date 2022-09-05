
## This is a simple website development using the Flask framework with Python. 

### **Flask methods** used in this project consist of:

  -  **Blueprint** - To allow us to create many templates
  -  **render_template** - Renders the template view
  -  **request** - For HTTP 'GET', 'POST' methods
  -  **flash** - To write alert messages within the website
  -  **redirect** - To redirect to url
  -  **url_for** -
    
  -  **Flask_Login** = login_user, login_required, logout_user, current_user
    
  -  **werkzeug.security** = generate_password_hash, check_password_hash
     To create authorisation when a user creates an account and has a password it will generate a hash password and will also be checked when logging in
    

Uses HTTP methods
GET, POST for sign up and login

**Jinja** - Jinja is a fast, expressive, 
extensible templating engine. Special 
placeholders in the template allow writing 
code similar to Python syntax.

*This app also touches on using Javascript to communicate with the backend when a user deletes a note. A javascript function delete note is created. The note is converted to json data where it can be deleted in the back end. Flask has a method **jsonify** that can be used in accordance to this.*


> The website focuses more on showcasing how we can develop a simple website with a back end and does not go into detail with css therefore the UI is basic > as this more focuses on how we can use python to build a fully functional website with a back end.
