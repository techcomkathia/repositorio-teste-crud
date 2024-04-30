import mysql.connector




conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="loja",
)

cursor = conexao.cursor()
print("Conexão como o banco de dados feita com sucesso! \n")


# funcao inserir
def cadastrar ( nome, preco, id) :
       comando_sql = f"insert into produtos (nome, preco, id) value ('{nome}', {preco},{id})"

       cursor.execute(comando_sql)
       conexao.commit()  # aqui é onde vamos inserir os dados
       print("Produto cadastrado com sucesso!")



#funcao selecionar
def selecionarTodosProdutos():
    comando_sql = f'select id, nome, preco from produtos'
    cursor.execute(comando_sql)
    resultado_consulta = cursor.fetchall()
    return resultado_consulta


#funcao atualizar
def atualizarPreco(id, novo_valor):
    comando_sql = f' UPDATE produtos SET preco = {novo_valor} WHERE id = {id}'
    cursor.execute(comando_sql)
    conexao.commit()

#funcao deletar
def deletarProduto(id):
   comando_sql = f'DELETE FROM produtos WHERE id = {id}'
   cursor.execute(comando_sql)
   conexao.commit()

