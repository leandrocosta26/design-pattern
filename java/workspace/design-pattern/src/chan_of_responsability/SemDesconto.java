package chan_of_responsability;

public class SemDesconto extends Descontos {

	public SemDesconto(Descontos proximoDesconto) {
		super(proximoDesconto);
	}

	@Override
	public Double calcular(Compras compras) {
		return 0.0;
	}

}
