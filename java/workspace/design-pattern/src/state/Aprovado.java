package state;

public class Aprovado extends EstadoDeUmOrcamento{

	@Override
	public void aprova(Orcamento orcamento) throws Exception {
		throw new Exception("Orçamento ja está aprovado");
	}

	@Override
	public void cancelado(Orcamento orcamento) throws Exception {
		throw new Exception("Orçamento ja está aprovado, não pode ser mais cancelado");
	}

	@Override
	public void finalizado(Orcamento orcamento) {
		orcamento.setEstadoAtual(new Finalizado());
	}

	@Override
	public void aplicaDescontoExtra(Orcamento orcamento) {
		orcamento.setDesconto(orcamento.getValorFinal() * 0.02);
	}

}