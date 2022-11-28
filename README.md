# Get Information About Schools

A Python 3 wrapper for the Department for Education's Get Information About Schools API.

## Install
```
pip install git+https://github.com/National-Education-Union/gias
```

## Examples

### Initialize
```python

from gias_api import GetInformationAboutSchools
gias = GetInformationAboutSchools(
  YOUR_GIAS_CLIENT_ID,
  YOUR_GIAS_PRIMARY_SECRET,
  YOUR_GIAS_SCOPE,
  YOUR_GIAS_API_KEY,
  YOUR_GIAS_TOEKN_ENDPOINT
  )
```

### Get establishment

```python
gias.establishment(100005)
```

#### Output
```
{'Urn': 100005,
 'La': {'Name': 'Camden', 'Code': '202'},
 'Establishment': {'Number': 1048, 'Name': 'Thomas Coram Centre'},
 'TypeOfEstablishment': {'Name': 'Local authority nursery school',
  'Code': '15'},
 'EstablishmentTypeGroup': {'Name': 'Local authority maintained schools',
  'Code': '4'},
 'EstablishmentStatus': {'Name': 'Open', 'Code': '1'},
 'ReasonEstablishmentOpened': {'Name': 'Not applicable', 'Code': '00'},
 'ReasonEstablishmentClosed': {'Name': 'Not applicable', 'Code': '00'},
 'PhaseOfEducation': {'Name': 'Nursery', 'Code': '1'},
 'Further fields': 'etcetcetc'
 }
```

### Get establishment's changes
```python
gias.establishment_changes(100005)
```

#### Output
```
[{'FieldShortName': 'EstablishmentName',
  'OldValue': 'Thomas Coram Early Childhood C',
  'NewValue': 'Thomas Coram Centre',
  'ValueType': 'String',
  'CreatedDate': '2011-10-21T16:28:40.367',
  'EffectiveDate': '2011-10-21T16:28:40.367'},
 {'FieldShortName': 'NumberOfGirls',
  'OldValue': '38',
  'NewValue': '31',
  'ValueType': 'String',
  'CreatedDate': '2011-11-16T20:27:37.607',
  'EffectiveDate': '2011-11-16T20:27:37.607'},
  ]
  ```
 
### Get establishment's groups
 ```python
gias.establishment_groups(137442)
```

#### Output
```
[{'GroupUid': 2711}]
```

### Get establishment's governors
 ```python
gias.establishment_governors(100005)
```

#### Output
```
[{'Gid': 1306077},
 {'Gid': 1306084},
 {'Gid': 1306087},
 {'Gid': 1524568},
 {'Gid': 1524573},
 {'Gid': 1539372},
 {'Gid': 1539373},
 {'Gid': 1585506},
 {'Gid': 1585627},
 {'Gid': 1602890},
 {'Gid': 1602891}]
```

### Get group
 ```python
gias.group(2711)
```

#### Output
```
{'GroupUid': 2711,
 'GroupId': 'TR00518',
 'Name': "CLAPTON GIRLS' ACADEMY TRUST",
 'CompaniesHouseNumber': '07698419',
 'GroupType': {'Name': 'Single-academy trust', 'Code': '10'},
 'OpenDate': '2011-07-08T00:00:00',
 'GroupStatus': {'Name': 'Open', 'Code': '1'},
 'Address': {'Street': "Clapton Girls'' Academy Laura Place",
  'Locality': 'Lower Clapton Road',
  'Town': 'London',
  'County': 'Not recorded',
  'Postcode': 'E5 0RB'},
 'Ukprn': 10059087,
 'HeadOfGroup': {'Title': 'Not recorded'},
 'Establishments': [{'Urn': 137442}],
 'Changes': [{'FieldShortName': 'GroupPostcode',
   'NewValue': 'E5 0RB',
   'ValueType': 'String',
   'CreatedDate': '2017-09-16T16:06:27.327'},
  {'FieldShortName': 'GroupLocality',
   'NewValue': 'Lower Clapton Road',
   'ValueType': 'String',
   'CreatedDate': '2017-09-16T16:06:27.357'},
  {'FieldShortName': 'OpenDate',
   'OldValue': '1900-01-01 00:00:00.000',
   'NewValue': '2011-07-08 00:00:00.000',
   'ValueType': 'Date',
   'CreatedDate': '2017-09-16T16:06:27.377'},
  {'FieldShortName': 'GroupStreet',
   'NewValue': "Clapton Girls'' Academy Laura ",
   'ValueType': 'String',
   'CreatedDate': '2017-09-16T16:06:27.407'},
  {'FieldShortName': 'GroupTown',
   'NewValue': 'London',
   'ValueType': 'String',
   'CreatedDate': '2017-09-16T16:06:27.417'},
  {'FieldShortName': 'UKPRN',
   'NewValue': '10059087',
   'ValueType': 'Numeric',
   'CreatedDate': '2020-03-19T00:00:00'}]}
```

