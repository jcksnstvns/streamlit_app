import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

# Load data
df = pd.read_csv("clt_offense.csv")

# HOME PAGE
def home_page():
    st.write("# 2023-24 Charlotte MBB")
    st.write("## Offensive Analysis")

    st.write("### Offensive Possessions Dataset")
    st.write("#### Tibble")
    st.write(df.head())
    st.write("#### Summary Stats")
    st.write(df.describe())

    st.write("While working for 49ers Men's Basketball this season, my team and I were asked to track the variables in the dataset above for all games and practices. The coaching staff requested this information to assess the team's offensive efficiency and its relation to some of their focal points: **passes**, **paint touches**, and **ball reversals**.")
    st.write("To better understand each of these measurements, their distribution within our dataset, and how they impact offensive efficiency, please navigate to the menu in the top-left corner of your screen and select a category!")
    pass

# POSSESSION TYPE
def display_possession_type():
    st.write("# Possession Type")

    # Total Poss. by Type
    st.write("### Frequency")
    st.write("Of 362 NCAA Division-I Men's Basketball teams, Charlotte ranked 356th in tempo this season. This checks out when breaking down the 49ers offense by possession; the low number of transition opportunities in relation to halfcourt ones suggests that the team was more comfortable playing at a slower pace.")
    sns.countplot(x = 'poss_type', data = df)
    plt.xlabel('Possession Type')
    plt.ylabel('Count')
    st.pyplot()

    # Points Per Possession by Type
    st.write("### Points Per Possession (PPP)")
    st.write("The plot below shows how efficient our offense was in both halfcourt and transition opportunities.")
    st.write("Although our play style was not conducive to getting out in transition, we managed to score an impressive 1.26 points per possession on these opportunities. This high figure can be attributed to two things:\n1) relatively small sample size\n2) Hesitance to attack in transition... unless we were in a prime position to score on the fastbreak, we would tend to pull back and run our halfcourt offense")
    st.write("The 49ers halfcourt offense excelled on the whole as well, scoring about 1.06 PPP. For reference, our offense ranked 131st nationally (of 362) in adjusted efficiency (per Kenpom).")

    # Calculate points per possession for each type
    hc_ppp = df[df['poss_type'] == 'halfcourt']['hc_points'].sum() / df[df['poss_type'] == 'halfcourt'].shape[0]
    t_ppp = df[df['poss_type'] == 'transition']['t_points'].sum() / df[df['poss_type'] == 'transition'].shape[0]
    hybrid_ppp = (df[df['poss_type'] == 'hybrid']['hc_points'].sum() + df[df['poss_type'] == 'hybrid']['t_points'].sum()) / df[df['poss_type'] == 'hybrid'].shape[0]

    # Create bar plot
    poss_types = ['Halfcourt', 'Transition', 'Hybrid']
    ppp = [hc_ppp, t_ppp, hybrid_ppp]
    plt.bar(poss_types, ppp)
    plt.xlabel('Possession Type')
    plt.ylabel('Points Per Possession')
    st.pyplot()
    pass

# HALFCOURT - PASSING
def display_halfcourt_passing():
    st.write("# Halfcourt - Passing")

    # Calculate possession counts for each category of passes
    possession_count_passes_0to3 = df['Passes_0to3'].sum()
    possession_count_passes_4to6 = df['Passes_4to6'].sum()
    possession_count_passes_7plus = df['Passes_7plus'].sum()

    # Create a bar plot for possession counts by passes
    st.write("### Frequency")
    st.write("The decision to bin halfcourt passes into three groups is based on:\n1) The 'feel' of the respective possessions (i.e. length, play types), and\n2) The distibution of pass quantities within the dataset.")
    plt.bar(['0-3', '4-6', '7+'], [possession_count_passes_0to3, possession_count_passes_4to6, possession_count_passes_7plus])
    plt.xlabel('Number of Passes')
    plt.ylabel('Possession Count')
    st.pyplot()

    # Calculate average points per possession for each category of passes
    total_points_passes_0to3 = df[df['Passes_0to3'] == 1]['hc_points'].sum()
    possession_count_passes_0to3 = df['Passes_0to3'].sum()
    average_ppp_passes_0to3 = total_points_passes_0to3 / possession_count_passes_0to3 if possession_count_passes_0to3 != 0 else 0

    total_points_passes_4to6 = df[df['Passes_4to6'] == 1]['hc_points'].sum()
    possession_count_passes_4to6 = df['Passes_4to6'].sum()
    average_ppp_passes_4to6 = total_points_passes_4to6 / possession_count_passes_4to6 if possession_count_passes_4to6 != 0 else 0

    total_points_passes_7plus = df[df['Passes_7plus'] == 1]['hc_points'].sum()
    possession_count_passes_7plus = df['Passes_7plus'].sum()
    average_ppp_passes_7plus = total_points_passes_7plus / possession_count_passes_7plus if possession_count_passes_7plus != 0 else 0

    # Create a bar plot for points per possession by passes
    st.write("### PPP")
    st.write("Our coaching staff emphasizes the importance of sharing the ball. While there are many variables that determine whether a possession results in points, the plot below indicates that increased ball movement proved to be beneficial for our halfcourt offense this season.")
    plt.bar(['0-3', '4-6', '7+'], [average_ppp_passes_0to3, average_ppp_passes_4to6, average_ppp_passes_7plus])
    plt.xlabel('Number of Passes')
    plt.ylabel('Average Points Per Possession')
    st.pyplot()
    pass

