package hashTable;

public class Aluno {
	
	private String nome;
	private Integer matricula;
	private Float mediaGeral;
	private Aluno proximo;
		
	public Aluno() {
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public Integer getMatricula() {
		return matricula;
	}
	public void setMatricula(Integer matricula) {
		this.matricula = matricula;
	}
	public Float getMediaGeral() {
		return mediaGeral;
	}
	public void setMediaGeral(Float mediaGeral) {
		this.mediaGeral = mediaGeral;
	}
	public Aluno getProximo() {
		return proximo;
	}
	public void setProximo(Aluno proximo) {
		this.proximo = proximo;
	}
		
}
