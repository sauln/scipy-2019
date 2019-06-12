class: center, middle, borderless

<div class="banner">
<img src="images/banner.jpg" alt="abstract rips complex">
</div>

# TDA of timeseries

An introduction and case study.

<p class="smallish">
<b>Nathaniel Rivera Saul</b><br>
.smallish[New Relic ML Unconf<br>June 13th 2019]
</p>

---

class: center, middle, qs

<!-- Topological Data Analysis is a new field of applicable mathematics gaining attention in the world of data science. This talk will introduce everything TDA working from holes and nerves to persistence. We'll then explore an application of TDA to time series analysis using new open source tools.  -->

# Outline

<hr>

**Topology**

**Persistent Homology**

**Anomaly Detection**

---

class: center, middle

## Topology

_Something about_ **donuts** _and_ **coffee cups**?

![Chief Wiggum from the Simpsons](images/Chief_Wiggum.png)

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

class: center

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

class: center

## Data &rarr; Complex

---

class: center

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

class: center

## Persistence diagrams

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

class: center, middle, qs

### Case study

<hr>

## Automatic anomaly detection

Sliding window embedding

Persistent homology of embedding

Comparison of Persistence diagrams

---

class: center, middle

Real New Relic data

<img src="images/case_study_ts/chart-builder-series.png" width="100%"/>

Can we tell when this periodic signal _falls apart_?

---

class: center, middle

## Compute period size

<img src="images/case_study_ts/sliding_peaks.png" width="50%"/>

<img src="images/case_study_ts/sliding_buckets.png" width="90%"/>

Autocorrelation curve

---

class: center, middle

# Sliding window embedding

Window size of 3 &rarr; 3 dimensional space.

Each window becomes 3-D vector.

<img src="images/case_study_ts/embedding_parea.png" width="100%"/>

.footnote[Image credit Jose Perea.]

---

class: center, middle

# Sliding window embedding

<img src="images/sliding_window/out.gif" width="100%"/>

.footnote[Gif credit Chris Tralie]

---

class: center, middle

<img src="images/case_study_ts/sliding5.gif" width="95%"/>

---

class: center, middle

# Comparison

## Max bar

<img src="images/case_study_ts/max_bar_canvas.png" width="100%"/>

---

class: center, middle

## Wasserstein distances

<img src="images/case_study_ts/wasserstein_comparison.png" width="70%"/><br>
<img src="images/case_study_ts/frames/frame3_signal.png" width="45%"/><br>
<img src="images/case_study_ts/frames/frame5_signal.png" width="45%"/>
<img src="images/case_study_ts/frames/frame8_signal.png" width="45%"/>

---

class: center, middle

## Wasserstein distance curve

Comparing 1st diagram to subsequent diagrams using Wasserstein distance

<img src="images/case_study_ts/wasser_curve.png" width="60%"/>

---

class: center, middle

## Wasserstien distance matrix

<img src="images/case_study_ts/wasser_dm.png" width="60%"/>

---

class: center, middle

## Bottleneck distances

<img src="images/case_study_ts/bottleneck_comparison.png" width="100%"/>

---

name: questions
class: center, middle, qs

Thank you to &#9734; Chris Tralie &#9734;

<hr>

.cols[
.thirty[
<br>

### Learn more

]
.thirty[

<br>

&#10132;
]

.thirty[
<i class="fab fa-slack"></i><br>
@nriverasaul

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

All code and data to replicate what is shown here:

- [source.github.com/insights/data-driven-exploration/TDAtimeseries](https://source.datanerd.us/insights/data-driven-exploration/blob/master/TDAtimeseries/TDA%20of%20Timeseries.ipynb)

Embedding technique:

- (Quasi)Periodicity Quantification in Video Data, Using Topology, Christopher J. Tralie, Jose A. Perea, https://arxiv.org/abs/1704.08382

All TDA libraries used are part of Scikit-TDA:

- [www.scikit-tda.org](https://www.scikit-tda.org)
