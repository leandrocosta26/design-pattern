package template_method;

public class DescontoCompostoItens extends TemplateCalculator{

	@Override
	protected Double calcularMaximaTaxacao(Orcamento orcamento) {
		return orcamento.getValorFinal() * 0.07;
	}

	@Override
	protected Boolean deveCalcularMaximaTaxacao(Orcamento orcamento) {
		return orcamento.getValorFinal() < 500 && orcamento.getItens().size() > 2;
	}

	@Override
	protected Double calcularMinimaTaxacao(Orcamento orcamento) {	
		return orcamento.getValorFinal() * 0.03;
	}
	
}
