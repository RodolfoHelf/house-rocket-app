import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#configurando as bibliotecas
pd.set_option('display.float_format', '{:.2f}'.format)
st.set_page_config( layout='wide' )
rc = {'figure.figsize':(8,4.5),
          'axes.facecolor':'#0e1117',
          'axes.edgecolor': '#0e1117',
          'axes.labelcolor': 'white',
          'figure.facecolor': '#0e1117',
          'patch.edgecolor': '#0e1117',
          'text.color': 'white',
          'xtick.color': 'white',
          'ytick.color': 'white',
          'grid.color': 'grey',
          'font.size' : 12,
          'axes.labelsize': 12,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12}
plt.rcParams.update(rc)




@st.cache( allow_output_mutation=True )
#Le o dado
def get_data( path ):
    data = pd.read_csv( path )
    return data



#criando novas colunas em relação a data para o dataframe
def transform_data(data):
    data["year"] = pd.to_datetime(data["date"]).dt.strftime( '%Y' )
    data["year_month"] = pd.to_datetime(data["date"]).dt.strftime( '%Y-%m' )
    data["month_day"]= pd.to_datetime(data["date"]).dt.strftime("%m-%d")
    data["date"] = pd.to_datetime(data["date"]).dt.strftime("%Y-%m-%d")
    data["season"] = data["month_day"].transform(lambda x: 
                                                "Primavera" if ((x >= "03-21") & (x <= "06-21")) else
                                                "Verão" if ((x >= "06-22") & (x <= "09-22")) else
                                                "Outono" if ((x >= "09-23") & (x <= "12-21")) else
                                                "Inverno")

    return data


