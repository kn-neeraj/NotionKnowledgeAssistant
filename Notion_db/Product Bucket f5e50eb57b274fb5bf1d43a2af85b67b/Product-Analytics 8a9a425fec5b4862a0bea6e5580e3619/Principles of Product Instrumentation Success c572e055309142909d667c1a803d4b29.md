# Principles of Product Instrumentation Success

Article Link - [https://docs.google.com/document/d/1yCizW2Vp7wtcdySuc2FoccZ_tLdf9Z9IGHy_oIwwAcU/edit#heading=h.ytqeuv6bgwa1](https://docs.google.com/document/d/1yCizW2Vp7wtcdySuc2FoccZ_tLdf9Z9IGHy_oIwwAcU/edit#heading=h.ytqeuv6bgwa1)

**Principles**

1. Measurement vs. metrics
2. Mixing approaches to measurement
3. Staying grounded in the customer domain
4. Learning how to “see” data
5. Unlocking the long tail of insights & t-shaped instrumentation
6. Learning how to ask better questions
7. Working small and working together

**Measurement vs. metrics**

- While instrumenting products & product analytics - measuring when events of interest happens along with additional information about event & the actor or user that triggered the event
- Don't think about generic metrics, think about events of interest that happen in the product (related to product experience)

Five "frames" to do instrumentation : 

1. Decisions & Questions 
    - Start with decisions and questions you want to answer. Disadvantage - New questions or decisions can arise later on
2. Specific KPIs (Industry standard metric) & Metrics
    - Starting with typical important KPIs.  We forget "why" behind these metrics or these metrics are too lagging, generic!
3. Workflow or feature specific
    - Identify the key workflows in your product and customer journey. How people are using it, why are they getting stuck, How might I improve it?
    - Disadvantage is you might get stuck with lot of data!
4. Goal or Objective
    - Based on goal - "Improve retention of a cohort of customers" - Figure out a reasonable set of leading indicators, Why certain cohorts have high retention rates
5. Model
    - What is the recent model you built - for customer acquisition, engagement, retention, expansion, CSAT, CLTV
    

### Keeping customer domain front and center

- Don't stuff User Interface related stuff into event names! Keep more events to be user goals related (View Crash Reports Video, Download crash reports). Keep the customer domain in mind!
- User goals remain fairly consistent! The details how goal can be achieved may change but the "goal" largely remains stable! Events that we care about in the product are User Interface agnostic

<aside>
💁 If one thing sticks about this tip, let it be this: to future-proof events, consider the customer domain. Fewer customer-centric events beat out more interface-specific or code-specific events any day.

</aside>

### Learning How to "See" data

- Think in terms of verb(View, Toggle,...), noun(Home, Collection,..), event-name (View Home, Toggle Collection), description, properties, user properties

### Long tail of insights

- to figure out which metrics to instrument, we do following exercises :
    - Name personas (the “actors”)
    - Product promise, explore growth assumptions, and competitive
    - Optional: North Star Workshop
    - Customer journey mapping, customer narrative
    - Indicate key narratives
    - Review the interface/product
    - Map key narratives to key events
    - Question-storming/decision-storming activity
    - Event brainstorming in areas of interest