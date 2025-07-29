# design_pattern

- ref: https://wikidocs.net/252293
## Structural Pattern
### Singleton pattern
- use when only instance is required for various reasons include efficiency, protection, security and such.
#### singletone meta pattern 
- the template of the singleton pattern

### Composite pattern
- a way to build a tree-like structure

### Flyweight pattern
- divided into intrinsic (common) and extrinsic states (unique to each flyweight)
- by sharing the common intrinsic states, it can increase memory efficiency

## Behavior Pattern
### Mediator pattern
- This pattern is similar to the observer pattern in a sense that the registered components will recieve notifications upon triggering.
- The key difference to the observer pattern is that the observer itself triggers notification events.
- In the mediator pattern, the component triggers the event becasue mediator contains some logic where who triggers who. 
