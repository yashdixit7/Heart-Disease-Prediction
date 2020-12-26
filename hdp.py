import streamlit as st 
import pickle
import numpy as np 


st.title("__ Heart Disease Prediction __")

st.sidebar.title("* Prediction Examples *")
st.sidebar.markdown("--------  __ With Heart Disease __  --------")
st.sidebar.markdown("`Age`: * 37 *")
st.sidebar.markdown("`Gender`: * Male *")
st.sidebar.markdown("`Chest Pain Type`:* Non-anginal Pain *")
st.sidebar.markdown("`Blood Pressure(mmHg) `:* 130 *")
st.sidebar.markdown("`Serum Choledterol`:* 250 *")
st.sidebar.markdown("`Blood Sugar Level`:* > 120 mg/dl *")
st.sidebar.markdown("`ECG`:* Having ST-T wave abnormality *")
st.sidebar.markdown("`Maximum Heart Rate`:* 187 *")
st.sidebar.markdown("`Chest Pain due to Exercise`:* Yes *")
st.sidebar.markdown("`Slope of ST segment`:* Up-sloping *")
st.sidebar.markdown("`OLD PEAK`:* 3.5 *")
st.sidebar.markdown("`Number of Vessels colored`:* 0 *")

st.sidebar.markdown("--------  __ No Heart Disease __  --------")
st.sidebar.markdown("`Age`:* 48 *")
st.sidebar.markdown("`Gender`:* Female *")
st.sidebar.markdown("`Chest Pain Type`:* Asymptomatic *")
st.sidebar.markdown("`Blood Pressure(mmHg) `:* 132 *")
st.sidebar.markdown("`Serum Choledterol`:* 274 *")
st.sidebar.markdown("`Blood Sugar Level`:* <= 120 mg/dl *")
st.sidebar.markdown("`ECG`:* Normal *")
st.sidebar.markdown("`Maximum Heart Rate`:* 118 *")
st.sidebar.markdown("`Chest Pain due to Exercise`:* N0 *")
st.sidebar.markdown("`Slope of ST segment`:* Flat *")
st.sidebar.markdown("`OLD PEAK`:* 3.0 *")
st.sidebar.markdown("`Number of Vessels colored`:* 0 *")


cols = st.beta_columns(3)
with cols[1]:
	AGE = st.slider("| Age |", 20, 80)
#--------------------------------------------------------------------!!
cols = st.beta_columns(2)
with cols[0]:
	sex = st.selectbox("| Gender |",["Male","Female"])
	if sex == "Male":
		SEX = 1
	else:
		SEX = 0
#--------------------------------------------------------------------!!
with cols[1]:
	cp = st.selectbox("| Chest Pain Type |",["Typical Angina",
										"Atypical Angina",
										"Non-anginal Pain",
										"Asymptomatic"])

	if cp == "Typical Angina":
		CP = 1
	elif cp == "Atypical Angina":
		CP = 2
	elif cp == "Non-anginal Pain":
		CP = 3
	else:
		CP = 4
#--------------------------------------------------------------------!!
TRESTBPS = st.slider("| Blood Pressure (mmHg) |",90,200)
#--------------------------------------------------------------------!!
cols = st.beta_columns(3)
with cols[1]:
	fbs = st.selectbox("| Bood Sugar Level |",["Greater than 120 mg/dl"," Equal/Less than 120 mg/dl"])
	if fbs=="Greater than 120 mg/dl":
		FBS=1
	else:
		FBS=0
#--------------------------------------------------------------------!!
CHOL = st.slider("| Serum Cholesterol (mg/dl) |",110,560)
#--------------------------------------------------------------------!!
cols = st.beta_columns(3)
with cols[1]:
	restecg = st.selectbox("| ECG |",["Normal", 
												"Having ST-T wave abnormality",
												"Showing probable or definite left ventricularhypertrophy by Estes' criteria"])
	if restecg=="Normal":
		RESTECG = 0
	elif restecg=="Having ST-T wave abnormality":
		RESTECG = 1
	else:
		RESTECG = 2
#--------------------------------------------------------------------!!
THALACH = st.slider("| Maximum Heart Rate |",71,200)
#--------------------------------------------------------------------!!
cols = st.beta_columns(3)
with cols[0]:
	exang = st.selectbox("| Chest Pain due to Exercise |",["Yes","No"])
	if exang == "Yes":
		EXANG = 1
	else:
		EXANG = 0
#--------------------------------------------------------------------!!
with cols[1]:
	CA = st.selectbox("| Number of Vessels colored |",[0,1,2,3,4])
#--------------------------------------------------------------------!!

with cols[2]:
	slope = st.selectbox("| Slope ST segment |",["Up-sloping","Flat", "Down-sloping"])
	if slope=="Up-sloping":
		SLOPE = 0
	elif slope=="Flat":
		SLOPE = 1
	else:
		SLOPE = 2
#--------------------------------------------------------------------!!
OLDPEAK = st.slider("| OLD PEAK |",0.0,6.0,0.1)
#--------------------------------------------------------------------!!
THAL = np.random.choice([0,1,2,3])
#--------------------------------------------------------------------!!

Model = pickle.load(open("Heart-disease-prediction.pkl", "rb"))
prediction = Model.predict([[AGE,SEX,CP,TRESTBPS,CHOL,FBS,RESTECG,THALACH,EXANG,OLDPEAK,SLOPE,CA,THAL]])


if st.button("EXAMINE"):
	if prediction==1:
		st.warning("You Might have a Heart Disease. Consider Concerning a Doctor!!")
	else:
		st.success("You Have a HEALTHY HEART :)")
		st.balloons()

		

		
