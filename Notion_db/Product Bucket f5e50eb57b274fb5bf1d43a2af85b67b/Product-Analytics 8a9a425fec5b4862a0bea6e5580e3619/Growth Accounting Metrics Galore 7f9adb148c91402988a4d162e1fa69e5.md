# Growth Accounting/Metrics Galore

## Accounting for user growth, revenue growth, cohort lifetime value, engagement and quality of revenue, GAAP for startups

## Monthly Active User growth accounting

MAU(t) = new(t) + retained(t) + resurrected(t) (MAU this month is either new, retained from previous month or resurrected from previous time period)

MAU(t-1) = retained(t) + churned(t) (MAU from last month either retained or churned)

MAU(t) - MaU (t-1) = new(t) + resurrected(t) - churned(t)

![Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/user_accounting_graph.png](Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/user_accounting_graph.png)

Quick Ratio = (new + resurrected)/churned (should be greater than 1)

<aside>
💡 Measure on a rolling 28 day basis

</aside>

## Revenue growth accounting

particularly useful for SaaS businesses or recurring revenue businesses

Apart from MAU accounting as before, look at MRR accounting

*MRR(t) = new(t) + retained(t) + resurrected(t) + expansion(t)*

*MRR(t - 1 month) = retained(t) + churned(t) + contraction(t)*

MRR(t)  = new(t) + resurrected (t) + expansion(t) - churned(t) - contraction(t)

![Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/MRR_accounting.png](Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/MRR_accounting.png)

quick ratio = (new + expansion + resurrected)/(churn + contraction)

<aside>
💡 Recurring subscription revenue is default-retained in contrast with recurring visitation which is default-not-retained. As such subscription revenue tends to have a much lower churn rate and higher quick ratio.

</aside>

<aside>
💡 You could use this kind of accounting for growth of other things such as link share on Twitter or L28 for Facebook

</aside>

**Review** - To review, growth accounting is a framework that can be used in just about any situation where a group of users/customers are accruing value to your business in some form or another (revenue, their attention via DAU, contributing content to the system, etc).

**Shortcoming of growth accounting -** doesn't tell whether churning users or contraction of unit of measure is recently added users or old users (doesn't take into account lifecycle of users. Therefore, doesn't give sense of lifecycle of a customer

### Lifetime Value of customer - cumulative revenue realized per customer

Most descriptions of lifetime value (LTV) use a model which ends up with a formula based on a combination of contribution margin (m), retention rate (r) and discount rate (d) which encapsulates the infinite time horizon LTV (e.g. the wikipedia article).

*LTV = m * r / (1 + d - r)*

This model turns out to be of **limited usefulness** for understanding early stage companies because of the following assumptions that are built into it’s derivation:

- **Retention is constant** both across cohorts and, perhaps more importantly, throughout the lifetime of a customer (i.e. it assumes that if you have a probability *r* of being retained from month 1 to 2 then you also have a the same probability *r* of being retained from month 20–21)
- **Constant unit economics** throughout cohorts and customer lifetime which leads to a constant contribution margin.
- It assumes that these quantities are sufficiently constant over **long enough time spans** such that including the discount rate is sensible.

**Empirically realized cohort LTV**

Weekly cohort LTV curves - Look for metrics like "9 month (36 week) LTV "

![Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/cohort_ltv.png](Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/cohort_ltv.png)

LTV for a cohort given at time T = total realized revenue / (total number of customers including who may have churned out)

4 types of LTV 

- Flat LTV - cohort spent up-front but never spent again
- Sub-linear LTV - cohort continuous to spend but it the incremental gains decreases with time
- Linear LTV - cohort consistently spends same amount per user in the cohort. Truly linear LTV would be extremely high retention
- Super Linear LTV  - Amount per user is increasing as they age. Ex - Amazon, Slack - Customer buys some licenses and then in future months buys even more license

