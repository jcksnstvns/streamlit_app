# 2023-24 Charlotte MBB: Offensive Analysis

### Link
https://appapp-gsrb5gfim6fy7pkrcvglxq.streamlit.app/

### Introduction
This app provides an overview of Charlotte MBB's offensive performance as a team during the 
2023-24 season. Using data that I collected during my time as their analyst, I attempt to 
walk the audience through each variable and its effects on offensive efficiency (points per 
possession).

### Data / Operation Abstraction Design
I've worked as an analytics intern for our men's basketball team for three years now. This
year, one of my usual tasks was to live-track all of our games (home & away) and report the
numbers to our coaching staff during halftime and/or media timeouts. The data was presented to
our staff in an easy-to-digest dashboard format, but I'm using the raw data I collected from
all games this season.

I prepared my data by adding bins for some of the variables. As explained within the app, my data
is distributed in such a way that binning some of these measurements into numeric ranges was
appropriate. I also find that binning variables helps tell my story, especially when said
variables don't have specific values that hold significant meaning on their own; in other words, 
my data is not drastically changed if I change the halfcourt passes on a given possession from 6
to 5.

### Future Work
There are several steps I can take to optimize my app:
1) Incorporate predictive modeling from my work in season; while the story I'm telling is not
changed by with this addition, including my linear regression results can help further validate
the findings & assumptions made in the current app
2) Diversify visualization types... my app is made up of strictly bar plots as of now, but this
can change as a product of more brainstorming; perhaps using other graphs/plots will enable me
to tell this story more effectively
3) Explain basketball terminology within app... while I try to break down the current concepts
in simple terms, I could add more definitions/explanations to connect with a wider audience
4) Make it prettier... other than the stock blue/orange colors within the seaborn bar plots,
there is no color or visual personality to help engage the audience
5) Incorporate interactivity with visualizations... allow user to add filters and adjust sliders
for a more personalized experienced while still telling the story effectively
