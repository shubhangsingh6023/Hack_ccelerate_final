import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image
import time
import webbrowser

st.set_page_config(page_title = "Hacker-ccelerateData-Analysis", page_icon = "❄️" ,layout="wide")  # For setting wide page configuration

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{      #For condensing the page layout
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

with st.spinner('Working on your request!'):
    time.sleep(8)  # Loading spinner call so that user does not get bored

col1, col2 = st.sidebar.columns([1, 8])
image1 = Image.open('WebsiteLogo2.jpg')
with col1:
    st.image(image1, width=45)
    with col2:
        st.markdown('<h3 style="color: lightyellow; font-family: courier;">MENU</h3>',
                        unsafe_allow_html=True)
url1 = 'https://share.streamlit.io/rajeev1815/microsoft-engage/main/Data_Visualisation.py'
url2 = 'https://share.streamlit.io/rajeev1815/car-predictor-engage/main/CarPredictor.py'
col1, col2 = st.sidebar.columns([1, 10])
with col1:
    st.image(
        "https://i.pinimg.com/736x/c9/23/d9/c923d95813aa64751088cd3a6dc65715.jpg", width=35)
    with col2:
        button1 = st.button('Home')
        
with col1:
    st.image("https://cdn3.vectorstock.com/i/1000x1000/94/42/data-icon-on-white-background-simple-element-from-vector-28229442.jpg", width=35)
    with col2:
        button2 = st.button('Data Visualization')
        if button2:
            webbrowser.open_new_tab(
                'https://share.streamlit.io/rajeev1815/microsoft-engage/main/Data_Visualisation.py')
        
with col1:
    st.image("https://media.istockphoto.com/vectors/report-icon-vector-sign-and-symbol-isolated-on-white-background-logo-vector-id1001207390?k=20&m=1001207390&s=170667a&w=0&h=9sctNa8KvgTkKq6dlatFqZElGgsS2lcmaraUES137pw=", width=35)
    with col2:
        button3 = st.button('Exploratory Data Analysis')
  
with col1:
    st.image("https://cdn.vectorstock.com/i/1000x1000/68/44/car-logo-with-circle-hand-colorful-logo-vector-22266844.webp", width=35)
    with col2:
        button4 = st.button('Car Price Predictor')
        if button4:
            webbrowser.open_new_tab(
                'https://share.streamlit.io/rajeev1815/car-predictor-engage/main/CarPredictor.py')
            
col1, col2 = st.sidebar.columns([1,12.5])
with col1:
    st.image("https://hoima.go.ug/wp-content/uploads/2021/09/662-6627316_person-icon-transparent-background-hd-png-download.png", width=30)
    with col2:
        button5 = st.button('About Us')

if ((button3 != True) & (button5 != True)):
    col1, col2 = st.columns([1, 4])
    logo = Image.open('WebsiteLogo.png')
    col1.image(logo, width=200)
    engage = Image.open('image001.jpg')
    col2.image(engage, width=900)

    data = pd.read_csv("Cleaned Engage Car.csv")
    data.drop('Unnamed: 0', inplace=True, axis=1)
    st.title("ENGAGE DATA ANALYSIS")

    st.markdown("""The cleaned data set can be downloaded here:""")


    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')


    csv = convert_df(data)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='Cleaned Engage Car 2.csv',
        mime='text/csv',
    )

    selected_car = st.selectbox(
        "Car Manufacturer", list(data['Manufacturer'].unique()))
    if st.checkbox("View Data of Selected Manufacturer"):
        st.write(data[data.Manufacturer == selected_car])

    n = st.slider("Top Manufacturers", 5, 15)
    numeric_columns = data.select_dtypes(
        ['float64', 'int64', 'float32', 'int32']).columns
    list_numeric_columns = (list(numeric_columns))
    manufacturer_names = data.Manufacturer.value_counts().index[:n]
    manufacturer_values = data.Manufacturer.value_counts().values[:n]
    option1 = st.selectbox(
        'What do you want to plot?',
        ('Pie Plot', 'Donut Plot'))
    if (option1 == 'Donut Plot'):
        fig1 = px.pie(data, values=manufacturer_values, names=manufacturer_names,
                    title='Top Manufacturers in Indian Market', hole=0.75)
    else:
        fig1 = px.pie(data, values=manufacturer_values, names=manufacturer_names,
                    title='Top Manufacturers in Indian Market')
    st.write(fig1)

