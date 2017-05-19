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
processing.runalg("qgis:clip", camada_input, camada_overlay, "D:/Python_USP/CLIP1.shp")
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
camada_input = QgsVectorLayer("D:/Python_USP/grid21.shp","grid21","ogr")
# Checa se é uma camada válida
camada_input.isValid()
>>> True
```
##### 9 - Acessando a tabela de atributos.
##### 9.1 - Imprime o nome do primeiro campo da tabela de atributos. 
```programming
# Neste caso, 0 refere-se ao índice do primeiro campo. 
print grid21.fields()[0].name()
>>> Id
```
##### 9.2 - Imprime o nome de todos os campos da tabela de atributos. 
```programming
for field in grid21.fields():
    print field.name(), field.typeName()
>>> Id Integer
```
##### 9.3 - Imprime os valores dos atributos.
```programming
# Pode-se criar um iterador (iter) e usá-lo no for loop. 
# Após rodar o for loop o iterador é apagado automaticamente, tendo de ser recriado caso seja necessário rodar outro for loop.
iter = grid21.getFeatures()
for feature in iter:
    # Imprime o id da feição
    print feature.id()
    # ou # print feature["Id"]

# Ou Criar um iterador já no enunciado do for loop.
for feature in grid21.getFeatures():
    # Imprime o id da feição
    print feature.id()
```
```programming
# Cria uma lista com todos dos valores do campo "Id"
# cria uma lista vazia que receberá os valores
Id = list()
for feature in grid21.getFeatures():
    Id.append (feature ["Id"])
```
##### 10 - Editando a tabela de atributos.
##### 10.1 - Adiciona um campo à tabela de atributos. 
```programming
# Opção 1: Nesta opção o shapefile com o novo campo tem que ser salvo. E é necessário fazer o import do módulo processing.
processing.runalg("qgis:addfieldtoattributestable", grid21, "grupo", 0, 3, 3, "D:/Python_USP/grid21_.shp")
```
```programming
# Opção 2: Nesta opção o novo campo é adicionado na camada carregada na memória.
from PyQt4.QtCore import QVariant
vpr = grid21.dataProvider()
vpr.addAttributes([QgsField("grupo", QVariant.Int)])
# É necessário atualizar os campos ao final do processo.
grid21.updateFields()
```
##### 10.2 - Altera o valor de um campo na tabela de atributos. 
```programming
iter = grid21.getFeatures()
for feature in iter:
    # feature.id()-> traz o id da feição, 1 -> é i índice do campo, 9 -> é o valor a ser inserido.
    # o índice da coluna pode ser acessado por: grid21.fieldNameIndex("grupo")
    grid21.changeAttributeValue(feature.id(),1,9)
    # outra opção:
    #grid21.changeAttributeValue(feature.id(),grid21.fieldNameIndex("grupo"),9)
```
##### 10.3 - Altera o valor de um campo na tabela de atributos utilizando-se de uma condição.
```programming
# Divide as feições em grupos aplicando-se uma condição. Neste caso serão 3 grupos com 7 feições cada. 
Id = list()
for feature in grid.getFeatures():
    Id.append(feature.id())

# len(Id)=> 21
num_grupos = 3
bloco = len(Id)/num_grupos
grupo = 1
for feature in grid.getFeatures():
     if feature ["Id"] <= bloco:
         atributo = {grid.fieldNameIndex("grupo") : grupo}
         grid.dataProvider().changeAttributeValues({feature.id() : atributo})
     else:
         atributo = {grid.fieldNameIndex("grupo") : (grupo+1)}
         grid.dataProvider().changeAttributeValues({feature.id() : atributo})
         grupo = grupo + 1
         bloco = bloco + len(Id)/num_grupos

# Verificar se o código abaixo também funciona
num_grupos = 3
bloco = len(Id)/num_grupos
grupo = 1
iter = grid21.getFeatures()
for feature in iter:
    if feature ["Id"] <= bloco:
        grid21.changeAttributeValue(feature.id(),grid21.fieldNameIndex("grupo"),grupo)
    else:
        grid21.changeAttributeValue(feature.id(),grid21.fieldNameIndex("grupo"),(grupo+1))
        grupo = grupo + 1
        bloco = bloco + len(Id)/num_grupos
``` 
##### 10.4 - Remove um campo da tabela de atributos.
```programming
# É necessário fornecer o índice do campo. Não funciona com o nome. O índice pode ser obtido com a função layer.fieldNameIndex("nome_do_campo")
for field in grid21.fields():
    grid21.dataProvider().deleteAttributes([grid21.fieldNameIndex("grupo")])
# Assim como na adição de um campo, é necessário atualizar os cmapos ao final do processo.
grid21.updateFields()
```
##### 11 - Salva um shapefile.
```programming

# Determina o sistema de referência espacial: EPSG WGS84 = 4326, SIRGAS 2000 = 4674, Albers_Equal_Area = 102033
crs = QgsCoordinateReferenceSystem("EPSG:4674")

# Cria variáveis com o caminho e nome do arquivo
save_path = "D:/Python_USP/"
nome_shp = "grid21_G"
save_path_nome = save_path+nome_shp+".shp"

# Salva o shapefile
QgsVectorFileWriter.writeAsVectorFormat(grid21, save_path_nome, "utf-8", crs, "ESRI Shapefile")
```




