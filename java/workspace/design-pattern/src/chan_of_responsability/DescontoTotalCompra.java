package chan_of_responsability;

public class DescontoTotalCompra extends Descontos {

	public DescontoTotalCompra(Descontos proximoDesconto) {
		super(proximoDesconto);
	}

	@Override
	public Double calcular(Compras compra){
		if(compra.getTotal() > 500){
			return compra.getTotal() * 0.1;
		}
		return this.getProximoDesconto().calcular(compra);
	}
}
