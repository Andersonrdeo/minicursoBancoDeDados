import DAO
#saida = DAO.inserir_usuario("anderson","anderson@gmail.com","1234");
#saida = DAO.inserir_usuario("vanessa","vanessa@gmail.com","1234");

#saida = DAO.buscar_usuario("anderson@gmail.com");

#print (saida);

#saida = DAO.listar_usuarios();

#print(saida);

#saida = DAO.atualizar_usuario(1,"carla","carla@gmail.com");

#print (saida);

saida = DAO.deletar_usuario(1);

print (saida);