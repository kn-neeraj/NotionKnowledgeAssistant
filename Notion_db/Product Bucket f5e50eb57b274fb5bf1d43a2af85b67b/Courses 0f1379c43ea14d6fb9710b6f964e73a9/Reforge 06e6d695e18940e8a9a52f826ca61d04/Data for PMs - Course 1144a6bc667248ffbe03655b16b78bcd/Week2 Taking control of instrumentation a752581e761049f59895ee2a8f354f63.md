# Week2 : Taking control of instrumentation

### Effective Analysis requires effective instrumentation

- Structured → Robust event dictionary to organise event tracking
- Actionable ⇒ Enables us to conduct Feature Performance, User Behaviour & User Experiences
- Ongoing ⇒ Keep improving it

Effective instrumentation helps us : 

- Create the analysis it needs
- Instrumentation → high quality data → high quality analysis →
- Tracked data reflects a product mindset
- Democratises data, enabling PMs to more effectively use self-serve tools

<aside>
💡 PMs responsible for iterability of the features

</aside>

---

### Creating Effective Event Dictionary

Event dictionary or taxonomy playbook → Single source of truth for tracking, Organizing, and documenting instrumentation.

- Events → Distinct actions a user can perform with the product (Event Syntax matters!!, noun + verb)
    - Success Events → Indicates that some part of user journey has been successfully completed
    - Intent Events → Precursor to the success event (awareness of a feature, intent to complete a step, )
    - Failure Events → Something prevents user from completing a goal
- Events properties→ Segmentation of the events
    - Different syntax → snake_case or camelCase
    - Action properties → What user does or action they are taking
    - Contextual properties → Helps us provide the context in which user took that action
    - Backstory properties → App installed source, campaign, etc
- Triggers when → When a user successfully does something in the product

---

### Designing Instrumentation for Current Solution or existing features

<aside>
💡 Divergence → identify and amass all relevant events and properties.
Convergence → Consolidate what we amassed into key events and events properties

</aside>

**Divergence**

- Establish primary user in our altitude → Who does my work primarily serve?
- Establish core actions in our product area → 2-5 core actions
- Describe the primary user’s journey of the first core action →
- Use user +ve or -ve pathways to define event properties →
- Faction in the other user dimensions →
- Repeat steps to account for other user dimensions and core actions →

U**ser Dimenstions**

