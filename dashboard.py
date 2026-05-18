import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Customer Retention Dashboard",
    layout="wide"
)

# -----------------------------
# SAMPLE DATA
# -----------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

retention_rate = [68.1, 69.3, 70.2, 71.4, 72.8, 73.1,
                  74.0, 74.6, 75.1, 75.9, 76.2, 76.5]

churn_rate = [6.8, 6.6, 6.4, 6.2, 6.0, 5.9,
              5.8, 5.7, 5.6, 5.5, 5.6, 5.6]

cohort_data = pd.DataFrame({
    "Cohort": ["Jan 2024", "Feb 2024", "Mar 2024",
               "Apr 2024", "May 2024", "Jun 2024"],
    "1": [100, 100, 100, 100, 100, 100],
    "2": [80, 82, 83, 84, 86, None],
    "3": [65, 67, 69, 71, None, None],
    "4": [55, 57, 59, None, None, None],
    "5": [45, 47, None, None, None, None],
    "6": [35, None, None, None, None, None]
})

retention_segments = pd.DataFrame({
    "Segment": [
        "VIP Customers",
        "Loyal Customers",
        "Regular Customers",
        "New Customers",
        "At Risk Customers"
    ],
    "Retention": [90.2, 82.7, 71.3, 52.6, 31.4]
})

churn_segments = pd.DataFrame({
    "Segment": [
        "At Risk Customers",
        "New Customers",
        "Regular Customers",
        "Loyal Customers",
        "VIP Customers"
    ],
    "Churn": [15.8, 9.7, 5.1, 2.3, 1.2]
})

churn_reasons = pd.DataFrame({
    "Reason": [
        "Too Expensive",
        "Found Better Product",
        "Not Using Enough",
        "Poor Customer Service",
        "Missing Features",
        "Other"
    ],
    "Percent": [32, 21, 16, 12, 9, 10]
})

# -----------------------------
# HEADER
# -----------------------------

st.title("CUSTOMER RETENTION ANALYSIS")
st.write("Overview of customer retention performance and trends")

# -----------------------------
# KPI CARDS
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Retention Rate",
        value="76.5%",
        delta="8.4%"
    )

with col2:
    st.metric(
        label="Retained Customers",
        value="12,842",
        delta="1,234"
    )

with col3:
    st.metric(
        label="Repeat Purchase Rate",
        value="65.3%",
        delta="6.7%"
    )

with col4:
    st.metric(
        label="Revenue From Retained Customers",
        value="$2.45M",
        delta="12.6%"
    )

# -----------------------------
# RETENTION SECTION
# -----------------------------

left, middle, right = st.columns([1.2, 1, 1])

# Retention Over Time
with left:
    fig_retention = go.Figure()

    fig_retention.add_trace(go.Scatter(
        x=months,
        y=retention_rate,
        mode='lines+markers',
        line=dict(color='blue', width=3),
        marker=dict(size=8),
        name="Retention Rate"
    ))

    fig_retention.update_layout(
        title="Retention Rate Over Time",
        yaxis_title="Retention %",
        template="plotly_white",
        height=400
    )

    st.plotly_chart(fig_retention, use_container_width=True)

# Cohort Heatmap
with middle:
    heatmap_data = cohort_data.set_index("Cohort")

    fig_heatmap = px.imshow(
        heatmap_data,
        text_auto=True,
        color_continuous_scale="Blues",
        aspect="auto"
    )

    fig_heatmap.update_layout(
        title="Retention Rate by Cohort",
        height=400
    )

    st.plotly_chart(fig_heatmap, use_container_width=True)

# Retention Segment
with right:
    fig_segment = px.bar(
        retention_segments,
        x="Retention",
        y="Segment",
        orientation="h",
        color="Retention",
        color_continuous_scale="Greens"
    )

    fig_segment.update_layout(
        title="Retention Rate by Customer Segment",
        template="plotly_white",
        height=400,
        showlegend=False
    )

    st.plotly_chart(fig_segment, use_container_width=True)

# -----------------------------
# CHURN SECTION
# -----------------------------

st.markdown("---")
st.title("CUSTOMER CHURN ANALYSIS")
st.write("Overview of customer churn performance and insights")

# KPI CARDS
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Churn Rate",
        value="5.6%",
        delta="-1.2%"
    )

with col2:
    st.metric(
        label="Churned Customers",
        value="942",
        delta="-210"
    )

with col3:
    st.metric(
        label="Risk At Risk",
        value="1,287",
        delta="-189"
    )

with col4:
    st.metric(
        label="Revenue Lost",
        value="$198K",
        delta="-18.7%"
    )

# -----------------------------
# CHURN CHARTS
# -----------------------------

left2, middle2, right2 = st.columns([1.2, 1, 1])

# Churn Trend
with left2:
    fig_churn = go.Figure()

    fig_churn.add_trace(go.Scatter(
        x=months,
        y=churn_rate,
        mode='lines+markers',
        line=dict(color='red', width=3),
        marker=dict(size=8),
        name="Churn Rate"
    ))

    fig_churn.update_layout(
        title="Churn Rate Over Time",
        yaxis_title="Churn %",
        template="plotly_white",
        height=400
    )

    st.plotly_chart(fig_churn, use_container_width=True)

# Churn Reasons Pie
with middle2:
    fig_pie = px.pie(
        churn_reasons,
        names="Reason",
        values="Percent",
        hole=0.45,
        color_discrete_sequence=px.colors.sequential.Reds
    )

    fig_pie.update_layout(
        title="Churn Reasons",
        height=400
    )

    st.plotly_chart(fig_pie, use_container_width=True)

# Churn Segment
with right2:
    fig_churn_seg = px.bar(
        churn_segments,
        x="Churn",
        y="Segment",
        orientation="h",
        color="Churn",
        color_continuous_scale="Reds"
    )

    fig_churn_seg.update_layout(
        title="Churn Rate by Customer Segment",
        template="plotly_white",
        height=400,
        showlegend=False
    )

    st.plotly_chart(fig_churn_seg, use_container_width=True)

# -----------------------------
# KEY INSIGHTS
# -----------------------------

st.markdown("---")
st.subheader("Key Insights")

st.success("Retention rate improved by 8.4% compared to last period.")
st.warning("At-risk customers show the highest churn rate at 15.8%.")
st.info("VIP customers maintain the strongest retention at 90.2%.")
st.error("Top churn reason: Customers found the product too expensive.")

# -----------------------------
# FOOTER
# -----------------------------

st.caption("Customer Analytics Dashboard | Python + Streamlit + Plotly")