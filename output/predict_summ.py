# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # GAINS - QAQC and Summary Statistics
# 
# ## Status: Preliminary DRAFT
# ### - Internal Use Only: Please to do not circulate or quote -
# 
# ## Country Coverage
# - All countries
# 
# ## Data source
# - Origin: Surveillance data extracts retrieved from http://gains.org in 7-day tranches
# - Date Extracted: **27-Nov-12**
# 
# ## Prepared by
# - Preston, Murray, Zambrano-Torrelio (@ EcoHealth Alliance NYC)
# 
# ## Caveats
# - This report focuses on surveillance samples (rows) in GAINS
# - The number of samples taken per animal varies widely with a mean of 5.3
# - These results are intended to guide QAQC of the GAINS database for modeling 
# - This is not a progress report on Predict
# - **Data entry and validation efforts are ongoing**
# - This report is automated and **formatting may vary**.
# 
# ## Intended Recipients:
# - **WCS Nanaimo:** Damien Joly, Tammie O'Rourke, Sarah Olson
# - **UC Davis:** Christine Kreuder Johnson

# <codecell>

import pandas as pd
from pandas import DataFrame, Series
import re
import glob
import os
from __future__ import division
import matplotlib.pyplot as plt

# <codecell>

#for files in glob.glob("data/surveys/*.csv"):
#    print files

# <codecell>

pieces = []

for files in glob.glob("data/surveys/*.csv"):
    path = '%s' % files
    df = pd.read_csv(path)
    pieces.append(df)
# Concatenate everything into a single DataFrame 
df = pd.concat(pieces, ignore_index=True)

# <markdowncell>

# ## Data Wrangling

# <markdowncell>

# - Total number of surveillance records

# <codecell>

#df.columns.tolist()
print "GAINS: n =", len(df)

# <markdowncell>

# - Remove parentheses, asterisks, and spaces from column names:

# <codecell>

df.columns = [re.sub(r'[^\w]', '', x) for x in df.columns]
df.columns

# <markdowncell>

# - Remove Pre-FY1 data

# <codecell>

# Remove Pre-Fiscal Year data
frame =df[(df['Quarter']!='Pre-FY1')]
print "Post-FY1: n =", len(frame)

# <markdowncell>

# - Number of samples in purgatory

# <codecell>

purg = frame[(frame['InPurgatory']==True)]
len(purg)

# <markdowncell>

# - Percent samples in purgatory

# <codecell>

purg_count = len(purg)
frame_count = len(frame)
purg_ratio = purg_count/frame_count
print purg_ratio * 100, "%"

# <markdowncell>

# - Remove samples in purgatory

# <codecell>

frame =frame[(frame['InPurgatory']==False)]
n = len(frame)
print "n =", n

# <markdowncell>

# - Rename organizations with consistent acronyms

# <codecell>

# Rename Organizations
frame['affil'] = np.where(frame['RecorderAffiliation'].str.contains('Wildlife Conservation Society'),
'WCS', np.where(frame['RecorderAffiliation'].str.contains('Ecohealth Alliance'),'EHA', 
np.where(frame['RecorderAffiliation'].str.contains('EcoHealth Alliance'),'EHA', 
np.where(frame['RecorderAffiliation'].str.contains('Global Viral Forecasting Inc.'),'GVFI',
np.where(frame['RecorderAffiliation'].str.contains('Smithsonian Conservation Biology Institute'),'Smithsonian', 
frame['RecorderAffiliation'])))))
frame['affil'].unique()

# <markdowncell>

# - Standardize missing and unknown values

# <markdowncell>

# - Create dataframe with core columns

# <codecell>

core = ['SiteName','Country', 'StateProv', 'Latitude', 'Longitude', 'AnthropogenicChange', 'DomesticAnimals', 'DateStarted', 'RecorderID', 
'RecorderAffiliation','PrimaryInterface', 'ReasonForCollection', 'AnimalIDGAINS', 'AnimalIDRecordedAs', 'IdentifiedBy', 
'AnimalClassification', 'TaxonomicDescriptor', 'SpeciesScientificName', 'IdentificationCertainty']
core_frame = frame.reindex(columns=core)
core_frame.columns

# <codecell>

core

# <codecell>

#Optional csv dump
#core_frame.to_csv("./G_core_surveys.csv")

# <markdowncell>

# # Summaries

# <markdowncell>

# ### Summaries of key fields (columns) for sample records in GAINS (rows)

# <codecell>

core_frame.ix[:,:3].describe()

# <codecell>

core_frame.ix[:,3:5].describe()

# <codecell>

core_frame.ix[:,5:10].describe()

# <codecell>

core_frame.ix[:,10:16].describe()

# <codecell>

core_frame.ix[:,16:19].describe()

# <markdowncell>

# ## Sample Counts

# <codecell>

