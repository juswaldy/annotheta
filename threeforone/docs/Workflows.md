# Workflows



## 1. Upload

```mermaid
stateDiagram-v2
	[*] --> Authenticated: Login (User)
	NewFile --> ExistingFile: Save (System)
	Authenticated --> NewFile: Upload (User)
	Authenticated --> Displayed: Display (User)
	Displayed --> ExistingFile: Choose (User)
	NewFile --> FeatureStored: Process (System)
	ExistingFile --> FeatureStored: Retrieve (System)
	FeatureStored --> Displayed: Display (System)
	Displayed --> [*]
```

Random Notes:

Interaction with user is very important. Introduce features and get easy feedback 3 times (Like or Not). At the 4th time, text box for comments and suggestions.

Feature: histogram of image. Maybe tasks for similar histograms will be similar as well? Night, mostly dark, mostly grass, etc.



## 2. Choose

```mermaid
stateDiagram-v2
	[*] --> ExistingFile: Choose (User)
	ExistingFile --> FeatureRetrieved: Retrieve (System)
	FeatureRetrieved --> Displayed: Display (System)
	Displayed --> Displayed: Hover (User)
	Displayed --> PolygonPoints: Click Box (User)
	Displayed --> NewObject: Draw Box (User)
	NewObject --> FeatureStored: Click Send (User)
	FeatureStored --> PolygonPoints
	FeatureStored --> FeatureRetrieved: Update (System)
	PolygonPoints --> [*]
```

## 3. Segment

```mermaid
stateDiagram-v2
	[*] --> PolygonPoints
	PolygonPoints --> PolygonUpdated: Move Point (User)
	PolygonUpdated --> PolygonPoints: Redraw Polygon (System)
	PolygonPoints --> FeatureStored: Save (User)
	FeatureStored --> [*]
```



# Older Stuff



## 1. Upload (Old)

```mermaid
graph LR
	User
	Frontend
	API
	Backend
	User -- 1. Upload<br>Image --> Frontend
	Frontend -- 2. Upload<br>File --> API
	API -- 3. Save<br>File --> Filesystem
	API -- 4. Get<br>Metadata --> Backend
	Filesystem -- 5. Read and<br> Process--> Backend
	Backend -- 6. Mapping <Filename, GUID><br/> + Metadata <bboxes, polygons>--> API
	API -- 7. GUID<br>+ Metadata --> Frontend
```

```mermaid
sequenceDiagram
	User ->> Frontend: Upload
	Frontend ->> API: Upload
    API ->> Filesystem: Save
    Filesystem -->> API: Status
	API ->> Backend: Process
	Backend ->> Filesystem: Read File	
	Backend -->> API: GUID + Metadata
	API -->> Frontend: 
	Frontend -->> User: Done
```



## 2. BBox (Old)

```mermaid
sequenceDiagram
	User ->> Frontend: BBox
	Frontend ->> API: GUID, BBox
    API ->> Backend: GUID, BBox
    Backend ->> Backend: Find Features for GUID
    loop if features not found
    Backend ->> Filesystem: Read File
    end
    Backend -->> API: GUID, BBox, Polygon
	API -->> Frontend:  
	Frontend -->> User: Done
```

