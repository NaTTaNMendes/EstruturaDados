package Principal;

public interface Fila {
	
	public void adiciona(int valor) throws Exception;
	
	public Integer remove() throws Exception;
	
	public Boolean vazio();
	
	public void reiniciar();
}
