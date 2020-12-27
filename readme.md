# What's inside? 

*   An ETL pipeline  using ESIOS data.(documentation: https://api.esios.ree.es/).
        * Extraction of the hourly power demand forecast of the Spanish power market (Previsión diaria de la demanda
eléctrica peninsular) , transformation via pandas and loading to an sql database    
        * The data is accessed via the public API of ESIOS (documentation: https://api.esios.ree.es/).

*   Time & memory optimization of functions dataframe loadinng

## Files
The repo contains:
* 4 folders 
    *  Data: contains the data source
    *  Scripts: optimization and etl python scripts
    *  Output: contains the Anas_etl.csv file
    *  Screeshots: some screenshots 
* 4 files
   *   README.md
   *   2 Jupyter notebook files describing the step by step programming

## version used

*   Python version: 3.8.3 
*   Panda version 1.0.5
*   Numpy version 1.18.5

## Demo 

*   Set up your environment & sql server
*   Run the ETL-iberian-power-consumption.py

```
python ETL-iberian-power-consumption.py
```
*   Run the Code_optimization.py

```
python Code_optimization.py
```


## Authors

* **Anass Khaldi** 