[https://medium.com/swlh/diligence-at-social-capital-part-3-cohorts-and-revenue-ltv-ab65a07464e1](https://medium.com/swlh/diligence-at-social-capital-part-3-cohorts-and-revenue-ltv-ab65a07464e1)

Sometimes heatmap view of cohort LTV is really helpful

## LTV approach applied to engagement and retention

- Look at retention heatmap

<aside>
💡 data on the diagonal in the heatmap represents an even in the fixed calendar date

</aside>

Similar to the revenue case, there are three qualitatively different cases of activity LTV curves here.

- **Flat**: No incremental visitation past a certain date.
- **Sub-linear**: Non-zero but decreasing visitation. This is what we’re seeing in the example. All users appear to be gradually losing interest.
- **Linear**: Consistent retention through the lifetime of the cohort. A core of users is consistently using the product indefinitely. The slope is determined by how much of the cohort is made up of core users vs. non-core users.
- **Super-linear**: Increasing retention as cohorts age. The propensity to use the product goes up as the user ages.

[https://medium.com/swlh/diligence-at-social-capital-part-4-cohorts-and-engagement-ltv-80b4fa7f8e41](https://medium.com/swlh/diligence-at-social-capital-part-4-cohorts-and-engagement-ltv-80b4fa7f8e41)

## Depth of engagement and quality of revenue

What is the distribution of engagement across the user-base? How solid is the revenue stream?

Separating users into highly engaged users vs marginally engaged users

Look at L28 = # of days user was active in the last 28 days

Plot the L28 distribution

![Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/L28distribution.png](Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/L28distribution.png)

It says that around 35% of the users had L28 = 1

## From depth of engagement to quality of revenue

The idea is that, in the context of enterprise SaaS, customers who are spending a lot of money in a highly recurring fashion are generally higher quality customers because they are more likely to survive a downturn.

# C**onclusion**

Let’s review the three areas that we’ve discussed in this series:

- **Growth accounting** provides a framework for understanding the underlying components that drive net growth by unpacking top-line new customers from resurrection and churn. The framework applies not just to [growing users](https://medium.com/swlh/diligence-at-social-capital-part-1-accounting-for-user-growth-4a8a449fddfc) but to growing [anything of value](https://medium.com/swlh/diligence-at-social-capital-part-2-accounting-for-revenue-growth-551fa07dd972) including subscription revenue, visitation, posting behavior, etc.
- The textbook explanation of **[lifetime value](https://medium.com/swlh/diligence-at-social-capital-part-3-cohorts-and-revenue-ltv-ab65a07464e1)** (LTV) is not the most useful one for understanding early stage companies (or early stage features). Empirical N-week or N-month LTV is preferred. The idea of LTV can be generalized from revenue generation to [other activities of value](https://medium.com/@jonathanhsu/diligence-at-social-capital-part-4-cohorts-and-engagement-ltv-80b4fa7f8e41) such as cumulative visitation, referrals, etc.
- Aggregate measures of engagement such as DAU/MAU provide a limited lens for understanding depth of engagement. A better practice is to observe the full **distribution of depth of engagement**. This is also true when considering the distribution of revenue generation where ACV is also a limited view compared with understanding the full distribution of contract values.

## 8 ball Analysis of startups

[https://medium.com/swlh/diligence-at-social-capital-epilogue-introducing-the-8-ball-and-gaap-for-startups-7ab215c378bc](https://medium.com/swlh/diligence-at-social-capital-epilogue-introducing-the-8-ball-and-gaap-for-startups-7ab215c378bc)

- The 8-ball consists of the three pieces that have been described in these posts: 1) growth accounting, 2) cohort behavior and 3) distribution of product-market fit all measured for the core unit of value for the business (typically users and/or (possibly recurring) revenue).
- [https://analytics.socialcapital.com/eightball/login?mode=select](https://analytics.socialcapital.com/eightball/login?mode=select)
- 

## GaaP analysis of startups

- We would propose that the 8-ball analyses that we have articulated in this series of posts comprise a reasonable GAAP-like standard for understanding product-market fit for early stage companies.
- [https://gist.githubusercontent.com/hsurreal/4062f2639d4bb6fab6fb/raw/83f2982e8187cdbb9b8e35a6f5aea9daf32bdea8/growth_accounting_and_ltv.sql](https://gist.githubusercontent.com/hsurreal/4062f2639d4bb6fab6fb/raw/83f2982e8187cdbb9b8e35a6f5aea9daf32bdea8/growth_accounting_and_ltv.sql)
- [https://app.mode.com/editor/neeraj_kumar422/reports/c949b3055a67](https://app.mode.com/editor/neeraj_kumar422/reports/c949b3055a67)

### Random metrics

**CX metrics**

- CSAT - is mostly transactional, how satisfied they are in with a recent interaction or purchase
- Tickets raised from various channels
- NPS - How likely as a customer are you to recommend product or service to friends or colleague?
- CES (Customer Effort Score) - How much effort did you have to expend to handle your request? or How easy was it for you to complete the task or action?
- **CAC**  - Customer Acquisition Cost
- **LTV** - Lifetime value (refer analytics book or top of this page)
- **ARPU** - Average revenue per active user
- **Unit economics**
    - [https://medium.com/ongrowth/unit-economics-in-practice-ebd0a2ef345c](https://medium.com/ongrowth/unit-economics-in-practice-ebd0a2ef345c)
    - SaaS - CAC, LTV, Churn (ideally : LTV/CAC ratio should be 3 or you should be able to recover CAC for a customer within in 12 months)
        - To improve unit economics one can - reduce churn, upsell, reduce CAC per customer
- **Churn** - monthly churn (refer analytics book)
- **Product North Star**
    - How to define it? how to use it to drive your long-term product strategy and growth?
    - Definition - A key measure of success of the product. It defines the relationship between the customer problems that the product team is trying to solve and the revenue that the business aims to generate by doing so.
    - North star metric
        - A statement of your product vision
        - a metric that serves as a key measure of your current product strategy
        
        <aside>
        💡 What action provides realized value to the customer. A leading indicator of success
        
        </aside>
        
        [North Star Examples](Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/North%20Star%20Examples%20be4baf7fcd0a49b891608e4fe45e0a47.csv)
        
        ![Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/north-star-metric-tree.png](Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/north-star-metric-tree.png)
        
        **How to find north star metric?**
        
        - What is your product's core customer engagment model
            - **The Attention Game:** How much of your customers’ time can you capture in your product
            - **The Transaction Game:** How many commercial transactions does your user make on your platform
            - **The Productivity Game:** How many high value digital tasks can your customer perform in your product
        
        **How to find your north star metric?**
        
        - Figure out a constellation of key output metrics - make sure they account for retention, monetization and engagement
        - Break output metrics to input metrics
        - Figure out the relationships between those metrics and look for tradeoffs
    - References
        - [https://amplitude.com/blog/2018/03/21/product-north-star-metric](https://amplitude.com/blog/2018/03/21/product-north-star-metric)
        - [https://thoughtbot.com/blog/north-star-metric](https://thoughtbot.com/blog/north-star-metric)
        - [https://www.reforge.com/blog/north-star-metric-growth](https://www.reforge.com/blog/north-star-metric-growth)
    
    ## Funnels - Conversion, Product, Customer
    
    - Registration and login Funnel
    - Tutorial funnel - how many skipping completely, abondment points,
    - Monetization and growth funnels
        - In App purchase funnel - checkout stages
        - freemium to premium funnel
        - level completion funnel - educational or gaming apps
    - Search Funnel
    - The Cancel subscription funnel
    
    ## User segmentation with RFM analysis
    
    - RFM Analysis (aka Recency, Frequency, Monetary Analysis) breaks your user base down into segments based on how frequently and recently they’ve launched the app, from champions to hibernating users, and provides engagement strategies tailored for each segment.
    - **The Recency and Frequency Grid breaks your user base down into:**
        - Champions [R(4 – 5), F(4 – 5)]
        - Loyal Customers [R(3 – 4), F(4 – 5)]
        - Potential Loyalists [R(4 – 5), F(2 – 3)]
        - Promising [R(3 – 4), F(0 – 1)]
        - Can’t Lose Them [R(1 – 2), F(4 – 5)]
        - At Risk [R(1 – 2), F(3 – 4)]
        - About to Sleep [R(2 – 3), F(1-2)]
        - Hibernating [R(1 – 2), F(1 – 2)]
        - New Customers R [(4 – 5), F(0 – 1)]
        - Need Attention R [(2 – 3), F(2 – 3)]
    - bar chats depicting recency and frequency histogram

![Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/In-content-screen-shot-2.png](Growth%20Accounting%20Metrics%20Galore%207f9adb148c91402988a4d162e1fa69e5/In-content-screen-shot-2.png)

Actions you can take based on rfm - 

**Get Insights Into Reachability**

Find out which users are primed for engagement campaigns and view the most popular engagement channels for each segment.

**Analyze Conversion Funnels for Specific User Segments**

Learn how each user group is moving through your funnels, and identify opportunities to improve conversion rates.

**Track Ratios for Insights Into Marketing Performance**