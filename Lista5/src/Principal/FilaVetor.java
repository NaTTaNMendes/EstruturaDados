package Principal;

public class FilaVetor implements Fila {
	
	private Integer quantidadeElementos;
	private Integer capacidadeMaxima;
	private Integer inicio;
	private Integer[] vetor;
	
	public FilaVetor(Integer capacidadeMaxima) {
		this.capacidadeMaxima = capacidadeMaxima;
		this.vetor = new Integer[capacidadeMaxima];
		this.quantidadeElementos = 0;
	}

	@Override
	public void adiciona(int valor) throws Exception {
		if (this.quantidadeElementos == 0) {
			this.vetor[0] = valor;
			this.quantidadeElementos++;
			this.inicio = 0;
			return;
		}
		if (this.quantidadeElementos == this.capacidadeMaxima) {
			throw new Exception("Capacidade máxima da pilha atingida");
		}
		
		for (int x = this.inicio; true; x++) {
			if (x > this.capacidadeMaxima - 1) {
				x = 0;
			}
			if (this.vetor[x] == null) {
				this.vetor[x] = valor;
				this.quantidadeElementos++;
				break;
			}
		}			
	}

	@Override
	public Integer remove() throws Exception {		
		if (vazio()) {
			throw new Exception("A pilha está vazia");
		}
		
		Integer retorno = this.vetor[this.inicio];
		this.vetor[this.inicio] = null;
		this.quantidadeElementos--;
		
		for (int x = this.inicio; true; x++) {
			if (x > this.capacidadeMaxima - 1) {
				x = 0;
			}
			if (vazio()) {
				this.inicio = null;
				break;
			}
			if (this.vetor[x] != null) {
				this.inicio = x;
				break;
			}
		}		
		return retorno;
	}

	@Override
	public Boolean vazio() {
		if(this.quantidadeElementos == 0) {return true;}
		return false;
	}

	@Override
	public void reiniciar() {
		for (int x = 0; x <= this.capacidadeMaxima - 1; x++) {
			this.vetor[x] = null;
		}
		this.quantidadeElementos = 0;
		this.inicio = null;
	}

	@Override
	public String toString() {
		if (this.vazio()) {
			return "[]";
		}
		String saida = "[" + Integer.toString(this.vetor[this.inicio]);
		int contador = 1;
		for (int x = this.inicio + 1; true; x++) {
			if (x > this.capacidadeMaxima - 1) {
				x = 0;
			}
			contador++;
			if ((this.vetor[x] == null) || (contador > capacidadeMaxima)) {
				break;
			} else {
				saida += "," + Integer.toString(this.vetor[x]);
			}
		}
		
		saida += ']';
		return saida;
	}
	
	public Integer getQuantidadeElementos() {
		return this.quantidadeElementos;
	}
	
	public Integer getCapacidadeMaxima() {
		return this.capacidadeMaxima;
	}
	
	public Integer getInicio() {
		return this.inicio;
	}
	
	public Integer[] getVetor() {
		return this.vetor;
	}
	
	public FilaVetor concatena(FilaVetor f2) throws Exception {
		if (vazio() || f2.vazio()) {
			throw new Exception("Pelo menos uma das filas é vazia");
		}
		FilaVetor resultado = new FilaVetor(getQuantidadeElementos() + f2.getQuantidadeElementos());
		
		for (int x = this.inicio; true; x++) {
			if (resultado.capacidadeMaxima == resultado.quantidadeElementos) {
				break;
			}
			if (x > this.capacidadeMaxima - 1) {
				x = 0;
			}
			if (this.vetor[x] == null) {
				break;
			}
			resultado.adiciona(this.vetor[x]);
		}
		
		for (int x = f2.getInicio(); true; x++) {
			if (resultado.capacidadeMaxima == resultado.quantidadeElementos) {
				break;
			}
			if (x > f2.getCapacidadeMaxima() - 1) {
				x = 0;
			}
			if (f2.getVetor()[x] == null) {
				break;
			}
			resultado.adiciona(f2.getVetor()[x]);
		}
		
		return resultado;			
	}
	
	public FilaVetor fundir(FilaVetor f2) throws Exception {
		if (vazio() || f2.vazio()) {
			throw new Exception("Pelo menos uma das filas é vazia");
		}
		
		FilaVetor resultado = new FilaVetor(getQuantidadeElementos() + f2.getQuantidadeElementos());
		Integer inicioPilhaAtual = getInicio();
		Integer inicioPilhaEstrangeira = f2.getInicio();
		
		int contadorPilhaAtual = 1;
		int contadorPilhaEstrangeira = 1;
		
		while (true) {
			
			if (contadorPilhaAtual <= this.quantidadeElementos) {
				resultado.adiciona(this.vetor[inicioPilhaAtual]);
				contadorPilhaAtual++;
			}
			
			if (contadorPilhaEstrangeira <= f2.getQuantidadeElementos()) {
				resultado.adiciona(f2.getVetor()[inicioPilhaEstrangeira]);
				contadorPilhaEstrangeira++;
			}
	
			inicioPilhaAtual++;
			inicioPilhaEstrangeira++;
			
			if (inicioPilhaAtual > this.capacidadeMaxima - 1) {
				inicioPilhaAtual = 0;
			}	
			if (inicioPilhaEstrangeira > f2.getCapacidadeMaxima() - 1) {
				inicioPilhaEstrangeira = 0;
			}
			if (resultado.capacidadeMaxima == resultado.quantidadeElementos) {
				break;
			}
		}

		return resultado;	
	}
}
