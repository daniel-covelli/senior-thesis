# Recommending Descent: YouTube and Political Polarization

Recommending Descent is my senior research thesis for UC Berkeley's Interdisiplanry Studies major. The project attempts to characterize the effect that political bias has on YouTube's video recommendation algorithm. This project uses three autonomous agents, or bots, to mock the behavior of a right-leaning, left-leaning, and apolitical YouTube user. The bots access videos through YouTube's [Data API](https://developers.google.com/youtube/v3). This repository contains all the code and data used for the project.

📑 [Thesis Paper](thesis.pdf) &nbsp; &nbsp;
✏️ [Works Cited](https://www.notion.so/b6f79f445d534b1fa2384c4d74b3d416?v=2fdc95e61e5646c6b9c231844f1fde45) &nbsp; &nbsp;
📊 [Recfluence](https://github.com/markledwich2/Recfluence)

## Abstract

This project attempts to determine the underlying causes of recommendation discrepancies for political content on YouTube. Much of the work on YouTube’s watch-next algorithm claims that the platform favors right-leaning political recommendations and consistently leads users down
"radicalization pipelines" of extreme content. To measure the validity of these claims, I used three autonomous agents, or bots, to collect and classify the political content of 3750 YouTube videos. Using a random-walk algorithm, these agents traversed YouTube’s video recommendation graph guided by conservative, liberal, and positional biases, respectively. This research finds that left-leaning and right-leaning recommendations occur almost equivalently for users who select for these biases. This paper also finds substantial qualitative differences in structure and content associated with left and right leaning video recommendations. These results suggest that radicalization pipelines are not unique to right-leaning content and that access to these pipelines are largely a user-driven phenomenon.

## Methods

The goal of this research is to capture the effect of user behavior on the output of YouTube’s recommendation algorithms using autonomous agents as proxies for actual users. These bots were designed to mock the content consumption and browsing behaviors of politically biased users. One bot represents a right wing partisan. This bot search’s for videos that have the highest level of right wing bias. Another bot represents a left wing partisan. This bot search’s for videos that have the highest level of left wing bias. Another bot will represent a content consumer with no political bias.

Each of the three bots in this paper use a similar random walk algorithm. The algorithm is described below:

<pre>
1. <b>Search</b>: Enter search query for a list of starting videos
2. <b>Categorize</b>: Catagorize each video based on its political content
3. <b>Pick</b>: Pick the video with greatest level of favorable political bias
4. <b>Collect</b>: Collect meta-data for videos
5. <b>Request</b>: Request 10 recommendations from the selected video
6. <b>Repeat</b>: Catagorize, pick, collect, and request 4 more times
</pre>

For more information on the methods used in this repository, reference the methods section of the [thesis paper](thesis.pdf). Categorizations for this project were provided by Mark Ledwich and Anna Zaitsev's, [Recfluence Channel Classification Data Set](https://github.com/markledwich2/Recfluence#data).

### Findings

#### Left/Right Network Topologies

---

<img src="images/fig_7_0_1.jpeg" alt="topologies" width="600"/>

This analysis finds that the majority of recommendations to the Right Bot were to Fox News and Fox Business. For the Left Bot, the majority of recommendations were to a more diverse pool of left-leaning media outlets like MSNBC, VOX, and late night shows.

For more, see [1](images/fig_7_1_0.jpeg), [2](images/fig_7_2_1.jpeg), and [3](images/fig_7_3_1.jpeg).

#### Divergent Recommendation Trends

---

<img src="images/fig_1_2.jpeg" alt="trends" width="600"/>

#### Recommendation Catagory Proportions

---

<img src="images/fig_3_2.png" alt="proportions"/>

### Discussion

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Read me coming soon...

[Link](https://colab.research.google.com/gist/daniel-covelli/d1201ff9e42e4ab39ef184b3cc10f091/demo.ipynb#offline=true&sandboxMode=false)