def data_load(data):

    #divide o website em duas colunas 
    c1, c2 = st.columns((1, 1) )  
    # website text
    c1.title('🏡️ House Rocket 🚀️')
    c1.markdown('Seja muito bem vindo a analise de dados da House Rocket!')
    c1.markdown("Aqui você encontrará uma analise descritiva dos imóveis do Condado de King, Estados Unidos vendidos pela empresa fictícia House Rocket.")
    c1.markdown("Você pode encontrar o repositório do projeto em [House Rocket App](https://github.com/RodolfoHelf/house-rocket-app)")

    c2.subheader("Aplicativo criado por [Rodolfo Helfenstein](https://www.linkedin.com/in/rodolfo-helfenstein/)")

    show_data = st.checkbox(
        "Mostrar dados",
        value= False
    )

    if show_data:
        st.dataframe(data)

    c1, c2 = st.columns((1, 1) )  

    # H1: Imóveis que possuem vista para água são são 20% mais caros na média

    

    #agrupando os imóveis por "waterfront" e calculando a média de preços
    df = data[["price","waterfront"]].groupby("waterfront").mean().reset_index()

    #trasnformando a tabela que será printada para ficar mais legível
    df["waterfront"] = df["waterfront"].transform(lambda x: "Sim" if x == 1 else "Não")
    df.columns = ["Possui vista para o mar","Média dos preços dos imóveis"]

    #printando a representação do resultado da hipótese
    c1.subheader("Média dos preços dos imóveis com e sem vista para o mar")
    c1.dataframe(df)
    c1.write("Imóveis com vista para o mar são {:.2f}% mais caros na média".format(((df["Média dos preços dos imóveis"][1]-df["Média dos preços dos imóveis"][0])/df["Média dos preços dos imóveis"][0]) * 100))


    # H2: Imóveis com data de construção menor que 1995 são 50% mais baratos na média

    #criando filtro do ano construido
    yr_built_limit = st.sidebar.slider(value = 1995,
                                    min_value = int(data["yr_built"].min()),
                                    max_value = int(data["yr_built"].max()),
                                    label = "Year Built limit ")

    

    #calcula a média de preços de imóveis construidos antes e depois do valor escolhido no filtro
    mean_price_under = data[data["yr_built"] < yr_built_limit]["price"].mean()
    mean_price_over = data[data["yr_built"] >= yr_built_limit]["price"].mean()

    #cria a tabela que será printada
    df = pd.DataFrame(data = {"Imóveis construídos antes de {}".format(yr_built_limit): [mean_price_under],
                        "Imóveis construídos depois de {}".format(yr_built_limit): [mean_price_over] })

    c2.subheader("Média dos preços dos imóveis construidos antes de {}".format(yr_built_limit))
    c2.dataframe(df)
    c2.write("Imóveis construídos antes de {} são {:.2f}% mais baratos na média".format(yr_built_limit,((mean_price_over - mean_price_under)/mean_price_over)* (100)))

    # H3: Imóveis sem porão possuem área total (sqfr_lot) são 40% maiores do que os imóveis com porão

    c1, c2 = st.columns((1, 1) )  


    mean_area_without_basement =  data[data["sqft_basement"] == 0]["sqft_lot"].mean()
    mean_area_with_basement =  data[data["sqft_basement"] > 0]["sqft_lot"].mean()

    df = pd.DataFrame(data = {"Imóveis sem porão": [mean_area_without_basement],
                            "Imóveis com porão": [mean_area_with_basement]
                        })

    c1.subheader("Média da área de imóveis com e sem porão")
    c1.dataframe(df)
    c1.write("Imóveis sem porão são {:.2f}% maiores na média".format(((mean_area_without_basement - mean_area_with_basement)/mean_area_with_basement)* 100))

    # H4: O crescimento do preço dos imóveis YoY é de 10%

    mean_price_2014 = data[data["year"] == "2014"]["price"].mean()
    mean_price_2015 = data[data["year"] == "2015"]["price"].mean() 

    df = pd.DataFrame({"Média dos preços dos imóveis vendidos em 2014": [mean_price_2014],
                        "Média dos preços dos imóveis vendidos em 2015": [mean_price_2015]})

    c2.subheader("Crescimento dos valores dos imóveis por ano")
    c2.dataframe(df)
    c2.write("O cresimento YoY é de {:.2f}%".format(((mean_price_2015-mean_price_2014)/mean_price_2014)*100))

    ### H6: Imóveis com "sqft_living" maior que 2000 são 45% mais caros em média

    c1, c2 = st.columns((1, 1) )   

    sqft_living_limit = st.sidebar.slider(value = 2000,
                                    min_value = int(data["sqft_living"].min()),
                                    max_value = int(data["sqft_living"].max()),
                                    label = "Sqft_living limit ")

    mean_over = data[data["sqft_living"] > sqft_living_limit]["price"].mean()
    mean_under = data[data["sqft_living"] <= sqft_living_limit]["price"].mean()

    df = pd.DataFrame(data = {"Imóveis com sqft_living maior que {}".format(sqft_living_limit): [mean_over],
                        "Imóveis com sqft_living menor que {}".format(sqft_living_limit): [mean_under] })

    c1.subheader("Média dos preços dos imóveis com sqft_living maior que {}".format(sqft_living_limit))
    c1.dataframe(df)        
    c1.write("Imóveis com sqft_living maior que {} são {:.2f}% mais caros ".format(sqft_living_limit,((mean_over-mean_under)/mean_under)*100))        
    
    ### H7: Imóveis com "condition" menor que 3 são 15% mais baratos em média

    condition_limit = st.sidebar.slider(value = 3,
                                    min_value = int(data["condition"].min()),
                                    max_value = int(data["condition"].max()),
                                    label = "Condition limit ")

    
    mean_under = data[data["condition"] < condition_limit ]["price"].mean()
    mean_over = data[data["condition"] >= condition_limit ]["price"].mean()

    df = pd.DataFrame(data = {"Imóveis com condition menor que {}".format(condition_limit): [mean_under],
                        "Imóveis com condition maior que {}".format(condition_limit): [mean_over] })

    c2.subheader("Média dos preços de imóveis com condition menor que {}".format(condition_limit))
    c2.dataframe(df)        
    c2.write("Imóveis com condition menor que {} são {:.2f}% mais baratos".format(condition_limit,(( mean_over - mean_under)/mean_over)*100) )

    ### H8: Imóveis com mais de 5 quartos tem em média 50% mais banheiros

    c1, c2 = st.columns((1, 1) )  


    bedrooms_limit = st.sidebar.slider(value = 5,
                                    min_value = int(data["bedrooms"].min()),
                                    max_value = int(data["bedrooms"].max()),
                                    label = "Bedrooms limit ")


    mean_under = data[data["bedrooms"] < bedrooms_limit ]["bathrooms"].mean()
    mean_over = data[data["bedrooms"] >= bedrooms_limit ]["bathrooms"].mean()

    df = pd.DataFrame(data = {"Imóveis com mais de {} quartos".format(bedrooms_limit): [mean_over],
                        "Imóveis com menos de {} quartos".format(bedrooms_limit): [mean_under] })

    c1.subheader("Média de banheiros de imóveis com mais de {} quartos".format(bedrooms_limit))
    c1.dataframe(df)     
    c1.write("Imóveis com bedrooms maior que {} tem em média {:.2f}% mais banheiros".format(bedrooms_limit,((mean_over - mean_under)/mean_under)*100) )

    ### H10: O crescimento YoY de imóveis com "grade" igual a 7 é de 1%

    df = data[data["grade"] == 7][["price","year"]].groupby("year").mean().reset_index()

    c2.subheader("Crescimento YoY de imóveis com grade igual a 7")
    c2.dataframe(df)
    c2.write("O YoY de imóveis com grade igual a 7 é de {:.2f}%".format(((df.loc[1,"price"]-df.loc[0,"price"])/df.loc[1,"price"])*100))
    


    ### H9: Imóveis vendidos no verão são 30% mais caros em média

    c1, c2 = st.columns((1, 1) )  

    seasons_dropdown = st.sidebar.selectbox(
        options=['Verão', 'Inverno', 'Outono',"Primavera"],
        label='Sazonalidade',
        disabled=False,
    )

    mean_season = data[data["season"] == seasons_dropdown]["price"].mean()
    mean_not_season = data[data["season"] != seasons_dropdown ]["price"].mean()

    summer_mean = data[data["season"] == "Verão"]["price"].mean()
    fall_mean = data[data["season"] == "Primavera"]["price"].mean()
    autumn_mean = data[data["season"] == "Outono"]["price"].mean()
    winter_mean = data[data["season"] == "Inverno"]["price"].mean()

    #construindo um gráfico de barras com a média de preços por estação do ano que será plotado
    fig3 = plt.figure()
    sns.barplot(x = ['Verão', 'Inverno', 'Outono',"Primavera"], y = [summer_mean,fall_mean,autumn_mean,winter_mean])
    plt.xlabel("Estação do Ano")
    plt.ylabel("Média dos preços dos imóveis")
    plt.title("Média dos preços por estação do ano")

    c1.subheader("Média dos imóveis por estação")
    c1.pyplot(fig3)
    c1.write("Imóveis vendidos no {} são {:.2f}% mais caros que a média das outras estações".format(seasons_dropdown,((mean_season - mean_not_season)/mean_not_season)*100))

    # H5: Imóveis com 3 banheiros tem um cresimento de MoM de 15%

    mean_price_per_month = data[data["bathrooms"] == 3][["price","year_month"]].groupby("year_month").mean().reset_index()

    #criando uma nova coluna "growth" que representa o crescimento percentual do preço de venda em relação ao mês anterior
    for index in range(len(mean_price_per_month)):
        if index != 0:
            mean_price_per_month.loc[index,"growth"] = ((mean_price_per_month.loc[index,"price"]-mean_price_per_month.loc[index-1,"price"])/mean_price_per_month.loc[index-1,"price"])*100

    #criando um gráfico de linhas com o crescimento percentual de cada mês
    fig2 = plt.figure()
    sns.lineplot(data = mean_price_per_month, x= "year_month",y = "growth")
    plt.xticks(rotation = 45)
    plt.xlabel("Mês")
    plt.ylabel("Crescimento (%)")
    plt.title("MoM dos preços dos imóveis")

    c2.subheader("Crescimento MoM de imóveis com 3 banheiros")
    c2.pyplot(fig2)
    c2.write("O cresimento MoM de imóveis com 3 banheiros é de {:.2f}%".format(mean_price_per_month["growth"].mean()))

    #Recomendação de compra e sugestão de valor de venda

    zipcode_median = data[["price","zipcode"]].groupby("zipcode").median().reset_index()

    #cria uma nova coluna "status" que recebe o valor de "Compra" caso o valor do imóvel seja menor que a mediana do seu grupo de zipcode e "Não compra" caso contrário
    for index in range(len(data)):
        if data.loc[index,"price"] > zipcode_median.loc[zipcode_median["zipcode"] == data.loc[index,"zipcode"],"price"].values[0]:
            data.loc[index,"status"] = "Não Compra"
        else:
            data.loc[index,"status"] = "Compra"

    season_zipcode_median = data[["price","zipcode","season"]].groupby(["zipcode","season"],axis=0).median("price").reset_index()

    #cria uma nova coluna "sell_price" que recebe o valor de "price" acrescidos de 30% caso o valor seja menor que seu grupo de zipcode+estação do ano e recebe "price" acrescido de 10% caso for maior
    for index in range(len(data)):
        if data.loc[index,"price"] > season_zipcode_median[(season_zipcode_median["season"]==data.loc[index,"season"]) & (season_zipcode_median["zipcode"]==data.loc[index,"zipcode"])]["price"].values[0]:
            data.loc[index,"sell_price"] = data.loc[index,"price"] * 1.1
        else:
            data.loc[index,"sell_price"] = data.loc[index,"price"] * 1.3

    st.subheader("Recomendações de Compra e Sugestão de preço")
    st.dataframe(data[["id","date","zipcode","price","season","status","sell_price"]])

    return None


if __name__ == "__main__":

    path = "../data/kc_house_data.csv"

    data_raw = get_data(path)

    data_processing = transform_data(data_raw)

    data_load(data_processing)