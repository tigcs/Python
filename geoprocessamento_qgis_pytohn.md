# Realizando análises no console Python do QGIS

##### Importa toda biblioteca de ferramentas disponível associada à instalação do QGIS.
```programming
>>> import processing
```
##### Lista todas as ferramentas(algoritmos) disponíveis.
```programming
>>> processing.alglist()
```
##### Lista todas as ferramentas(algoritmos) disponíveis que tenham uma string ou parte dela. A segunda coluna da lista fornece o nome da linha de comando da função.
```programming
>>> processing.alglist("clip")
Clip------------------------------------------------->qgis:clip
Clip Data-------------------------------------------->lidartools:clipdata
Poly Clip Data--------------------------------------->lidartools:polyclipdata
lasclip---------------------------------------------->lidartools:lasclip
Clip points with polygons---------------------------->saga:clippointswithpolygons
Clip raster with polygon----------------------------->saga:clipgridwithpolygon
Clip raster by extent-------------------------------->gdalogr:cliprasterbyextent
Clip raster by mask layer---------------------------->gdalogr:cliprasterbymasklayer
Clip vectors by extent------------------------------->gdalogr:clipvectorsbyextent
Clip vectors by polygon------------------------------>gdalogr:clipvectorsbypolygon
```
