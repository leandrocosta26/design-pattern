package state;

public abstract class EstadoDeUmOrcamento {

	public abstract void aprova(Orcamento orcamento) throws Exception;
	
	public abstract void cancelado(Orcamento orcamento) throws Exception;
	
	public abstract void finalizado(Orcamento orcamento) throws Exception;
	
	public abstract void aplicaDescontoExtra(Orcamento orcamento) throws Exception;
}
