# Data Manipulation

### Questions

<details>

<summary>[GOOGLE] Score Bucketization</summary>

Let’s say you’re given a list of standardized test scores from high schoolers from grades 9 to 12

Given the dataset, write code in Pandas to return the cumulative percentage of students that received scores within the buckets of <50, <75, <90, <100

Example Input:

```
|  user_id | grade | test score |
| -------- | ----- | ---------- |
| 1        | 10    | 85         |
| 2        | 10    | 60         |
| 3        | 11    | 90         |
| 4        | 10    | 30         |
| 5        | 11    | 99         |
```

Example Output:

```
| grade | test score | percentage |
| ----- | ---------- | ---------- |
| 10    | <50        | 30%        |
| 10    | <75        | 65%        |
| 10    | <90        | 96%        |
| 10    | <100       | 99%        |
| 11    | <50        | 15%        |
| 11    | <75        | 50%        |
```

**Answer**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame([[1,10,85],[2,10,60],[3,11,90],[4,10,30],[5,11,99]], columns = ["user_id","grade","test score"])

df["<50"] = np.where(df["test score"]<50,1,0)
df["<75"] = np.where(df["test score"]<75,1,0)
df["<90"] = np.where(df["test score"]<90,1,0)
df["<100"] = np.where(df["test score"]<100,1,0)

df = df.groupby(["grade"])[["<50","<75","<90","<100"]].sum().reset_index()
df = df.melt(id_vars=["grade"],var_name="test score",value_name="count")

df["grp_ttl"] = df.groupby("grade")["count"].transform('max')
df["percentage"] = 100*df["count"]/df["grp_ttl"]

df = (df[["grade","test score","percentage"]].copy()).sort_values(["grade","percentage"],ascending=True)

df["percentage"] = df.percentage.astype(int).astype(str)
df["percentage"] = df["percentage"] + "%"

df.head(10)
```

</details>

<details>

<summary>[NEXTDOOR] Complete Addresses</summary>

You’re given two dataframes. One contains information about addresses and the other contains relationships between various cities and states:

df\_addresses

address

_4860 Sunset Boulevard, San Francisco, 94105 3055 Paradise Lane, Salt Lake City, 84103 682 Main Street, Detroit, 48204 9001 Cascade Road, Kansas City, 64102 5853 Leon Street, Tampa, 33605_

df\_cities

_city state Salt Lake City Utah Kansas City Missouri Detroit Michigan Tampa Florida San Francisco California_

Write a function complete\_address to create a single dataframe with complete addresses in the format of street, city, state, zipcode.

**Answer**

```python
import pandas as pd

addresses = {"address": ["4860 Sunset Boulevard, San Francisco, 94105", "3055 Paradise Lane, Salt Lake City, 84103", "682 Main Street, Detroit, 48204", "9001 Cascade Road, Kansas City, 64102", "5853 Leon Street, Tampa, 33605"]}

cities = {"city": ["Salt Lake City", "Kansas City", "Detroit", "Tampa", "San Francisco"], "state": ["Utah", "Missouri", "Michigan", "Florida", "California"]}

df_addresses = pd.DataFrame(addresses)
df_cities = pd.DataFrame(cities)


def complete_address(df_addresses,df_cities):
    temp = df_addresses['address'].str.split(", ", n = 4, expand = True)
    temp.columns = ['street','city','zip']
    temp = temp.merge(df_cities, on=["city"], how="inner")
    temp["final"] = temp[["street","city","state","zip"]].apply(lambda x: (", ").join(x), axis = 1)
    temp = temp[["final"]].copy()
    temp.columns = ["address"]
    return temp

