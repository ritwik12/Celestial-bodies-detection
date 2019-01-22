# Celestial-bodies-detection

## CELESTIAL BODIES

An astronomical object or celestial object is a naturally occurring physical entity, association, or structure that exists in the observable universe. [1] In astronomy, the terms object and body are often used interchangeably. However, an astronomical body or celestial body is a single, tightly bound, contiguous entity, while an astronomical or celestial object is a complex, less cohesively bound structure, which may consist of multiple bodies or even other objects with substructures. 

Examples of astronomical objects include planetary systems, star clusters, nebulae, and galaxies, while asteroids, moons, planets, and stars are astronomical bodies. A comet may be identified as both body and object: It is a body when referring to the frozen nucleus of ice and dust, and an object when describing the entire comet with its diffuse coma and tail.

### GALAXIES
A galaxy is a gigantic collection of interstellar dust, gas, stellar remnant, stars along with their own solar systems. All held together by the force of gravity. Earth is located in a galaxy called the Milky Way. The Milky Way is a spiral shaped galaxy that has a diameter between 100,000 and 180,000 light years across. We used to think that our galaxy contained all the stars in the universe until in 1920, observations by Edwin Hubble showed that Milky Way is just one of many galaxies in the universe and that each galaxy contains billions or even trillions of stars within it.

There are so many galaxies out there in the universe that there could be as many as tens of billions of undiscovered galaxies and we have only discovered a fraction of that. In recent years, with numerous digital sky surveys across a wide range of wavelengths, astronomy has become an immensely data-rich field. For example, the Sloan Digital Sky Survey will produce more than 50,000,000 images of galaxies in the near future. Studying the viimorphology of galaxies is one of the most important aspects of answering many of the questions that mankind does not know the answer to yet and that is the creation of the universe. By  classifying galaxies into different groups in terms of their structure appearance, scientists will be able to understand the origin and formation of galaxies as well as the evolution process of the universe. Galaxy morphological classification on a
large-scale database is important to help astronomers reduce classification errors and to help them produce collections of statistical and observational purposes as well as discovering the mystery of nature at large.

With the help of space telescopes that are much more powerful than our eyesight, astronomers are able to look into time and space as far as billions of light years away from Earth and explore millions of galaxies far away from our own.


## Train model

`python retrain.py   --bottleneck_dir=bottlenecks   --how_many_training_steps=500   --model_dir=inception --summaries_dir=training_summaries/basic   --output_graph=retrained_graph.pb   --output_labels=retrained_labels.txt  --image_dir=./training_data
`

## Test model

`python /home/ritwik/git/celestial_body_detection/hub/examples/image_retraining/label_image.py /home/ritwik/git/celestial_body_detection/hub/examples/image_retraining/test_data/uranus.jpg
`
