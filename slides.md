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

**Case Study**

**Timeseries Anomaly Detection**

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

<!-- ---

class: center, middle, qs

### Case Study

<hr/>
<br>
<br>

# TDA of timeseries

**Spike detection**

**Change detection** -->

<!-- ---

class: center, middle

Collect data with chart builder

<img src="images/case_study_ts/chart-builder-spike.png" width="100%"/> -->

<!-- ---

class: center, middle

Can we use TDA to detect this spike?

<img src="images/case_study_ts/just_series.png" width="100%"/>

<img src="images/case_study_ts/just_series_spike.png" width="100%"/> -->

<!-- ---

class: center, middle, qs

## Processing steps

<hr>
<br>

**Compute length of a period using autocorrelation**

**Construct sliding window embedding for normal wave and spike**

**Compare Persistence Diagrams of both embedding** -->

<!-- ---

class: center, middle

Compute period from autocorrelation curve

<img src="images/case_study_ts/autocorrelation_spike.png" width="60%"/>

<img src="images/case_study_ts/window-overlay.png" width="100%"/> -->

<!-- ---

class: center, middle

Pretty okay automatic identification ¯\\\_(ツ)\_/¯ -->

<!-- ---

class: center, middle

<img src="images/case_study_ts/just_series.png" width="100%"/>

<img src="images/case_study_ts/series_ph.png" width="100%"/>

.footnote[Projection with PCA] -->

<!-- ---

class: center, middle

<img src="images/case_study_ts/just_series_spike.png" width="100%"/>

<img src="images/case_study_ts/spike_ph.png" width="100%"/>

.footnote[Projection with PCA] -->

<!-- ---

class: center

<img src="images/case_study_ts/series_ph.png" width="70%"/>

<img src="images/case_study_ts/spike_ph.png" width="70%"/> -->

<!-- ---

class: center

# Distances between diagrams

<img src="images/case_study_ts/spike_was.png" width="45%"/>
<img src="images/case_study_ts/spike_bottleneck.png" width="45%"/> -->

---

class: center, middle, qs

### Case study

<hr>

## Automatic anomaly detection

<img src="images/case_study_ts/chart-builder-series.png" width="100%"/>

Can we tell when this periodic signal _falls apart_?

---

class: center, middle

## Compute period size

<!-- <img src="images/case_study_ts/full_series.png" width="100%"/> -->

<img src="images/case_study_ts/sliding_peaks.png" width="50%"/>

<img src="images/case_study_ts/sliding_buckets.png" width="100%"/>

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

---

class: center, middle

<!-- <img src="images/case_study_ts/full_series.png" width="700px" height="100px"/> -->
<img src="images/case_study_ts/sliding5.gif" width="95%"/>

<!-- ---

class: center, middle, qs

## Automatic detection

<hr>
<br>

**Measures on diagrams**

**Distances on diagrams** -->

---

class: center, middle

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
