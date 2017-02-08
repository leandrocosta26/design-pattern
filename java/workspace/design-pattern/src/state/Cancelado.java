package state;

public class Cancelado extends EstadoDeUmOrcamento{

	@Override
	public void aprova(Orcamento orcamento) throws Exception {
		throw new Exception("Orçamento ja está cancelado");
	}

	@Override
	public void cancelado(Orcamento orcamento) throws Exception {
		throw new Exception("Orçamento ja está cancelado");
	}

	@Override
	public void finalizado(Orcamento orcamento) throws Exception {
		throw new Exception("Orçamento ja está finalizado");
	}

	@Override
	public void aplicaDescontoExtra(Orcamento orcamento) throws Exception {
		throw new Exception("Orçamento cancelaod não recebe desconto");
	}
}