fd = 'affil'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'

# <codecell>

fd_counts = clean_fd.value_counts()
fd_counts

# <codecell>

fd_counts[:15].plot(kind='barh', rot=0, title='Samples by organization')

# <markdowncell>

# ### Counts by Country

# <codecell>

fd = 'Country'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Site name (SiteName)

# <codecell>

fd = 'SiteName'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### State/Province (StateProv)

# <codecell>

fd = 'StateProv'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Recorder ID (RecorderID)

# <codecell>

fd = 'RecorderID'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Anthropogenic Change (AnthropogenicChange)

# <codecell>

fd = 'AnthropogenicChange'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Domestic Animals (DomesticAnimals)

# <codecell>

fd = 'DomesticAnimals'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Primary Interface (PrimaryInterface)

# <codecell>

fd = 'PrimaryInterface'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Animal Classification (AnimalClassification)

# <codecell>

fd = 'AnimalClassification'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Taxonomic Descriptor (TaxonomicDescriptor)

# <codecell>

fd = 'TaxonomicDescriptor'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Primary Interface (PrimaryInterface)

# <codecell>

fd = 'PrimaryInterface'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Species Scientific Name (SpeciesScientificName)

# <codecell>

fd = 'SpeciesScientificName'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Identification Certainty (IdentificationCertainty)

# <codecell>

fd = 'IdentificationCertainty'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Field Storage Method (FieldStorageMethod)

# <codecell>

fd = 'FieldStorageMethod'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Laboratory Storage Method (LaboratoryStorageMethod)

# <codecell>

fd = 'LaboratoryStorageMethod'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Specimen Location Facility Name (SpecimenLocationFacilityName)

# <codecell>

fd = 'SpecimenLocationFacilityName'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Plasma Collected (PlasmaCollected)

# <codecell>

fd = 'PlasmaCollected'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Serum Collected (SerumCollected)

# <codecell>

fd = 'SerumCollected'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Quarter

# <codecell>

fd = 'Quarter'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts.sort_index()

# <codecell>

fd_counts.sort_index().plot(kind='barh', title='Samples by Quarter')

# <markdowncell>

# ### Origin Known (OriginKnown)

# <codecell>

fd = 'OriginKnown'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Pregnant

# <codecell>

fd = 'Pregnant'
clean_fd = frame[fd].fillna('Missing')
clean_fd[clean_fd == ''] = 'Unknown'
fd_counts = clean_fd.value_counts()
fd_counts

# <markdowncell>

# ### Sample counts by country and taxa

# <codecell>

country_taxa = []

for x in frame.Country.unique():
    country_frame = frame[(frame['Country']==x)]
    country_taxa.append({'samples':country_frame.pivot_table('SampleDate', rows=['AnimalTaxa'],aggfunc='count'),
'country':x})
#country_taxa[2]

# <codecell>

country_taxa.sort()
#country_taxa.sort(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
#country_taxa[2]

# <codecell>

#country_taxa[1].plot(kind='barh')
#country_taxa[1].plot(kind='barh', title='Samples by Quarter')
#country_taxa[2]['samples'].plot(kind='barh')

# <codecell>

fig, axes = plt.subplots(nrows=5, ncols=4, figsize=(12, 10), sharex=True, sharey = True)
fig.subplots_adjust(hspace=0.4, wspace=0.05)
cid = 0
tickers = [0, 4000,8000, 12000, 16000]

for ax in axes.flat:
    country_taxa[cid]['samples'].plot(kind='barh', ax=ax, xticks=tickers,title=country_taxa[cid]['country'], 
alpha=0.7)
    cid += 1

# <codecell>

dist_taxa = frame.pivot_table('SampleDate', rows=['Country','AnimalTaxa'],aggfunc='count')
#dist_taxa = frame.pivot_table('SampleDate', rows=['Country','AnimalTaxa'], cols='Country',aggfunc='count')
#dist_taxa = frame.pivot_table('SampleDate', rows=['AnimalTaxa','SpeciesScientificName'], aggfunc='count')
dist_taxa

# <codecell>

#dist_taxa.plot(kind='barh')

# <markdowncell>

# ## Counts by animal

# <markdowncell>

# - Sample types grouped by individual animal

# <codecell>

#bga = frame[(frame['Country']=='Bangladesh')]
an_id = frame.pivot_table('SampleDate', rows='AnimalIDGAINS', cols='SpecimenType', aggfunc='count')
an_id
#mean(an_id)

# <markdowncell>

# - Number of Animals Sampled

# <codecell>

len(an_id)

# <markdowncell>

# - Mean number of samples per animal

# <codecell>

sam_per_an = n/len(an_id)
sam_per_an

# <markdowncell>

# - Animals by organization

# <codecell>

