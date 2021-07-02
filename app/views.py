import os
from io import BytesIO
from base64 import b64encode

import requests
import tensorflow as tf
from PIL import Image
from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, validators

from app import app
from hub.examples.image_retraining.label_image import get_labels, wiki
from hub.examples.image_retraining.reverse_image_search import reverseImageSearch

# no secret key set yet
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY


class SelectImageForm(FlaskForm):
    image_url = StringField(
        "image_url",
        validators=[validators.Optional(), validators.URL()],
        render_kw={"placeholder": "Enter a URL"},
    )
    image_file = FileField(
        "file",
        validators=[
            validators.Optional(),
            FileAllowed(["jpg", "jpeg", "png", "gif"], "Invalid File"),
        ],
        render_kw={"class": "custom-file-input"},
    )

@app.route("/", methods=["GET", "POST"])
def index():
    # image in memory will be used on reload
    global imageBytes
    form = SelectImageForm()
    if form.validate_on_submit():

        if request.files.get(form.image_file.name):
            # from file
            imageBytes = request.files[form.image_file.name].read()
            im = Image.open(BytesIO(imageBytes))
            # cant save RGBA as JPEG
            im_resize=im.convert('RGB')
            # resize using PIL
            max_width = 1000
            if(im.size[0]>max_width):
                im_resize=im.resize((max_width,int(max_width/im.size[0]*im.size[1])))
            buf = BytesIO()
            filext = request.files[form.image_file.name].filename.split('.')[-1].upper()
            if(filext=='JPG'):
                filext='JPEG'
            im_resize.save(buf, format=filext)
            # get back bytes
            imageBytes = buf.getvalue()
            print("using form")

        elif form.image_url.data:
            # from url
            response = requests.get(form.image_url.data)
            imageBytes = BytesIO(response.content).read()
            print("using url")
        else:
            # empty form
            return render_template("index.html", form=form)

        return redirect(url_for("result"))
    # print(form.errors)

    return render_template("index.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/result")
def result():
    cwd = os.path.join(app.root_path, "..", "hub", "examples", "image_retraining")
    try:
        celestial_object, labels = get_labels(imageBytes, cwd)
    except NameError:
        return render_template("error.html", detail="You are not supposed to be here.")
    except Exception as e:
        return render_template("error.html", detail=str(e))
    title, properties, description = wiki(celestial_object, cwd)

    return render_template(
        "result.html",
        image=b64encode(imageBytes).decode("utf-8"),
        labels=labels,
        title=title,
        description=description,
        properties=properties,
    )


@app.route("/redirectToGoogle")
def redirectToGoogle():
    searchUrl = reverseImageSearch(imageBytes)
    return redirect(searchUrl, 302)