#import packages and set packages options

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.float_format', '{:.2f}'.format)
st.set_page_config( layout='wide' )


# Functions

@st.cache( allow_output_mutation=True )
#Read Data
def get_data( path ):
    data = pd.read_csv( path )

    return data




# Extract

path = "../data/kc_house_data.csv"

data = get_data(path)



# Transform
data["year"] = pd.to_datetime(data["date"]).dt.strftime( '%Y' )
data["year_month"] = pd.to_datetime(data["date"]).dt.strftime( '%Y-%m' )
data["month_day"]= pd.to_datetime(data["date"]).dt.strftime("%m-%d")
data["season"] = data["month_day"].transform(lambda x: 
                                            "Primavera" if ((x >= "03-21") & (x <= "06-21")) else
                                            "Verão" if ((x >= "06-22") & (x <= "09-22")) else
                                            "Outono" if ((x >= "09-23") & (x <= "12-21")) else
                                            "Inverno")

# website text
st.title('🏡️ House Rocket Company 🚀️')
st.markdown('Welcome to House Rocket Data Analysis!')

c1, c2 = st.columns((1, 1) )  

# H1: Imóveis que possuem vista para água são são 20% mais caros na média
c1.header("Média de preço de imóveis com e sem vista para o mar")

df = data[["price","waterfront"]].groupby("waterfront").mean().reset_index()


c1.write("Imóveis com vista para o mar são {:.2f}% mais caros na média".format(((df["price"][1]-df["price"][0])/df["price"][0]) * 100))
df["waterfront"] = df["waterfront"].transform(lambda x: "Sim" if x == 1 else "Não")

df.columns = ["Possui vista para o mar","Média dos preços dos imóveis"]
c1.dataframe(df)


# H2: Imóveis com data de construção menor que 1995 são 50% mais baratos na média

yr_built_limit = st.sidebar.slider(value = 1995,
                                min_value = int(data["yr_built"].min()),
                                max_value = int(data["yr_built"].max()),
                                label = "Year Built limit ")

c2.header("Média dos preço de imóveis construidos antes de {}".format(yr_built_limit))



mean_price_under = data[data["yr_built"] < yr_built_limit]["price"].mean()
mean_price_over = data[data["yr_built"] >= yr_built_limit]["price"].mean()

df = pd.DataFrame(data = {"Imóveis construídos antes de {}".format(yr_built_limit): [mean_price_under],
                    "Imóveis construídos depois de {}".format(yr_built_limit): [mean_price_over] })


c2.write("Imóveis construídos antes de {} são {:.2f}% mais baratos na média".format(yr_built_limit,((mean_price_over - mean_price_under)/mean_price_over)* (100)))

c2.dataframe(df)

# H3: Imóveis sem porão possuem área total (sqfr_lot) são 40% maiores do que os imóveis com porão

c1, c2 = st.columns((1, 1) )  

c1.header("Média da área de imóveis com e sem porão")

mean_area_without_basement =  data[data["sqft_basement"] == 0]["sqft_lot"].mean()
mean_area_with_basement =  data[data["sqft_basement"] > 0]["sqft_lot"].mean()

df = pd.DataFrame(data = {"Imóveis sem porão": [mean_area_without_basement],
                        "Imóveis com porão": [mean_area_with_basement]
                     })

c1.write("Imóveis sem porão são {:.2f}% maiores na média".format(((mean_area_without_basement - mean_area_with_basement)/mean_area_with_basement)* 100))
c1.dataframe(df)

# H4: O crescimento do preço dos imóveis YoY é de 10%
c2.header("Crescimento dos valores de venda dos imóveis por ano")

mean_price_2014 = data[data["year"] == "2014"]["price"].mean()
mean_price_2015 = data[data["year"] == "2015"]["price"].mean() 

fig = plt.figure()

df = pd.DataFrame({"Média dos preços dos imóveis vendidos em 2014": [mean_price_2014],
                    "Média dos preços dos imóveis vendidos em 2015": [mean_price_2015]})

c2.write("O cresimento YoY é de {:.2f}%".format(((mean_price_2015-mean_price_2014)/mean_price_2014)*100))

c2.dataframe(df)


### H6: Imóveis com "sqft_living" maior que 2000 são 45% mais caros em média

c1, c2 = st.columns((1, 1) )   

sqft_living_limit = st.sidebar.slider(value = 2000,
                                min_value = int(data["sqft_living"].min()),
                                max_value = int(data["sqft_living"].max()),
                                label = "Sqft_living limit ")

c1.header("Média dos preços de imóveis com sqft_living maior que {}".format(sqft_living_limit))


