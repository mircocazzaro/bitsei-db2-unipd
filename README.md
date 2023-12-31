###
<img src="bitsei-db2-logo.png" width="220" alt="BITSEI Logo"/>


## BITSEI - Graph Databases Course - Prof. Gianmaria Silvello
### University of Padova - A.A. 2023-24
---

## Objective
The objective of this repository is to propose an ontology that can effectively handle socio-economic information about the population of Los Angeles, specifically focusing on the years of CoVid pandemic (2020-2022). The proposed system aims to model:
- The data associated with the pandemic spread and growth;
- The data associated with the businesses opened and closed;
- The data associated with the criminal activities registered during our period of interest.

Data have been modelled in a way they can be filtered both by date and by location.

This repository is developed for the [Database II](https://iiia.dei.unipd.it/education/database-2/) course.

## Group Members
BITSEI (graph-Based InformaTion SystEms for Insights analysis) Group

| Surname         | Name         | ID        |
| --------------- | ------------ | --------- |
| Boscolo Cegion  | Nicola       | 2074285   |
| Cazzaro         | Mirco        | 2076745   |
| Martinelli      | Marco        | 2087646   |
| Shami           | Farzad       | 2090160   |

---

## Datasets Overview
To accomplish this, we leverage on four comprehensive datasets, allowing us to capture and reflect the impact of pandemic and restrictions on the population:
#### 1. [LA County COVID Cases](https://catalog.data.gov/dataset/la-county-covid-cases): 
reporting COVID cases and deaths for LA County and California State. For each day, from 2020 to 2022, the dataset provides information about:
* confirmed cases: the number of confirmed CoVid cases cumulative, from the start of the pandemic to the current day;
* active cases: the number of active CoVid cases of the day;
* deaths: the number of CoVid deaths cumulative, from the start of the pandemic to the current day.     

Taking advantage from these, we were able to create and populate, for each day in the timeline, the following fields:
* new cases: the number of new covid cases of the day d (activeCases(d)-activeCases(d-1)).
* new deaths: the number of new deaths cases of the day d (deaths(d)-deaths(d-1)).

In addition, by searching various newspapers, we were able to create a subdivision in period of the CoVid timeline. Specifically, a *CoVid Periods* dataset has been created, having the following fields:
* period name: the label used to refer to a certain period (e.g. 'First Lockdown Period');
* start date: the date in which the period starts;
* end date: the date in which the period ends.

#### 2. [LA County Active Businesses](https://catalog.data.gov/dataset/listing-of-active-businesses): 
reporting all the active businesses registered with the Office of Finance. An "active" business is defined as a registered business whose owner HAS NOT notified the Office of Finance of a cease of business operations. For each business opened in between 2020 and 2022, the dataset provides information about:
* business name: the name of the business and, eventually, the DBA (Doing Business As) alias;
* address: street address, city, and zip code where the business is located;
* location: geographical coordinates (lat, lon) where the business is located;
* opening date: the date in which the business has been opened;
* NAICS code and description: the North American Industry Classification System code provides ;information about the business typology. 

#### 3. [La County Closed Businesses](https://data.lacity.org/Administration-Finance/All-Closed-Businesses/tkh9-tssh): 
reporting all the closed businesses registered with the Office of Finance. A "closed" business is defined as a registered business whose owner HAS notified the Office of Finance of a cease of business operations. The dataset provides the same information as the one referring to active businesses, the only difference is the trivial presence of the "closing date" field.

Using the columns about NAICS from both the businesses datasets, we were able to create the *NAICS Codes and Descriptions* dataset, a simple dataset which maps uniquely all the different NAICS codes to their descriptions.

#### 4. [La County Crime Events](https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8): 
reporting incidents of crime in the City of Los Angeles dating back to 2020. For each crime event, the dataset provides information about:
* occurred and reported date: the dates in which the crime event has occurred and has been reported;
* location: geographical coordinates (lat, lon) and area in which the crime event occurred;
* crime typology: which type of crime has happened (e.g. burglary, assault);
* victim: age, sex, and descent of the victim of the crime event;
* premise: the premise in which the crime event occurred;
* weapon: the weapon used in the crime event;

Using the column about crime typology, we were able to create the *Crime Codes and Descriptions* dataset, a simple dataset which maps uniquely all the different crime codes to their descriptions.

In the same way, we generated the *Weapon Codes and Descriptions* dataset, for weapon codes and descriptions.

In addition, we also created the *Community Planning Areas* dataset, which contains geometries of the various Los Angeles Planning Areas. More information about this can be found in the [script](https://github.com/mircocazzaro/bitsei-db2-unipd/tree/main/scripts) folder.
---

## Project Description
Our development strategy followed a 5 phases approach:

#### Phase 1: Requirements Analysis
In that phase we wanted to:
- determine the scope of the ontology
- see if it was possible to reuse other ontologies
- enumerate important terms in the ontology
- define the classes and class hierarchy
- define the properties of the classes   

#### Phase 2: Ontology Design
For designing the ontology, we used [PROTÉGÉ](https://protege.stanford.edu/).
However, before starting the actual implementation, the overall ontology design has been drawn based on the requirements analysis. For doing that we used [draw.io](https://drawio-app.com/).
By studying the various fields in the datasets we decided what they would have been the classes, the object and data properties, and the individuals.

#### Phase 3: Serialization
For serializing the data we used [Python RDFlib](https://rdflib.readthedocs.io/en/stable/).
For various reasons, some data have been imported directly in the ontology, using the [Cellfie](https://github.com/protegeproject/cellfie-plugin) plugin.
In particular:
- All datasets related to businesses, covid updates over days and georeferenced information about positions, cities and areas have been serialized through the [`serializeLAdata.py`](https://github.com/mircocazzaro/bitsei-db2-unipd/blob/main/serialization/serializeLAdata.ipynb) notebook, using RDFLib;
- All datasets related to crimes, including related data of premises, weapons, victims, ecc... have been serialized through the [`serializeLAcrimes.py`](https://github.com/mircocazzaro/bitsei-db2-unipd/blob/main/serialization/serializeLAcrimes.ipynb) notebook, using [RDFLib](https://rdflib.readthedocs.io/en/stable/);
- Data related to crime categories and covid periods have been serialized through [Cellfie](https://github.com/protegeproject/cellfie-plugin), so to have the individuals in [Protégé](https://protege.stanford.edu/) and being able to write first order logic rules.

#### Phase 4: Validation
Once all the turtle files associated to the serialization have been generated, they have been uploaded to a shared server, allowing us for a better cooperation.  
Before proceeding with querying the database, a validation phase on object and data properties has been conducted using [SHACL](https://www.w3.org/TR/shacl/).

#### Phase 5: Querying
Once the database has been validated and is correctly running on the server, we selected 10 insightful queries. These queries were selected based on their direct relevance to identifying temporal, spatial, and categorical trends within our dataset, crucial for finding patterns in business operations, mortality rates, crime occurrences, and the impact of restrictions on various events:
1. Query 1: retrieve the number of `opened businesses`, `closed businesses`, `deaths` and `crime events`, grouped by `months` (over the 3 years);
2. Query 2: retrieve the ratios of `opened businesses`, `closed businesses`, `deaths` and `crime events`, grouped by different `restriction periods` (ratio is computed over the duration in days of the periods);
3. Query 3: retrieve the ratios of `opened businesses`, `closed businesses`, `deaths`, and of all the typologies of `crime events`, grouped by city area (ratio is computed over the surface in kmq of the areas);
4. Query 4: retrieve the number of `opened businesses`, `closed businesses`, `deaths` and `crime events`, grouped by the North America Industry Classification System;
5. Query 5: retrieve the distribution, over different `areas` and `periods` of the different typologies of `crime events`;  
6. Query 6: retrieve the distribution of the crime events' `modus operandi` over different `restriction periods`;
7. Query 7: retrieve the distribution of the crime events' `premise` over different `restriction periods`;
8. Query 8: retrieve the distribution of the crime events' `weapon` over different `restriction periods`;
9. Query 9: retrieve the number of `crime events`, for each `day` and for each `area`;
10. Query 10: retrieve the location of `crime events`, for each `day`.
---

## Organization of the Repository
The project is developed using:
- [draw.io](https://drawio-app.com/) for drawing the ontology model.
- [PROTÉGÉ](https://protege.stanford.edu/) for implementing the ontology model.
- [Cellfie](https://github.com/protegeproject/cellfie-plugin) plugin.
- [Python RDFlib](https://rdflib.readthedocs.io/en/stable/) for serializing the data.
- [SHACL](https://www.w3.org/TR/shacl/) for validating the data.
- [GraphDB](https://www.ontotext.com/products/graphdb/) for querying the data.

The overall structure of the repository is as follows:

📁 bitsei-db2-unipd<br/>
├── 📄 .gitattributes<br/>
├── 📄 .gitignore<br/>
├── 📄 bitsei-db2-logo.png<br/>
├── 📄 LICENSE<br/>
├── 📄 README.md<br/>
├── 📁 datasets: a folder containing all the datasets used in serialization<br/>
│   ├── 📁 ACTIVE BUSINESSES<br/>
│   │   ├── 📄 fixed-Listing_of_Active_Businesses_parsed.csv<br/>
│   │   └── 📁 misc<br/>
│   │       ├── 📄 active_businesses_parser.py<br/>
│   │       └── 📄 Listing_of_Active_Businesses_parsed.csv<br/>
│   ├── 📁 CLOSED BUSINESSES<br/>
│   │   └── ⤵️<br/>
│   ├── 📁 COVID DATA<br/>
│   │   └── ⤵️<br/>
│   ├── 📁 COVID TIMELINE<br/>
│   │   ├── 📄 covid_periods.csv<br/>
│   │   └── 📁 misc<br/>
│   │       ├── 📄 Timeline The Coronavirus Pandemic in California – NBC Los Angeles.csv<br/>
│   │       └── 📄 Timeline The Coronavirus Pandemic in California – NBC Los Angeles.pdf<br/>
│   ├── 📁 CRIME DATA<br/>
│   │   └── ⤵️<br/>
│   ├── 📁 LOS ANGELES GEO DATA<br/>
│   │   └── ⤵️<br/>
├── 📁 ontology: a folder containing the ontology model design and implementation<br/>
│   ├── 📄 Bitsei_ontology.drawio<br/>
│   ├── 📄 Bitsei_ontology.svg<br/>
│   └── 📁 requirements analysis<br/>
│       └── 📄 link_to_requirements_analysis.txt<br/>
├── 📁 queries: a folder containing the selected queries and associated outputs<br/>
│   ├── 📄 BitseiQueries.ipynb<br/>
│   ├── 📁 1<br/>
│   │   └── ⤵️<br/>
│   ├── 📁 2<br/>
│   │   └── ⤵️<br/>
│   ├── 📁 3<br/>
│   │   └── ⤵️<br/>
│   ├── 📁 4<br/>
│   │   └── ⤵️<br/>
│   ├── 📁 5<br/>
│   │   └── ⤵️<br/>
│   ├── 📁 6<br/>
│   │   └── ⤵️<br/>
│   ├── 📁 7<br/>
│   │   └── ⤵️<br/>
│   ├── 📁 8<br/>
│   │   └── ⤵️<br/>
│   └── 📁 9-10<br/>
│       └── ⤵️<br/>
├── 📁 scripts: a folder containing the scripts used to produce the *Community Planning Areas* dataset<br/>
│   ├── 📄 loacation_process.ipynb<br/>
│   ├── 📄 README.md<br/>
│   └── 📄 requirements.txt<br/>
├── 📁 serialization: a folder containing the Python scripts used in serialization and the turtle files produced with these<br/>
│   ├── 📄 areas.ttl<br/>
│   ├── 📄 BitseiQueries.ipynb<br/>
│   ├── 📄 businesses.ttl<br/>
│   ├── 📄 cities.ttl<br/>
│   ├── 📄 covidDays.ttl<br/>
│   ├── 📄 crimeCrimeEvents.ttl<br/>
│   ├── 📄 crimeCrimesTypology.ttl<br/>
│   ├── 📄 crimeModusOperandi.ttl<br/>
│   ├── 📄 crimePremis.ttl<br/>
│   ├── 📄 crimeVictims.ttl<br/>
│   ├── 📄 crimeWeapons.ttl<br/>
│   ├── 📄 locations.ttl<br/>
│   ├── 📄 naics.ttl<br/>
│   ├── 📄 serializeLAcrimes.ipynb<br/>
│   └── 📄 serializeLAdata.ipynb<br/>
├── 📁 validation: a folder containing the SHACL script for validating data<br/>
│   └── 📄 validateDataProperties.txt<br/>
└── 📁 webapp: a folder containing our web application<br/>
    └── ⤵️<br/>

---

## Ontology Diagram


<img src="ontology/Bitsei_ontology.svg" alt="Ontology Diagram"/>

The image provided above displays the class diagram for reference. The most relevant entities for our purposes are highlighted in purple.

## System Hardware & Software

We worked together in a shared environment: in particular, we instantiated a platform independent instance of GraphDB and we uploaded there all our RDF data.
### VPS:
- CPU: Intel(R) Xeon(R) CPU E5-2697 v2 @ 2.70GHz (1 vCore)
- RAM: 4GB
- SSD disk
- OS: CentOS 7
- GraphDB: ver. 10.4.2

GraphDB is executed through the command `./graphdb -Ddefault.min.distinct.threshold=1024m -d`

---

## Output of the project

### Queries and Python SPARQLWrapper Notebook:

As stated before, we carried out 10 insightful queries over our graph database. You will find 10 subfolders into the `queries` folder: inside each of them there are the outputs (in csv format) and the plots related to each of them. For each of the 10 queries, there might be different versions, just selecting different data properties. The actual SPARQL queries are instead available on the python notebook `queries/BitseiQueries.ipynb`. While looking at our notebook, you can actually run our queries on our remote server!

N.B. For security reasons, IP's are filtered on the remote server. Please make sure you are connecting from any of the buildings of the University of Padova (The IP class `147.162.0.0\16` is allowed to connect).

### Webapp:

For presenting our webapp, we also carried out a simple web application capable of running our queries, and showing them by means of plots (using `Chart.js` library).
For running the webapp, you can follow the instructions in the `webapp` folder.
These instructions are available in the `webapp/README.md` file.


---

*Database II* is a course of the

* [Master Degree in Computer Engineering](https://degrees.dei.unipd.it/master-degrees/computer-engineering/) of the [Department of Information Engineering](https://www.dei.unipd.it/en/), [University of Padua](https://www.unipd.it/en/), Italy.
* [Master Degree in Data Science](https://datascience.math.unipd.it/) of the [Department of Mathematics "Tullio Levi-Civita"](https://www.math.unipd.it/en/), [University of Padua](https://www.unipd.it/en/), Italy.

*Database II* is part of the teaching activities of the [Intelligent Interactive Information Access (IIIA) Hub](http://iiia.dei.unipd.it/).

---

## License

All the contents of this repository are shared using the [GNU GENERAL PUBLIC LICENSE - VER. 3](https://www.gnu.org/licenses/gpl-3.0.html)