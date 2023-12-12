###
<img src="bitsei-db2-logo.png" width="220" alt="BITSEI Logo"/>


# BITSEI - Graph Databases Course - Prof. Gianmaria Silvello
### University of Padova - A.A. 2023-24
---

## Objective
The objective of this repository is to propose an ontology that can effectively handle socio-economic information about the population of Los Angeles, specifically focusing on the years of CoVid pandemic (2020-2022). The proposed system aims to model:
- The data associated with the pandemic spread and growth;
- The data associated with the businesses opened and closed;
- The data associated with the criminal activities registered during our period of interest.

To accomplish this, we leverage on four comprehensive datasets:
1. [Dataset Name](link): insert description 
2. [Dataset Name](link): insert description
3. [Dataset Name](link): insert description
4. [Dataset Name](link): insert description
allowing us to capture and reflect the impact of pandemic and restrictions on the population.

This repository is developed for the [Database II](https://iiia.dei.unipd.it/education/database-2/) course.

---

## Group Members
BITSEI (graph-Based InformaTion SystEms for Insights analysis) Group

| Surname         | Name         | ID        |
| --------------- | ------------ | --------- |
| Boscolo Cegion  | Nicola       | 2074285   |
| Cazzaro         | Mirco        | 2076745   |
| Martinelli      | Marco        | 2087646   |
| Shami           | Farzad       | 2090160   |

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
For (insert reasons) various reasons, some data have been imported directly in the ontology, using the [Cellfie](https://github.com/protegeproject/cellfie-plugin) plugin.
#### Phase 4: Validation
Once all the turtle files associated to the serialization have been generated, they have been uploaded to a server ...
Here insert some funny things to flex how much we are good since we installed and runned graphdb on a shared server.
Before proceeding with querying the database, a validation phase on data properties has been conducted using [SHACL](https://www.w3.org/TR/shacl/).
#### Phase 5: Querying
Once the database has been validated and is correctly running on the server, we selected 10 insightful queries (here give some motivations for why these are relevant, how we decided to pick these)
1. Query1: retrieve the ... with this query we want to understand/see ...
2. Query2
3. Query3
4. Query4
5. Query5
6. Query6
7. Query7
8. Query8
9. Query9

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
├── 📄 loadSoccerData.ipynb<br/>
├── 📄 newREADME.md<br/>
├── 📄 README.md<br/>
├── 📁 datasets<br/>
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
├── 📁 ontology<br/>
│   ├── 📄 Bitsei_ontology.drawio<br/>
│   ├── 📄 Bitsei_ontology.svg<br/>
│   └── 📁 requirements analysis<br/>
│       └── 📄 link_to_requirements_analysis.txt<br/>
├── 📁 queries<br/>
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
├── 📁 scripts<br/>
│   ├── 📄 loacation_process.ipynb<br/>
│   ├── 📄 README.md<br/>
│   └── 📄 requirements.txt<br/>
├── 📁 serialization<br/>
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
├── 📁 validation<br/>
│   └── 📄 validateDataProperties.txt<br/>
└── 📁 webapp<br/>
    └── ⤵️<br/>

---

## Ontology Diagram


<img src="ontology/Bitsei_ontology.svg" alt="Ontology Diagram" style="height: 100px; width:100px;"/>

Describe the ontology diagram (if needed)

Note: The image provided above displays the class diagram for reference.

## System Hardware

Here do we want to describe the server in which the database is running?
### Machine 1:
- CPU: Intel centrino
- GPU: NVIDIA schiacciasassi
- RAM: 1GB if needed
- SSD: a floppy disk
---

## How to Run and Use the Codes
TODO
Before any attempt, make sure you have the **collection** and **topics** files available in your system. If you want to use the query expansion, put your open-api key in the python script and run it. The script will create a file named "result.json" which will be used by the searcher. If you want to use the Re-ranking method, you should run it on a system that supports `pytorch cuda` version. Please note that it is not supported on the `macOS system with Apple Silicon chip`. Pass the [sbert](https://huggingface.co/sentence-transformers) model to the searcher. If your model exists in `dl4j`, it will automatically download it. Otherwise, you should download it, convert it to `torch-script`, and put it somewhere, using the path in the `re-ranker` class.

### Running using CLI
We provide here in the folder `final_jar_executable` a jar executable version of our program that automatically creates its own working environment and changes the parameters based on your needs in `CloseSearchEngine.java`. To run it, follow these steps:

1. Open the command line and change directory to where the project folder is located.
2. Build the project by running the `mvn clean install` command.
3. Run the following command, passing the correct parameters:
```
java -jar close-1.00-jar-with-dependencies.jar <collection path> <topic path> <index path>
```

---

*Database II* is a course of the

* [Master Degree in Computer Engineering](https://degrees.dei.unipd.it/master-degrees/computer-engineering/) of the [Department of Information Engineering](https://www.dei.unipd.it/en/), [University of Padua](https://www.unipd.it/en/), Italy.
* [Master Degree in Data Science](https://datascience.math.unipd.it/) of the [Department of Mathematics "Tullio Levi-Civita"](https://www.math.unipd.it/en/), [University of Padua](https://www.unipd.it/en/), Italy.

*Database II* is part of the teaching activities of the [Intelligent Interactive Information Access (IIIA) Hub](http://iiia.dei.unipd.it/).

---

### License

All the contents of this repository are shared using the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

![CC logo](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)