### Get group's changes
```python
gias.group_changes(2711)
```

#### Output
```
[{'FieldShortName': 'GroupPostcode',
  'NewValue': 'E5 0RB',
  'ValueType': 'String',
  'CreatedDate': '2017-09-16T16:06:27.327'},
 {'FieldShortName': 'GroupLocality',
  'NewValue': 'Lower Clapton Road',
  'ValueType': 'String',
  'CreatedDate': '2017-09-16T16:06:27.357'},
 {'FieldShortName': 'OpenDate',
  'OldValue': '1900-01-01 00:00:00.000',
  'NewValue': '2011-07-08 00:00:00.000',
  'ValueType': 'Date',
  'CreatedDate': '2017-09-16T16:06:27.377'},
 {'FieldShortName': 'GroupStreet',
  'NewValue': "Clapton Girls'' Academy Laura ",
  'ValueType': 'String',
  'CreatedDate': '2017-09-16T16:06:27.407'},
 {'FieldShortName': 'GroupTown',
  'NewValue': 'London',
  'ValueType': 'String',
  'CreatedDate': '2017-09-16T16:06:27.417'},
 {'FieldShortName': 'UKPRN',
  'NewValue': '10059087',
  'ValueType': 'Numeric',
  'CreatedDate': '2020-03-19T00:00:00'}]
```


 ### Get governor
```python
gias.governor(1306084)
```

#### Output
```
{'Gid': 1306084,
 'Role': 'Governor',
 'Title': 'Ms',
 'Forename1': 'Perina',
 'Surname': 'Holness',
 'DateOfAppointment': '2017-09-01T00:00:00',
 'DateTermOfOfficeEndsEnded': '2023-08-31T00:00:00',
 'AppointingBody': 'Ex-officio by virtue of office as headteacher/principal',
 'Establishments': [{'Urn': 100005}],
 'Changes': [{'FieldShortName': 'forename1',
   'CreatedDate': '2018-09-05T09:25:52.157',
   'EffectiveDate': '2018-09-05T09:25:52.517'},
  {'FieldShortName': 'surname',
   'CreatedDate': '2018-09-05T09:25:52.157',
   'EffectiveDate': '2018-09-05T09:25:52.53'},
  {'FieldShortName': 'appointmentDate',
   'CreatedDate': '2018-09-05T09:25:52.17',
   'EffectiveDate': '2018-09-05T09:25:52.547'},
  {'FieldShortName': 'stepdownDate',
   'CreatedDate': '2018-09-05T09:25:52.17',
   'EffectiveDate': '2018-09-05T09:25:52.577'},
  {'FieldShortName': 'stepdownDate',
   'CreatedDate': '2021-09-09T16:48:09.41',
   'EffectiveDate': '2021-09-09T16:48:09.507'},
  {'FieldShortName': 'stepdownDate',
   'CreatedDate': '2022-07-08T10:59:17.357',
   'EffectiveDate': '2022-07-08T10:59:17.623'}]}
```

### Get governor's establishments
```python
gias.governor_establishments(1306084)
```

#### Output
```
[{'Urn': 100005}]
```

### Get governor's changes
```python
gias.governor_changes(1306084)
```

#### Output
```
[{'FieldShortName': 'forename1',
  'CreatedDate': '2018-09-05T09:25:52.157',
  'EffectiveDate': '2018-09-05T09:25:52.517'},
 {'FieldShortName': 'surname',
  'CreatedDate': '2018-09-05T09:25:52.157',
  'EffectiveDate': '2018-09-05T09:25:52.53'},
 {'FieldShortName': 'appointmentDate',
  'CreatedDate': '2018-09-05T09:25:52.17',
  'EffectiveDate': '2018-09-05T09:25:52.547'},
 {'FieldShortName': 'stepdownDate',
  'CreatedDate': '2018-09-05T09:25:52.17',
  'EffectiveDate': '2018-09-05T09:25:52.577'},
 {'FieldShortName': 'stepdownDate',
  'CreatedDate': '2021-09-09T16:48:09.41',
  'EffectiveDate': '2021-09-09T16:48:09.507'},
 {'FieldShortName': 'stepdownDate',
  'CreatedDate': '2022-07-08T10:59:17.357',
  'EffectiveDate': '2022-07-08T10:59:17.623'}]
```

## Get all establishments
```python
gias.establishments()
```

## Get all groups
```python
gias.groups()
```

## Get all governors
```python
gias.governors()
```

## Search Get Information About Schools
Create a GraphQL query
```python
graphql_query = """
{
    governorByGid(gid: 1009531)
    {  
	urn
	role
    title
    }
}
"""
gias.search(graphql_query)
```

### Output
```
{'data': {'governorByGid': {'urn': 135264,
   'role': 'Accounting Officer',
   'title': 'Ms'}}}
```
