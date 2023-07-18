from flask import Flask, request, jsonify
from bardapi import Bard
import os

app = Flask(__name__)

os.environ['_BARD_API_KEY'] = "YwjINDGxf536sZ-cBs-jTIHvG1w4wC718LWZJivc8IsjAWjxtbwzg_agx51044O4DfNO-Q."

@app.route('/api/answer', methods=['POST'])
def get_answer():
    # Retrieve data from the request
    data = request.json
    message = data['message']

    # Call Bard API to get the answer
    answer = Bard().get_answer(str(message))['content']

    # Return the answer as a JSON response
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')