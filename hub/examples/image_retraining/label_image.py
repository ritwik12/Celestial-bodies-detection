import tensorflow as tf, sys
from subprocess import Popen
import os
import wikipedia

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

    if(ans == "spiral"):
        print("--------------------------------------------------------")
        print("Classified Celestial Object is Spiral Galaxy : ")
        print("-------------------------------------------------------- \n")
        #print(wikipedia.summary("Spiral Galaxy", sentences=2))
        print(wikipedia.WikipediaPage(title = 'Spiral galaxy').summary)
    elif(ans == "elliptical"):
        print("--------------------------------------------------------")
        print("Classified Celestial Object is Elliptical Galaxy : ")
        print("-------------------------------------------------------- \n")
        #print(wikipedia.summary("Elliptical galaxy", sentences=2))
        print(wikipedia.WikipediaPage(title = 'Elliptical galaxy').summary)
    elif(ans == "mercury"):
        print("--------------------------------------------------------")
        print("Classified Celestial Object is Mercury Planet : ")
        print("-------------------------------------------------------- \n")
        #print(wikipedia.summary("Mercury (planet)", sentences=2))
        print(wikipedia.WikipediaPage(title = 'Mercury (planet)').summary)
    elif(ans == "venus"):
        print("--------------------------------------------------------")
        print("Classified Celestial Object is Venus Planet : ")
        print("-------------------------------------------------------- \n")
        #print(wikipedia.summary("Venus", sentences=2))
        print(wikipedia.WikipediaPage(title = 'Venus').summary)
    elif(ans == "earth"):
        print("--------------------------------------------------------")
        print("Classified Celestial Object is Earth Planet : ")
        print("-------------------------------------------------------- \n")
        #print(wikipedia.summary("Earth", sentences=2))
        print(wikipedia.WikipediaPage(title = 'Earth').summary)
    elif(ans == "mars"):
        print("--------------------------------------------------------")
        print("Classified Celestial Object is Mars Planet : ")
        print("-------------------------------------------------------- \n")
        #print(wikipedia.summary("Mars", sentences=2))
        print(wikipedia.WikipediaPage(title = 'Mars').summary)
    elif(ans == "jupiter"):
        print("--------------------------------------------------------")
        print("Classified Celestial Object is Jupiter Planet : ")
        print("-------------------------------------------------------- \n")
        #print(wikipedia.summary("Jupiter", sentences=2))
        print(wikipedia.WikipediaPage(title = 'Jupiter').summary)
    elif(ans == "saturn"):
        print("--------------------------------------------------------")
        print("Classified Celestial Object is Saturn Planet : ")
        print("-------------------------------------------------------- \n")
        #print(wikipedia.summary("Saturn", sentences=2))
        print(wikipedia.WikipediaPage(title = 'Saturn').summary)
    elif(ans == "uranus"):
        print("--------------------------------------------------------")
        print("Classified Celestial Object is Uranus Planet : ")
        print("-------------------------------------------------------- \n")
        #print(wikipedia.summary("Uranus", sentences=2))
        print(wikipedia.WikipediaPage(title = 'Uranus').summary)
    elif(ans == "neptune"):
        print("--------------------------------------------------------")
        print("Classified Celestial Object is Neptune Planet : ")
        print("-------------------------------------------------------- \n")
       # print(wikipedia.summary("Neptune", sentences=2))
        print(wikipedia.WikipediaPage(title = 'Neptune').summary)
    return " "

print wiki(celestial_object)
print("------------------------------------------------------ \n")
ans = raw_input("Want to know more about this image? y/n \n")
if ans.rstrip() is "y":
    Popen(["python", "reverse-image-search.py", image_path])