# Data Manipulation

### Questions[#](broken-reference)

<details>

<summary>[GOOGLE] Score Bucketization</summary>

Let’s say you’re given a list of standardized test scores from high schoolers from grades 9 to 12

Given the dataset, write code in Pandas to return the cumulative percentage of students that received scores within the buckets of <50, <75, <90, <100

Example Input:&#x20;



</details>

Problem:&#x20;



| user\_id | grade | test score |
| -------- | ----- | ---------- |
| 1        | 10    | 85         |
| 2        | 10    | 60         |
| 3        | 11    | 90         |
| 4        | 10    | 30         |
| 5        | 11    | 99         |

Example Output:

| grade | test score | percentage |
| ----- | ---------- | ---------- |
| 10    | <50        | 30%        |
| 10    | <75        | 65%        |
| 10    | <90        | 96%        |
| 10    | <100       | 99%        |
| 11    | <50        | 15%        |
| 11    | <75        | 50%        |

```
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

|   | grade | test score | percentage |
| - | ----- | ---------- | ---------- |
| 0 | 10    | <50        | 33%        |
| 2 | 10    | <75        | 66%        |
| 4 | 10    | <90        | 100%       |
| 6 | 10    | <100       | 100%       |
| 1 | 11    | <50        | 0%         |
| 3 | 11    | <75        | 0%         |
| 5 | 11    | <90        | 0%         |
| 7 | 11    | <100       | 100%       |

Problem: \[NEXTDOOR] Complete Addresses

You’re given two dataframes. One contains information about addresses and the other contains relationships between various cities and states:

df\_addresses

address

4860 Sunset Boulevard, San Francisco, 94105 3055 Paradise Lane, Salt Lake City, 84103 682 Main Street, Detroit, 48204 9001 Cascade Road, Kansas City, 64102 5853 Leon Street, Tampa, 33605

df\_cities

city state Salt Lake City Utah Kansas City Missouri Detroit Michigan Tampa Florida San Francisco California

Write a function complete\_address to create a single dataframe with complete addresses in the format of street, city, state, zipcode.

Input:

import pandas as pd

addresses = {“address”: \[“4860 Sunset Boulevard, San Francisco, 94105”, “3055 Paradise Lane, Salt Lake City, 84103”, “682 Main Street, Detroit, 48204”, “9001 Cascade Road, Kansas City, 64102”, “5853 Leon Street, Tampa, 33605”]}

cities = {“city”: \[“Salt Lake City”, “Kansas City”, “Detroit”, “Tampa”, “San Francisco”], “state”: \[“Utah”, “Missouri”, “Michigan”, “Florida”, “California”]}

df\_addresses = pd.DataFrame(addresses) df\_cities = pd.DataFrame(cities)

Output:

def complete\_address(df\_addresses,df\_cities) ->

address 4860 Sunset Boulevard, San Francisco, California, 94105 3055 Paradise Lane, Salt Lake City, Utah, 84103 682 Main Street, Detroit, Michigan, 48204 9001 Cascade Road, Kansas City, Missouri, 64102 5853 Leon Street, Tampa, Florida, 33605

```
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

|   | address                                          |
| - | ------------------------------------------------ |
| 0 | 4860 Sunset Boulevard, San Francisco, California |
| 1 | 3055 Paradise Lane, Salt Lake City, Utah, 84103  |
| 2 | 682 Main Street, Detroit, Michigan, 48204        |
| 3 | 9001 Cascade Road, Kansas City, Missouri, 64102  |
| 4 | 5853 Leon Street, Tampa, Florida, 33605          |

Problem: PANDAS vs SQL

Can you tell me what is approximately Windows function equivalent in Pandas?

Solution:

Windows function in SQL brings row wise calculation capabilities. An approximate equivalent of it can be `transform` in pandas it brings row wise calculation capabilities in Python.
