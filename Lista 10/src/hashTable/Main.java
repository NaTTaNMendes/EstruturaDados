package hashTable;

public class Main {

	public static void main(String[] args) {
		TabelaHash tabela = new TabelaHash(13);
		
		tabela.set("Nattan" , 1  , 8.0F);
		tabela.set("Leticia", 2  , 4.0F);
		tabela.set("Pedro"  , 3  , 2.3F);
		tabela.set("Kelvin" , 4  , 8.5F);
		tabela.set("Poliana", 5  , 4.7F);
		tabela.set("Daniela", 6  , 9.0F);
		tabela.set("João"   , 7  , 5.8F);
		tabela.set("Ícaro"  , 8  , 8.7F);
		tabela.set("Kelly"  , 9  , 6.9F);
		tabela.set("Ronaldo", 10 , 10.0F);
		tabela.set("Thiago" , 11 , 7.2F);
		tabela.set("Rebeca" , 12 , 3.4F);
		tabela.set("Lourdes", 13 , 4.7F);
		tabela.set("Agenor" , 14 , 5.8F);
		tabela.set("Silvia" , 15 , 7.4F);
		tabela.set("Valdir" , 16 , 8.9F);
		tabela.set("Frajola", 17 , 0.0F);
		tabela.set("Robin"  , 19 , 0.3F);
		tabela.set("Robin"  , 20 , 0.3F);
		tabela.set("Robin"  , 21 , 0.3F);
		tabela.set("Robin"  , 22 , 0.3F);
		tabela.set("Robin"  , 23 , 0.3F);
		tabela.set("Robin"  , 24 , 0.3F);
		tabela.set("Robin"  , 25 , 0.3F);
		tabela.set("Robin"  , 26 , 0.3F);
		tabela.set("Robin"  , 27 , 0.3F);
				
		System.out.println(tabela);
		Aluno busca = tabela.get(20);
		
		if (busca != null)
		   System.out.println(busca.getMatricula() + " " + busca.getNome());
		else
		   System.out.println("Aluno não encontrado");
		
		tabela.remove(14);
		System.out.println(tabela);
	}

}
