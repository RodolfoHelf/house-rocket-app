# House Rocket App

Nesse projeto de estudo, é feito uma análise descritiva dos dados dos imóveis vendidos entre maio de 2014 e maio de 2015 do condado de King. São levantadas hipóteses sobre as características dos imóveis e verificado se a hipótese é valida ou não. No final, são sugeridas compras de imóveis através da análise dos preços de imóveis por região e posteriormente um possível valor de venda do imóvel de acordo com seu preço e período em que ele foi comprado. Esse estudo quem como objetivo o aprendizado de novas ferramentas e bibliotecas de Ciência de dados por meio da simulação de atividades que um Cientista de dados faria em uma empresa desse ramo utilizando dados reais.

A análise feita pode ser vista através do site: https://rodolfohelf-house-rocket-app-house-rocket-app-1j4rre.streamlit.app/ (é possível que o site esteja fora do ar por inatividade)

Os dados utilizados foram obtidos do Kagle pelo site: https://www.kaggle.com/datasets/harlfoxem/housesalespredictioncd 

As hipóteses levantadas são as seguintes:

- H1: Imóveis que possuem vista para o mar são 20% mais caros na média
- H2: Imóveis com data de construção menor que 1995 são 50% mais baratos na média
- H3: Imóveis sem porão possuem área total (sqfr_lot) são 40% maiores do que os imóveis com porão
- H4: O crescimento do preço dos imóveis YoY é de 10%
- H5: Imóveis com 3 banheiros tem um crescimento de MoM de 15%
- H6: Imóveis com "sqft_living" maior que 2000 são 45% mais caros em média
- H7: Imóveis com "condition" menor que 3 são 15% mais baratos em média
- H8: Imóveis com mais de 5 quartos tem em média 50% mais banheiros
- H9: Imóveis vendidos no verão são 30% mais caros em média
- H10: O crescimento YoY de imóveis com "grade" igual a 7 é de 1%

Os dados dos imóveis forma extraídos e analisados utilizando Python para verificar se as hipóteses são verdadeiras.

H1: Falsa

Os imóveis foram agrupados em 2 grupos: imóveis que tem vista para o mar e imóveis sem vista para o mar. Posteriormente, foi feito a média dos preços de cada grupo e a conclusão obtida é que imóveis com vista para o mar são, em média, 212,64% mais caros que imóveis sem vista para o mar.

H2: Falsa

Os imóveis foram agrupados em 2 grupos: imóveis construídos antes de 1995 e imóveis construídos depois de 1994. Após isso, foi feito a média dos preços de cada grupo e constatou-se que imóveis construídos antes de 1995 são 17,14% mais baratos em relação ao outro grupo.

H3: Falsa

Os imóveis foram agrupados em 2 grupos: imóveis com "sqft_basement" igual a 0 e imóveis com "sqft_basement" maior que 0. Então, foi feito a média de "sqft_lot" de cada grupo e o resultado obtido foi que imóveis sem porão são 22,56% maiores que imóveis com porão

H4: Falsa

Foi calculado a média dos preços de venda dos imóveis para cada ano (2014 e 2015). O crescimento médio do ano de 2015 em relação ao de 2014 foi de 0,52%

H5: Falsa

Os imóveis foram agrupados conforme o mês que foram vendidos. Constatou-se que o crescimento médio de cada mês foi de 0,23%. O MoM de cada mês pode ser visto no gráfico a seguir

![Alt text](img/MoM.png?raw=true)

H6: Verdadeira

Agruparam-se os imóveis em: imóveis com "sqft_living" maior que 2000 e imóveis com "sqft_living" menor ou igual a 2000. Comparando as médias de preço de cada grupo, constatou-se que imóveis com "sqft_living" maior que 2000 são 87,15% mais caros em média.

H7: Verdadeira

Os imóveis foram divididos em 2 grupos: imóveis com "condition" menor que 3 e imóveis com "condition" maior ou igual a 3. Então, foram feitas as médias de preço de cada grupo e constatou-se que imóveis com "condition" menor que 3 são, em média, 39,43% mais baratos.

H8: Falsa

Dividiram-se os imóveis em: imóveis com mais de 5 quartos e imóveis com 5 quartos ou menos. Foi feito a média do número de banheiros de cada grupo e obteve-se o resultado que imóveis com mais de 5 quarto tem 39,39% mais banheiros em média.

H9: Falsa

Os imóveis foram divididos em 2 grupos: imóveis vendidos no verão e imóveis vendidos nas outras estações. Depois, foi calculado a média dos preços de cada grupo e constatou-se que imóveis vendidos no verão são 0,05% mais baratos em média. O gráfico abaixo mostra a média dos preços por estação do ano.

![Alt text](img/season_mean.png?raw=true)

H10: Falsa

Foi calculado a média dos preços de venda dos imóveis com "grade" igual a 7 para cada ano (2014 e 2015). O crescimento médio do ano de 2015 em relação ao de 2014 foi de 3,7%

Por meio dessa análise, alguns insights interessantes podem ser extraídos

- Imóveis com vista para o mar são 212,64% mais caros que imóveis sem vista para o mar em média
- Imóveis sem porão tem 22,56% área total maior que imóveis com porão na média
- Não há uma diferença relevante entre as médias de venda de imóveis por estação do ano
- Imóveis com "sqft_living" maior que 2000 são 87,15% mais caros que imóveis com "sqft_living" menor que 2000
- O crescimento médio do preço de imóveis de 2015 é de apena 0,52% maior que o de imóveis vendidos em 2014

Após a verificação das hipóteses levantadas, foi feito uma análise se era vantajoso comprar o imóvel ou não. Para tal, foi adicionada uma nova coluna na tabela denominada "status" a qual pode receber dois valores: "Compra" ou "Não Compra". Os imóveis foram agrupados por "zipcode", ou seja, pela região onde se encontram, sendo feito o cálculo da mediana para cada grupo. Assumiu-se que imóveis com valores menores que a mediana do seu grupo são imóveis bons para compra e, caso contrário, não são bons imóveis para compra.

Também foi sugerido um valor de venda para cada imóvel. Se o valor do imóvel for menor que a mediana do seu grupo de zipcode+sazonalidade, o valor de venda é o valor de "price" + 30% e se
o valor do imóvel for menor que a mediana do seu grupo, ele recebe o valor de "price" + 10%. Suponde que todos os imóveis fossem comprados pelo valor sugerido, haveria um lucro 54% maior na compra de imóveis com status igual a não compra.

Por meio desse projeto foi possível aprender a fazer analises descritivas simples por meio de um conjunto de dados real e também como a utilizar a biblioteca streamlit para criação de websites para divulgação de projetos. Apesar de ser uma simulação de atividades de um cientista de dados, foi possível ganhar experiência na extração, limpeza, transformação e visualização de dados. O aprendizado não se restringiu a área de programação em dados, mas também se estendeu na visão e raciocínio analítico de um problema de negócio que é se assemelha a problemas reais, encontrados em empresas do setor privado.

Uma possível continuação desse projeto seria a utilização de ferramentas de visualização de dados, como Tableu e Power BI, para fazer representação gráfica de maior qualidade. Outro incremento que poderia ser feito é a utilização de algorítimos de machine learning para calcular possíveis valores de venda de imóveis, diferentemente da forma arbitrária feita nesse projeto. Ainda, a utilização de mais dados de outras regiões dos Estados Unidos, além da do Condado de King, poderiam agregar mais valor nos resultados e conclusões.
