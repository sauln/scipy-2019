class: center, middle, borderless

<div class="banner">
<img src="images/banner.jpg" alt="abstract rips complex">
</div>

# Scikit-TDA
Topological Data Analysis for the Python ecosystem.
<p class="smallish">
<b>Nathaniel Rivera Saul</b><br>
.smallish[Scipy<br>July 2019]
</p>

---

# Preface

- Before Scikit-TDA 
    - Lots of different tools. 
    - Large amounts of feature overlap. 
    - Small amounts of interoperability.

- After Scikit-TDA
    - Lots of different tools + 1 more.

- Our objectives
    - Curate implementations rather than building new ones.
    - Build something that was easy to use. 
    - Build something people could contribute to.

---

# Preface


.cols[
.fifty[
- Easy installation. 

- Lots of documentation.

- Easy to contribute.

] 

.fifty[
``` Python
pip install sktda
```

``` Python
www.scikit-tda.org
```

``` Python
www.github.com/scikit-tda
```
]
]









---

class: center, middle

# Preface

.center[
| .smallfixed[![alpatania](images/contributors/alpatania.jpg)] | .smallfixed[![arfon](images/contributors/arfon.jpg)] | .smallfixed[![blasern](images/contributors/blasern.png)] | .smallfixed[![chparsons](images/contributors/chparsons.jpg)] | .smallfixed[![ctralie](images/contributors/ctralie.jpg)] | .smallfixed[![ubauer](images/contributors/ubauer.png)] |.smallfixed[![retdop](images/contributors/retdop.png)] |
|---|---|---|---|---|---|
| .smallfixed[![deargle](images/contributors/deargle.jpg)] | .smallfixed[![emerson-escolar](images/contributors/emerson-escolar.png)] | .smallfixed[![empet](images/contributors/empet.jpg)] | .smallfixed[![galtay](images/contributors/galtay.jpg)] | .smallfixed[![joperea](images/contributors/joperea.png)] | .smallfixed[![trainorpj](images/contributors/trainorpj.jpg)] | .smallfixed[![eduph](images/contributors/eduPH.jpg)] |
| .smallfixed[![karinsasaki](images/contributors/karinsasaki.png)] | .smallfixed[![leouieda](images/contributors/leouieda.jpg)] | .smallfixed[![michiexile](images/contributors/michiexile.jpg)] | .smallfixed[![MLWave](images/contributors/MLWave.png)] | .smallfixed[![moh3th1](images/contributors/moh3th1.png)] |.smallfixed[![tmelorc](images/contributors/tmelorc.png)] |.smallfixed[![cmorph1](images/contributors/cmorph1.jpg)]  |
| .smallfixed[![mtsch](images/contributors/mtsch.jpg)] | .smallfixed[![outlace](images/contributors/outlace.jpg)] | .smallfixed[![rannbaron](images/contributors/rannbaron.png)] | .smallfixed[![Roj](images/contributors/Roj.jpg)] | .smallfixed[![smangham](images/contributors/smangham.jpg)] | ||
]
---

class: center, middle, qs

# Outline

<hr>

**Topological Data Analysis**

**Controlled Examples**

**Anomaly Detection**

---

class: center, middle

## Topology

.center[study of _shape_, **holes**, and **_connectivity_**.

.fit[![Donut to coffee cup transition by Henry Segerman](images/segerman.png)]
]

.footnote[Image credit Henry Segerman]

---

class: center, middle

## Topological Data Analysis

<img src="images/generated/circles.png" width="100%">
<br>
Adapt topology to point cloud data.

---

class: center, middle

## Clustering is TDA!

.cols[
.fifty[
.fit[![Unlabeled clusters](images/generated/clusters_no_color.png)]
]

.fifty[
.fit[![Color coded clusters](images/generated/clusters_color.png)]
]
]

.center[zero dimensional holes]

---

class: center, middle

## High dimensional holes

.cols[
.thirty[
.center[
.fit[![points sampled on a loop](images/generated/loop.png)]

1d holes = loops
]]

.thirty[
.center[
.fit[![points sampled on a sphere](images/generated/sphere.png)]

2d holes = voids
]]

.thirty[
.center[
.fit[![points sampled on a torus](images/generated/torus.png)]

lots of combinations
]
]
]


---


class: center, middle

## Data &rarr; Complex

<img src="images/ph/cech-canvas.png" width="100%">

---

class: center, middle

## One radius can be misleading

<img src="images/ph/cech-radius-canvas.png" width="100%">

---

class: center, middle

## Look at entire sequence of radii

<img src="images/ph/sizing_playground.gif" width="100%">

tinyurl.com/cech-playground

---

class: center

## Persistent homology

.center[
.fitheight[![points sampled on a loop](images/ph/persistenthomology.png)]
]

.footnote[Image credit Robert Ghrist]

---

class: center, middle, qs

# Outline

<hr>

~~**Topological Data Analysis**~~

**Controlled Examples**

**Anomaly Detection**


---

# Constrolled Examples

