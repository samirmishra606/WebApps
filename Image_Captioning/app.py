from flask import Flask, render_template, redirect, request

import caption


#__name__ == __main__
app = Flask(__name__)

# model = joblib.load("model.pkl")


@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def marks():
	if request.method == 'POST':

		f = request.files['userfile']
		path = "./static/{}".format(f.filename)  #./static/images.jpg
		f.save(path) 

		caption_it = caption.caption_this_image(path)
		print(caption_it)
		

	return render_template("index.html", your_caption = caption_it)


if __name__ == '__main__':
	app.run(debug=True)