#an_id = frame.pivot_table('AnimalIDGAINS', rows='affil', aggfunc='count')
#an_id
an_id = frame.pivot_table('SampleDate', rows='AnimalIDGAINS', cols='affil', aggfunc='count')
an_id

# <markdowncell>

# - Animals by Taxa

# <codecell>

an_id = frame.pivot_table('SampleDate', rows='AnimalIDGAINS', cols='AnimalTaxa', aggfunc='count')
an_id

# <markdowncell>

# - Animals by country

# <codecell>

an_id = frame.pivot_table('SampleDate', rows='AnimalIDGAINS', cols='Country', aggfunc='count')
an_id

# <codecell>

## Plot animals by taxa and country

# <codecell>

#ans = frame.pivot_table('SampleDate', rows=['AnimalIDGAINS', cols= 'Country',aggfunc='count')                                  

# <codecell>

#country_taxa = []

#for x in frame.Country.unique():
#    country_frame = frame[(frame['Country']==x)]
    
#    country_taxa.append({'animals':country_frame.pivot_table('SampleDate', rows=['AnimalIDGAINS', 'AnimalTaxa'],aggfunc='count'),
#'country':x})
#country_taxa[2]

# <codecell>

#country_taxa.sort()

# <codecell>

#fig, axes = plt.subplots(nrows=5, ncols=4, figsize=(12, 10), sharex=True, sharey = True)
#fig.subplots_adjust(hspace=0.4, wspace=0.05)
#cid = 0
#tickers = [0, 4000,8000, 12000, 16000]

#for ax in axes.flat:
#    country_taxa[cid]['samples'].plot(kind='barh', ax=ax, xticks=tickers,title=country_taxa[cid]['country'], 
#alpha=0.7)
#    cid += 1

# <codecell>

## Counts by species

# <codecell>

#data = dist_taxa

#fig, axes = plt.subplots(2, 2)
#data.plot[21:40](kind='barh', ax=axes[0])
#data.plot[21:40](kind='barh', ax=axes[1])

# <codecell>

#dist_taxa[21:40].plot(kind='barh', rot=0, figsize=(12, 10), lw=2)

# <markdowncell>

# ## Tranches by prevalance

# <codecell>

by_sp_tranche = frame.groupby(['SpeciesScientificName', 'Country'])
sp_counts = by_sp_tranche.size().unstack().fillna(0)
indexer = sp_counts.sum(1).argsort()
#indexer[:10]

# <codecell>

count_subset = sp_counts.take(indexer)[-20:]
#count_subset

# <codecell>

count_subset.plot(kind='barh', stacked=True, figsize=(14, 12))

# <codecell>

by_sp_tranche = frame.groupby(['SpeciesScientificName', 'SpecimenType'])
sp_counts = by_sp_tranche.size().unstack().fillna(0)
indexer = sp_counts.sum(1).argsort()
#indexer[:10]

# <codecell>

count_subset = sp_counts.take(indexer)[-20:]
#count_subset

# <codecell>

normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True, figsize=(14, 12)); plt.legend(loc='upper center', bbox_to_anchor=(0.5,1.5),
          ncol=4, fancybox=True, shadow=True)

# <codecell>

### Dataframe built-in function approach

# <codecell>

count_sp = frame.pivot_table('SampleDate', rows='SpeciesScientificName', aggfunc='count')
#count_sp[:10]

# <codecell>

sam_by_sp = frame.groupby('SpeciesScientificName').size()
sam_by_sp.sort()
#sam_by_sp

# <markdowncell>

# ### Species with > 250 samples

# <codecell>

main_sp = sam_by_sp.index[sam_by_sp >= 250]
main_sp

# <codecell>

# hybrid solution
#by_sp_sex = frame.groupby(['SpeciesScientificName', 'Sex'])
#sp_counts = by_sp_sex.size().unstack().fillna(0)
#sp_counts_main = sp_counts.ix[main_sp]
#sp_counts_main

# <codecell>

top_sp = sam_by_sp.index[sam_by_sp >= 1000]
top_sp

top_500 = count_sp.ix[top_sp]
#top_sp
#top_sp = by_sp.sort_index(by='F', ascending=False)

# <codecell>

#top_female_sp = top_sp.sort_index(by='Female', ascending=False)
#top_female_sp

# <codecell>

#top_male_sp = top_sp.sort_index(by='Male', ascending=False)
#top_male_sp

# <markdowncell>

# ### Species with >1000 samples

# <codecell>

top_500.plot(kind='barh', figsize=(14, 12), title="Distribution by species where > 1000 samples ")

# <codecell>

### Calculate the counts

# <codecell>

#count_sp['Male'].fillna('Missing')
#clean_sp[clean_sp == ''] = 'Unknown'

#count_sp['diff'] = count_sp['Male'] - count_sp['Female'] 
#sorted_by_diff = count_sp.sort_index(by='diff')
#sorted_by_diff

