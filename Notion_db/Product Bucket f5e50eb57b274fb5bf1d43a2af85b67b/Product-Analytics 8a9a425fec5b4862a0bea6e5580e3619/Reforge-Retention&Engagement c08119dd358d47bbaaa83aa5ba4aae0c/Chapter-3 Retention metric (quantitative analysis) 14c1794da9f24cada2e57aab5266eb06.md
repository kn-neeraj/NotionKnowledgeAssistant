# Chapter-3 Retention metric (quantitative analysis)

<aside>
💡 Define a retention metric and analyse it

</aside>

### **Common mistakes to avoid while defining retention metric**

- Not aligning with natural usage frequency of the product
    - Retention metric should be informed by the use case
- Combining actions to create the metric
    - Teams usually go with easier action to move the metric
- Optimising just for revenue
    - Remember! - Revenue is output metric, input metric is usage (users constantly deriving core value out of the product!)
    

### Define retention metric

there are 3 components of retention metric

- **Frequency**
    - *What is the natural frequency in which the user experiences the problem?*
    - We use the Use Case Analysis to develop our qualitative natural frequency hypothesis
    - We then validate it with quantitative product usage data
        - Select a use case
        - Create a frequency histogram of active users in last 28 days (L28)
        - Analyze the distribution - (wherever there is higher frequency it will validate or invalidate your hypothesis)
            - If it invalidates, there is a difference between use case you had set out to solve vs actual usage. You have to either change the product to solve natural frequency of the use case or look back at the use case analysis
- **Core behaviour**
    - *What action indicates we are delivering the value to the user? (Look at problem & why part of use case analysis)*
        - Define core action hypothesis
    - Validate hypothesis
        - Create Cohort retention curves for various core action hypotheses [Retention Curves]
        - You are looking for action that leads to highest retention
- **Who**
    - We are looking for who in the use case analysis and give an internal name such that everybody in the organization understands

<aside>
💡 Final metric could be : Pinterest - Weekly Active repinners, SurveyMonkey -Monthly active surveryors etc

</aside>

### Analyzing retention using Cohorts

- Acquisition Cohorts - Users who signed in a particular date
- Time period - WOW, MOM
- Define "Active"
- Avg retention

5 ways to look at cohorts

- Absolute - number of users still active in Week or Month x
- Percentage - % of users still active in week or month x
- Absolute Relative - how many users went dormant after week or month x
- Percentage Relative - what % went dormant after week or month x
- Avg Relative - How is cohort behaving relative to avg

Retention Curve - Line graph visualization of the avg of the individual cohorts over time

- Overall shape of the curve
    - Slope towards X axis - BAD
    - Flattens after a period
    - Smile  - GOOD ( with flattening product is resurrecting dormant users)