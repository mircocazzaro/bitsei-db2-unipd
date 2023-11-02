###
<img src="bitsei-db2-logo.png" width="220" alt="BITSEI Logo"/>


## BITSEI - Graph Databases Course - Prof. Gianmaria Silvello
#### University of Padova - A.A. 2023-24
---
## Getting Started

### 1: What is the domain that the ontology will cover?
We want to model some socio-economical information about the population of Los Angeles during the years of CoVid pandemic, with particular focus on the years 2020-21.
In detail, we want to model:
- The data associated with the pandemic spread and growth;
- The data associated with the businesses opened and closed;
- The data associated with the criminal activities registered during our period of interest.

### 2: For what are we going to use the ontology?
We want to keep track and get information about what happened during a specific day and/or period of time (e.g. month, trimester, semester), keeping track of the events that happened and if these are (eventually) related to each other.

### 3: For what types of questions the information in the ontology should provide answers?
- (CoVid) how many active cases there were on day x
- (CoVid) how many active cases there were on period x-y
- (CoVid) how many new cases there were on period x-y
- (CoVid) in period x-y the pandemic trend was increasing/decreasing
- (Businesses) how many opened/closed businesses there were on day x
- (Businesses) how many opened/closed businesses there were on period x-y
- (Businesses) how many opened/closed businesses of typology t there were on period x-y
- (Businesses) how many opened/closed businesses there were on day x in Zone z
- (Businesses) how many opened/closed businesses there were in period x-y  in Zone z
- (Crimes) how many crimes happened during period x-y in Zone z
- (Crimes) what is the percentage of crimes having typology t in period x-y (in Zone z)
- (Crimes) what are the most frequent weapons used for committing crimes t 
- (Crimes) what are the typologies t1, t2… of crimes that take more time to be reported
- (Crimes) what is the most common period of the day (hour) in which a crime t tends to happen
- (Crimes) what is the most common typology t of crime that tends to happen during the night, from 01:00 to 04:00 AM


### 5: Which technologies are involved?
- For designing the ontology: [PROTÉGÉ](https://protege.stanford.edu/)
- For serializing the data: [Python RDFlib](https://rdflib.readthedocs.io/en/stable/)
- For querying the data: [GraphDB](https://www.ontotext.com/products/graphdb/) 

---
### Contributors
- Mirco Cazzaro - 2076745
- Nicola Boscolo Cegion - 2074285
- Marco Martinelli - 2087646
- Farzad Shami - 2090160

<p><em>Database 2 course of <a href="http://www.unipd.it">University of Padova </a></em>