mean_over = data[data["sqft_living"] > sqft_living_limit]["price"].mean()
mean_under = data[data["sqft_living"] <= sqft_living_limit]["price"].mean()

c1.write("Imóveis com sqft_living maior que {} são {:.2f}% mais caros ".format(sqft_living_limit,((mean_over-mean_under)/mean_under)*100))

df = pd.DataFrame(data = {"Imóveis com sqft_living maior que {}".format(sqft_living_limit): [mean_over],
                    "Imóveis com sqft_living menor que {}".format(sqft_living_limit): [mean_under] })
c1.dataframe(df)        

### H7: Imóveis com "condition" menor que 3 são 15% mais baratos em média

condition_limit = st.sidebar.slider(value = 3,
                                min_value = int(data["condition"].min()),
                                max_value = int(data["condition"].max()),
                                label = "Condition limit ")

c2.header("Média dos preços de imóveis com condition menor que {}".format(condition_limit))

mean_under = data[data["condition"] < condition_limit ]["price"].mean()
mean_over = data[data["condition"] >= condition_limit ]["price"].mean()

c2.write("Imóveis com condition menor que {} são {:.2f}% mais baratos".format(condition_limit,(( mean_over - mean_under)/mean_over)*100) )

df = pd.DataFrame(data = {"Imóveis com condition menor que {}".format(condition_limit): [mean_under],
                    "Imóveis com condition maior que {}".format(condition_limit): [mean_over] })
c2.dataframe(df)        



### H8: Imóveis com mais de 5 quartos tem em média 50% mais banheiros

c1, c2 = st.columns((1, 1) )  


bedrooms_limit = st.sidebar.slider(value = 5,
                                min_value = int(data["bedrooms"].min()),
                                max_value = int(data["bedrooms"].max()),
                                label = "Bedrooms limit ")

c1.header("Média de banheiros de imóveis com mais de {} quartos".format(bedrooms_limit))

mean_under = data[data["bedrooms"] < bedrooms_limit ]["bathrooms"].mean()
mean_over = data[data["bedrooms"] >= bedrooms_limit ]["bathrooms"].mean()

c1.write("Imóveis com bedrooms maior que {} tem em média {:.2f}% mais banheiros".format(bedrooms_limit,((mean_over - mean_under)/mean_under)*100) )

df = pd.DataFrame(data = {"Imóveis com mais de {} quartos".format(bedrooms_limit): [mean_over],
                    "Imóveis com menos de {} quartos".format(bedrooms_limit): [mean_under] })
c1.dataframe(df)     


### H10: O crescimento YoY de imóveis com "grade" igual a 7 é de 1%

df = data[data["grade"] == 7][["price","year"]].groupby("year").mean().reset_index()

c2.header("Crescimento YoY de imóveis com grade igual a 7")
c2.write("O YoY de imóveis com grade igual a 7 é de {:.2f}%".format(((df.loc[1,"price"]-df.loc[0,"price"])/df.loc[1,"price"])*100))
c2.dataframe(df)
# Load


### H9: Imóveis vendidos no verão são 30% mais caros em média

c1, c2 = st.columns((1, 1) )  

c1.header("Média dos imóveis por estação")

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





c1.write("Imóveis vendidos no {} são {:.2f}% mais caros que em relação às outras estações".format(seasons_dropdown,((mean_season - mean_not_season)/mean_not_season)*100))

fig3 = plt.figure()
sns.barplot(x = ['Verão', 'Inverno', 'Outono',"Primavera"], y = [summer_mean,fall_mean,autumn_mean,winter_mean])
plt.xlabel("Estação do Ano")
plt.ylabel("Média dos preços dos imóveis")
plt.title("Média dos preços pors estação do ano")
c1.pyplot(fig3)

# H5: Imóveis com 3 banheiros tem um cresimento de MoM de 15%

c2.header("Crescimento MoM de imóveis com 3 banheiros")

mean_price_per_month = data[data["bathrooms"] == 3][["price","year_month"]].groupby("year_month").mean().reset_index()


for index in range(len(mean_price_per_month)):
    if index != 0:
        mean_price_per_month.loc[index,"growth"] = ((mean_price_per_month.loc[index,"price"]-mean_price_per_month.loc[index-1,"price"])/mean_price_per_month.loc[index-1,"price"])*100


c2.write("O cresimento MoM de imóveis com 3 banheiros é de {:.2f}%".format(mean_price_per_month["growth"].mean()))

fig2 = plt.figure()
sns.lineplot(data = mean_price_per_month, x= "year_month",y = "growth")
plt.xticks(rotation = 45)
plt.xlabel("Mês")
plt.ylabel("Crescimento (%)")
plt.title("MoM dos preços dos imóveis")

c2.pyplot(fig2)
