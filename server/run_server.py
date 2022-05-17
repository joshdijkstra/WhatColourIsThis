import numpy as np
import time
from flask import Flask , request
from colourPicker import find_closest_colour

app = Flask(__name__)

@app.route('/Guess', methods=["GET"])
def predict_colour():
    input_data = request.args.get("colour")
    print(input_data)
    colour_name , colour_hex = find_closest_colour(input_data)
    print(colour_name)
    return {'colour_name' : colour_name,
            'colour_hex' : colour_hex}
    
@app.route('/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == '__main__':
    app.run()
