package template_method;

public abstract class TemplateCalculator {

	protected abstract Double calcularMaximaTaxacao(Orcamento orcamento);
	
	protected abstract Boolean deveCalcularMaximaTaxacao(Orcamento orcamento);
	
	protected abstract Double calcularMinimaTaxacao(Orcamento orcamento);
	
	public Double calcula(Orcamento orcamento){
		if(deveCalcularMaximaTaxacao(orcamento)){
			return calcularMaximaTaxacao(orcamento);
		}
		return calcularMinimaTaxacao(orcamento);
	}
	
}
