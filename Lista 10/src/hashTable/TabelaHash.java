package hashTable;

public class TabelaHash {
	
	private Aluno[] tabela;

	public TabelaHash(Integer tamanhoTabela) {
		tabela = new Aluno[tamanhoTabela];
	}
	
	private int hash(Integer valor) {
		return valor % tabela.length;
	}
	
	public void set(String nome, Integer matricula, Float mediaGeral) {
		Integer indice = hash(matricula);
		Aluno alunoAtual = tabela[indice];
		
		// Procurando algum aluno igual
		while (alunoAtual != null) {
			
			if (alunoAtual.getMatricula() == matricula) {
				break;
			}
			alunoAtual = alunoAtual.getProximo();
			
		}
		
		// Adicionando o novo alunos
		if (alunoAtual == null) {
			alunoAtual = new Aluno();
			alunoAtual.setMatricula(matricula);
			alunoAtual.setProximo(tabela[indice]);
			tabela[indice] = alunoAtual;
		}
		
		tabela[indice].setNome(nome);
		tabela[indice].setMediaGeral(mediaGeral);
	}
	
	public Aluno get(Integer matricula) {
		Integer indice = hash(matricula);
		Aluno alunoAtual = tabela[indice];
		
		// Procurando algum aluno igual
		while (alunoAtual != null) {
			
			if (alunoAtual.getMatricula() == matricula) {
				return alunoAtual;
			}
			alunoAtual = alunoAtual.getProximo();
			
		}
		
		return null;
	}
	
	public void remove(Integer matricula) {
		Integer indice = hash(matricula);
		Aluno alunoAtual = tabela[indice];
		Aluno anterior = null;	
		// Procurando algum aluno igual
		while (alunoAtual != null) {
			
			if (alunoAtual.getMatricula() == matricula) {
				if (tabela[indice] == alunoAtual) {
					if (alunoAtual.getProximo() != null) {
						tabela[indice] = alunoAtual.getProximo();
					} else {
						tabela[indice] = null;
					}
					
				} else {
					anterior.setProximo(alunoAtual.getProximo());
				}
				
			}
			anterior = alunoAtual;
			alunoAtual = alunoAtual.getProximo();
			
		}

	}

	@Override
	public String toString() {
		String saida = "";
		
		for (int i = 0; i < tabela.length; i++) {
			
			
			if (tabela[i] != null) {
				
				Aluno alunoAtual = tabela[i]; 
				while (alunoAtual != null) {
					saida = saida + " - " +  alunoAtual.getMatricula();
					alunoAtual = alunoAtual.getProximo();
				}
				
				saida = saida + '\n';
								
			} else {
				saida = saida + "null" + '\n';
			}
			
		}
		
		return saida;
	}
		
}