<aside>
💡 User Categorization → Refer to new users, returning users or power users. (based on usage)
User personas → Refers to the problems our product is solving and who we are solving them for
User Roles → User types (different sizes of users, sides of users in a marketplace ((Example - Streamers)

</aside>

**Convergence**

- Group events

---

### Progressing instrumentation for new features

<aside>
💡 Data is not an afterthought. It is critical to advance our new solutions and future wins!

</aside>

---

### Instrumentation best practices

- Track events on the back event
- Test before launching instrumentation
- Don’t forget about user properties

---

---

## Generating Data Insights

### Consistent Insight Generation is a loop

<aside>
💡 Methodical and iterative process for insight generation

</aside>

Good insights

- Actionable →
    - A justified next step
    - **Who** are the users who will have greates opportunity for impact,
    - What - Are the actions we want these users to take
    - Why - What is the business impact
- Clear → Easy to understand and relevant
- High Quality → Demonstrates thoughtful data analysis
- Progressive → Leads to additional analysis iterations

### Insight Generation Loop

1. Define conjectures → Should be a debatable & testable statement.  
2. Plan the analysis → Ensures the resulting insight is clear
3. Perform the analysis → Analyze the data we have instrumented 
4. Pressure test our findings → Ensure resulting insight is high-quality

<aside>
💡 Mistakes - It is not a simple insight generation process!!. Data analysis is not the insight generation itself.

</aside>

**Example** - GoPay mobile payment and digital wallet of GoPay.

Conjectures → can we break even on our investment within five years? 
Plan analysis → ROI vs cost of installing charging banks
PM finds more evidence to justify decision

### Define Conjectures

- Debatable, testable, meaningful statement
- Ideally, PMs limit themselves to ≤ 4 conjectures
- Steps
    - Prioritise a metric to dig into based on the current goals
    - Pick metric you have least info about
    - Don’t start insight generation process with only on conjecture, you will be stuck answering just that statement.
    - Broad question gives a manageable, high-level starting point to brainstorm as many possible
    - Conventional conjectures → What keeps us from reaching our goals
    - Unconventional conjectures  → Pushes our boundaries of “what is” and “what could be”
    - Narrow down your set of conjectures by validating them
    - Check if each conjecture debatable, testable, meaningful statement
    
    **Question** : How would Fortnite game improve its monetisation?
    
    1. Prioritise the metric to dig into → Business metric → $50M in V-Bucks revenue
    2. Brainstorm conjectures → 
    3. Conventional
        1. **Users can pay and value items but don’t pay**
        2. **Users can pay but don’t value items**
        3. ~~Users can’t pay but do value items and earn from sign-ins → small groups~~
        4. Users can’t pay but value items and earn from upleveling
        5. **Users can pay but don’t pay enough as they are price sensitive**
        
        Unconventional
        
        - Offer more strong weapons
        - Free rewards cannibalizing potentially paying users
    
    ### Planning Analysis
    
    <aside>
    💡 Partner with data analyst
    
    </aside>
    
    - Starting analysis type -  Quick data pulls (can be answered with a quick number), segmentation or correlation analysis.
    - Analysis parameters - Priority data sets and specific variables as inputs in analysis
        - Target group’s behaviours that we are interested in
        - Timeframe - what timeframe
    - Expected Outcome - What are you expecting!!
    - Control for confounding factors - Extraneous variables in the same timeframe as our analysis. How to control for confounding factors
    
    ---
    
    ### Pressure Testing Analysis
    
    - Confirmation Bias →
    - Selection Bias →
    - Pressure test →
        - What additional analysis is needed?
        - Am I addressing the intended target audiences? ,
        - What is the relative impact of my findings?,
        - Could my causality be backwards? Can you invert causality
        
    
    ---
    
    ### Identifying Great Insights
    
    - Identifying insights
    - Packaging insights
    
    ### Identifying Insights
    
    - Take the process as a loop
    - Explore vs Exploit an existing insight
    - Explore other work → Running out of time, Diminishing marginal utility
    - Exploit and improve insight →
    
    **RECAP**
    
    - Instrumentation → Effective Instrumentation
    - Insight generation loop → methodogical & iterative process : Define conjectures,  plan analysis, perform analysis, pressure testing findings
    - 
    
    ---
    
    **CLASSROOM - Session 2**
    
    Behavorial data → requires instrumentation
    
    **How do you segment your customers at Amplitude?** 
    
    Behaviour cohorts
    
    Predictive cohorts → Lookalike audiences, these users might do these things
    
    <aside>
    💡 Analytics as a feature. Constantly iterate!! Don’t ship without it!! Anlaytics as code.
    
    </aside>
    
    Most orgs use Google sheets.
    
    Events Dictionary → Atlassian Internal schema registry. Repository for Schema. PMs look for what business questions that you might have to answer. Codified event dictionary is important!!
    
    Our PRDs → section related to any new tracking requirements
    
    <aside>
    💡 Think about analytics and not just shipping features!! It is very costly to forget analytics
    
    </aside>
    
    <aside>
    💡 Good PM → you can take your metrics down to the mettle!!
    
    </aside>
    
    ---
    
    ---
    
    ## Week 2 - Videos
    
    ### Effective Analysis Requires Effective Instrumentation
    
    [Effective Analysis.mov](Week2%20Taking%20control%20of%20instrumentation%20a752581e761049f59895ee2a8f354f63/Effective_Analysis.mov)
    
     
    
    ### Building a structured event dictionary
    
    [Building a structured event dictionary.mov](Week2%20Taking%20control%20of%20instrumentation%20a752581e761049f59895ee2a8f354f63/Building_a_structured_event_dictionary.mov)
    
    ### Designing current solution instrumentation
    
    [Current Solution Instrumentaiotn.mov](Week2%20Taking%20control%20of%20instrumentation%20a752581e761049f59895ee2a8f354f63/Current_Solution_Instrumentaiotn.mov)
    
    ### Progressing Instrumentation for New Features
    
    [progressing_instrumentation_of_new_features.mov](Week2%20Taking%20control%20of%20instrumentation%20a752581e761049f59895ee2a8f354f63/progressing_instrumentation_of_new_features.mov)
    
    ### Instrumentation best practices
    
     
    
    [instrumentation_best_practices.mov](Week2%20Taking%20control%20of%20instrumentation%20a752581e761049f59895ee2a8f354f63/instrumentation_best_practices.mov)
    
    ### Consistent Insight Generation is a loop
    
    [Consistent Insight Generation in a loop.mov](Week2%20Taking%20control%20of%20instrumentation%20a752581e761049f59895ee2a8f354f63/Consistent_Insight_Generation_in_a_loop.mov)
    
    ### Defining Conjectures Correctly
    
    [Defining Conjectures Correctly.mov](Week2%20Taking%20control%20of%20instrumentation%20a752581e761049f59895ee2a8f354f63/Defining_Conjectures_Correctly.mov)
    
    ### Planning Effective Analysis
    
    [Planning Effective Analysis.mov](Week2%20Taking%20control%20of%20instrumentation%20a752581e761049f59895ee2a8f354f63/Planning_Effective_Analysis.mov)
    
    ### Pressure Test Your Own Findings
    
    [Pressure Test your findinds.mov](Week2%20Taking%20control%20of%20instrumentation%20a752581e761049f59895ee2a8f354f63/Pressure_Test_your_findinds.mov)
    
    ### Identify Great insights
    
    [Identify Great Insights.mov](Week2%20Taking%20control%20of%20instrumentation%20a752581e761049f59895ee2a8f354f63/Identify_Great_Insights.mov)