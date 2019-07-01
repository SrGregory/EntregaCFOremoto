# EntregaCFOremoto

In the next repository you will find a Django RESTFUL api which takes some indicators from "miindicador.cl" and saves it on the db, then it serialize the data and offer a display of the historical data of the indicators (uf or dolar), it suposed to have a functionality that makes the user search for an especific date, value and currency but its not finished yet.

In the proyect folder, you are gona find a folder called "loaders", these python files are the one used to backup the data from the api to our own db, to use them you have to:
1) open python shell
2) import loaders ej: from indicator.loaders import uf_loader
3) all of the loaders have a run function, so after you called the loader you have to type "uf_loader.run()"
4) sit and relax, the process might take a while (more than 1300 intances per object)

after the data is loaded into our database we can run the server and go to:
localhost:8000/indicatr/uf or localhost:8000/indicatr/dolar to watch a list of the needed indicator.

pd: the search functionality seems to be easy to crack, just a bit more search
