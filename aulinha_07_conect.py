import mysql.connector

conecsssao = mysql.connector.connect(host='localhost',database='db_nota',user='root',password='root')


# if  conecsssao.is_connected():
#     db_info = conecsssao.get_server_info()
#     print('Vose ta conequitadu nu servidor mai éssi que éli',db_info)
#     # criando cursor pra manipular o banco de dados
#     cursor = conecsssao.cursor()
#     cursor.execute('select database(db_nota);')
#     linha = cursor.fetchone()
#     print('conequitadu au bancu',linha )

criar_tabela = """create table tb_cliente(
                    nr_cnpj char(14) primary key,
                    nm_razao_sozial varchar(35) not null,
                    nm_pais varchar(20),
                    nm_email varchar(40) not null
                  );
                 """
cursor = conecsssao.cursor()
cursor.execute(criar_tabela)
print('tabela criada com suçesço')

