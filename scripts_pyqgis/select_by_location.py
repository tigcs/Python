# Partindo de um rio principal, são feitas seguidas seleções por locaização até
# que todos os rios que fazem parte da bacia do rio principal sejam selecionados.
    # SCRIPT para rodar dentro do terminal Python do qgis
    # Desenvolvido no Qgis 2.18.17 em 31/05/2019
    # É necessário que os rios sejam feições independentes e possuam um
        # identificador único na tabela de atributos. Cada rio seja uma única
        # linha na tabela de atributos (Dissolve).

import processing

#Carrega as camadas a serem processadas
rio0 = QgsVectorLayer('/home/tiago/Documentos/PRIM_Mineracao/rio/mata/rio_doce.shp', 'rio_doce','ogr')
drenagem = QgsVectorLayer('/home/tiago/Documentos/PRIM_Mineracao/rio/mata/rio_mata_disol.shp','rio_mata_disol','ogr')

# Faz a selecao por localizacao
processing.runalg("qgis:selectbylocation", drenagem, rio0,['intersects'],0,0)

# Cria variaveis que serao usadas para salvar o shapefile resultante da selecao
p=1
nome1 = '/home/tiago/Documentos/PRIM_Mineracao/rio/mata/'
nome2 = 'rio_doce_P'+str(p)
caminho = nome1+nome2+'.shp'
# Cria uma variavel com o sistema de referencia espacial CRS
crs = QgsCoordinateReferenceSystem("EPSG:4674")

# Salva o shapefile
processing.runalg('qgis:saveselectedfeatures', drenagem, caminho)

# Carrega o shapefile resultante da selecao
rio1 = QgsVectorLayer('/home/tiago/Documentos/PRIM_Mineracao/rio/mata/rio_doce_P1.shp', 'rio_doce_P1','ogr')

# Conta quantas feicoes tem nos shapefiles
feicoes_rio0 = int(rio0.featureCount())
feicoes_rio1 = int(rio1.featureCount())

while feicoes_rio1 != feicoes_rio0:
    # Carrega o shapefile resultante da selecao anterior
    rio0 = QgsVectorLayer('/home/tiago/Documentos/PRIM_Mineracao/rio/mata/rio_doce_' + str(p) + '.shp', 'rio_doce_P'+str(p),'ogr')
    feicoes_rio0 = int(rio0.featureCount())
    # Faz a selecao por localizacao
    processing.runalg("qgis:selectbylocation", drenagem, rio0,['intersects'],0,0)
    # Cria variaveis que serao usadas para salvar o shapefile resultante da selecao
    p=p+1
    nome2 = 'rio_doce_P'+str(p)
    caminho = nome1+nome2+'.shp'
    # Salva o shapefile
    processing.runalg('qgis:saveselectedfeatures', drenagem, caminho)
    # Carrega o shapefile resultante da selecao
    rio1 = QgsVectorLayer(caminho, 'rio_doce_P'+str(p),'ogr')
    feicoes_rio1 = int(rio1.featureCount())
print ('Fim')
