# house-rocket-app

Nesse projeto, é feito uma análise descritiva dos dados dos imóveis vendidos entre maio de 2014 e maio de 2015 do condado de King. São levantadas hipóteses sobre as caracteríscas dos imóveis e verificado se a hipótese é valida ou não. No final, são sugeridas compras de imóveis através da análise dos preços de imóveis por região e posteriormente um possível valor de venda do imóvel de acordo com seu preço e período em que ele foi comprado. 

A analise feita pode ser vista através do site: (é possivel que o site esteja fora do ar por inatividade)

Os dados utilizados foram obtidos do Kagle pelo site: https://www.kaggle.com/datasets/harlfoxem/housesalespredictioncd 

As hipoteses levantadas sao as seguintes:

- H1: Imóveis que possuem vista para o mar são são 20% mais caros na média
- H2: Imóveis com data de construção menor que 1995 são 50% mais baratos na média
- H3: Imóveis sem porão possuem área total (sqfr_lot) são 40% maiores do que os imóveis com porão
- H4: O crescimento do preço dos imóveis YoY é de 10%
- H5: Imóveis com 3 banheiros tem um cresimento de MoM de 15%
- H6: Imóveis com "sqft_living" maior que 2000 são 45% mais caros em média
- H7: Imóveis com "condition" menor que 3 são 15% mais baratos em média
- H8: Imóveis com mais de 5 quartos tem em média 50% mais banheiros
- H9: Imóveis vendidos no verão são 30% mais caros em média
- H10: O crescimento YoY de imóveis com "grade" igual a 7 é de 1%

Os dados dos imóveis forma extraidos e analisados utilizando Python para verificar se as hipoteses são verdadeiras.

H1: Falsa

Os imóveis foram agrupados em 2 grupos: imóveis que tem vista para o mar e imóveis sem vista para o mar. Posteriormente, foi feito a média dos preços de cada grupo e a conclusão obtida é que imóveis com vista para o mar são, em média, 212,64% mais caros que imóveis sem vista para o mar.

H2: Falsa

Os imóveis foram agrupados em 2 grupos: imóveis construídos antes de 1995 e imóveis construídos depois de 1994. Após isso, foi feito a média dos preçõs de cada grupo e constatou-se que imóveis construídos antes de 1995 são 17,14% mais baratos em relação ao outro grupo.

H3: Falsa

Os imóveis foram agrupados em 2 grupos: imóveis com "sqft_basement" igual a 0 e imóveis com "sqft_basement" maior que 0. Então, foi feito a média de "sqft_lot" de cada grupo e o resultado obtido foi que imóveis sem porão são 22,56% maiores que imóveis com porão

H4: Falsa

Foi calculado a média dos preços de venda dos imóveis para cada ano (2014 e 2015). O crescimento médio do ano de 2015 em relação ao de 2014 foi de 0,52%

H5: Falsa

Os imóveis foram agrupados de acordo com o mês que foram vendidos. Constatou-se que o crescimento médio de cada mês foi de 0,23%. O MoM de cada mês pode ser visto no gráfico a seguir

![Alt text](img/MoM.png?raw=true)

H6: Verdadeiro

Agrupou-se os imóveis em: imóveis com "sqft_living" maior que 2000 e imóveis com "sqft_living" menor ou igual a 2000. Comparando as médias de preço de cada grupo constatou-se que imóveis com "sqft_living" maior que 2000 são 87,15% mais caros em média.





1. Questão de negócio.
- O que você quer resolver?
- Encontrar as melhores oportunidades de
compra de imóveis do portfólio da House Rocket.
- Qual a problema, a dor, a necessidade do time
de negócio ?
- O time do negócio não consegue tomar
boas decisões de compra sem analisar os dados.
- O portfólio é muito grande, muito tempo
para fazer o trabalho manualmente.




2. Premissas de negócio.
- O que você está assumindo para realizar o
projeto ?
- Retirando casas com valor de venda maior
que R$ 500.000.000,00 ( possível erro do sistema ).
- A média do preço das casas na região de
Seattle é de R$ 300.000,00.
- Todas as casas estão em ótimas
condições.




3. Planejamento da solução:
- Qual o seu plano para resolver o problema?



4. Os 5 principais insights dos dados:
- O que há de relevante nos dados que pode
ajudar o time de negócio à tomar decisão.



5. Resultados financeiros para o negócio:
- Quanto a empresa espera lucrar com a sua
solução ?




6. Conclusão:
- Seu objetivo inicial foi alcançado? Sim ? Não ?
Porque ?
 
 
 
 7. Conclusão:
- Seu objetivo inicial foi alcançado? Sim ? Não ?
Porque ?
