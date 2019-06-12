class: center, middle, borderless

<div class="banner">
<img src="images/banner.jpg" alt="abstract rips complex">
</div>

# TDA of timeseries

### A introduction and case study of Topological Data Analysis.

<p class="smallish">
<b>Nathaniel Rivera Saul</b><br>
.smallish[New Relic Unconf<br>June 13th 2019]
</p>

---

class: center, middle, qs

<!-- Topological Data Analysis is a new field of applicable mathematics gaining attention in the world of data science. This talk will introduce everything TDA working from holes and nerves to persistence. We'll then explore an application of TDA to time series analysis using new open source tools.  -->

# Topological Data Analysis

**What is topology?**

**Persistent Homology**

~~**Mapper**~~

<br>
# Case Study

**Anomaly Detection**

---

# What is Topology?

.center[
*Something about* **donuts** *and* **coffee cups**?
]

![Chief Wiggum from the Simpsons](images/Chief_Wiggum.png)

---

## What is Topology?

.center[study of shape, holes, and connectivity.

.fit[![Donut to coffee cup transition by Henry Segerman](images/segerman.png)]
]

.footnote[Image credit Henry Segerman]

---

## What is Topological Data Analysis?

.center[
apply these theories to high dimensional point cloud data

.fit[
![Image of annulus and data sampled on annulus.](images/generated/circles.png)]
]

---

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

class: center, middle, qs

# Persistent Homology

<hr>

<br>

**Simplicial Complexes**

**Homology**

**Persistence & Filtrations**

**Persistent Homology & Diagrams**

---

class: center

## Simplicial Complexes

.center[
.fitheight[![points sampled on a loop](images/ph/simpcom.png)]
]

.footnote[Image credit wikipedia?]

---

class: center

## Compute homology

Count the k-**cycles** that are not **boundaries** of k+1-cycles

.fitheight[![points sampled on a loop](images/ph/homology-of-complex.jpg)]

---

class: center

## Data &rarr; Complex

---

class: center

## Data &rarr; Complex

<img src="images/ph/cech-canvas.png" width="100%">

---

class: center, middle

# One radius can be misleading

<img src="images/ph/cech-radius-canvas.png" width="100%">

---

class: center, middle

# tinyurl.com/cech-playground

<img src="images/ph/cech-playground.png" width="100%">

---

## Persistent homology

.center[
.fitheight[![points sampled on a loop](images/ph/persistenthomology.png)]
]

.footnote[Image credit Robert Ghrist]

---

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

### Case Study

<hr/>
<br>
<br>

# TDA of timeseries

**Spike detection**

**Change detection**

---

class: center, middle

Collect data with chart builder

<img src="images/case_study_ts/chart-builder-spike.png" width="100%"/>

---

class: center, middle

Can we use TDA to detect this spike?

<img src="images/case_study_ts/just_series.png" width="100%"/>

<img src="images/case_study_ts/just_series_spike.png" width="100%"/>

---

class: center, middle, qs

## Processing steps

<hr>
<br>

**Compute length of a period using autocorrelation**

**Construct sliding window embedding for normal wave and spike**

**Compare Persistence Diagrams of both embedding**

---

class: center, middle

Compute period from autocorrelation curve

<img src="images/case_study_ts/autocorrelation_spike.png" width="100%"/>

---

class: center, middle

Pretty okay automatic identification ¯\\\_(ツ)\_/¯

<img src="images/case_study_ts/window-overlay.png" width="100%"/>

---

class: center, middle

Window size of 30 &rarr; 30 dimensional space.

Slide window length 30 over series.

Each window becomes 30-D vector.

.footnote[please let me know if you have a nice way of visualizing this.]

---

class: center, middle

<img src="images/case_study_ts/just_series.png" width="100%"/>

<img src="images/case_study_ts/series_ph.png" width="100%"/>

---

class: center, middle

<img src="images/case_study_ts/just_series_spike.png" width="100%"/>

<img src="images/case_study_ts/spike_ph.png" width="100%"/>

---

class: center

# Woah those look pretty different to me.

<img src="images/case_study_ts/series_ph.png" width="60%"/>

<img src="images/case_study_ts/spike_ph.png" width="60%"/>

---

class: center

But looks aren't everything.

Can't we automatically tell if they are different?

---

class: center, middle, qs

### Case study

<hr>

## Change detection

<img src="images/case_study_ts/chart-builder-series.png" width="100%"/>

Can we tell this periodic signal _fell apart_?

---

class: center, middle

<img src="images/case_study_ts/full_series.png" width="100%"/>

Detect length period

Embed 10 periods

Persistence Diagrams for each group

---

class: center, middle

<!-- <img src="images/case_study_ts/full_series.png" width="700px" height="100px"/> -->
<img src="images/case_study_ts/sliding3.gif" width="100%"/>

---

class: center, middle, qs

## Automatic detection

<hr>
<br>

**Divergence of distances?**

**Changes in persistent entropy?**

**IDK**

---

class: center, middle

## Max bar

<img src="images/case_study_ts/max_bar_canvas.png" width="100%"/>

---

class: center, middle

## Persistent entropy

<img src="images/case_study_ts/persistent_entropy.png" width="60%"/>

(provably better stability properties, but IDK how it's calculated)

---

class: center, middle

## Wasserstein distances

<img src="images/case_study_ts/wasserstein_comparison.png" width="100%"/>

---

class: center, middle

## Wasserstein distance curve

Comparing first diagram to subsequence diagrams using Wasserstein distance

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

class: center, middle

## Bottleneck curve

Comparing first diagram to subsequent

<img src="images/case_study_ts/bottleneck_curve.png" width="60%"/>

---

class: center, middle

## Bottleneck distance matrix

<img src="images/case_study_ts/bottleneck_dm.png" width="60%"/>

---

name: questions
class: center, middle, qs

# Questions?

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
 Thank you to &#9734; Christopher Tralie &#9734;

---

class: outline

# References

All code and data to replicate what is shown here:

- [source.github.com/insights/data-driven-exploration/TDAtimeseries](https://source.datanerd.us/insights/data-driven-exploration/blob/master/TDAtimeseries/TDA%20of%20Timeseries.ipynb)

Embedding technique:

- (Quasi)Periodicity Quantification in Video Data, Using Topology, Christopher J. Tralie, Jose A. Perea, https://arxiv.org/abs/1704.08382

All TDA libraries used are part of Scikit-TDA:

- [www.scikit-tda.org](https://www.scikit-tda.org)
