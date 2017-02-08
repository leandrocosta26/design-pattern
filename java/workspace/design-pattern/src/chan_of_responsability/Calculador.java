package chan_of_responsability;

public class Calculador {
	public static void main(String[] args) {
		Compras compra = new Compras(500.0 , 2);
		Double desconto = new DescontoQuantidadeItens(new DescontoTotalCompra(new SemDesconto(null))).calcular(compra);
		System.out.println(String.format("Valor do desconto %s", desconto.toString()));
	}
}
