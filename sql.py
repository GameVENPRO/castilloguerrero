import sqlite3

querry1 = '''CREATE TABLE heroes(
    id integer PRIMARY KEY,
    username text default null,
    heroflag text default null,
    castlename text default null,
    heroname text default null,
    nivel integer default 1,
    guild integer default 0,
    attack integer default 1,
    defense integer default 1,
    exp integer default 5,
    stamina integer default 5,    
    hp integer default 300,
    mana integer default 0,
    gold integer default 0,
    pouchgold integer default 0,    
    gems integer default 0,
    libros_exp integer default null,
    wins integer default 0,
    effects text default 1,
    arma_p text default 0,
    arma_s text default 0,
    caso text default 0,
    guantes text default 0,
    armadura text default 0,
    botas text default 0,
    especial text default 0,
    anillo text default 0,
    collar text default 0,
    bag integer default 15,
    stock integer default 4000,
    pet text default 0,
    clase text default 0,
    estado text default '🛌Descanso',
    mods text default null
);'''

querry2 = '''  CREATE TABLE inventario(
    id integer PRIMARY KEY,
    hero_nom text default null,
    cod_rec text default null,
    nom_rec text default null,
    cantidad integer default 0,
    peso integer default 0
);'''

querry3 = ''' CREATE TABLE balso(
    id integer PRIMARY KEY,
    hero_nom text default null,
    cod_itms text default null,
    nom_itms text default null,
    cantidad integer default 0,
    peso integer default 0
 
); '''
querry4 = '''CREATE TABLE efectos(
    id integer PRIMARY KEY,
    hero_name text default null,
    cod_efec text default null,
    nom_efec text default null,
    duracion text default null
);  '''
querry5 = ''' CREATE TABLE logros(
    id integer PRIMARY KEY,
    hero_name text default null,
    cod_logro text default null,
    nom_logro text default null,
    cantidad text default null,
    temporada integer default 1
); '''
querry6 = '''CREATE TABLE clases(
    id integer PRIMARY KEY,
    nom_hab text default null,
    cod text default null,
    castlename text default null
);  '''
querry7 = ''' CREATE TABLE habilidades(
    id integer PRIMARY KEY,
    hero_name text default null,
    heroflag text default null,
    castlename text default null,
    heroname text default null,
    nivel integer default 0,
    attack integer default 1
); '''
querry8 = '''CREATE TABLE guilds(
    id integer PRIMARY KEY,
    nom_g text default null,
    etiqueta text default null,
    comandante text default null,
    capacidad text default 3,
    nivel integer default 1,
    exp integer default 0,
    gloria text default 0,
    decadencia text default 0,
    gems text default 0,
    stock integer default 1000,
    attack integer default null,
    defense integer default null
);  '''

querry9 = '''CREATE TABLE heros_gulids(
    id integer PRIMARY KEY,
    guild text default null,
    etiqueta text default null,
    heroname text default null,
    nivel text default null,
    ataque text default null,
    defensa text default null
);  '''

querry10 = ''' CREATE TABLE locations(
    id integer PRIMARY KEY,
    nombre_l text default null,
    codigo text default null
); '''

querry11 = '''CREATE TABLE estado(
    id integer PRIMARY KEY,
    cod_estado text default null,
    estado text default null
); '''

conn = sqlite3.connect('castillowars.db')
c = conn.cursor()
c.execute(querry1)
c.execute(querry2)
c.execute(querry3)
c.execute(querry4)
c.execute(querry5)
c.execute(querry6)
c.execute(querry7)
c.execute(querry8)
c.execute(querry9)
c.execute(querry10)
c.execute(querry11)
conn.commit()
conn.close()

# localizacioes 
# name,code
# Colmena Perezosa,N4UYE7
# Halcón nocturno suave,xe91zS
# Mina inacabada lvl.24,fpEAyD
# Ruinas dudosas lvl.44,ibl3N0
# Codicioso Fox,EnZVnL
# Acróbata En Posición,FhHzKT
# Ruinas de confianza lvl.44,xkWLaP
# Ruinas antiguas lvl.70,zsaI5I
# Abandoné la mina lvl.57,NV2UrM
# Fort lvl.55,PDi5WA
# Mal Caimán,G1Dcji
# Se derrumbó la mina lvl.28,nX6L5I
# Buzzing Sastre,WD31t6
# Ruinas antiguas lvl.67,zBOP0T
# Cirujano Tímido,tEs7tZ
# Abandoné la mina lvl.47,BPgaBJ
# Honesto Watchman,uX0ufr
# Torre Difusa,LfJWR8
# Ruinas dudosas lvl.31,nSF0H1
# Dasher Egoísta,NPn84E
# Jasper Dragón,3GG8rX
# Oso Ansioso,9DjVmi
# Ruinas dudosas lvl.31,nSF0H1
# Ruinas dudosas lvl.31,nSF0H1
# Colmena Perezosa,N4UYE7
# Ruinas de confianza lvl.44,xkWLaP
# Colmena Perezosa,N4UYE7
# Ruinas dudosas lvl.31,nSF0H1
# Mal Caimán,G1Dcji
# Ruinas dudosas lvl.44,ibl3N0
# Honesto Watchman,uX0ufr
# Se derrumbó la mina lvl.73,HECkTF
# Ruinas dudosas lvl.31,nSF0H1
# Ruinas dudosas lvl.31,nSF0H1
# Ruinas dudosas lvl.31,nSF0H1
