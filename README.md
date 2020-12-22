## Recommending Descent: The Politics of YouTube Recommendations

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<a href="thesis.pdf" download>Thesis Paper</a>

### Abstract

This paper attempts to determine the underlying causes of recommendation discrepancies for political content on YouTube. Much of the work on YouTube’s watch-next algorithm claims that the platform favors right-leaning political recommendations and consistently leads users down
"radicalization pipelines" of extreme content. To measure the validity of these claims, I used three autonomous agents, or bots, to collect and classify the political content of 3750 YouTube videos. Using a random-walk algorithm, these agents traversed YouTube’s video recommendation graph guided by conservative, liberal, and positional biases, respectively. This research finds that left-leaning and right-leaning recommendations occur almost equivalently for users who select for these biases. This paper also finds substantial qualitative differences in structure and content associated with left and right leaning video recommendations. These results suggest that radicalization pipelines are not unique to right-leaning content and that access to these pipelines are largely a user-driven phenomenon.

### Methods

The goal of this paper is to capture the effect of user behavior on the output of YouTube’s recommendation algorithms using autonomous agents as proxies for actual users. These bots were designed to mock the content consumption and browsing behaviors of politically biased users. One bot represents a right wing partisan. This bot search’s for videos that have the highest level of right wing bias. Another bot represents a left wing partisan. This bot search’s for videos that have the highest level of left wing bias. Another bot will represent a content consumer with no political bias.

Each of the three bots in this paper use a similar random walk algorithm. The algorithm is described below:

<pre>
1. <b>Search</b>: Enter search query for list of starting videos
2. <b>Categorize</b>: Catagorize each video based on its political content
3. <b>Pick</b>: Pick the video with greatest level of favorable political bias (for the Neutral Bot pick the first video)
4. <b>Request</b>: Request 10 recommendations from this pick
5. <b>Repeat</b>: Catagorize, pick, and request 4 more times
</pre>

As Kanye West said:

> We're living the future so
> the present is our past.

### Findings

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Discussion

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Read me coming soon...

[Link](https://colab.research.google.com/gist/daniel-covelli/d1201ff9e42e4ab39ef184b3cc10f091/demo.ipynb#offline=true&sandboxMode=false)
