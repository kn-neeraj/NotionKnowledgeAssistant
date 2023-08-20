# Amplitude Guides

[MasteringRetention.pdf](Amplitude%20Guides%203bc83a3290e248019aa1cd5a5d6c3617/MasteringRetention.pdf)

[Mastering Engagement.pdf](Amplitude%20Guides%203bc83a3290e248019aa1cd5a5d6c3617/Mastering_Engagement.pdf)

[product-analytics-playbook-vol1-amplitude.pdf](Amplitude%20Guides%203bc83a3290e248019aa1cd5a5d6c3617/product-analytics-playbook-vol1-amplitude.pdf)

### Mastering Retention

1. **Define the retention metric** 
- Critical Event
- Natural usage frequency of the product
- Who are you solving for

**Example  - App Automate**

- Critical Event - Ran a test
- Who are we solving for - SDETs (Automation QAs)
- Natural Usage Frequency
    - Users who have ≥ 2 critical events in last 60 days
    - Measure how long it takes for users to perform the critical event the second time
    - Find out by what time 80% of users have done the critical event 2nd time
    
    or
    
    - Histogram of number of days a user was active in L28 days
- Retention metric - Monthly Active Testers

Type of retentions

- N-day/week/month retention - regular usage pattern
- Unbounded retention - inverse of churn
- bracket retention

### Retention Lifecycle Framework

- The way we think about analyzing retention and putting strategies in place to im prove it should change depending on what stage a user is at in their product journey.
- The objective of the Retention Lifecycle Framework, and this playbook, is to get your  new users, current users, and resurrected users to become more engaged current users. **New user retention, current user retention, and resurrected user retention**
- Total active users = new user + retained user + resurrected user - dormant users

![Amplitude%20Guides%203bc83a3290e248019aa1cd5a5d6c3617/Screenshot_2020-11-29_at_5.28.54_AM.png](Amplitude%20Guides%203bc83a3290e248019aa1cd5a5d6c3617/Screenshot_2020-11-29_at_5.28.54_AM.png)

### New user retention

- Which behaviours or features bring new users back

### Current user retention

- Find our what certain group of users are or aren't doing
- Critical for long term growth

### Resurrected user retention

- Analyze why users are coming back - notification, campaign, etc

**Retention Lifecycle Framework**

- Important to understand what is contributing to "Monthly Active Testers" growth
- Breakdown your active user base into - New, current and resurrected users
- New users - a user in first internval of using the product
- Current user - who used in previous interval and current interval
- dormant user - used in previous interval and used in current interval
- resurrected user - did not use in previous interval but used in current interval

### Retention lifecycle split

Total Active users 

- New users
- Current users
- Resurrected users
- Dormant users

- [x]  Which type of retention
- [ ]  Complete the worksheet "Your retention Lifecycle"
    - [ ]  Retention lifecycle split
        - Total active users
            - New users
            - Current users
            - Resurrected users
            - Dormant users
    - [ ]  Pulse ratio
        - (number of new users + number of resurrected users )/ number of dormant users