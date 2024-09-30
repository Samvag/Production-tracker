import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# --- Initialize DataFrames ---
# Ensure these DataFrames are defined at the top of the script and are globally accessible
production_data = {
    'Metric': ['Production Output', 'Production Costs', 'Raw Material Turnover', 'Production Waste (kg)', 'Energy Consumption (kWh)', 
               'Product A Output', 'Product B Output', 'Product C Output', 'Product D Output', 'Product E Output', 
               'Product Quality (Defects)', 'Safety Incidents'],
    'Target': [10000, 50000, 1000, 50, 2000, 2000, 2000, 2000, 2000, 2000, 5, 0],
    'Actual': [9500, 52000, 1100, 60, 2100, 1800, 1900, 2000, 1950, 1850, 7, 1],
    'Status': ['Delayed', 'Issue', 'On Track', 'Issue', 'Issue', 'On Track', 'Delayed', 'On Track', 'On Track', 
               'Delayed', 'Issue', 'Issue'],
    'Problem Area': ['Downtime', 'Increased material costs', 'Inventory management', 'Waste reduction needed', 
                     'Energy usage high', 'Production inefficiencies', 'Material shortages', 'Stable output', 
                     'Stable output', 'Stable output', 'Increased defects', 'Safety protocols'],
    'Potential Solution': ['Preventive maintenance', 'Cost control initiatives', 'Better inventory management', 
                           'Implement waste reduction', 'Energy-saving technologies', 'Improve machine efficiency', 
                           'Improve material availability', 'Monitor closely', 'Monitor closely', 'Monitor closely', 
                           'Enhanced QA processes', 'Staff safety training']
}
df = pd.DataFrame(production_data)

# Data for productivity improvements
productivity_data = {
    'Training Needs': [],
    'Suggested Workflow Changes': [],
    'Due Date': [],
    'Assigned User': [],
    'Status': [],
}
prod_df = pd.DataFrame(productivity_data)

# Sample action item tracking
action_data = {
    'Action Item': ['Reduce downtime', 'Optimize energy use', 'Improve safety', 'Enhance quality control'],
    'Assigned To': ['Maintenance Lead', 'Energy Manager', 'Safety Officer', 'Quality Manager'],
    'Due Date': [datetime.now() + timedelta(days=30), datetime.now() + timedelta(days=20), 
                 datetime.now() + timedelta(days=15), datetime.now() + timedelta(days=25)],
    'Status': ['Open', 'Open', 'In Progress', 'Open'],
    'Projected Benefit': ['Increased uptime', 'Lower costs', 'Fewer incidents', 'Better product consistency'],
}
action_df = pd.DataFrame(action_data)

# Sample Monthly Data for Visualizations (dummy data)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthly_production = [900, 1200, 1500, 1300, 1600, 1400, 1700, 1800, 1600, 1900, 2000, 2100]
monthly_production_costs = [40000, 42000, 45000, 44000, 47000, 46000, 48000, 50000, 49000, 51000, 52000, 53000]
monthly_raw_material_turnover = [800, 850, 900, 850, 950, 1000, 1100, 1050, 1150, 1200, 1250, 1300]
monthly_energy = [450, 500, 520, 480, 550, 540, 600, 620, 580, 600, 610, 630]
monthly_defects = [5, 4, 3, 6, 7, 3, 2, 4, 5, 3, 2, 4]
monthly_safety_incidents = [2, 0, 1, 2, 1, 3, 0, 1, 0, 2, 1, 0]

# Sidebar Menu
st.sidebar.title("Production Dashboard Menu")
menu_options = st.sidebar.radio(
    "Choose a section:",
    ("Overview", "Production Metrics", "Productivity Improvement", "Action Item Tracker", "Data Persistence", "Monthly Trends", 
     "Visual Analysis", "Reports & Analytics", "Settings & Configurations")
)

# Utility functions for data persistence
def save_data(dataframe, filename):
    dataframe.to_csv(filename, index=False)
    st.sidebar.success(f"Data saved as {filename}")

def load_data(filename):
    try:
        loaded_df = pd.read_csv(filename)
        st.sidebar.success(f"Data loaded from {filename}")
        return loaded_df
    except FileNotFoundError:
        st.sidebar.error(f"No saved data found for {filename}")
        return pd.DataFrame()  # Return an empty DataFrame if file is not found

# Handling Menu Selections
if menu_options == "Overview":
    st.title("Production Plant Health Check and Productivity Improvement Dashboard")
    st.write("""
    This dashboard tracks key performance metrics, identifies problem areas, tracks productivity improvement initiatives, 
    and helps plant managers manage tasks with action items, deadlines, and potential benefits.
    """)

elif menu_options == "Production Metrics":
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
    fig1, ax1 = plt.subplots()
    ax1.plot(months, monthly_production, marker='o', label='Production Output')
    ax1.set_title("Monthly Production Output")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Output")
    ax1.legend()
    st.pyplot(fig1)

elif menu_options == "Visual Analysis":
    st.write("### Visual Analysis")
    fig2, ax2 = plt.subplots()
    ax2.scatter(monthly_energy, monthly_production, color='green')
    ax2.set_title("Energy Consumption vs Production Output")
    ax2.set_xlabel("Energy Consumption (kWh)")
    ax2.set_ylabel("Production Output")
    st.pyplot(fig2)

elif menu_options == "Reports & Analytics":
    st.write("### Reports & Analytics")
    benefits = ["Increased outputs: 10%", "Lower costs: 8% reduction in energy costs", "Reduced time: 12% decrease in downtime"]
    benefits_input = st.text_area("Edit Projected Benefits", "\n".join(benefits), height=100)

elif menu_options == "Settings & Configurations":
    st.write("### Settings & Configurations")
    st.write("Manage system configurations, alert settings, and more.")

# Provide an option to download the current data
st.sidebar.write("### Download Data")
if 'df' in globals() and not df.empty:
    csv_data = df.to_csv(index=False)
    st.sidebar.download_button(
        label="Download Production Data as CSV",
        data=csv_data,
        file_name="production_data.csv",
        mime="text/csv"
    )
else:
    st.sidebar.write("No data available for download.")
