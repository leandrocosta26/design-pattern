package state;

public class Finalizado extends EstadoDeUmOrcamento{

	@Override
	public void aprova(Orcamento orcamento) throws Exception {
		throw new Exception("Orçamento ja está finalizado e não pode ser revertido para aprovado");
	}

	@Override
	public void cancelado(Orcamento orcamento) throws Exception {
		throw new Exception("Orçamento ja está finalizado e não pode ser revertido para cancelado");
	}

	@Override
	public void finalizado(Orcamento orcamento) throws Exception {
		throw new Exception("Orçamento ja está finalizado, e não pode ser finalizado novamente");
	}

	@Override
	public void aplicaDescontoExtra(Orcamento orcamento) throws Exception {
		throw new Exception("Orçamento ja está finalizado e não recebe desconto extra");
	}

}