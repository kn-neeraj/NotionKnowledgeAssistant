# Tools - Looker

### Getting Started

Reference - [https://looker.com/guide/getting-started#viewing-data](https://looker.com/guide/getting-started#viewing-data)

**Viewing Data -** Dashboards and Looks (Reports), schedule it for looking at every morning via email or other services 

**Find and Understand dashboards**

- Basic Looker Terminology
    - Query -Questions using data (How many sales were made last month?)
    - Answer could be in form of - Content (Looks or Dashboards (bunch of metrics))
    - Under "Browse" tab
    - Boards - possible to create boards
    - Shared folders - folder for different products
    - Your own personal folder
    - All folders - "Other people folders"
    - Search for Content - "search query"

**Viewing Dashboard**

- Content - Looks (saved reports) and Dashboards
- Each tile has an answer to a particular question
- Filters at the top
- Drill further into the data by hovering in

**Scheduling and Sending reports**

- schedule in mail using Create "Schedule or settings"

**Building Tools** 

- Grouping things together by "dimensions" (attributes such as type, color etc)
- Calculations on groups are called "measures"
- **Creating your own reports**
    - Results, SQL, and Visualization - can soft data and add column totals
    - Pivot data and add row totals
        - Can Pivot dimensions
    - Dashboard settings
        - Click in "Edit" mode
        - Rename Title
        - Tile can be rearranged or made small/big
        - Filters for each tile

**Developing Models** 

- LookML - language (Written by the Looker developer or admin)
- 

```sql
explore: order {
	join: customer {
		sql: 
		type: number
	}
}
```

---

---

### Retrieve and Chart Data

[https://docs.looker.com/exploring-data/retrieve-chart-intro](https://docs.looker.com/exploring-data/retrieve-chart-intro)

### Retrieving Data

- Exploring data in looker
    -