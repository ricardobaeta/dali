# {d}ali

### Understanding and applying Gestalt Laws of Perceptual Organization

![{d}ali](assets/{d}ali.png)

### Vision for Release 1.1

The objective for this release is to address the fundamental principle of Gestalt Laws of Perception - the law of Prägnanz - focusing on understanding and applying the Laws of **Proximity**, **Similarity** and **Good Gestalt**.

The law of proximity states that when an individual perceives an assortment of objects they perceive objects that are close to each other as forming a **group**. For now, we'll only be addressing the composition of this group perception on a **vertical stack**.

The law of similarity states that elements within an assortment of objects are perceptually grouped together if they are **similar to each other**. For now we'll only be addressing when perception occurs in the form of **shape**.

The law of good gestalt explains that elements of objects tend to be perceptually grouped together if they form a pattern that is regular, simple, and orderly. For now we'll only be adressing this perception on a **horizontal stack** of the **vertical stack** composition.

> The birth of {d}ali will be grounded on the undertsanding of the purest expression of primitive visual artifacts: circles, triangles and squares.

---

### Coding Principles

#### Module One

The objective of this module is to **analyse**, **recognize**, and **group** similar simple geometric shapes.

The Analysis, ideally, would benefit from having a dataset of simple geometric shapes, for the analysis to be streamlined. This analysis will only have a structured output if the input itself is structured as well, therefore people will be able to input as many and diverse simple geometric shapes as they want. The Recognition, ideally, would benefit from the dataset analysis output, and would help to start creating some meta-information about each object. Hard data, easy solutions. The grouping, ideally, would be a comprehensive data composition, strong enough to feed Module Two. This is not aesthetics.

For this release, I'm getting the geometric shapes with an adaptation of [OpenCV shape detection](https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/). It's a marvelous work done by [Adrian Rosebrock](@PyImageSearch) from [PyImageSearch](https://www.pyimagesearch.com/). It's miles ahead from the method used on the previous release, nevertheless I welcome the work there is to be done, time and time again, to get it better.

#### Module Two

The objective of this module is to **eliminate complexity and unfamiliarity** so we can obtain an output in its most simplistic form. Eliminating extraneous stimuli helps our minds creating meaning. This meaning created by perception implies a global regularity, which is often mentally prioritized over spatial relations. The visual translation of every group of shapes composition implies the ideas of salience, conciseness and orderliness.

> For now, this module it's based on the vertical stack of similar shape groups, which is pretty much immature. I welcome the work there is to be done, time and time again.

#### Module Three

The objective of this module is an attempt to understand the laws behind the ability to **acquire and maintain meaningful perceptions** in an apparently chaotic world. Based on the input from Module One and Module Two, this third module should decrease the effort of the perception of simplicity in the midst of the compositions of several and diverse objects and increase the ability to recognize order.

> For now, this module it's based on the horizontal stack of the vertical stack of similar shape groups, which is pretty much immature. I welcome the work there is to be done, time and time again.

---

### Installation

> This is a pretty straightforward setup, and I'll do my best to keep it as simple as possible on the following releases.

The recommended way to install **{d}ali** is:

1. Install Homebrew

To install or upgrade Homebrew, read the instructions from the [oficial site](https://brew.sh).

2. Install Python 3

To install or upgrade Python 3, read the instructions from the [oficial site](https://www.python.org/).

3. Install PIP

To install or upgrade pip, read the instructions from the [oficial site](https://pip.pypa.io/en/stable/installing/).

4. Install numpy

To install or upgrade numpy, read the instructions from the [oficial site](https://scipy.org/install.html/).

5. Install OpenCV

To install or upgrade OpenCV, read the instructions from the [oficial site](https://pypi.org/project/opencv-python/).

5. Install opencv_contrib Module

To install or upgrade opencv_contrib Module, read the instructions from the [oficial site](https://pypi.org/project/opencv-contrib-python/).

6. Install imutils

To install or upgrade imutils, read the instructions from the [oficial site](https://pypi.org/project/imutils/).

---

### Running {d}ali

```
$ python3 main.py
```

---

#### Acknowledgements

Thanks to all the brilliant people at [source{d}](https://sourced.tech/) who I have the luck to work with, being always such a huge inspiration. A strong hug to my special друг [Egor](https://github.com/EgorBu).

Many statements in this file are partially taken from [Gestalt Psychology](https://en.wikipedia.org/wiki/Gestalt_psychology).