if button3:
    st.header("EXPLORATORY DATA ANALYSIS:")
    st.subheader("Here you can view the EDA of given Dataset and queries answered by me on the basis of the dataset.")
    st.markdown("QUERY: THE POPULAR CAR SPECIFICATION COMBINATION")
    st.image('top7sevenmanufacturer.png', width = 900)
    st.write("The above plots shows that the most cars sold in the market are manufactured by MARUTI SUZUKI followed by MAHINDRA and then HYUNDAI.\n")
    st.write("According to the given dataset, 143 out of 986 are of Maruti Suzuki then followed by Mahindra, Hyumdai, Toyota and 605 out of 986 are from top 7 manufacturers.")
    st.write("\n")
    st.image('countplotonroadprice.png',width = 900)
    st.write("It can be observed from the above plots that the cars which are around 10 lakhs are frequently bought by customers in India.\n")
    st.write("Automotive Industry Manufacturers should try to manufacture cars which had on road price from 5 lakhs to 15 lakhs so that there would be more number of buyers compared to other prices.\n")
    st.write("\n")
    st.image('countplotbodytype.png',width = 900)
    st.write("It can be seen from the above plot that SUV is the most selling Body type according to the given data set. It is followed by Hatchback and Sedan.\n")
    st.write("Hatchback, Suv, Sedan should be manufactured more by Automotive Industry as their sales is greater than the rest of the cars.\n")
    st.write("\n")
    st.image('countplotfueltype.png',width = 600)
    st.write("Cars which run on Petrol and Diesel are most preferred by customers. Hybrid and CNG+Petrol cars are around 8% of the complete dataset.\n")
    st.write("Automotive Industry should try to focus on cars that run on Petrol and Deisel as these are easily accessible.\n")
    st.write("\n")
    st.image('countplotdisplacement.png',width = 900)
    st.write("It can be observed from above displacement plot is that 1000-1600 cc is the most coomon displacement. cars from these range are sold in large number as per given dataset. The displacement of higher than 3000 cc are either less bought or less manufactured by Automotive Industries.\n")
    st.write("\n")
    st.image('scatterplotdisplacementpower.png',width = 900)
    st.write("1. The most combination between Displacement and Power is around (100,1600) co-ordinate. That means the most selling combination is dipacement of 1400-1600 cc and power around 70-120 hp.\n")
    st.write("2. The most popular combination have body type Hatchback, SUV , Sedan , MPV,etc.\n")
    st.write( "3. The Body types such as Convertible, Coupe , Sports have high power and high displacement. This also concludes that these card would be expensive.\n")
    st.write("\n")
    st.image('scatterplotonroadpricepower.png',width = 900)
    st.write("1. The most popular combination is around 10-20 lakhs with power of 120-180 hps followed by power of 40-70 hps and price around 3-6 lakhs.\n")
    st.write("2. The cars with power of around 700 hps are of price nearly 5 crores. Thus greater the power greater will be the on road price. This is also concluded from this plot.\n")
    st.write("3. Hatchbacks, Sedan, SUVs have less power specification and costs less as compared to the other car body types.\n")
    st.write("\n")
    st.image('fueltypemileageplot.png',width = 900)
    st.write("1. CNG + Petrol Cars give best mileage of around 22km/litres followed by Deisel Cars and than Petrol Cars\n")
    st.write("2. But CNG+Petrol Cars are less in number so we consider that company should focus more on Deisel as number of cars that run of Deisel is more and even mileage by them is close to 20km/litres.\n")
    st.write("3. Petrol Cars are usually elite cars thus the average mileage is less than Dieseland is around 16.5 km/litres\n")
    st.write("\n")
    st.image('geartypemileageplot.png',width = 900)
    st.write("1. Cars having Gear-Type as AMT give the best average mileage followed by cars having manual gear type which is close to 20km/litres.\n")
    st.write("2. The automatic Gear Type gives least mileage as most of elite cars have less mileage and are automatic. This somewhere decreases the average mileage.\n")
    st.write("\n")
    st.image('mileagegeartypestripplot.png',width = 900)
    st.write("It can be seen that Automatic cars have even mileage close to 5km/litres and number of cars having AMT,CVT and DCT is very less while mileage is good. But since less number of observation in AMT, CVT and DCT , we would conclude that Manual Cars give a great mileage with compared to other gear type. Automotive Industry should try to manufacture more Deisel Cars as mileage (which is important for Customers) is highest in this classification.\n")
    st.write("\n")
    st.image('cylinderpowerkdeplot.png',width = 900)
    st.write("The KDE plot above shows that a large number of cars have combination of power and number of cylinders as 150 hp and 4 cylinders in the engine. One may also colclude that more would be the number of cylinders more would be the power of engine. For any particular number of cylinders there can different powers depending upon the car's other features. But one conclusion is that popular combination is (145,4).\n")
    st.write("\n")
    st.image('drivetrainmileageplot.png',width = 900)
    st.write("It can be concluded from above plot that cars having drivetrain as Front Wheel Drivetrain are more popular and provides best mileage.\n")
    st.write("\n")
    st.image('drivetrainonroadpricestripplot.png',width = 900)
    st.write("1. Average On road price of Front Wheel Drive Car would be within 20 lakhs and would be least. It can be seen from above strip plot.\n")
    st.write("2. All other drivetrain have price ranges upto 5 crores and even mileage is not that great. So, Automotive Industries should focus on larger section of customers and great mileage that is generally by manufacturing Front Wheel Drive Cars.\n")
    st.write("\n")
    st.image('mileagedrivetrainstripplot.png',width = 900)
    st.write("The above strip plot gives us conclusive evidences that Front Wheel Drive cars are most popular and provide best mileage as compared to other.\n")
    st.write("\n")
    st.image('drivetrainpowerswarmplot.png',width = 900)
    st.write("The average engine power of FWD Cars is close to 150-160 hp and that is most popular power range as seen in the earlier. Other Drivetrain provide a variety of power range.\n")
    st.write("\n")
    st.image('powermileagefueltypeplot.png',width = 900)
    st.write("1. Not a lot of observation markers are there for Petrol+CNG and Hybrid. So these are  not popular.\n")
    st.write("2. Comparing Deisel and Pretrol, it can be seen that Deisel Cars have better mileage and even Linear Regression is better followed, making Diesel better choice.\n")
    st.write("\n")
    st.image('mileagepowermanufacturerscatterplot.png',width = 900)
    st.write("Manufacturers such as Tata, Datsun , Maruti Suzuki , Hyundai manufacture cars with decent average mileage and decent average power.\n")
    st.image('datadescribe1.png',width = 900)
    st.write("Using data.describe(), we get following statistics.\n")
    st.write("Based on these statistics and all plots above, we will define most popular car specification combination, which is given in form of dataframe below :\n")
    dict = {'Manufacturer' : 'Maruti Suzuki/Hyundai/Tata', 'Body-Type' : 'SUV/Sedan/Hatchback',  'Fuel-Type' : 'Deisel' , 'Gear-Type' : 'Manual',
            'Drivetrain' : 'Front Wheel Drive', 'Displacement' : '1760 cc' , 'Cylinders' : '4' , 'Mileage' : '18.52 km/L' , 'Power': '152.88 hp',
            'Torque' : '244 Nm', 'Fuel Tank' : '51 Litres', 'Height' : '1584 mm' , 'Length' : '4253 mm', 'Width' : '1776 mm' , 'Doors' : '5',
            'Seats' : '5', 'Wheelbase' : '2607 mm' }
    new = pd.DataFrame(list(dict.items()),columns = ['Popular Feature','Popular Category'])
    st.dataframe(new)
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.caption("QUERY : MANUFACTURER SEGMENTATION")
    st.write("Based on a research and reviews from people, I concluded that Indian Customer usually segment manufacturers on the basis of two things./n")
    st.write("1. Mileage per car of that manufacturing company.\n")
    st.write("2. On road price per car of that manufacturing company.\n")
    st.write("On the basis of above two categorises, I plotted two line plots which are given below:\n")
    st.image('manufactureronroadpricelineplot.png',width = 900)
    st.markdown("INSIGHTS :\n")
    st.write("The objective for using the mean of all data is to show overall performance of manufacturers in terms of on road price per car. This can also be seen as the amount of the money contribution in the economy. We may derive the following assertions from the data provided:\n")
    st.write("a) There are about 9 automobile manufacturers that ( whose car ) costs over 1 crore per car.\n")
    st.write("b) In terms of On road price per car, the Ferrari outperforms the Datsun and Maruti Suzuki by a great margin.")
    st.write("c) After Mini there is sudden jump in the slope thus the manufacturer after Mini can be classified as Elite Manufacturers since the on road price per car is very high for these.\n")
    st.write("d) It may also be deduced that the Manufacturer Unit which are initially ( such as Maruti Suzuki, Renault, Tata, Hyundai )in the plot produces more car than those at the edge of the plot.\n")
    st.write("\n")
    st.image('manufacturermileagelineplot.png',width = 900)
    st.markdown("INSIGHTS :\n")
    st.write("The above plot is eesential for finding out those manufacturer which provide cars with good mileage. We may derive the following assertions from the data provided:\n")
    st.write("a) There are about 19 automobile manufacturers that ( whose car ) mileage is over 16 km per litres.\n")
    st.write("b) In terms of Mileage per car, the Maruti Suzuki and Datsun outperforms the elite cars such as Ferrari, Bentley, Lamborghini by a great margin. This is just opposite to the above observation where elite cars outperformed these cars in terms of On road price.\n")
    st.write("c) In India mileage of 16 km per litre is considered to be a good average, so cars in this plot afetr Kia can be considered good enough in terms of mileage.\n")
    st.write("\n")
    st.write("CONCLUSION: On the basis of the above two plots it can be concluded that manufacturers such as Maruti Suzuki, Datsun, Renault , Honda, Hyundai , etc provides cars with a good mileage along with a decent on road  price range that an average Indian Customer would pay for.\n")
    st.write("\n")
    st.write("NOTE: Lexus and Volvo are the only two Elite Cars to have a high on road price and an average mileage. It can be concluded from the above two plots.\n")

if button5:
    st.header("ABOUT Us")
    st.write("We are tem of Rajeev Joshi, Rishikesh Maurya, Shubhang Singh, Samanway Ray and Gourav Parashar")
    st.write("We are currently pursuing our undergraduation in Mechanical Engineering and Civil Engineering from Indian Institute of Technology Kharagpur.")
