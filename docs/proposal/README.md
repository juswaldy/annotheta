# annotheta



### Small Picture

```mermaid
graph LR
	User --> Frontend --> Backend --> Jose --> Frontend
```



### The Backend

```mermaid
graph LR
	subgraph Backend
        Feature(Feature<br>Store)
        Trainer(Model<br>Trainer)
        Analyzer(Model<br>Analyzer)
        Runner(Inference<br>Runner)
        Model(Trained<br>Model)
    end
    API(API)

	Frontend --> API --> Frontend
    Feature --> Trainer --> Model --> Runner --> API
    API --> Feature
    Trainer --> Analyzer
    Model --> Analyzer
    Feature --> Runner
    
    classDef mix fill:#89ef89
    classDef prod fill:#8989ef
    class Feature,Analyzer mix
	class Trainer,Model,Runner prod
```

```mermaid
graph
	prod(Production)
	mix(Both P & D)
	dev(Development)
    classDef prod fill:#8989ef
	classDef dev fill:#ef8989
	classDef mix fill:#89ef89
    class prod prod
	class dev dev
	class mix mix
```



### Bigger Picture

```mermaid
graph LR
	Feature(Feature<br>Store)
	Incubator(Model<br>Incubator)
    Trainer(Model<br>Trainer)
    Analyzer(Model<br>Analyzer)
    Repo(Code<br>Repo)
    Deployer(Code<br>Deployer)
    Runner(Inference<br>Runner)
    Model(Trained<br>Model)
	Monitor(Performance<br>& Anomaly<br>Monitor)
    
    Feature --> Trainer --> Model --> Runner
	Feature --> Incubator --> Repo --> Deployer --> Trainer
    Trainer --> Analyzer
    Model --> Analyzer
    Analyzer --> Incubator
	Runner --> Monitor --> Incubator

    classDef prod fill:#8989ef
	classDef dev fill:#ef8989
	classDef mix fill:#89ef89
    class Trainer,Model,Runner,Monitor prod
	class Incubator dev
	class Feature,Analyzer mix
```



### The Incubator vs the Trainer

The Incubator and the Trainer are alike. The Incubator produces the "baby." The Trainer produces the "athlete." The difference is in the output. The "baby" source code is passed on to the Trainer who trains the model to "lift weights." The end result of this process is learned weights.

```mermaid
graph LR
    Feature(Feature<br>Store)
    Source(Source<br>Code)
	subgraph Model Incubator
        Extractor(Data<br>Extractor)
        Analyzer(Data<br>Analyzer)
        Validator(Data<br>Validator)
        Cleaner(Data<br>Cleaner)
        Trainer(Model<br>Trainer)
        Evaluator(Model<br>Evaluator)
	end

	Feature --> Extractor --> Analyzer --> Validator --> Cleaner --> Trainer --> Evaluator --> Source
	Evaluator --> Trainer
	Evaluator --> Cleaner
	Evaluator --> Validator
	Evaluator --> Analyzer

	classDef mix fill:#89ef89
	class Source mix
```

```mermaid
graph LR
    Feature(Feature<br>Store)
    Model(Trained<br>Model)
	subgraph Model Trainer
        Extractor(Data<br>Extractor)
        Analyzer(Data<br>Analyzer)
        Validator(Data<br>Validator)
        Cleaner(Data<br>Cleaner)
        Trainer(Model<br>Trainer)
        Evaluator(Model<br>Evaluator)
	end

	Feature --> Extractor --> Analyzer --> Validator --> Cleaner --> Trainer --> Evaluator --> Model
	Evaluator --> Trainer
	Evaluator --> Cleaner
	Evaluator --> Validator
	Evaluator --> Analyzer

    classDef prod fill:#8989ef
    class Model prod
```





## Background

Background and Significance of Project.



## Related Work

(Papers, github)



## Datasets

ADE20K

Cityscapes



## Processes and Methods





## Outcomes



Possible usage: run against segmentation datasets like ADE20K, Cityscapes, and score. In cases where our model is better, re-evaluate dataset. https://arxiv.org/pdf/2103.14749.pdf

Why not generate scenes together with segementations? Or generate the masks first and then fill up?

50 images: should go to 150 or stay 50? make existing data better, or make it easier to get more data? Then parameter could be: metric wish. e.g. accuracy=60% etc



## System Design and Ethical Considerations

Language:

- vim-like, with 4 modes: Normal, Command, Insert, Visual
- https://yanpritzker.com/learn-to-speak-vim-verbs-nouns-and-modifiers-d7bfed1f6b2d
- https://stackoverflow.com/questions/1218390/what-is-your-most-productive-shortcut-with-vim/1220118#1220118
- https://dev.to/iggredible/mastering-vim-grammar-1dfi
- https://benmccormick.org/2014/07/02/learning-vim-in-2014-vim-as-language



Ethics:

- Mouse and keyboard vs tablet and stylus? cheap labor with cheap equipment?



## Future work and Timeplan

