import data_preprocessing as dp
import prediction as pred
import streamlit as st
import pandas as pd
import joblib

feature_columns = joblib.load("model/feature_columns.joblib")

data = pd.DataFrame(columns=feature_columns)

feature_options = {
    "Scholarship_holder": ["Yes", "No"],
    "Tuition_fees_up_to_date": ["Yes", "No"],
    "Daytime_evening_attendance": ["Daytime", "Evening"],
    "Gender": ["Male", "Female"],
    "Displaced": ["Yes", "No"],
}

value_mapping = {
    "Scholarship_holder": {"Yes": 1, "No": 0},
    "Tuition_fees_up_to_date": {"Yes": 1, "No": 0},
    "Daytime_evening_attendance": {"Daytime": 1, "Evening": 0},
    "Gender": {"Male": 1, "Female": 0},
    "application_mode": {
        "1st phase - general contingent": 1,
        "Ordinance No. 612/93": 2,
        "1st phase - special contingent (Azores Island)": 5,
        "Holders of other higher courses": 7,
        "Ordinance No. 854-B/99": 10,
        "International student (bachelor)": 15,
        "1st phase - special contingent (Madeira Island)": 16,
        "2nd phase - general contingent": 17,
        "3rd phase - general contingent": 18,
        "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
        "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
        "Over 23 years old": 39,
        "Transfer": 42,
        "Change of course": 43,
        "Technological specialization diploma holders": 44,
        "Change of institution/course": 51,
        "Short cycle diploma holders": 53,
        "Change of institution/course (International)": 57
    },
    "Displaced": {"Yes": 1, "No": 0},
}

selected_feature = ["Previous_qualification_grade", "Admission_grade", "Age_at_enrollment", "Curricular_units_1st_sem_credited", "Curricular_units_1st_sem_enrolled", "Curricular_units_1st_sem_evaluations",
                    "Curricular_units_1st_sem_approved", "Curricular_units_1st_sem_grade", "Application_order", "Application_mode", "Debtor", "Scholarship_holder", "Tuition_fees_up_to_date", "Daytime_evening_attendance", "Gender", "Displaced"]

header = st.header("Student Dropout Prediction App")
st.write("This app predicts whether a student will graduate, enroll, or dropout based on their data.")
st.write("Please fill in the following information:")
# 131.0	127.2	18	0	6	6	6	13.17	3	1	0	1	1	1	0	1	Dropout
col1, col2, col3 = st.columns(3)
with col1:
    prev_qualification = st.number_input("Previous qualification grade", min_value=0,
                                         max_value=200, value=131, step=1, key="Previous_qualification_grade")
    data['Previous_qualification_grade'] = [prev_qualification]
with col2:
    admission_grade = st.number_input("Admission grade", min_value=0, max_value=200,
                                      value=127, step=1, key="Admission_grade")
    data['Admission_grade'] = [admission_grade]
with col3:
    age_enroll = st.number_input("Age at enrollment", min_value=0,
                                 max_value=100, value=18, step=1, key="Age_at_enrollment")
    data['Age_at_enrollment'] = [age_enroll]

col1, col2, col3 = st.columns(3)
with col1:
    curr_1s_cred = st.number_input("Curricular units 1st sem credited", min_value=0,
                                   step=1, value=0, key="Curricular_units_1st_sem_credited")
    data['Curricular_units_1st_sem_credited'] = [curr_1s_cred]
with col2:
    curr_1s_enrolled = st.number_input("Curricular units 1st sem enrolled", min_value=0,
                                       max_value=100, value=0, step=1, key="Curricular_units_1st_sem_enrolled")
    data['Curricular_units_1st_sem_enrolled'] = [curr_1s_enrolled]
with col3:
    curr_1st_eval = st.number_input("Curricular units 1st sem evaluations", min_value=0,
                                    max_value=100, value=0, step=1, key="Curricular_units_1st_sem_evaluations")
    data['Curricular_units_1st_sem_evaluations'] = [curr_1st_eval]

col1, col2, col3 = st.columns(3)
with col1:
    curr_1st_approved = st.number_input("Curricular units 1st sem approved", min_value=0,
                                        max_value=100, value=0, step=1, key="Curricular_units_1st_sem_approved")
    data['Curricular_units_1st_sem_approved'] = [curr_1st_approved]
with col2:
    st.number_input("Curricular units 1st sem grade", min_value=0.0, max_value=20.0,
                    value=13.17, step=0.01, key="Curricular_units_1st_sem_grade")
    data['Curricular_units_1st_sem_grade'] = [
        st.session_state.Curricular_units_1st_sem_grade]
with col3:
    st.number_input("Application order", min_value=0, max_value=9,
                    value=3, step=1, key="Application_order")
    data['Application_order'] = [st.session_state.Application_order]

col1, col2, col3 = st.columns(3)
with col1:
    st.number_input("Debtor", min_value=0, max_value=1,
                    value=0, step=1, key="Debtor")
    data['Debtor'] = [st.session_state.Debtor]
with col2:
    st.selectbox(
        "Displaced", options=feature_options["Displaced"], index=0, key="Displaced")
    data['Displaced'] = [value_mapping["Displaced"][st.session_state.Displaced]]
with col3:
    st.selectbox("Scholarship holder",
                 options=feature_options["Scholarship_holder"], index=0, key="Scholarship_holder")
    data['Scholarship_holder'] = [value_mapping["Scholarship_holder"]
                                  [st.session_state.Scholarship_holder]]

col1, col2, col3 = st.columns(3)
with col1:
    st.selectbox("Tuition fees up to date",
                 options=feature_options["Tuition_fees_up_to_date"], index=0, key="Tuition_fees_up_to_date")
    data['Tuition_fees_up_to_date'] = [
        value_mapping["Tuition_fees_up_to_date"][st.session_state.Tuition_fees_up_to_date]]
with col2:
    st.selectbox("Daytime evening attendance",
                 options=feature_options["Daytime_evening_attendance"], index=0, key="Daytime_evening_attendance")
    data['Daytime_evening_attendance'] = [
        value_mapping["Daytime_evening_attendance"][st.session_state.Daytime_evening_attendance]]
with col3:
    st.selectbox(
        "Gender", options=feature_options["Gender"], index=0, key="Gender")
    data['Gender'] = [value_mapping["Gender"][st.session_state.Gender]]

display_options = list(value_mapping['application_mode'].keys())
default_index = display_options.index("1st phase - general contingent")
selected = st.selectbox("Application mode",
                        options=display_options, index=default_index, key="Application_mode")
data['Application_mode'] = value_mapping['application_mode'][selected]

st.divider()

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

st.divider()

if st.button('Predict'):
    new_data = dp.preprocess(data)
    with st.expander("View the Raw Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Status: {}".format(pred.prediction(new_data)))
