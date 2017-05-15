# Realizando análises no console Python do QGIS

##### 1 - Importa toda biblioteca de ferramentas disponível associada à instalação do QGIS.
```programming
>>> import processing
```
##### 2 - Lista todas as ferramentas(algoritmos) disponíveis.
```programming
>>> processing.alglist()
```
##### 3 - Lista todas as ferramentas(algoritmos) disponíveis que tenham uma string ou parte dela. A segunda coluna da lista fornece o nome da linha de comando da função.
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
##### 4 - Acessa às informações de ajuda da função. 
```programming
>>> processing.alghelp("nome_da_linha_de_comando_da_função")
```
```programming
>>> processing.alghelp("qgis:clip")
ALGORITHM: Clip
	INPUT <ParameterVector>
	OVERLAY <ParameterVector>
	OUTPUT <OutputVector>
```
##### 5 - Roda o algoritmo (ferramenta). 
```programming
>>> processing.runalg(nome_da_linha_de_comando_da_função, param1, param2, ..., paramN,Output1, Output2, ..., OutputN)
```
