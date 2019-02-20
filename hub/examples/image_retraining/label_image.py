import tensorflow as tf, sys
from subprocess import Popen
import os
import wikipedia
from yaml import load

image_path = sys.argv[1]

# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line in tf.gfile.GFile("./retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("./retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')
    
# Feed the image_data as input to the graph and get first prediction
with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print "\n--------------------------------------------------------"
        print('%s (score = %.5f)' % (human_string, score))
        print '  %.5f' % (score*100),"%"
        print "--------------------------------------------------------"
# Get the predicted celestial object after classification
celestial_object = label_lines[top_k[0]]
#Popen(["python", "wiki.py"])

image_preview="display "+image_path
os.system(image_preview)        
print "\n"


def wiki(celestial_object):
    ans = celestial_object
    with open(os.path.join(r'examples/image_retraining/display_info.yaml'), 'r') as stream:
        all_display_statistics = load(stream)

    req_statistics = all_display_statistics.get(ans, {})
    statistics = "\n".join(['{}:{}'.format(parameter, value) for parameter, value in req_statistics.items()])

    if ans in ["spiral", "elliptical"]:
        print("--------------------------------------------------------")
        print("Classified Celestial Object is {} Galaxy : ".format(ans.capitalize()))
        print("-------------------------------------------------------- \n")
        # print(wikipedia.summary("Spiral Galaxy", sentences=2))
        print(statistics)
        print(wikipedia.WikipediaPage(title='{} galaxy'.format(ans)).summary)
    elif ans in ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']:
        print("--------------------------------------------------------")
        print("Classified Celestial Object is {} Planet : ".format(ans.capitalize()))
        print("-------------------------------------------------------- \n")
        print(statistics)
        # print(wikipedia.summary("Mercury (planet)", sentences=2))
        print(wikipedia.WikipediaPage(title='{} (planet)'.format(ans)).summary)
    return " "

print wiki(celestial_object)
print("------------------------------------------------------ \n")
ans = raw_input("Want to know more about this image? y/n \n")
if ans.rstrip() is "y":
    Popen(["python", "reverse-image-search.py", image_path])