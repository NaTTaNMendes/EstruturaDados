package Principal;

public class Main {

	public static void main(String[] args) {
		FilaVetor fila = new FilaVetor(10);
		FilaVetor fila2 = new FilaVetor(3);
		
		try {
			fila.adiciona(1);
			fila.adiciona(3);
			fila.adiciona(203);
			fila.adiciona(1);
			fila.adiciona(3);
			fila.adiciona(203);
			fila.adiciona(1);
			fila.adiciona(3);
			fila.adiciona(203);
			fila.adiciona(1);
			
			System.out.println(fila);
			System.out.println(fila.vazio());
			
			fila.reiniciar();
			
			System.out.println(fila.vazio());
			
			fila.adiciona(3);
			fila.adiciona(90);
			fila.adiciona(824);
			fila.adiciona(41829);
			
			fila.remove();
			fila.remove();
			fila.remove();
			fila.remove();
			
			System.out.println(fila);
			
			fila.adiciona(1);
			fila.adiciona(3);
			fila.adiciona(5);
			fila.adiciona(6);
			
			fila2.adiciona(14);
			fila2.adiciona(16);
			fila2.adiciona(512);
			
			FilaVetor fila3 = fila.concatena(fila2);
			
			System.out.println(fila3);
			
			FilaVetor fila4 = fila.fundir(fila2);
			
			System.out.println(fila4);
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
