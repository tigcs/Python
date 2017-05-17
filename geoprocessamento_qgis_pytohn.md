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
```programming
# Faz o clip
processing.runalg("qgis:clip", camada_input, camada_overlay, "C:/Users/tigcs/Desktop/Python_USP/CLIP1.shp")
```
##### 6 - Lista as opções de parâmetros a serem selecionados ao rodar o algoritmo (ferramenta). Para tanto deve-se informar o número inteiro correspondente.
```programming
>>> processing.algoptions("nome_da_linha_de_comando_da_função")
```
```programming
>>> processing.algoptions("qgis:selectbylocation")
METHOD(Modificar seleção atual por)
	0 - Criar uma nova seleção
	1 - Adicionar à seleção atual
	2 - Remover da seleção atual
```
```programming
>>> processing.alghelp("qgis:selectbylocation")
ALGORITHM: Select by location
	INPUT <ParameterVector>
	INTERSECT <ParameterVector>
	PREDICATE <ParameterGeometryPredicate>
	PRECISION <ParameterNumber>
	METHOD <ParameterSelection>
	OUTPUT <OutputVector>
METHOD(Modificar seleção atual por)
	0 - Criar uma nova seleção
	1 - Adicionar à seleção atual
	2 - Remover da seleção atual
```
##### 7 - Lista todos os caminhos para os shapefiles armazenados em um diretório. 
```programming
# Importa o módulo `os` que permite acessar as funcionalidades do sistema operacional
>>> import os
# Cria uma variável com o caminho do diretório desejado
>>> wd = "D:/PRIM_estrada" 
# Cria uma lista vazia que irá receber os caminhos
>>> lf = list()
# Loop pela lista de todos os caminhos de arquivos existentes no diretório
# e adiciona à lista (lf) apenas aqueles que terminam com ".shp"
>>> for file in os.listdir(wd):
	if file.endswith(".shp"):
		lf.append (file)
>>> lf
['rodovia_ferrovia_CER.shp', 'rodovia_ferrovia_CER_1.shp', 'rodovia_ferrovia_CER_2.shp']
```
##### 8 - Carrega um shapefile para ser processado. 
```programming
layer = QgsVectorLayer(data_source, layer_name, provider_name)
if not layer.isValid():
  print "Layer failed to load!"
```
```programming
# Carrega a camada de input
camada_input = QgsVectorLayer("C:/Users/tigcs/Desktop/Python_USP/grid21.shp","UF","ogr")
# Checa se é uma camada válida
camada_input.isValid()
>>> True
```
##### 9 - Imprime o nome do primeiro campo da tabela de atributos. 
```programming
# Neste caso, 0 refere-se ao índice do primeiro campo. 
print grid21.fields()[0].name()
>>> Id
```
##### 10 - Imprime o nome de todos os campos da tabela de atributos. 
```programming
for field in grid21.fields():
    print field.name(), field.typeName()
>>> Id Integer
```
##### 11 - Adiciona um campo à tabela de atributos. 
```programming
# Opção 1: Nesta opção o shapefile com o novo campo tem que ser salvo. E é necessário fazer o import do módulo processing.
processing.runalg("qgis:addfieldtoattributestable", grid21, "grupo", 0, 3, 3, "C:/Users/tigcs/Desktop/Python_USP/grid21_.shp")
```




