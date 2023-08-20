# Product Instrumentation Setup

**Article** - [https://www.reforge.com/blog/why-most-analytics-efforts-fail](https://www.reforge.com/blog/why-most-analytics-efforts-fail)

<aside>
💡 Data initiatives - "What to track, how to track it, and manage it over time"

</aside>

**Issues**

- Lack of shared langauge
    - No shared language for product flows → onboarding, checkout etc
- Slow transfer of knowledge
    - Issues due to movement of people..
- Lack of trust
    - trust issues
- Inability to act on data quickly
    - When faced with a tradeoff of taking a lot of time just to get data they trust and can understand, and skipping that step just to move forward, a lot of teams will choose the latter.
    

Root Causes

- Tracking metrics as the goals vs analyzing them
    - REAL GOAL IS TO ANALYZE THE METRICS AND NOT TRACK THEM!!
- Developer-Data mindset vs business user mindset
    - Can a non-tech savvy user consume the data without full onboarding session
- Wrong level of abstraction
    - Events being either too broad or too generic
        - too board - Facebook Sign up, Google Sign up
        - too specific - Sign up clicked,
        - apt. abstraction - Sign up selected event with property having "source" =
- Written only vs visual communication
    - Having a shared source of "truth" about what an analytics event is and means is critical.
    - A visual that corresponds with an event. Visual representation of customer journeys
- Data as a project vs ongoing initiative
    - It is an ongoing initiative
    

### Step by step process

1. Even tracking dictionary - Data we are tracking and aspects of it (Shared language and context!)
    - [https://docs.google.com/spreadsheets/d/1UmAU9aNvGOPNY0vG-LKE5Ka2VEbbNtTSgVlob2irb-4/edit#gid=0](https://docs.google.com/spreadsheets/d/1UmAU9aNvGOPNY0vG-LKE5Ka2VEbbNtTSgVlob2irb-4/edit#gid=0)
    
    Characteristics
    
    - Simple and easy to understand
    - Clean naming conventions are the basics
    - Can someone new quickly understand it
    - Actionable -
    - Visual - some screenshots, when the event gets triggered
    

1. Mindset of the business user 

- What are business goals and objectives?
- Product experiences around these goals and objective?
    - Product experiences that correspond to these goals and objectives
    - screen or funnel
    - more context around in which decision is taken by the user
    - anything that inhibits the user from achieving those goals and objectives
    - What would we want to know about this experience?
- What are the questions or hypothesis then I might want to answer around these goals and product experiences?

2. Track Journeys instead of metrics

- Journey
- **Intent**: Create Invoice Selected → New Invoice Started → Contact Search
- **Success**: Recipient Added to Invoice → Invoice Sent
- **Failure**: Invoice Draft Saved (a default action)
    - Implicit failures - user drops off
    - Explicit failures  - some error happened!
- **Properties**
    - Used to segment the events
    - Questions
        - how will I be able to segment users
        - How will I be able to identify the different paths that mature vs casual users use
        - Does this give me enough nuanced data to compare and contrast successful users from dropped off users
        - If this were the last event that I ever tracked from a user, what would I want to know about the user's experience on this screen
    - Properties can be in these buckets
        - Profile of the user - demographics, product tier etc
        - marketing properties - source , campaign, entry page
        - User action properties - actions of the user → first purchase date, first service type, total orders
            - set and forget - signup_date etc
            - append and increment → total orders, total revenue
            - Type of action properties
                - User initiated vs system initiated
                - Facebook vs email vs phone
        - Contextual properties
            - Question - What might be influencing the motivation of the user to complete or not complete the goal?
            - What could influence motivation
            - How could I differentiate an increase or decrease in motivation?
    
    Testing your events 
    
    - Understanding
        - Business Users close to product
        - Business users away from product
        - New employees
    - Actionability
        - Check with the questions and hypothesis  and whether it will answer this question
    

[Event Tracking Implementation Spec Temp.xlsx](Product%20Instrumentation%20Setup%208794fc8806c446f4b1fe2f8bed7ef3ad/Event_Tracking_Implementation_Spec_Temp.xlsx)