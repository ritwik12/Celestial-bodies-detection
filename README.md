# Celestial-bodies-detection

## Setup

#### Tensorflow
    
Create a virtual environment (recommended)

Python virtual environments are used to isolate package installation from the system.

Create a new virtual environment by choosing a Python interpreter and making a ./venv directory to hold it:

`virtualenv --system-site-packages -p python3 ./venv`

Activate the virtual environment using a shell-specific command:

`source ./venv/bin/activate  # sh, bash, ksh, or zsh`

If using conda, you can run
    `conda create -n tensorflow python=3.7`
    `source activate tensorflow`

#### Install Requirements
`pip install -r requirements.txt`

OR

Install Tensorflow

`pip install tensorflow==1.14`  

Install wikipedia

`pip install wikipedia` 

Install PyYAML

`pip install PyYAML`
 
#### Inception

Downloaded automatically while training

## Using Model

#### Classified Neptune Image and percentage of Accuracy

![output1](https://user-images.githubusercontent.com/20038775/51538729-0cbafa80-1e78-11e9-95c1-492693e60aaa.png)


#### Classified Jupiter Image and percentage of Matched Accuracy

![output3](https://user-images.githubusercontent.com/20038775/51538741-16dcf900-1e78-11e9-9ef7-bcf2ca35ed91.png)


#### Shows the percentage of every class

![output2](https://user-images.githubusercontent.com/20038775/51539062-05e0b780-1e79-11e9-9073-03d33bfa25aa.png)


#### Fetched information from Internet

![output4](https://user-images.githubusercontent.com/20038775/51538745-180e2600-1e78-11e9-9636-bce4ce66cbae.png)


#### Reverse Search of Classified Image

![output5](https://user-images.githubusercontent.com/20038775/51538748-18a6bc80-1e78-11e9-822e-ae588ed2f78b.png)


#### Accuracy of matching of Spiral Galaxy

![output6](https://user-images.githubusercontent.com/20038775/51538750-193f5300-1e78-11e9-85a2-841a7a35490f.png)


#### Fetched information from Internet of the Classified Class

![output7](https://user-images.githubusercontent.com/20038775/51538753-19d7e980-1e78-11e9-9d55-cfbda95200fa.png)



## Train model

`python retrain.py --bottleneck_dir=bottlenecks --how_many_training_steps=500 --model_dir=inception --summaries_dir=training_summaries/basic --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --image_dir=./training_data
`

## Test model

`python label_image.py test_data/uranus.jpg`

## INCEPTION

![1_c26y0gugmtvnskibfuja_w](https://user-images.githubusercontent.com/20038775/51536739-8f40bb80-1e72-11e9-8863-b79a347d80f4.png)


The Inception network was an important milestone in the development of CNN classifiers. Prior to its inception (pun intended), most popular CNNs just stacked convolution layers deeper and deeper, hoping to get better performance.

The Inception network, on the other hand, was complex (heavily engineered). It used a lot of tricks to push performance; both in terms of speed and accuracy. Its constant evolution led to the creation of several versions of the network.

The below image is the “naive” inception module. It performs convolution on an input, with 3 different sizes of filters (1x1, 3x3, 5x5). Additionally, max pooling is also performed. The outputs are concatenated and sent to the next inception module.

![inception](https://user-images.githubusercontent.com/20038775/51536689-68828500-1e72-11e9-8a7c-ae8e3a3939e9.png)


## CELESTIAL BODIES

An astronomical object or celestial object is a naturally occurring physical entity, association, or structure that exists in the observable universe. [1] In astronomy, the terms object and body are often used interchangeably. However, an astronomical body or celestial body is a single, tightly bound, contiguous entity, while an astronomical or celestial object is a complex, less cohesively bound structure, which may consist of multiple bodies or even other objects with substructures. 

Examples of astronomical objects include planetary systems, star clusters, nebulae, and galaxies, while asteroids, moons, planets, and stars are astronomical bodies. A comet may be identified as both body and object: It is a body when referring to the frozen nucleus of ice and dust, and an object when describing the entire comet with its diffuse coma and tail.

### ASTEROIDS

Asteroids are minor planets, especially of the inner Solar System. Larger asteroids have also been called planetoids. These terms have historically been applied to any astronomical object orbiting the Sun that did not resolve into a disc in a telescope and was not observed to have characteristics of an active comet such as a tail. As minor planets in the outer Solar System were discovered that were found to have volatile-rich surfaces similar to comets, these came to be distinguished from the objects found in the main asteroid belt.(https://en.wikipedia.org/wiki/Asteroid)

* **16 Psyche:** 16 Psyche is a giant metal asteroid, about three times farther away from the sun than is the Earth. Its average diameter is about 140 miles. Unlike most other asteroids that are rocky or icy bodies, scientists think the M-type (metallic) asteroid 16 Psyche is comprised mostly of metallic iron and nickel similar to Earth’s core. Scientists wonder whether Psyche could be an exposed core of an early planet, maybe as large as Mars, that lost its rocky outer layers due to a number of violent collisions billions of years ago.(https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/16-psyche/in-depth/)

![16 Psyche](https://solarsystem.nasa.gov/system/content_pages/main_images/416_16_psyche_main.jpg)

* **10199 Chariklo:** Chariklo was one fo the first asteroids found in our solar system to have a ring system.With a diameter of about 188 miles, Chariklo is one of the largest memebrs of the asteroid class known as Centaurs.Its orbit is located between Saturn and Uranus in the outer solar system.(https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/10199-chariklo/in-depth/)

![10199 Chariklo](https://solarsystem.nasa.gov/system/content_pages/main_images/411_10199_chariklo_main.jpg)

* **101955 Bennu:** Bennu is estimated to be more than 4.5 Billion years old. Scientist think that it mayt contain organic molecules similar to that of which life on Earth sprouted from. Bennu is known as a potentially hazardous asteroid with a 1-ini-2,700 chance of impacting Earth during its close approach in the late 22nd century. (https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/101955-bennu/overview/)

![101955 Bennu](https://solarsystem.nasa.gov/system/feature_items/images/455_20181029t1019ut_bennu_800.jpg)

* **243 Ida:** Ida is the first asteroid found to have its own moon and the second to be visited by a spacecraft.Located in the main belt between Mars and Jupyter, Ida is one of the Kornis family of asteroids. An S-type asteroid, Ida is composed of mainly silicate rock.   (https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/243-ida/in-depth/)

![243 Ida](https://solarsystem.nasa.gov/system/content_pages/main_images/417_Ida_Dactyl_main.jpg)

* **25143 Itokawa:** Itokawa is the first asteroid to have samples captured and brought back to earth. The samples delivered by the Japanese spacecraft Hyabusa revealed that this asteroid was once part of a larger object. Few craters are visible on its surface, presumably becouse any impact is quickly filled by the loose rocks and dust on its surface.  (https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/25143-itokawa/in-depth/)

![25143 Itokawa](https://solarsystem.nasa.gov/system/content_pages/main_images/425_itokawa_main.jpg)

* **253 Matilde:** 253 Mathilde is an asteroid in the main belt between Mars and Jupiter, where it orbits the Sun once every 4.3 years. It's about 52 kilometers across, and notable for its very slow rotation rate--it takes 17.4 days for the asteroid to turn on its axis.Mathilde is a C-type asteroid, which means that it is made of rock rich in carbon, and is probably very little changed in the last 4.5 billion years, a time capsule from the time the planets first formed. All that carbon helps make Mathilde one of the darkest objects in the Solar System. It reflects only 4 percent of the light falling on it.  (https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/253-mathilde/in-depth/)

![253 Matilde](https://solarsystem.nasa.gov/system/content_pages/main_images/427_Mathilde1_main.jpg)

* **433 Eros:** 433 Eros

433 Eros was discovered on Aug. 13, 1898 by Gustav Witt, director of the Urania observatory in Berlin, and independently on the same day by Auguste H.P. Charlois at Nice, France.Witt's discovery was the accidental byproduct of a two-hour photographic exposure he conducted of a different asteroid: 185 Eunike. Along with Eunike, the image he produced showed a 0.4-mm image trail, and observations on the following evening identified the object as one of unusually high apparent motion on the sky. Less than two weeks later, Adolf J. Berberich computed that the object's orbit brought it well inside the orbit of Mars, making it the first-known near-Earth asteroid.

 (https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/433-eros/in-depth/)

![433 Eros](https://solarsystem.nasa.gov/system/content_pages/main_images/454_Eros_main.jpg)

### GALAXIES
A galaxy is an enormous collection of interstellar dust, gas, stellar remnant, stars along with their own solar systems held together by gravity. Earth is situated in the Milky Way galaxy. The Milky Way is a spiral-shaped galaxy with a diameter ranging 100,000 and 180,000 light-years. Our galaxy was thought to contain all the stars in the universe until, in 1920, Edwin Hubble observed that the Milky Way is one of many galaxies in the universe and that every galaxy contains potentially billions or trillions of stars. To this day, only a small fraction of galaxies have been discovered. 

In recent years, astronomy has become an immensely data-rich field with numerous digital sky surveys across a wide range of wavelengths. For example, the Sloan Digital Sky Survey will produce over 50,000,000 images of galaxies in the near future. Studying the morphology of galaxies is one of the most important aspects of answering many of the questions to which humanity does not yet know the answer, namely the creation of the universe. Scientists can understand the origin, formation, and evolution of galaxies by classifying galaxies by their structural appearance. The morphological classification of galaxies in a large database is important to help astronomers reduce classification errors and to help them collect statistical and observational data and discover the mystery of nature in general. 

Astronomers can look into time and space as far as billions of light years away from Earth and explore millions of galaxies far away using space telescopes that are much more powerful than our eyesight.

![galaxies](https://user-images.githubusercontent.com/20038775/51533376-a7abd880-1e68-11e9-831f-18a1b0cc4f07.png)
Figure 1: Three classes of galaxy morphological. From left to right: Elliptical Shaped Galaxy, Spiral
Shaped Galaxy and Irregular Shaped Galaxy (en.Wikipedia.org, 2006)

There are different types of galaxies:

* **ELLIPTICAL** 

    An elliptical galaxy is a type of galaxy having an approximately ellipsoidal shape and a smooth, nearly featureless image.      
    Unlike flat spiral galaxies with organization and structure, elliptical galaxies are more three-dimensional, without much 
    structure, and their stars are in somewhat random orbits around the center.
    
* **SPIRAL**

    Spiral galaxies form a class of galaxy originally described by Edwin Hubble in his 1936 work The Realm of the Nebulae and, as 
    such, form part of the Hubble sequence. Most spiral galaxies consist of a flat, rotating disk containing stars, gas and dust, 
    and a central concentration of stars known as the bulge.
    
* **IRREGULAR**

    An irregular galaxy is a galaxy that does not have a distinct regular shape, unlike a spiral or an elliptical galaxy. 
    Irregular galaxies do not fall into any of the regular classes of the Hubble sequence, and they are often chaotic in 
    appearance, with neither a nuclear bulge nor any trace of spiral arm structure.
    
### PLANETS

A planet is an astronomical body orbiting a star or stellar remnant that is massive enough
to be rounded by its own gravity, is not massive enough to cause thermonuclear fusion,
and has cleared its neighbouring region of planetesimals.
There are a total of 8 planets in our solar system:

* **Mercury:** is the closest planet to the sun and the smallest planet in our solar system. Mercury has a rotation of 88 days around the sun. The close proximity of Mercury to the sun causes the surface temperatures to reach a high of 840°F during the day and hundreds of degrees below the freezing point at night. Mercury does not have an atmosphere due to the extreme temperatures. Without an atmosphere, the surface of Mercury is covered with pockmarks and craters from meteor impacts. 

![mercury](https://user-images.githubusercontent.com/20038775/51534561-16d6fc00-1e6c-11e9-8e7b-1859f81f6213.jpg)

* **Venus:** is the third planet from the sun and the hottest planet in the solar system. [Venus](https://en.wikipedia.org/wiki/Venus) primarily consists of carbon dioxide which makes the planet toxic. The atmospheric pressure of Venus is capable of crushing anyone who landed on its surface. Venus can be seen by the naked eye from Earth. Thick clouds shroud Venus, making it difficult to see the details of the planet's surface. 

![venus](https://user-images.githubusercontent.com/20038775/51534566-18082900-1e6c-11e9-9756-2a90522b5b0a.jpg)

* **Earth:** also known as "Terra", is the third planet from the sun. [Earth](https://en.wikipedia.org/wiki/Earth) is the only planet in our solar system that is capable of sustaining life. The rotation of Earth around the sun is approximately 365 days. The estimated age of the Earth is 4.54 billion years.

![earth](https://user-images.githubusercontent.com/20038775/51534558-163e6580-1e6c-11e9-920e-1f495fae4179.jpg)

* **Mars:** is the fourth planet from the sun. [Mars](https://en.wikipedia.org/wiki/Mars) is also known as the "red planet" because of the reddish color formed by the high iron content in its soil. The rotation of Mars around the sun is approximately 686 days. The thin atmosphere of Mars consists mainly of carbon dioxide which makes it unsuitable for sustaining life. Scientists believed Mars to have once been capable of sustaining life and still might be able to in the future. 

![mars](https://user-images.githubusercontent.com/20038775/51534560-16d6fc00-1e6c-11e9-96bf-3e71e6819326.jpg)

* **Jupiter:**  the largest planet in our system, the mysteries of Jupiter has fascinated
astronomers and non-astronomers alike for centuries. Poisonous gases completely
cover its surface, hiding what lies beneath and violent storms prevent any landings
of probes onto or images taken of the giant planet. Jupiter's atmosphere has been
determined to be similar to that of the sun containing elements of hydrogen and
helium.

![jupiter](https://user-images.githubusercontent.com/20038775/51534559-163e6580-1e6c-11e9-8938-500f7ad8849f.jpg)

* **Saturn:**  first viewed via telescope in 1610 by Galileo Galilei, is the 6th planet
in our solar system from the sun. Like Jupiter, its atmosphere is composed
primarily of helium and hydrogen and it is the only planet discovered so far that
has a lower density than water, approximately 30% lower. It is surrounded by a set
of 9 whole rings and 3 broken rings that are comprised mainly of ice, rock, and
space "dust".

![saturn](https://user-images.githubusercontent.com/20038775/51534564-176f9280-1e6c-11e9-9289-10da8ba0677a.jpg)

* **Uranus:** also known as the "sideways planet" because of its awkward rotation, is the 7th planet in our solar system from the sun. Uranus' North and South poles are located where other planets equators are. Seasons are 20 years long due to Uranus' strange rotation. The bluish color of Uranus' atmosphere is caused by methane gases, but the main elements are helium and hydrogen. 

![uranus](https://user-images.githubusercontent.com/20038775/51534565-176f9280-1e6c-11e9-98d5-2894a5a2b1ba.jpg)


* **Neptune:**  is known as the windiest planet in our solar system and 8th furthermost
known "planet" from our sun. It has a revolution around the sun of 165 Earth years.
Like Uranus, Neptune has high traces of methane in its atmosphere, which
contributes to its blue color. It is believed there is a second "unknown" element,
though, that makes it a much brighter blue than Uranus.

![neptune](https://user-images.githubusercontent.com/20038775/51534562-16d6fc00-1e6c-11e9-913a-39d91368573a.jpg)

# License

ritwik12/Celestial-bodies-detection is licensed under the GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.
1. The origin of this software must not be misrepresented; you must not
 claim that you wrote the original software. If you use this software
 in a product, an acknowledgment in the product documentation would be
 appreciated but is not required.
 2. Altered source versions must be plainly marked as such, and must not be
 misrepresented as being the original software.



