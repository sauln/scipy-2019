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
<img src="images/case_study_ts/sliding3.gif" width="550px"/>

---

class: outline

# Scikit-TDA

## What is it?

## Highly open source

## Highly collaborative

## Highly documented

## Used!

---

## What is it?

<br><br>

.center[
| Ripser.py | Kepler Mapper | Persim | Cechmate | TaDAsets |
|---|---|---|---|---|
| .smallimg[![Ripser logo](images/logo/ripser.png)] | .smallimg[![Kepler Mapper logo](images/logo/kepler-mapper.png)] | .smallimg[![Persim logo](images/logo/persim.png)] | .smallimg[![Cechmate logo](images/logo/cechmate.png)] | .smallimg[![tadasets logo](images/logo/tadasets.png)] |
]

---

## Highly open source

.fit[![Screenshot of scikit-tda github](images/scikit/scikit-tda-github.png)]

---

## Highly documented

.fit[![Screenshot of scikit-tda website](images/scikit/scikit-tda-website.png)]

---

## Highly collaborative

.center[
| .smallfixed[![alpatania](images/contributors/alpatania.jpg)] | .smallfixed[![arfon](images/contributors/arfon.jpg)] | .smallfixed[![blasern](images/contributors/blasern.png)] | .smallfixed[![chparsons](images/contributors/chparsons.jpg)] | .smallfixed[![ctralie](images/contributors/ctralie.jpg)] | .smallfixed[![ubauer](images/contributors/ubauer.png)] |.smallfixed[![retdop](images/contributors/retdop.png)] |
|---|---|---|---|---|---|
| .smallfixed[![deargle](images/contributors/deargle.jpg)] | .smallfixed[![emerson-escolar](images/contributors/emerson-escolar.png)] | .smallfixed[![empet](images/contributors/empet.jpg)] | .smallfixed[![galtay](images/contributors/galtay.jpg)] | .smallfixed[![joperea](images/contributors/joperea.png)] | .smallfixed[![trainorpj](images/contributors/trainorpj.jpg)] | .smallfixed[![eduph](images/contributors/eduPH.jpg)] |
| .smallfixed[![karinsasaki](images/contributors/karinsasaki.png)] | .smallfixed[![leouieda](images/contributors/leouieda.jpg)] | .smallfixed[![michiexile](images/contributors/michiexile.jpg)] | .smallfixed[![MLWave](images/contributors/MLWave.png)] | .smallfixed[![moh3th1](images/contributors/moh3th1.png)] |.smallfixed[![tmelorc](images/contributors/tmelorc.png)] |.smallfixed[![cmorph1](images/contributors/cmorph1.jpg)] |
| .smallfixed[![mtsch](images/contributors/mtsch.jpg)] | .smallfixed[![outlace](images/contributors/outlace.jpg)] | .smallfixed[![rannbaron](images/contributors/rannbaron.png)] | .smallfixed[![Roj](images/contributors/Roj.jpg)] | .smallfixed[![smangham](images/contributors/smangham.jpg)] | ||
]

---

## Persistent Homology with Ripser.py

Very fast for point clouds

```Python
from ripser import Rips

rip = Rips()
diagrams = rip.fit_transform(data)
rip.plot(diagrams)
```

---

## Flexible diagrams with Cechmate

```Python
import cechmate

cech = cechmate.Cech()
rips = cechmate.Rips()
alpha = cechmate.Alpha()
jaccard = cechmate.Cover()
extended = cechmate.Extended.from_kmapper(mapper)
```

Pretty much the same API for all of them:

```Python
jaccard.build(data)
diagrams = jaccard.diagrams()
jaccard.plot(diagrams)
```

---

background-image: url(images/mapper/breast-cancer.png)

## Mapper with Kepler Mapper

```Python
from kmapper import KeplerMapper
km = KeplerMapper()
lens = km.fit_transform(data, projection=[0])
graph = km.map(lens, data)
km.visualize()
```

---

## datasets with TaDAsets

```Python
import tadasets

loop = tadasets.dsphere(d=1, n=2000, noise=0.1)
sphere = tadasets.dsphere(d=2, n=1000)
torus = tadasets.torus(n=1000, ambient=100)
swiss_roll = tadasets.swiss_roll(n=1000, r=25)
```

.cols[
.thirty[
.center[.fit[![points sampled on a loop](images/generated/loop.png)]]
]
.thirty[
.center[.fit[![points sampled on a sphere](images/generated/sphere.png)]]
]
.thirty[
.center[.fit[![points sampled on a torus](images/generated/torus.png)]]
]
]

---

## distances with Persim

```Python
import persim

dx = persim.heat(diagramA, diagramB)
dx = persim.bottleneck(diagramA, diagramB)
dx = persim.sliced_wasserstein(diagramA, diagramB)
ims = persim.PersImage().fit_transform(diagrams)
```

.center[
.fullsize[![Persistence images of fake datasets](images/persim_classification.png)]
]

---

name: questions
class: center, middle, qs

# Questions?

## Thank you!

-- Christopher Tralie

<br>

.center[
<i class="fab fa-twitter"></i> <br>
@scikit_tda <br>
@NathanielSaul

<i class="fas fa-globe"></i> <br>
scikit-tda.org
]

<br>
