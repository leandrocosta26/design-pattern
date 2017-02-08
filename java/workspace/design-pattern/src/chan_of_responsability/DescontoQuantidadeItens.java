package chan_of_responsability;

public class DescontoQuantidadeItens extends Descontos {

	public DescontoQuantidadeItens(Descontos proximoDesconto) {
		super(proximoDesconto);
	}

	@Override
	public Double calcular(Compras compras) {
		if(compras.getQuantidade() > 5){
			return compras.getTotal() * 0.05;
		}
		return this.getProximoDesconto().calcular(compras);
	}
}