# <markdowncell>

# ## Time Series

# <codecell>

#count_sp = frame.pivot_table('SampleDate', rows='SpeciesScientificName',cols='Sex', aggfunc='count')

tot_sp_taxa = frame.pivot_table('SpeciesScientificName', rows='SampleDate',cols='AnimalTaxa', aggfunc='count')
tot_sp_taxa.plot(title='Sample counts by taxa and sampling date', figsize=(12, 10), lw=2)

# <codecell>

tot_sp_sex = frame.pivot_table('SpeciesScientificName', rows='SampleDate',cols='Sex', aggfunc='count')
#tot_sp_sex.plot(title='Sample counts by sex and sampling date', figsize=(12, 10), lw=2)

# <codecell>

tot_sp_int1 = frame.pivot_table('SpeciesScientificName', rows='SampleDate',cols='PrimaryInterface', aggfunc='count')
tot_sp_int1.plot(title='Sample counts by interface and sampling dates', figsize=(12, 12), lw=2) ; plt.legend(loc='upper center', bbox_to_anchor=(0.5,1.5),
          ncol=2, fancybox=True, shadow=True)

# <codecell>

tot_sp_int1 = frame.pivot_table('SpeciesScientificName', rows='SampleDate',cols='District', aggfunc='count')
#tot_sp_int1.plot(title='Country Sample counts by interface and sampling date', figsize=(12, 10), lw=2)

# <markdowncell>

# ## Sampling sites: Africa

# <codecell>

#AFRICA
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
fig = plt.figure(figsize=(12,12))
m = Basemap(width=12000000,height=10000000,projection='lcc', resolution=None,lat_1=25.,lat_2=55,lat_0=0,lon_0=20.)
m.shadedrelief()
lon, lat = 0, 0
xpt,ypt = m(frame['Longitude'],frame['Latitude'])
m.plot(xpt,ypt,'bo')
plt.show()

# <markdowncell>

# ## Sampling Sites: South America

# <codecell>

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
fig = plt.figure(figsize=(12,12))
m = Basemap(width=12000000,height=10000000,projection='lcc', resolution=None,lat_1=25.,lat_2=55,lat_0=-20,lon_0=-55.)
m.shadedrelief()
lon, lat = 0, 0
xpt,ypt = m(frame['Longitude'],frame['Latitude'])
m.plot(xpt,ypt,'bo')
plt.show()

# <markdowncell>

# ## Sampling Sites: Asia

# <codecell>

#ASIA
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
fig = plt.figure(figsize=(12,12))
m = Basemap(width=12000000,height=10000000,projection='lcc', resolution=None,lat_1=25.,lat_2=55,lat_0=25,lon_0=95.)
m.shadedrelief()
lon, lat = 0, 0
xpt,ypt = m(frame['Longitude'],frame['Latitude'])
m.plot(xpt,ypt,'bo')
plt.show()

# <markdowncell>

# ## Sampling Sites: Americas 

# <codecell>

#MEXICO
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
fig = plt.figure(figsize=(12,12))
m = Basemap(width=12000000,height=10000000,projection='lcc', resolution=None,lat_1=25.,lat_2=55,lat_0=24,lon_0=-102.)
m.shadedrelief()
lon, lat = 0, 0
xpt,ypt = m(frame['Longitude'],frame['Latitude'])
m.plot(xpt,ypt,'bo')
plt.show()


# <markdowncell>

# ## Spatial Validation

# <codecell>

core_frame[['Latitude','Longitude']].describe()

# <codecell>

X = np.array(frame['Longitude']) 
Y = np.array(frame['Latitude']) 

# <markdowncell>

# - Number of valid longitudes

# <codecell>

in_X = X[(X > -180) & (X < 180)]
len(in_X)

# <markdowncell>

# - Number of valid latitudes

# <codecell>

in_Y = Y[(Y > -90) & (Y < 90)]
len(in_Y)

# <markdowncell>

# - Difference between valid longs and lats

# <codecell>

diffs = len(in_X)-len(in_Y)
diffs

# <codecell>

out_X = np.array(frame['Longitude']) 
out_Y = np.array(frame['Latitude']) 

# <markdowncell>

# - # of longitudes out-of-range (<-181 or >181)

# <codecell>

out_X = out_X[(out_X < -181) | (out_X > 181)]
len(out_X)

# <markdowncell>

# - # of latitudes out-of-range (<-91 or > 91)

# <codecell>

out_Y = out_Y[(out_Y < -91) | (out_Y > 91)]
len(out_Y)

# <markdowncell>

# ## Distribution of Longitudes (X) and Latitudes (Y)

# <codecell>

%load_ext rmagic 

# <codecell>

%%R -i in_X,in_Y
hist(in_X,breaks = 8)

# <codecell>

%%R 
hist(in_Y,breaks = 8)