# HALFCOURT - PAINT TOUCHES
def display_paint_touches():
    st.write("# Halfcourt - Paint Touches")

    possession_count_touch_0 = df['PtTouch_0'].sum()
    possession_count_touch_1 = df['PtTouch_1'].sum()
    possession_count_touch_2plus = df['PtTouch_2plus'].sum()

    # Create a bar plot for possession counts by paint touches
    st.write("### Frequency")
    st.write("The decision to bin paint touches into three categories is based on the distribution of paint touches in our dataset. While simply making variable binary (yes/no) would tell the story sufficiently, I think it's important to recognize the impact that getting multiple paint touches in a single possession has on a team's offensive efficiency. We can infer that if a defense allows multiple paint touches in a given possession, it has been significantly pressured and, thus, compromised.")
    plt.bar(['0', '1', '2+'], [possession_count_touch_0, possession_count_touch_1, possession_count_touch_2plus])
    plt.xlabel('Number of Paint Touches')
    plt.ylabel('Possession Count')
    st.pyplot()

    # Calculate average points per possession for each category of paint touches
    total_points_touch_0 = df[df['PtTouch_0'] == 1]['hc_points'].sum()
    possession_count_touch_0 = df['PtTouch_0'].sum()
    average_ppp_touch_0 = total_points_touch_0 / possession_count_touch_0 if possession_count_touch_0 != 0 else 0

    total_points_touch_1 = df[df['PtTouch_1'] == 1]['hc_points'].sum()
    possession_count_touch_1 = df['PtTouch_1'].sum()
    average_ppp_touch_1 = total_points_touch_1 / possession_count_touch_1 if possession_count_touch_1 != 0 else 0

    total_points_touch_2plus = df[df['PtTouch_2plus'] == 1]['hc_points'].sum()
    possession_count_touch_2plus = df['PtTouch_2plus'].sum()
    average_ppp_touch_2plus = total_points_touch_2plus / possession_count_touch_2plus if possession_count_touch_2plus != 0 else 0

    # Create a bar plot for points per possession by paint touches
    st.write("### PPP")
    st.write("Not to the surprise of our coaching staff, possessions in which we did not touch the paint rendered very poor results comparatively. When our halfcourt offense can successfully dissect the defense and penetrate the paint, good things tend to happen.")
    plt.bar(['0', '1', '2+'], [average_ppp_touch_0, average_ppp_touch_1, average_ppp_touch_2plus])
    plt.xlabel('Number of Paint Touches')
    plt.ylabel('Average Points Per Possession')
    st.pyplot()
    pass

