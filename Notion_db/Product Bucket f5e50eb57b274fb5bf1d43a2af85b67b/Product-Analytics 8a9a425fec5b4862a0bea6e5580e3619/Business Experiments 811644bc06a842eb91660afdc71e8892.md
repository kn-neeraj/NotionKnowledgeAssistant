# Business Experiments

### Causal inference - Randomize, isolate the effect and measure the difference

endogeneity - x is correlated with the error term

issues win causal inference - omitted variables, selection bias, measurement error, simultaneity

## Lecture 4

- Google Oxygen case
    - <Think about what steps were needed or superfluous> - intervention, buy-in, instituionalization
    - cautions about predictive analytics
        - correlation is not causation
        - past is not the future
        - prediction is not explanation
    - 
    
    <aside>
    💡 good attributes of a manager
    
    - set me up for success
    - trust → no micromanagement
    - open channel of communication
    - help me grow in carrier in holistic way
    
    </aside>
    
    ## Lecture - 5
    
    - If Oxygen attributes cause good team performance
    - Advantages of within context data
        - you can get buy in
        - relevance
    - Disadvantages
        - if organization changes - not relevant
        - expensive
    - Radomization - causality
    
    ## Lecture - 7
    
    - pointers for causality from observational data
        - confidence about data
        - cost of conducting an experiment
            - reputational cost...
        - how well past data to be predictor of future behaviour
    - Prediction vs Causality
        - What to do with prediction or look for explanation?
        - Descriptive, Diagnostic, Predictive and PRescriptive
    - Techniques
        - Hypothesis Testing - only with numeraical data
        - Data mining - possible with unstructured data
        - interaction effect -
    - Example
        - DV - exit (60%), days they were employable, fired (3%)
        - Demographics - Gender(85%), age, education, city tier
        - Personal - Fresher, Insurance experience, performance(EPA)
    
    ## Ideal Experiment
    
    - Randomization
        - People cannot self select
        - Avoid un-intented self selection - certain characteristics are over-represented in a group because they correlate with the chance of being included in that group
        - sample bias - certain characteristics are over-represented in our findings because they correlate with willingness to be included - Geeralizability
    - Observers real behaviour
    - Question: Funny video created to encourage people to workout more
        - Would a funny video like that encourage or discourage people from working out?
        - Will it effect different demographics differently?
        - Caveat : without producing a video
        - Solution
            - Consent
            - Demographics
            - Pretest-questions - your mood,
            - Randomization
            - Treatment1, Treatment2, Control video
            - measure
            - end
            
    
    ## Lecture 9
    
    - hetereogenous treatment effect
        - different effect - female/male, age group, education
        - refer-photo
    - P-Hacking
        - data fishing, data snooping, data butchery
        - misuse of data analysis to find patterns in data that can be presented
    - Experimental validity
        - statistical conclusion validity
        - threats to internal validity
            - Selection - have we randomized perfectly?
                - did the group become different over time?
                - different pre-test questions
                - Have I created a different situation for control and experiment group?
                - Different retention
                    - treatment group has to do something - how many of them survive
                - Confounding
                    - extraneous that correlates with both dependent and independent variable
                    - think about it in the beginning during regression equation
                - Diffusion
                - Paper - carry over effect dies after 3 weeks (proper time b/w experiments )
        - external validity
            - generalizability
            - business relevance
            
    
    ---
    
    ---
    
    ## Regression
    
    - [https://www.ime.unicamp.br/~dias/Intoduction to Statistical Learning.pdf](https://www.ime.unicamp.br/~dias/Intoduction%20to%20Statistical%20Learning.pdf) - Introduction to statistical learning
    - Simple linear regression
        - linear equation - output = alpha + beta0 x0 + beta1 x1 + beta x2....
        - Estimate the coefficients
            - We need to find coefficients such that the line is of best fit on the available data points measured through least squares function
            - RSS - Residual Sum of Squares - Sum of squares of (predicted - actual)
            - In other words, in real applications, we have access to a set of observations from which we can compute the least squares line
        - Assessing the accuracy of the models
            - Residual Standard Error, R2, F Statistic
            - RSE is measure of standard deviation of (e) error term in linear regression equation
            - R2 - Proportion of variance explained (0 and 1) explained using X (or squared correlation between X and Y (only in simple linear regression))
    - Multiple Linear Regression (multiple predictors)
        - Y = β0 + β1X1 + β2X2 + ··· + βpXp + E(eta)
        - βj is the average effect on Y of a one unit increase in Xj , holding all other predictors fixed.
        
        <aside>
        💡 if any of the predictors are correlated then it leads to misleading estimates of the individual media effects on sales
        
        </aside>
        
        - Estimating regression coefficients
            - we chose betas such that it minimizes the sum of squared residuals
        
        <aside>
        💡 Important example - Shark attacks and ice cream sales are positively correlated if shark attack is regressed on ice cream sales. However, it is the increase in temperature that is the underlying reason. Therefore, a multiple regression of attack versus ice cream sales and temperature reveals that, ice cream sales are no longer significant
        
        </aside>
        
        - Answer important questions from linear regression
            - Is there a relationship between response and the predictors?
                - If all the betas are insignificant then no relationship.
            - Deciding on important variables?
                - Forward selection - keep adding significant ones
                - Backward selection - keep removing insignificant ones
            - Model fit?
                - R2 - how much of variation in the output variable is explained by the predictors
            - Qualitative Predictors
                - Predictors with only two levels
                    - We can create a new variable with 0 and 1 value
                    - yi = β0 + β1xi + error = (β0 + β1 + error if ith person is female, β0 + error if ith person is male)
                    - Beta1 becomes the avg. difference between the male and female
                - Qualitative Predictors with More than Two Levels
                    - Create accordingly dummy variables and based on that definition Betas will defined and interpreted
                    - If Beta3 is significant it shows heterogeneity effect because the treatment effected gender with G = 1 more than gender with G = 0

![Business%20Experiments%20811644bc06a842eb91660afdc71e8892/WhatsApp_Image_2020-02-14_at_12.22.08_AM.jpeg](Business%20Experiments%20811644bc06a842eb91660afdc71e8892/WhatsApp_Image_2020-02-14_at_12.22.08_AM.jpeg)

- Linear Regression + Causality
    - Possible to establish causality with linear regression /background(/background<Thoda zyaada statistics tha..samajh nahi aaya>)

## Establishing causality with observational data (where RCT is not possible or too expensive)

- Difference in Differences
    - Used with Panel Data
    - Assumptions
        - no influence between groups
        - control group is the right counterfactual for treatment group
    - Typical Example - Effect of increased minimum wages on employment in NJ
    - Assumption - trend in the treated and counterfactual would be the same in the absence of treatment
    - Difference of before and after the treatment and their difference establishes causality
    - Regression DD
        - Write the regression equation with dummy variables and betas and interaction terms
        - If you apply DID - you will get the difference in outcome variable that could be attributed to the cause
    - Picking Controls
    - Questions to answer
        - What would the unit of analysis be?
        - Who would comprise the subject pool / sample?
        - What would the treatment be?
        - What are we worried about?
        - Why DID is an alternative?
        - What assumptions are we making? - counterfactual, no influence between groups
- PSM - Propensity Score Matching
    - Used with Cross Section Data
    - when the counterfactual is not available or you know there was selection bias in treatment (ex - effect of scholarship on number of years spent in school)
    - You don't have a randomized assignment;treatment is correlated with observed features that also impact the outcome directly
    - Benefits of matching
        - when number of confounders is large relative to sample size  - collapsing confounders into a single feature
        - Using an observational dataset, can construct an experimental setup after the fact
    - Issues
        - size of the sample
        - omitted variables
        - there may not be good matches with similar propensity score in control group
        - propensity function
    - Steps
        - Estimate propensity score (probability of being treated) on unit of analysis - logistic regression
        - Match the sample in treated with similar propensity score in control - caliper, nearest neghbour, matching with replacement...
        - Stratify and find the difference in control and treatment
        - Avg. of differences is a good estimate of treatment effect
    
    [DD vs PSM](Business%20Experiments%20811644bc06a842eb91660afdc71e8892/DD%20vs%20PSM%207d75f70ce03f43f296cfeaa21135849f.csv)
    
    ## Lecture - 8 - ideal experiment and intro to qualtrics
    
    - Two conditions for ideal experiment
        - Perfect randomization - equal chance of getting the treatment
            - participants cannot self select into a condition
            - avoid un-intended self selection - in random assignment consider - time, location, people
            - participants cannot select to be in an experiment - certain characteristics are over-represented in our findings because they correlate with willingness to be included
        - observes real behaviour
            - people respond differently to hypothetical vs real situations
            - people change their behaviour when they are being observed
            - people may simple be unaware of their motivations
    
    ## Lecture - 9 - Experimental validity, Statistical analysis
    
    - **statistical conclusion validity** - accuracy of the conclusion drawn from a statistical test
        - Main effect - differences in avg b/w treatment and control
        - Heterogeneous treatment effects - does treatment has same effect on all treated cases - Female/Male, Age group, Education - Check the interaction term
        - p-hacking issues - stopping when the effect is significant, running many experiments and reporting only that "worked"
    - **internal validity** - is the experiment measuring the causal effect of X on Y?
        - selection - groups equivalent beginning of the study?, did group become different over time (any other reason than treatment)
        - Confounding - an extraneous variable that correlates with both dependent and independent variable
        - Diffusion - some aspects of intervention are passed from treatment to control group
        - Carry over effect - effect that carries over from one experimental condition to another
    - **external validity**
        - Generalizability - limits to generalizability
            - aptitude - some treatments are more or less effective on particular individuals
            - situation - time, location, scope of study limits
            - pre -test effects - hints to people to respond in a certain way
            - post - test effects  -
            - Reactivity - people in placebo also feel they are doing well just because part of experiment
            - 
    
    ## Designing experiments : Check list
    
    - Think first about these..
        - Choose a question you can test and has business value
        - Plan treatment that only manipulates one variable
        - randomize over people, time and location
        - predefine your overall evaluation criteria
    - Design the treatment & randomisation
        - Describe the setting and participants
        - What are treatment and control groups? - group sizes
        - What is the unit of randomization - any concerns such as - selection, spillovers etc
    - Evaluation of results
        - main effect - statistical and economic
        - secondary effects - subgroups, long term, spillovers
        - Ponder over possible effects driving the result

---

---

---

## ABCs of A/B Experiment

- Decisions are expensive! so we need to test before taking the decision!
- A : Control, B : Experiment (there could be 3-4 variants but not too many! as attributing the cause to the effect observed will be difficult)
- Things to keep in mind
    - What needs to be tested
    - Sufficient Traffic
    - Traffic diversion techniques (they may not be equal so be need sufficient numbers)
    - Duration of the A/B test - 3, 3.5 weeks (Check online - duration calculator for A/B test)
- Statistics
    - Null Hypothesis - Status quo (no impact)
    - Alternate Hypothesis -
    
    <aside>
    💡 Strongly written hypothesis is extremely important! Specifics are important!
    
    </aside>
    
    - Tools for A/B test - Google Analytics, KISSMetrics, Optimizely, Visual Website Optimizer, Unbounce etc
    - Look for significant of p-value
    - [https://thumbtack.github.io/abba/demo/abba.html](https://thumbtack.github.io/abba/demo/abba.html)
    

## Correlation vs Causation

- What could happen when you observe A and B
    - A causes B (ideal case)
    - B causes A
    - A and B are correlated, they'are actually caused by C
    - A cause B, as long as D happens
    - A causes E, which leads to E to cause B
- Hypothesis Testing
    - When you are trying to identify whether a relationship exists between two variables
    - Longitudinal analysis - looks at changes over time -  panel data
        - first adopters of product launches are biggest customers
    - Cross sectional analysis - a snapshot of data
        - relatinoship between holiday specific promotions and sales
- A/B Experiments
    - Ex - People who join commmunities with their first month on the app have higher retention by a factor of 2 at the end of the year
        - Look for onboarding flow and make one half join the communities

[https://amplitude.com/blog/2017/01/19/causation-correlation](https://amplitude.com/blog/2017/01/19/causation-correlation)