Fuzzy multi-criteria decision making
-------------------------------------

Simple tool for fuzzy multi-criteria decision making with use of fuzzy preference structures (FPS).

**FuzPrefStruct**
  The class represents a **(s, phi)-FPS** with phi being the identity automorphism and s={0,1, 'inf'}. When initating a structure one must provide:
    - numpy array R (representing matrix of large preference relation) 
    - a value of s (if other than {0,1,'inf'} then s=0 is set as default). The structure has Parray, Iarray and Jarray that corresponds respectively to strict preference, indifference and incomparability fuzzy relations. 

**solve(A, R, method=1, s=0)** 
  Solve function for a given set of alternatives A and R vector of large preference relations returns: set of optimal decisions, fuzzy set of non-dominated alternatives and its type. Decision maker may choose one of two option:
    - method=1 , "aggregation, scoring" approach
    - method=2 , "scoring, aggregation" approach
    
The mathematical apparatus used for the implementation is available in /docs.