# HALFCOURT - BALL REVERSALS
def display_ball_reversals():
    st.write("# Halfcourt - Ball Reversals")
    # Calculate possession counts for each category of ball reversals
    possession_count_no_reversal = df['hc_reversal'].value_counts().get(0, 0)
    possession_count_with_reversal = df['hc_reversal'].value_counts().get(1, 0)

    # Create a bar plot for possession counts by ball reversals
    st.write("### Frequency")
    st.write("The decision to make this variable binary is supported by the lack of possessions with multiple ball reversals. While this variable was initially numeric, the sample size of possessions with 2+ ball reversals was small and did not render signifcant findings.")
    plt.bar(['No', 'Yes'], [possession_count_no_reversal, possession_count_with_reversal])
    plt.xlabel('Ball Reversal?')
    plt.ylabel('Possession Count')
    st.pyplot()

    # Calculate average points per possession for each category of ball reversals
    total_points_no_reversal = df[df['hc_reversal'] == 0]['hc_points'].sum()
    possession_count_no_reversal = df['hc_reversal'].value_counts().get(0, 0)
    average_ppp_no_reversal = total_points_no_reversal / possession_count_no_reversal if possession_count_no_reversal != 0 else 0

    total_points_with_reversal = df[df['hc_reversal'] == 1]['hc_points'].sum()
    possession_count_with_reversal = df['hc_reversal'].value_counts().get(1, 0)
    average_ppp_with_reversal = total_points_with_reversal / possession_count_with_reversal if possession_count_with_reversal != 0 else 0

    # Create a bar plot for points per possession by ball reversals
    st.write("### PPP")
    st.write("When our players reverse the ball (or pass it quickly from one side of the three-point arc to the other), it forces the defense to make adjustments on the fly. Since the opposition is vulnerable when the ball moves in such fashion, it creates a better scoring opportunity for our offense. This claim is supported by the plot below.")
    plt.bar(['No', 'Yes'], [average_ppp_no_reversal, average_ppp_with_reversal])
    plt.xlabel('Ball Reversal?')
    plt.ylabel('Average Points Per Possession')
    st.pyplot()
    pass

# TRANSITION - PASSES
def display_transition_passing():
    st.write("# Transition - Passing")

    # Calculate possession counts for each category of transition passes
    possession_count_tpasses_0to1 = df['TPasses_0to1'].sum()
    possession_count_tpasses_2plus = df['TPasses_2plus'].sum()

    # Create a bar plot for possession counts by transition passes
    st.write("### Frequency")
    st.write("The decision to bin transition passes into two categories is supported by the distribution of 't_passes' values; since '1' was the pass quantity most represented by far (116 of 288 transition possessions), the chosen split is most appropriate.")
    plt.bar(['0-1', '2+'], [possession_count_tpasses_0to1, possession_count_tpasses_2plus])
    plt.xlabel('Number of Passes')
    plt.ylabel('Possession Count')
    st.pyplot()

    # Calculate average points per possession for each category of transition passes
    total_points_tpasses_0to1 = df[df['TPasses_0to1'] == 1]['t_points'].sum()
    possession_count_tpasses_0to1 = df['TPasses_0to1'].value_counts().get(0, 0)
    average_ppp_tpasses_0to1 = total_points_tpasses_0to1 / possession_count_tpasses_0to1 if possession_count_tpasses_0to1 != 0 else 0

    total_points_tpasses_2plus = df[df['TPasses_2plus'] == 1]['t_points'].sum()
    possession_count_tpasses_2plus = df['TPasses_2plus'].value_counts().get(1, 0)
    average_ppp_tpasses_2plus = total_points_tpasses_2plus / possession_count_tpasses_2plus if possession_count_tpasses_2plus != 0 else 0

    # Create a bar plot for points per possession by transition passes
    st.write("### PPP")
    st.write("Based on the bar plot below, we can conclude that 'more passing' doesn't always equate to 'better offense'. Especially in fast-paced situations, taking the first 'good' shot can lead to better scoring rates than patiently waiting for the 'best' shot.")
    plt.bar(['0-1', '2+'], [average_ppp_tpasses_0to1, average_ppp_tpasses_2plus])
    plt.xlabel('Number of Passes')
    plt.ylabel('Average Points Per Possession')
    st.pyplot()
    pass

def main():
    st.sidebar.title("Navigation")
    selected_section = st.sidebar.radio("Go to", ["Home", "Possession Type", "Halfcourt - Passing", "Halfcourt - Paint Touches", "Halfcourt - Ball Reversals", "Transition - Passing"])

    if selected_section == "Home":
        home_page()
    elif selected_section == "Possession Type":
        display_possession_type()
    elif selected_section == "Halfcourt - Passing":
        display_halfcourt_passing()
    elif selected_section == "Halfcourt - Paint Touches":
        display_paint_touches()
    elif selected_section == "Halfcourt - Ball Reversals":
        display_ball_reversals()
    elif selected_section == "Transition - Passing":
        display_transition_passing()

if __name__ == "__main__":
    main()