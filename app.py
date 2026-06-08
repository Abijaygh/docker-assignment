# from flask import Flask, jsonify # importing flask, telling python we need flask to run the app
# import socket # the name tag of the machine runing the app
# app = Flask(__name__) # setting up the app and giving it a name
# @app.route('/') # the route to the home page
# def home(): # the function that runs when the home page is accessed
#     return jsonify({
#         "message": "Hello from Docker!",
#         "hostname": socket.gethostname()
#     })     # returning a json response with a message and the hostname of the machine running the app

# if __name__ == '__main__': # if the script is run directly, start the app
#     app.run(host="0.0.0.0", port=5000) # running the app on all available network and on port 5000


from flask import Flask, jsonify
import socket, redis, os

app = Flask(__name__)
r = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379)

@app.route("/")
def home():
    visits = r.incr('visits')
    return jsonify({
        "message": "Hello from Docker Compose!",
        "hostname": socket.gethostname(),
        "visits": int(visits)
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)