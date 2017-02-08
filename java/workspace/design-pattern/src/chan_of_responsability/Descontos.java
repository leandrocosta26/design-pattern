package chan_of_responsability;

public abstract class Descontos {

	public Descontos(Descontos proximoDesconto){
		this.proximoDesconto = proximoDesconto;
	}
	
	private Descontos proximoDesconto;
	
	protected Descontos getProximoDesconto(){
		return this.proximoDesconto;
	}

	public abstract Double calcular(Compras compras);
}
