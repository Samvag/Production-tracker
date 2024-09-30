import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define Sidebar Menu
st.sidebar.title("Production Dashboard Menu")

menu_options = st.sidebar.radio(
    "Choose a section:",
    ("Overview", "Production Metrics", "Productivity Improvement", "Action Item Tracker", "Data Persistence", "Monthly Trends", "Visual Analysis", "Reports & Analytics", "Settings & Configurations")
)

# Function to save DataFrame to a CSV file
def save_data(df, filename):
    df.to_csv(filename, index=False)
    st.sidebar.success(f"Data saved as {filename}")

# Function to load DataFrame from a CSV file
def load_data(filename):
    try:
        df = pd.read_csv(filename)
        st.sidebar.success(f"Data loaded from {filename}")
        return df
    except FileNotFoundError:
        st.sidebar.error(f"No saved data found for {filename}")
        return pd.DataFrame()

# Display relevant section based on the menu selection
if menu_options == "Overview":
    st.title("Production Plant Health Check and Productivity Improvement Dashboard")
    st.write("""
    This dashboard tracks key performance metrics, identifies problem areas, tracks productivity improvement initiatives, and helps plant managers manage tasks with action items, deadlines, and potential benefits.
    """)

elif menu_options == "Production Metrics":
    # Display production metrics
    st.write("### Production Metrics")
    st.data_editor(df, use_container_width=True)

elif menu_options == "Productivity Improvement":
    st.write("### Productivity Improvement")
    st.write("#### Add Training Needs and Workflow Suggestions")
    
    with st.form("productivity_form"):
        training_needs = st.text_input("Training Needs (Individual/Group)")
        workflow_suggestion = st.text_input("Suggested Workflow Change")
        due_date = st.date_input("Due Date")
        assigned_user = st.text_input("Assigned User")
        action_status = st.selectbox("Status", ['Open', 'In Progress', 'Completed'])
        
        submitted_prod = st.form_submit_button("Add Productivity Improvement")

        if submitted_prod:
            new_prod_entry = {
                'Training Needs': training_needs,
                'Suggested Workflow Changes': workflow_suggestion,
                'Due Date': due_date,
                'Assigned User': assigned_user,
                'Status': action_status
            }
            prod_df = pd.concat([prod_df, pd.DataFrame([new_prod_entry])], ignore_index=True)
            st.success("New productivity improvement data added successfully!")

    st.write("### Current Productivity Improvements")
    st.data_editor(prod_df, use_container_width=True)

elif menu_options == "Action Item Tracker":
    st.write("### Action Item Tracker")
    st.write("Action items assigned to team members with due dates and projected benefits:")
    st.data_editor(action_df, use_container_width=True)

elif menu_options == "Data Persistence":
    st.write("### Data Persistence")
    if st.sidebar.button("Save Production Data"):
        save_data(df, "production_data.csv")
        
    if st.sidebar.button("Load Production Data"):
        df = load_data("production_data.csv")
        
    if st.sidebar.button("Save Productivity Improvements"):
        save_data(prod_df, "productivity_data.csv")
        
    if st.sidebar.button("Load Productivity Improvements"):
        prod_df = load_data("productivity_data.csv")
        
    if st.sidebar.button("Save Action Items"):
        save_data(action_df, "action_items.csv")
        
    if st.sidebar.button("Load Action Items"):
        action_df = load_data("action_items.csv")

elif menu_options == "Monthly Trends":
    st.write("### Monthly Production Trends")
    st.write("Visual representation of production data over the months.")

    # Display monthly trends visualizations
    fig1, ax1 = plt.subplots()
    ax1.plot(months, monthly_production, marker='o', label='Production Output')
    ax1.set_title("Monthly Production Output")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Output")
    ax1.legend()
    st.pyplot(fig1)

elif menu_options == "Visual Analysis":
    st.write("### Visual Analysis")
    
    # Display energy consumption vs production
    fig2, ax2 = plt.subplots()
    ax2.scatter(monthly_energy, monthly_production, color='green')
    ax2.set_title("Energy Consumption vs Production Output")
    ax2.set_xlabel("Energy Consumption (kWh)")
    ax2.set_ylabel("Production Output")
    st.pyplot(fig2)
    
    fig3, ax3 = plt.subplots()
    ax3.bar(months, monthly_defects, width=0.4, label="Defects", color='red', align='center')
    ax3.bar(months, monthly_safety_incidents, width=0.4, label="Safety Incidents", color='orange', align='edge')
    ax3.set_title("Monthly Defects and Safety Incidents")
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Count")
    ax3.legend()
    st.pyplot(fig3)

elif menu_options == "Reports & Analytics":
    st.write("### Reports & Analytics")
    st.write("Provide in-depth analysis, download reports, and examine the monthly projections and insights.")
    
    benefits_input = st.text_area("Projected Benefits for the Current Month", "\n".join(benefits), height=100)
    
elif menu_options == "Settings & Configurations":
    st.write("### Settings & Configurations")
    st.write("Manage system configurations, alert settings, and more.")

# Provide an option to download the current data
st.sidebar.write("### Download Data")
csv_data = df.to_csv(index=False)
st.sidebar.download_button(
    label="Download Production Data as CSV",
    data=csv_data,
    file_name="production_data.csv",
    mime="text/csv"
)
