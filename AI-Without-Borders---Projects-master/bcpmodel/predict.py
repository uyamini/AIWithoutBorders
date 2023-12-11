from flask import Flask, jsonify, make_response, request
#curl http://localhost:5000/predict \
#--request POST \
#--header "Content-Type: application/json" \
#--data '{"address": "cell"}'
import keras
import numpy as np
from PIL import Image
import os

# IMAGE_PATH = "/home/gajendra/bcpmodel/"
def channel_zeropad(x, channel_axis=3):
	'''
	Zero-padding for channle dimensions.
	Note that padded channles are added like (Batch, H, W, 2/x + x + 2/x).
	'''
	shape = list(x.shape)
	y = keras.backend.zeros_like(x)

	if channel_axis == 3:
	    y = y[:, :, :, :shape[channel_axis] // 2]
	else:
	    y = y[:, :shape[channel_axis] // 2, :, :]

	return keras.layers.concatenate([y, x, y], channel_axis)

def channel_zeropad_output(input_shape, channel_axis=3):
	'''
	Function for setting a channel dimension for zero padding.
	'''
	shape = list(input_shape)
	shape[channel_axis] *= 2

	return tuple(shape)

model = keras.models.load_model('mySeResnextModel.hdf5', custom_objects= {'channel_zeropad': channel_zeropad, 'channel_zeropad_output': channel_zeropad_output})
# model.compile(loss='categorical_crossentropy', optimizer='Adamax', metrics=['accuracy'])

app = Flask(__name__)

def load_image(image):
	image = image + ".bmp"
	image = np.array(Image.open(image))
	image = float(image/255)
	return image


def predict_image(image):
	image = load_image(image)
	prediction = model.predict(image)
	return prediction

@app.route('/')
def hello_world():
	value = "Hello World! \n This api is made to predict blood cancer for a provided cell image!"
	return value


@app.route('/value', methods = ["GET"])
def bringit():
	if request.method == 'GET':
		string = input("Enter address of image: ")
		string = str(string) + " VOILA!"
		return jsonify(string)

@app.route('/predict', methods = ["POST"])
def predict():
	try:
		if "address" in request.get_json():
			data = request.get_json()['address']
			return jsonify(predict_image(data))
	except KeyError:
		return jsonify("Provide a proper value for address!")



if __name__ == '__main__':
	app.run(debug = True)
