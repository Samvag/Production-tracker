import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Data structure for production metrics
production_data = {
    'Metric': ['Production Output', 'Production Costs', 'Raw Material Turnover', 'Production Waste (kg)', 'Energy Consumption (kWh)', 'Product A Output', 'Product B Output', 'Product C Output', 'Product D Output', 'Product E Output', 'Product Quality (Defects)', 'Safety Incidents'],
    'Target': [10000, 50000, 1000, 50, 2000, 2000, 2000, 2000, 2000, 2000, 5, 0],
    'Actual': [9500, 52000, 1100, 60, 2100, 1800, 1900, 2000, 1950, 1850, 7, 1],
    'Status': ['Delayed', 'Issue', 'On Track', 'Issue', 'Issue', 'On Track', 'Delayed', 'On Track', 'On Track', 'Delayed', 'Issue', 'Issue'],
    'Problem Area': ['Downtime', 'Increased material costs', 'Inventory management', 'Waste reduction needed', 'Energy usage high', 'Production inefficiencies', 'Material shortages', 'Stable output', 'Stable output', 'Stable output', 'Increased defects', 'Safety protocols'],
    'Potential Solution': ['Preventive maintenance', 'Cost control initiatives', 'Better inventory management', 'Implement waste reduction', 'Energy-saving technologies', 'Improve machine efficiency', 'Improve material availability', 'Monitor closely', 'Monitor closely', 'Monitor closely', 'Enhanced QA processes', 'Staff safety training']
}

# Convert to DataFrame
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
    'Due Date': [datetime.now() + timedelta(days=30), datetime.now() + timedelta(days=20), datetime.now() + timedelta(days=15), datetime.now() + timedelta(days=25)],
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

# Title and description
st.title("Production Plant Health Check and Productivity Improvement Dashboard")
st.write("""
This dashboard tracks key performance metrics, identifies problem areas, tracks productivity improvement initiatives, and helps plant managers manage tasks with action items, deadlines, and potential benefits.
""")

# Display production metrics
st.write("### Production Metrics")
st.data_editor(df, use_container_width=True)

# Productivity Improvement Section
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
        # Use pd.concat instead of append
        prod_df = pd.concat([prod_df, pd.DataFrame([new_prod_entry])], ignore_index=True)
        st.success("New productivity improvement data added successfully!")

# Display Productivity Improvement Data
st.write("### Current Productivity Improvements")
st.data_editor(prod_df, use_container_width=True)

# Send Alert Notifications (dummy for now, could be linked to email or messaging service)
st.write("#### Alert Notifications")
for index, row in prod_df.iterrows():
    if row['Due Date'] <= datetime.now().date() and row['Status'] != 'Completed':
        st.warning(f"Action '{row['Training Needs']}' assigned to {row['Assigned User']}' is overdue!")

# Action Item Tracker Section
st.write("### Action Item Tracker")
st.write("Action items assigned to team members with due dates and projected benefits:")
st.data_editor(action_df, use_container_width=True)

# Dashboard Section: Metrics
st.write("### Dashboard: Action Items and Productivity Metrics")

# Calculate the number of open, closed, and in-progress items
open_items = len(action_df[action_df['Status'] == 'Open'])
in_progress_items = len(action_df[action_df['Status'] == 'In Progress'])
completed_items = len(action_df[action_df['Status'] == 'Completed'])

st.write(f"**Number of Action Items Planned:** {len(action_df)}")
st.write(f"**Number of Action Items Open:** {open_items}")
st.write(f"**Number of Action Items In Progress:** {in_progress_items}")
st.write(f"**Number of Action Items Closed:** {completed_items}")

# Projected benefits for the current month (editable by users)
st.write("#### Projected Benefits for the Current Month")
benefits = [
    "Increased outputs: 10%",
    "Lower costs: 8% reduction in energy costs",
    "Reduced time: 12% decrease in downtime"
]
benefits_input = st.text_area("Edit Projected Benefits", "\n".join(benefits), height=100)

# --- New Visualizations ---

# 1. Monthly Production Output Trend (Line Chart)
st.write("### Monthly Production Output Trend")
fig1, ax1 = plt.subplots()
ax1.plot(months, monthly_production, marker='o', linestyle='-', color='blue', label='Production Output')
ax1.plot(months, monthly_production_costs, marker='o', linestyle='-', color='green', label='Production Costs')
ax1.plot(months, monthly_raw_material_turnover, marker='o', linestyle='-', color='purple', label='Raw Material Turnover')
ax1.set_title("Monthly Production Output, Costs, and Raw Material Turnover")
ax1.set_xlabel("Month")
ax1.set_ylabel("Value")
ax1.legend()
st.pyplot(fig1)

# 2. Energy Consumption vs Production Output (Scatter Plot)
st.write("### Energy Consumption vs Production Output")
fig2, ax2 = plt.subplots()
ax2.scatter(monthly_energy, monthly_production, color='green')
ax2.set_title("Energy Consumption vs Production Output")
ax2.set_xlabel("Energy Consumption (kWh)")
ax2.set_ylabel("Production Output")
st.pyplot(fig2)

# 3. Defects and Safety Incidents Over Time (Bar Chart)
st.write("### Defects and Safety Incidents Over Time")
fig3, ax3 = plt.subplots()
ax3.bar(months, monthly_defects, width=0.4, label="Defects", color='red', align='center')
ax3.bar(months, monthly_safety_incidents, width=0.4, label="Safety Incidents", color='orange', align='edge')
ax3.set_title("Monthly Defects and Safety Incidents")
ax3.set_xlabel("Month")
ax3.set_ylabel("Count")
ax3.legend()
st.pyplot(fig3)

# Visualization for Action Items Status
st.write("### Action Items Status Distribution")
fig, ax = plt.subplots()
ax.pie([open_items, in_progress_items, completed_items], 
       labels=['Open', 'In Progress', 'Completed'], 
       autopct='%1.1f%%', 
       colors=['orange', 'blue', 'green'])  # Added the closing of colors list and parentheses
ax.set_title("Action Items Status Distribution")
st.pyplot(fig)
