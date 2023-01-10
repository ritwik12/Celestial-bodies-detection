import tensorflow as tf
import sys
from subprocess import Popen
import os
import wikipedia
from yaml import load, SafeLoader

# returns celestial_object and labels_and_scores


def get_labels(image_data, cwd):
    # Loads label file, strips off carriage return
    label_lines = [
        line.rstrip() for line in tf.io.gfile.GFile(cwd + "/retrained_labels.txt")
    ]
    # print(label_lines)
    # Unpersists graph from file
    with tf.io.gfile.GFile(cwd + "/retrained_graph.pb", "rb") as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name="")

    # Feed the image_data as input to the graph and get first prediction
    with tf.compat.v1.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name("final_result:0")
        predictions = sess.run(
            softmax_tensor, {"DecodeJpeg/contents:0": image_data})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        labels_and_scores = [
            (label_lines[node_id], predictions[0][node_id]) for node_id in top_k
        ]

    # Get the predicted celestial object after classification
    celestial_object = label_lines[top_k[0]]
    return celestial_object, labels_and_scores

# return title, statistics and summary


def wiki(celestial_object, cwd):
    ans = celestial_object
    with open(os.path.join(cwd, "display_info.yml"), "r") as stream:
        all_display_statistics = load(stream, Loader=SafeLoader)

    req_statistics = all_display_statistics.get(ans, {})
    statistics = None
    title = None
    summary = None
    if ans in ["spiral", "elliptical"]:
        title = ("Classified Celestial Object is {} Galaxy : ".format(
            ans.capitalize()))
        summary = (wikipedia.WikipediaPage(
            title="{} galaxy".format(ans)).summary)
    elif ans in [
        "mercury",
        "venus",
        "earth",
        "mars",
        "jupiter",
        "saturn",
        "uranus",
        "neptune",
        "pluto"
    ]:
        title = ("Classified Celestial Object is {} Planet : ".format(
            ans.capitalize()))
        statistics = req_statistics.items()
        summary = (wikipedia.WikipediaPage(
            title="{} (planet)".format(ans)).summary)
    elif ans == "moon":
        statistics = req_statistics.items()
        summary = (wikipedia.WikipediaPage(title="{}".format(ans)).summary)
        title = ("Classified Celestial Object is the {} : ".format(
            ans.capitalize()))
    return title, statistics, summary


if __name__ == "__main__":
    image_path = sys.argv[1]

    # Read in the image_data
    image_data = tf.io.gfile.GFile(image_path, "rb").read()
    image_preview = "display " + image_path
    os.system(image_preview)
    print("\n")
    celestial_object, labels_and_scores = get_labels(image_data, ".")

    # Print results
    for (human_string, score) in labels_and_scores:
        print("\n--------------------------------------------------------")
        print("%s (score = %.5f)" % (human_string, score))
        print("  %.5f" % (score * 100), "%")
        print("--------------------------------------------------------")

    # Summary
    # Popen(["python", "wiki.py"])
    title, statistics, summary = wiki(celestial_object, os.getcwd())
    print("--------------------------------------------------------")
    print(title)
    print("-------------------------------------------------------- \n")
    if(statistics):
        statistics = "\n".join(
            [
                "-- {}: {}".format(parameter, value)
                for parameter, value in statistics
            ]
        )
        print("{}\n\n".format(statistics))
    print(summary)
    print("------------------------------------------------------ \n")

    ans = input("Want to know more about this image? y/n \n")
    if ans.rstrip() == "y":
        Popen(["python", "reverse_image_search.py", image_path])