complete_address(df_addresses,df_cities)
```

</details>

<details>

<summary>PANDAS vs SQL</summary>

Can you tell me what is approximately Windows function equivalent in Pandas?

**Answer**

Windows function in SQL brings row wise calculation capabilities. An approximate equivalent of it can be `transform` in pandas it brings row wise calculation capabilities in Python.

</details>

<details>

<summary>[Forbes] Most Profitable Companies</summary>

[Check this link to practice​.](https://platform.stratascratch.com/coding/10354-most-profitable-companies?code\_type=2)

Find the 3 most profitable companies in the entire world. Output the result along with the corresponding company name. Sort the result based on profits in descending order.

**Answer**

```python
forbes_global_2010_2014.head()
t = forbes_global_2010_2014.sort_values('profits', ascending = False)
t.head(3)
```

</details>

<details>

<summary>[Amazon] [DoorDash] Workers With The Highest Salaries</summary>

[Check this link to practice​.](https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code\_type=2)

You have been asked to find the job titles of the highest-paid employees.

Your output should include the highest-paid title or multiple titles with the same salary.

**Answer**

```python
t = pd.merge(worker, title, left_on = 'worker_id', right_on = 'worker_ref_id', how='inner')
t.sort_values('salary', ascending = False, inplace = True)
t['rank'] = t['salary'].rank(method='dense', ascending= False)
t[t['rank']==1]
```

</details>

<details>

<summary>[Meta] Users By Average Session Time</summary>

[Check this link to practice​.](https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code\_type=2)

Calculate each user's average session time. A session is defined as the time difference between a page\_load and page\_exit. For simplicity, assume a user has only 1 session per day and if there are multiple of the same events on that day, consider only the latest page\_load and earliest page\_exit, with an obvious restriction that load time event should happen before exit time event . Output the user\_id and their average session time.

**Answer**

```
# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
entry = facebook_web_log[facebook_web_log['action'].isin(['page_load'])].copy()
exit = facebook_web_log[facebook_web_log['action'].isin(['page_exit'])].copy()
entry['day'] = entry['timestamp'].dt.date
exit['day'] = exit['timestamp'].dt.date
entry = entry.groupby(['user_id','day'], as_index=False).max()
exit = exit.groupby(['user_id','day'], as_index=False).max()

t =pd.merge(entry, exit, on=['user_id','day'], how='inner')
t['diff'] = t['timestamp_y'] - t['timestamp_x']
t.groupby(['user_id']).apply(np.mean)
```

</details>

<details>

<summary>[Google] Activity Rank</summary>

[Check this link to practice​.](https://platform.stratascratch.com/coding/10351-activity-rank?code\_type=2)

Find the email activity rank for each user. Email activity rank is defined by the total number of emails sent. The user with the highest number of emails sent will have a rank of 1, and so on. Output the user, total emails, and their activity rank. Order records by the total emails in descending order. Sort users with the same number of emails in alphabetical order. In your rankings, return a unique value (i.e., a unique rank) even if multiple users have the same number of emails. For tie breaker use alphabetical order of the user usernames.

**Answer**

```python
import pandas as pd
import numpy as np

result = google_gmail_emails.groupby(
    ['from_user']).count().to_frame('total_emails').reset_index()
result['rank'] = result['total_emails'].rank(method='first', ascending=False)
result = result.sort_values(by=['total_emails', 'from_user'], ascending=[False, True])
```

</details>

<details>

<summary>[Amazon] Finding User Purchases</summary>

[Check this link to practice​.](https://platform.stratascratch.com/coding/10322-finding-user-purchases?code\_type=2)

Write a query that'll identify returning active users. A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. Output a list of user\_ids of these returning active users.

**Answer**

```python
import pandas as pd
import numpy as np
from datetime import datetime

amazon_transactions["created_at"] = pd.to_datetime(amazon_transactions["created_at"]).dt.strftime('%m-%d-%Y')
df = amazon_transactions.sort_values(by=['user_id', 'created_at'], ascending=[True, True])
df['prev_value'] = df.groupby('user_id')['created_at'].shift()
df['days'] = (pd.to_datetime(df['created_at']) - pd.to_datetime(df['prev_value'])).dt.days
result = df[df['days'] <= 7]['user_id'].unique()

```

</details>
