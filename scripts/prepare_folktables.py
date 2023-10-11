#!/usr/bin/env python
from folktables import ACSDataSource

data_source = ACSDataSource(survey_year="2018", horizon="1-Year", survey="person")
data_source.get_data(states=["CA"], download=True)
