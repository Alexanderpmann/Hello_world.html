from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name): #don't overthink it. remember to value the two above for say_name = say/name
    return f"Hi, {name.capitalize()}!" #f string to tie together function

@app.route('/repeat/<int:num>/<string:word>') #as simple as just using int:num, and string:word
def repeat_word(num, word): # num, word
    output= ''

    for i in range(0,num):
        output += f"<p>{word}</p>" #function to repeat/print count out numbers based on the num input in route

    return output

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# import statements, maybe some other routes
    
# @app.route('/success')
# def success():
#     return "success"
    
# # app.run(debug=True) should be the very last statement! 

# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(name)
#     return "Hello, " + name

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
# #     print(id)
#     return "username: " + username + ", id: " + id