.cols[
.thirty[

]
.thirty[
``` Python
loop = tadasets.dsphere(d=1)
dgms = ripser(loop)
persim.plot_diagrams(dgms)
```
]
.thirty[

]
]

.center[
<img src="images/generated/loop.png" width="340px">
<img src="images/generated/loop_pd.png" width="340px">
]
---


# Controlled examples

.cols[
.thirty[

]
.thirty[
``` Python
sphere = tadasets.dsphere(d=2)
dgms = ripser(sphere)
persim.plot_diagrams(dgms)
```
]
.thirty[

]
]

.center[
<img src="images/generated/sphere.png" width="340px">
<img src="images/generated/sphere_pd.png" width="340px">
]

---



# Controlled examples

.cols[
.thirty[

]
.thirty[
``` Python
torus = tadasets.torus()
dgms = ripser(torus)
persim.plot_diagrams(dgms)
```
]
.thirty[

]
]


.center[
<img src="images/generated/torus.png" width="340px">
<img src="images/generated/torus_pd.png" width="340px">
]


---


class: center

## Comparison

.cols[
.thirty[
.center[.fit[![points sampled on a loop](images/generated/loop.png)]<br>.fit[![points sampled on a loop](images/generated/loop_pd.png)]]
]
.thirty[
.center[.fit[![points sampled on a sphere](images/generated/sphere.png)]<br>.fit[![points sampled on a sphere](images/generated/sphere_pd.png)]]
]
.thirty[
.center[.fit[![points sampled on a torus](images/generated/torus.png)]<br>.fit[![points sampled on a torus](images/generated/torus_pd.png)]]
]
]



---

class: center

# Comparison

- Show distances between multiple diagrams
- Show distances with varying levels of noise.

---

class: center, middle, qs

# Outline

<hr>

~~**Topological Data Analysis**~~

~~**Controlled Examples**~~

**Anomaly Detection**


<!-- ---

class: center, middle, qs

### Case study

<hr>

## Anomaly detection

Sliding window embedding

Persistent homology of embedding

Comparison of Persistence diagrams -->

---

class: center, middle

## Time series data

<img src="images/case_study_ts/full_series.png" width="100%"/>

<small> Average duration of web transactions aggregated over ~5 seconds.</small>

Can we tell when this periodic signal _falls apart_?

---

class: center, middle

## Preprocessing

<img src="images/case_study_ts/sliding_peaks.png" width="40%"/><br>
Autocorrelation curve

<img src="images/case_study_ts/sliding_buckets.png" width="90%"/><br>
Periods found from peak 

<!-- ---

class: center, middle

# Sliding window embedding

Window size of 3 &rarr; 3 dimensional space.

Each window becomes 3-D vector.

<img src="images/case_study_ts/embedding_parea.png" width="100%"/>

.footnote[Image credit Jose Perea.] -->

---

class: center, middle

# Sliding window embedding

<img src="images/sliding_window/out.gif" width="100%"/>

.footnote[Gif credit Chris Tralie]

---

class: center, middle

``` Python
diagrams = Rips().fit_transform(embedding)
persim.plot_diagrams(diagrams)
```

<img src="images/case_study_ts/sliding5.gif" width="70%"/>

---

class: center, middle

## Wasserstein distances

``` Python
d = persim.wasserstein(diagram3, diagram5)
```

<img src="images/case_study_ts/wasserstein_comparison.png" width="60%"/><br>
<img src="images/case_study_ts/frames/frame3_signal.png" width="40%"/><br>
<img src="images/case_study_ts/frames/frame5_signal.png" width="40%"/>
<img src="images/case_study_ts/frames/frame8_signal.png" width="40%"/>




<!-- ---

class: center, middle, qs

### Case study

<hr>

## Classification

Level set persistence

Persistence images

Classification algorithms -->



---

# Next time

- Persistence images
- TDA of machine learning
- Mapper and Sheaves

---

# Sprint

- Help with conda-forge packaging
- Help with automated builds



---

# Thank you

- Chris Tralie
- Leland McInnes

---

name: questions
class: center, middle, qs

Thank you to &#9734; Chris Tralie &#9734;

<hr>

.cols[
.thirty[
<br>

### Learn more &#10132;

]


.fifty[
<i class="fab fa-slack"></i><br>
tinyurl.com/scikit-tda-slack

<i class="fas fa-globe"></i> <br>
www.scikit-tda.org
]

]

<hr>

<br>

# Questions?

---

class: outline

# References

Embedding technique:

- (Quasi)Periodicity Quantification in Video Data, Using Topology, Christopher J. Tralie, Jose A. Perea, https://arxiv.org/abs/1704.08382

Beautiful diagram of the persistence barcode

- R. Ghrist, “Barcodes: The persistent topology of data,” Bulletin-American Mathematical Society 45, 1-15 (2008). [PDF in AMS](http://www.ams.org/journals/bull/2008-45-01/S0273-0979-07-01191-3/S0273-0979-07-01191-3.pdf)

Notebooks to reproduce case study

- [www.github.com/sauln/scipy-2019](www.github.com/sauln/scipy-2019)