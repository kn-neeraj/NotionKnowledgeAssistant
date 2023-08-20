# Stripe's Payments APIs

Reference - [https://stripe.com/blog/payment-api-design](https://stripe.com/blog/payment-api-design)

**Principles**

- Abstracting away the complexity of payments has driven the evolution of our APIs over the last decade
- **It  is hard to get your users to fundamentally restructure their API integration**
- It's much easier to get them to add a parameter or two to their existing API requests
- How do you evolve as complexity of feature set evolves. More importantly, how do you abstract → Unify  these payment methods or features using just one integration path or a single client side API

**How they came up with a unified payments API**

- Pace your questions - start session with bunch of questions you want to answer. Write new questions and avoid discussing them. End each session with clear answers and questions to explore in the next session
- Use colors and shapes - lean on simple representations for complex, nascent concepts
- Focus on enabling real user integrations - Writing "hypothetical integration guides" to validate our concepts and to make sure we didn't introduce old or new pits of failure
- Question every assumption - think from first principles
- Lean on domain experts
- Make decision quickly knowing you might change your mind - Avoid stasis

<aside>
💡 A great API product stays out of the developer's way for as long as possible

</aside>

<aside>
💡 Keeping things simple means APIs are consistent and predictable YET giving developers power to control!

</aside>

Other important products

- Documentation to supplement integration experience
- Stripe CLI made webhooks much less daunting
- Stripe samples - allows developers who prefer to learn by example than prose

### Stripe's APIs as infrastructure - API versions

[https://stripe.com/blog/api-versioning](https://stripe.com/blog/api-versioning)

- When it comes to APIs, change isn't popular
- API developers lose that flexibility as soon as even one user starts consuming their interface

<aside>
💡 Changes should be backwards compatible

</aside>

- Fields should preserve their same type and name

**API versioning schemes**

- <DID NOT UNDERSTAND>

**Principles of change**

- Lightweight - Make upgrades cheap as possible for users and for ourselves
- First-class - make versioning a first class concept in your API so that it can be used to keep documentation and tooling accurate and up-to-date and to generate changelog automatically
- Fixed-cost - Ensure old versions add only minimal maintenance cost by tightly encapsulating them in version change modules. Put another way, the less thought that needs to be applied towards old behavior while writing new code, the better.
    
    

## SaaS : Fundamental equations

[https://stripe.com/en-sg/atlas/guides/business-of-saas#hybrid-sales-approaches](https://stripe.com/en-sg/atlas/guides/business-of-saas#hybrid-sales-approaches)

$Revenue = number of customers * Avg LTV per customer$

$number of customers = acquisition * conversion$

$Avg LTV per customer = price per period * avg number of period user stays$

Average Revenue per user (ARPU) = average revenue for an account over their lifetime

<aside>
💡 SaaS are capital intensive to grow ⇒ Marketing and Sales dominate marginal cost per customer,

</aside>

### Levers for growing SaaS

- Price
- Can ignore COGS
- CAC is important

<aside>
💡 the business needs to triple annual revenues for two consecutive years and then double them for three consecutive years.

</aside>

### Benchmarks

**High Touch SaaS Model**

- More heterogeneity with regards to conversion rate
- Churn Rate - 10% annualized churn is reasonable for companies in their early years. 7% is an excellent churn rate.
- High-touch businesses often measure so-called “logo” churn
- Net revenue churn - Difference in revenue per cohort per year. (negative net revenue churn: the impact of upgrades, increases in contract size, and cross selling exceeds the revenue impact from churn or reduce their use of software)
    - lost revenue from customers cancelling
    - lost revenue from downgrading
    - increased revenue from customer upgrading
    - increased revenue from cross selling
- Gross revenue churn  or Gross MRR churn rate