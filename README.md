# Animal Rescue Dashboard

## Project Overview
This project delivers a full-stack web application for Grazioso Salvare, a company that trains rescue dogs for specialized missions. 
With over 10,000 animals in the Austin Animal Center database, manually finding correct rescue candidates takes too long. Different 
rescue operations need different breeds.

The interface has four radio button options. Reset shows all 10,000 dogs. Water Rescue filters are added for Labrador Retriever Mix, 
Chesapeake Bay Retriever, and Newfoundland breeds, specifically intact females between 26 and 156 weeks old. Mountain/Wilderness Rescue 
identifies German Shepherds, Alaskan Malamutes, Old English Sheepdogs, Siberian Huskies, and Rottweilers that are intact males in the 
same age range. Disaster Tracking is a broader category with breeds like Doberman Pinschers, German Shepherds, Golden Retrievers, 
Bloodhounds, and Rottweilers, allowing an age range from 20 to 300 weeks.

## Tools

### MongoDB
MongoDB handles the data layer because shelter records don't always fit neatly into certain table structures. Some animals have 
vaccination histories and microchip IDs; others don't. Traditional relational databases make you create columns for every possible 
field, possibly leaving empty cells throughout. MongoDB's document model lets each record contain exactly what it needs.

### Python and PyMongo
Python provides the backend logic through MongoDB's official driver, PyMongo. The project's custom CRUD module, the AnimalShelter 
class wraps all database operations. The dashboard never writes MongoDB queries directly. It calls methods like 
`shelter.filter_water_rescue()` and gets back query dictionaries. This means the database logic can be tested independently and reused
in other projects.

### Dash
Dash enforces clean architecture. The `app.layout` defines what users see (View). Callback functions handle interactions and coordinate
updates (Controller). The CRUD module manages all data operations (Model). Quality visualizations come built-in through Plotly charts
and Dash Leaflet maps.


## Development
Development started with confirming MongoDB was running and the Austin Animal Center data was loaded. Initial queries in the 
MongoDB shell display the data structure and field names. Next, Radio buttons went into the layout, then the callback connecting 
filter selection to data updates. Once basic filtering worked, the map integration was added using Dash Leaflet. The breed chart 
came last, requiring dataset aggregation and Plotly pie chart generation. The logo loaded as a base64-encoded image with a link 
to www.snhu.edu.

## Challenges
Standard `localhost:8051` didn't work in Codio's cloud environment. The console confirmed the app was running, but browser access 
continued to fail. Codio's documentation showed their URL routing uses `https://coolmambo-waterigor-8051.codio.io`.

---

## Reflection

### Writing Maintainable Code
The CRUD module from Project One shows how separating concerns makes code reusable. The dashboard calls `filter_water_rescue()` 
without knowing anything about MongoDB syntax. This means I can drop the same CRUD module into a command-line tool, a different
web framework, or any other project that needs to talk to this database. \

### Approaching Problems
I broke this project into layers: MongoDB for storage, the CRUD module for queries, and Dash for the interface. Building 
CRUD first and testing each filter meant catching issues early instead of debugging everything at 
once.

### Why This Matters
Grazioso Salvare was spending hours manually querying rescue candidates. Now they can click a button and get results instantly.
Faster candidate identification means more dogs get trained, which means more effective rescue operations. 
