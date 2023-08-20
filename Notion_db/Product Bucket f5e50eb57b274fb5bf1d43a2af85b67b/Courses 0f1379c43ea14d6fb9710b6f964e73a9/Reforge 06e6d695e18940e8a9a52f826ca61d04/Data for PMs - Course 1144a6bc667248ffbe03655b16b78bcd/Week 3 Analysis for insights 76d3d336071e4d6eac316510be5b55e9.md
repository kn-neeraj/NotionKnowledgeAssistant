# Week 3 : Analysis for insights

### Good Insights

- Actionable
    - Who → Free users,  Riders
    - What → who received at-least 2- responses on their surveys in the first month, whose average wait time is less than 5 minutes
    - Why → 6x more likely to covert to paid users after the first month, 40% more likely to continue using the app over a 6 month period
    
    <aside>
    💡 2 key analytical tools → Segmentation analysis & Correlation b/w 2 variables, Other → Time series, historgram, funnel analysis
    
    </aside>
    
    ### Segmentation
    
    - Dividing and grouping users based on a chosen set of parameters defined by 4 variables :
        - Population
        - Starting point
        - Behaviour
        - Time period
    
    Segmentation analysis who, what & why of the analysis
    
    Which users and what behaviours tend to convert free to paid
    
    Example 
    
    - SurveyMonkey
    - Free users who sent more surveys were more likely to convert too paid because surveys are a core unit of value in the product
    - But this did not help. Then they looked the # of responses and there was a clear difference b/w people who got more responses
    
    ### Correlation
    
    Correlate user action or behaviour to product/business metric
    
    **Mistakes**
    
    - Back it up with Qualitative Conjectures
    - Mistake correlation to causation but there is a confounding variable (external factor)
    - Pressure test insights
    
    ---
    
    ---
    
    ### Segmentation Analysis
    
    Dividing and grouping users based on a chosen set of parameters.
    
    **Variables**
    
    - Populations → Which user segments are included in the analysis
    - Starting point → entry criteria we use to include users in the analysis (user action & a time)
    - Behaviour → User behaviour we are measuring
    - Time period → Fixed period over which we measure the behaviour
    
    <aside>
    💡 Understand how our users are different.  Aggregate numbers obscure idiosyncrasies of user behaviour!!
    
    </aside>
    
    <aside>
    💡 We want segmentation such that → Lines are distinct from one another and is predictable
    
    </aside>
    
    ### Basic Segmentation
    
    - Demographic - Gender, language, race, and geography (if it meaningfully impacts user’s product behaviour) (Limited use esp. B2B.)
    - Device - Different across platforms they use
    - Acquisition Source -
    - Persona → demographic characteristics, who is my target market and do they behave differently, RATHER do behavorial segmentation
    - Product categories - Payment or engagement tiers → Be careful!! paid users will have higher retention
    
    ### Advanced Segmentation
    
    Focus on population’s own behaviour → what they do in the product
    
    **Feature Segmentation**
    
    - Usage of certain feature or group of features in the product
    
    <aside>
    💡 Features provide value as a bundle!! Group features as a use case.
    
    </aside>
    
    **Did X in Y time**
    
    - Example - 7 friends in 10 days.
    
    ### Cohort Analysis
    
    Cohort → Group of users who share a common characteristic over time
    
    Example - Users who signed up in a month, Users 2 months before they convert to paid users, etc
    
    Cohort view & line view
    
    Common Mistakes
    
    - Weighted average instead of average
    - 
    
    ---
    
    ---
    
    ### Relationships between Variables Deep Dive
    
    <aside>
    💡 Product Management is about making investments to create most user and business value.
    
    </aside>
    
    - Odds Ratio Analysis
    - Correlation Analysis
    
    Use data to validate relationships between variables. Validate user behaviour relationships to core business metrics. 
    
    **Validate user behaviour relationship to core business metric**
    
    - Desired outcome’s relationship with various input variables
    
    <aside>
    💡 Non-actionable insights!! → Make sure the insight is actionable, clear, and progressive insights
    
    </aside>
    
    If dependent variable is Discrete 
    
    - Odds Ratio analysis
    
    If dependent variable is Continuous 
    
    - Correlation analysis
    
    ---
    
    ---
    
    ### Odds Ratio analysis
    
    Discrete → Retention (Yes, No), Completed Signup (true, false)
    
    Odds of an event occurring for a test group compared against a control group.
    
    Odds ratio → Odds of an event occurring as a result of an action for a test group compared to control group
    
    Calculation → (Odds of desired outcome if user does X ) / (Odds of desired outcome happening if user doesn’t do X)
    
    >1 = +ve influence after intervention
    
    Confusion matrix → 2X 2  feature adoption vs retention
    
    Odds of desired outcome if user does X = A/B (first row)
    
    Odds of desired outcome if user does NOT do X = C/D (second row)
    
    Calculate NPV & PPV → check..
    
    Calculate your Confidence Interval → 95% CI i.e. It is 95% likely to fall between this interval.
    
    <aside>
    💡 ≥ 2 desired outcome of an odds ratio analysis, Strong PPV and NPV approaching 1 reinforce each other!! Indicates stronger relationship b/w → user action and desired outcome
    
    </aside>
    
    If 95% CI interval contains → 1 it means that it is probably by chance! 
    
    **Requisite** **Sample Size**
    
    - Should be large enough to be statistically significant!!
    
    ---
    
    ### Correlation Analysis
    
    When User action and desired outcome are continuous & NOT discreet
    
    How much variance is one explained by another!!
    
    R value (-1 to 1)
    
    ---
    
    ---
    
    ### Case Study
    
    **Problem** : PM at GoFood is trying to build compounding wins.
    
    **Context** : User Journey
    
    - Use search
    - View search results  → Restaurant Tab → Restaurant name, address, category, default picture,  Dishes Tab → dishes that match search query
    - add dish to cart → Rest. information, ETA, Rating, dishes, prices
    - review order → Overall dishes price, delivery price,
    - confirm order
    
    Roleplayer : Search & Recommendations PM at GoFood. Working on usability of Search Bar & “Recommended Categories” in GoFood home page.
    
    Her supervisor : browser & discover more restaurants
    
    **Insight Generation Loop**
    
    1. Establishing Good Conjectures
        1. Prioritise a metric to dig
        2. broad question to brainstorm conjectures
        3. Narrow down to a set of conjectures
    2. Plan the analysis
    3. Conduct the analysis
    4. Pressure test findings
    
    ---
    
    ---