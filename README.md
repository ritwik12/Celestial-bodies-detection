# Celestial-bodies-detection

## Train model

`python retrain.py   --bottleneck_dir=bottlenecks   --how_many_training_steps=500   --model_dir=inception --summaries_dir=training_summaries/basic   --output_graph=retrained_graph.pb   --output_labels=retrained_labels.txt  --image_dir=./training_data
`

## Test model

`python /home/ritwik/git/celestial_body_detection/hub/examples/image_retraining/label_image.py /home/ritwik/git/celestial_body_detection/hub/examples/image_retraining/test_data/uranus.jpg
`
