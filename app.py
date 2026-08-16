import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="DataShadow",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =================================================
# CUSTOM CSS
# =================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap');

/* ---------- MAIN APP ---------- */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(124, 58, 237, 0.15), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(59, 130, 246, 0.15), transparent 30%),
        linear-gradient(135deg, #eef2ff 0%, #f8fafc 50%, #f5f3ff 100%);
    font-family: 'DM Sans', sans-serif;
    color: #172033;
}


/* ---------- MAIN CONTAINER ---------- */

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}


/* ---------- HEADINGS ---------- */

h1, h2, h3 {
    font-family: 'Outfit', sans-serif !important;
    color: #172033 !important;
}

h2 {
    font-size: 1.7rem !important;
    font-weight: 700 !important;
}


/* ---------- NORMAL TEXT ---------- */

p, span, label, .stMarkdown {
    color: #334155;
}


/* ---------- SIDEBAR ---------- */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #16102e 0%,
        #21174a 50%,
        #302160 100%
    );
    border-right: none;
}

[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

[data-testid="stSidebar"] .stRadio label {
    border-radius: 10px;
    padding: 8px 10px;
    transition: 0.2s;
}


/* ---------- DATAFRAME ---------- */

[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid #dbe3f0;
}


/* ---------- METRIC CARDS ---------- */

[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.85);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(226, 232, 240, 0.9);
    box-shadow: 0 8px 25px rgba(80, 70, 140, 0.08);
    min-height: 125px;
}

[data-testid="stMetricLabel"] {
    font-size: 14px;
    font-weight: 600;
    color: #64748b !important;
}

[data-testid="stMetricValue"] {
    font-family: 'Outfit', sans-serif;
    font-size: 30px;
    font-weight: 700;
    color: #241b4f !important;
}


/* ---------- BUTTONS ---------- */

.stButton > button {
    background: linear-gradient(135deg, #6d4aff, #8b5cf6);
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: 600;
}


/* ---------- SELECT BOX ---------- */

[data-baseweb="select"] {
    background-color: white;
    border-radius: 10px;
}


/* ---------- FILE UPLOADER ---------- */

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.08);
    border: 1px dashed rgba(255,255,255,0.35);
    padding: 10px;
    border-radius: 14px;
}


/* ---------- DIVIDER ---------- */

hr {
    border-color: #dbe3f0 !important;
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
}


/* ---------- HERO ---------- */

.hero {
    background: linear-gradient(
        135deg,
        #21194a,
        #39286e 55%,
        #5b3fa8
    );
    padding: 34px 40px;
    border-radius: 24px;
    margin-bottom: 28px;
    box-shadow: 0 15px 40px rgba(61, 43, 120, 0.20);
}

.hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 46px;
    font-weight: 800;
    color: white !important;
    margin: 0;
}

.hero-subtitle {
    color: #dcd5ff !important;
    font-size: 17px;
    margin-top: 6px;
}


/* ---------- SECTION CARD ---------- */

.section-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 8px 25px rgba(30,41,59,0.06);
}


/* ---------- ALERTS ---------- */

[data-testid="stAlert"] {
    border-radius: 14px;
}


/* ---------- PLOTLY CHART ---------- */

[data-testid="stPlotlyChart"] {
    background: white;
    padding: 10px;
    border-radius: 18px;
    border: 1px solid #e2e8f0;
}


/* ---------- HIDE STREAMLIT BRANDING ---------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)


# =================================================
# HEADER
# =================================================

st.markdown("""
<div class="hero">
    <div class="hero-title">◈ DataShadow</div>
    <div class="hero-subtitle">
        Automated Data Intelligence, Quality Auditing & Pattern Discovery
    </div>
</div>
""", unsafe_allow_html=True)


# =================================================
# SIDEBAR
# =================================================

st.sidebar.markdown("## ◈ DataShadow")
st.sidebar.markdown(
    "<p style='color:#b9b1e5 !important;'>DATA INTELLIGENCE PLATFORM</p>",
    unsafe_allow_html=True
)

st.sidebar.divider()

page = st.sidebar.radio(
    "EXPLORE",
    [
        "Overview",
        "Data Quality",
        "Pattern Discovery",
        "Anomalies",
        "Visual Explorer"
    ]
)

st.sidebar.divider()

uploaded_file = st.sidebar.file_uploader(
    "Upload Dataset",
    type=["csv"]
)

st.sidebar.divider()

st.sidebar.markdown(
    """
    <div style='
        text-align: center;
        color: #b9b1e5;
        font-size: 13px;
        padding-top: 10px;
    '>
        ◈ DataShadow<br>
        <span style='font-size: 11px;'>
            Automated Data Intelligence
        </span>
    </div>
    """,
    unsafe_allow_html=True
)


# =================================================
# NO DATASET
# =================================================

if uploaded_file is None:

    st.markdown("## Welcome to DataShadow")

    st.markdown("""
    <div class="section-card">
        <h3>Start your investigation</h3>
        <p>
            Upload a CSV dataset from the sidebar and DataShadow will
            automatically inspect your data, evaluate quality, discover
            patterns and identify unusual records.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.stop()


# =================================================
# LOAD DATA
# =================================================

df = pd.read_csv(uploaded_file)

total_records = df.shape[0]
total_features = df.shape[1]

missing_values = df.isnull().sum().sum()
duplicate_rows = df.duplicated().sum()

numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

categorical_columns = df.select_dtypes(
    exclude=np.number
).columns.tolist()


# =================================================
# QUALITY SCORE
# =================================================

total_cells = total_records * total_features

completeness = (
    ((total_cells - missing_values) / total_cells) * 100
    if total_cells > 0
    else 0
)

uniqueness = (
    ((total_records - duplicate_rows) / total_records) * 100
    if total_records > 0
    else 0
)

data_quality_score = round(
    (completeness + uniqueness) / 2,
    1
)

# =================================================
# ANALYSIS REPORT
# =================================================

report = f"""
DATASHADOW - DATA ANALYSIS REPORT
{'=' * 45}

DATASET OVERVIEW
-----------------
Total Records: {total_records}
Total Features: {total_features}

DATA COMPOSITION
----------------
Numerical Columns: {len(numeric_columns)}
Categorical Columns: {len(categorical_columns)}

DATA QUALITY
------------
Missing Values: {missing_values}
Duplicate Records: {duplicate_rows}
Completeness Score: {completeness:.1f}%
Uniqueness Score: {uniqueness:.1f}%
Overall Quality Score: {data_quality_score}/100
"""

# =================================================
# OVERVIEW
# =================================================

if page == "Overview":

    st.markdown("## Dataset Overview")
    st.caption("A high-level snapshot of your uploaded dataset")

    # METRIC CARDS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("TOTAL RECORDS", f"{total_records:,}")

    with col2:
        st.metric("FEATURES", total_features)

    with col3:
        st.metric("MISSING VALUES", f"{missing_values:,}")

    with col4:
        st.metric(
            "QUALITY SCORE",
            f"{data_quality_score}/100"
        )

    st.download_button(
        label="📄 Download Analysis Report",
        data=report,
        file_name="datashadow_analysis_report.txt",
        mime="text/plain",
        use_container_width=True
        )

    st.write("")

    # DATASET PREVIEW + STRUCTURE
    left, right = st.columns(2, gap="large")

    with left:

        st.markdown("### Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True,
            hide_index=True,
            height=420
        )

    with right:

        st.markdown("### Dataset Structure")

        structure_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str).values,
            "Missing": df.isnull().sum().values,
            "Unique": df.nunique().values
        })

        st.dataframe(
            structure_df,
            use_container_width=True,
            hide_index=True,
            height=420
        )

    st.divider()

    # SMART INSIGHTS
    st.markdown("## 🧠 Smart Insights")
    st.caption("Automatically generated observations about your dataset")

    insight_col1, insight_col2 = st.columns(2, gap="large")

    with insight_col1:

        st.markdown("### Dataset Composition")

        st.info(
            f"This dataset contains **{total_features} features**, "
            f"including **{len(numeric_columns)} numerical columns** "
            f"and **{len(categorical_columns)} categorical columns**."
        )

        if missing_values == 0:

            st.success(
                "The dataset contains no missing values."
            )

        else:

            missing_by_column = df.isnull().sum()

            highest_missing_column = (
                missing_by_column.idxmax()
            )

            highest_missing_count = (
                missing_by_column.max()
            )

            st.warning(
                f"**{highest_missing_column}** contains the highest "
                f"number of missing values "
                f"({highest_missing_count})."
            )


    with insight_col2:

        st.markdown("### Data Integrity")

        if duplicate_rows == 0:

            st.success(
                "No duplicate records were detected."
            )

        else:

            st.warning(
                f"{duplicate_rows} duplicate records were detected."
            )

        if data_quality_score >= 95:

            st.success(
                "The dataset currently has excellent overall data quality."
            )

        elif data_quality_score >= 80:

            st.info(
                "The dataset has good quality but may require minor cleaning."
            )

        else:

            st.error(
                "The dataset requires significant cleaning before analysis."
            )

    st.divider()

    st.markdown("### 🔗 Relationship Insight")

    if len(numeric_columns) < 2:

        st.info(
            "At least two numerical columns are required "
            "to discover relationships."
        )

    else:

        correlation_matrix = df[numeric_columns].corr()

        correlation_pairs = (
            correlation_matrix
            .where(
                np.triu(
                    np.ones(correlation_matrix.shape),
                    k=1
                ).astype(bool)
            )
            .stack()
        )

        if not correlation_pairs.empty:

            strongest_pair = correlation_pairs.abs().idxmax()

            strongest_value = correlation_pairs.loc[
                strongest_pair
            ]

            column_1, column_2 = strongest_pair

            direction = (
                "positive"
                if strongest_value > 0
                else "negative"
            )

            strength = abs(strongest_value)

            if strength >= 0.8:
                relationship_strength = "very strong"

            elif strength >= 0.6:
                relationship_strength = "strong"

            elif strength >= 0.4:
                relationship_strength = "moderate"

            else:
                relationship_strength = "weak"

            st.success(
                f"The strongest relationship in this dataset is between "
                f"**{column_1}** and **{column_2}**. "
                f"It shows a **{relationship_strength} {direction} "
                f"correlation** of **{strongest_value:.3f}**."
            )            
# =================================================
# DATA QUALITY
# =================================================

elif page == "Data Quality":

    st.markdown("## Data Quality Audit")
    st.caption(
        "Evaluate the completeness, uniqueness and overall reliability "
        "of your dataset."
    )

    # ---------------------------------------------
    # QUALITY METRICS
    # ---------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "COMPLETENESS",
            f"{completeness:.1f}%"
        )

    with col2:
        st.metric(
            "UNIQUENESS",
            f"{uniqueness:.1f}%"
        )

    with col3:
        st.metric(
            "OVERALL QUALITY",
            f"{data_quality_score}/100"
        )

    st.write("")

    # ---------------------------------------------
    # QUALITY BREAKDOWN
    # ---------------------------------------------

    st.markdown("### Quality Breakdown")

    quality_df = pd.DataFrame({
        "Metric": [
            "Completeness",
            "Uniqueness"
        ],
        "Score": [
            completeness,
            uniqueness
        ]
    })

    fig = px.bar(
        quality_df,
        x="Metric",
        y="Score",
        text="Score",
        range_y=[0, 100]
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    fig.update_layout(
        title="Dataset Quality Metrics",
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="#172033"),
        yaxis_title="Quality Score (%)",
        xaxis_title="",
        margin=dict(l=20, r=20, t=60, b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ---------------------------------------------
    # ISSUE ANALYSIS
    # ---------------------------------------------

    left, right = st.columns(2, gap="large")

    with left:

        st.markdown("### Missing Value Analysis")

        missing_df = pd.DataFrame({
            "Column": df.columns,
            "Missing Values": df.isnull().sum().values
        })

        missing_df = missing_df[
            missing_df["Missing Values"] > 0
        ].sort_values(
            by="Missing Values",
            ascending=False
        )

        if missing_df.empty:

            st.success(
                "No missing values detected in the dataset."
            )

        else:

            st.warning(
                f"{missing_values} missing values were detected "
                f"across {len(missing_df)} columns."
            )

            st.dataframe(
                missing_df,
                use_container_width=True,
                hide_index=True
            )

    with right:

        st.markdown("### Duplicate Analysis")

        duplicate_percentage = (
            (duplicate_rows / total_records) * 100
            if total_records > 0
            else 0
        )

        st.metric(
            "Duplicate Records",
            duplicate_rows,
            f"{duplicate_percentage:.2f}% of dataset"
        )

        if duplicate_rows == 0:

            st.success(
                "No duplicate records were detected."
            )

        else:

            st.warning(
                "Duplicate records may affect the reliability "
                "of analysis results."
            )

    st.divider()

    # ---------------------------------------------
    # AUTOMATIC QUALITY ASSESSMENT
    # ---------------------------------------------

    st.markdown("### 🧠 Automatic Assessment")

    if data_quality_score >= 95:

        st.success(
            "Excellent data quality detected. The dataset is highly "
            "complete and contains very few or no duplicate records."
        )

    elif data_quality_score >= 80:

        st.info(
            "Good data quality detected. The dataset is generally "
            "suitable for analysis, but some cleaning may improve reliability."
        )

    elif data_quality_score >= 60:

        st.warning(
            "Moderate data quality detected. Missing values or duplicate "
            "records should be addressed before deeper analysis."
        )

    else:

        st.error(
            "Poor data quality detected. Significant cleaning is recommended "
            "before using this dataset for analysis or modeling."
        )




# =================================================
# PATTERN DISCOVERY
# =================================================

elif page == "Pattern Discovery":

    st.markdown("## Pattern Discovery")
    st.caption("Explore relationships and hidden connections")

    if len(numeric_columns) < 2:

        st.warning(
            "At least two numerical columns are required."
        )

    else:

        correlation = df[numeric_columns].corr()

        fig = px.imshow(
            correlation,
            text_auto=".2f",
            aspect="auto"
        )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="#172033")
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("### Strongest Relationships")

        corr_pairs = (
            correlation
            .where(
                np.triu(
                    np.ones(correlation.shape),
                    k=1
                ).astype(bool)
            )
            .stack()
            .sort_values(
                key=lambda x: abs(x),
                ascending=False
            )
        )

        for (column_1, column_2), value in corr_pairs.head(5).items():

            direction = (
                "positive"
                if value > 0
                else "negative"
            )

            st.info(
                f"{column_1} and {column_2} show a "
                f"{direction} relationship "
                f"(correlation: {value:.3f})"
            )
# =================================================
# ANOMALY DETECTION
# =================================================

elif page == "Anomalies":

    st.markdown("## Anomaly Detection")
    st.caption(
        "Identify statistically unusual observations using the "
        "Interquartile Range (IQR) method."
    )

    if not numeric_columns:

        st.warning(
            "No numerical columns are available for anomaly detection."
        )

    else:

        selected_column = st.selectbox(
            "Select a numerical feature to investigate",
            numeric_columns
        )

        series = df[selected_column].dropna()

        # ---------------------------------------------
        # IQR CALCULATION
        # ---------------------------------------------

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        anomalies = df[
            (df[selected_column] < lower_bound) |
            (df[selected_column] > upper_bound)
        ]

        anomaly_count = len(anomalies)

        anomaly_percentage = (
            (anomaly_count / total_records) * 100
            if total_records > 0
            else 0
        )

        # ---------------------------------------------
        # ANOMALY METRICS
        # ---------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "LOWER LIMIT",
                round(lower_bound, 2)
            )

        with col2:
            st.metric(
                "UPPER LIMIT",
                round(upper_bound, 2)
            )

        with col3:
            st.metric(
                "ANOMALIES DETECTED",
                anomaly_count
            )

        with col4:
            st.metric(
                "ANOMALY RATE",
                f"{anomaly_percentage:.2f}%"
            )

        st.write("")

        # ---------------------------------------------
        # VISUALIZATION
        # ---------------------------------------------

        st.markdown(
            f"### Distribution Analysis: {selected_column}"
        )

        fig = px.box(
            df,
            y=selected_column,
            points="outliers"
        )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="#172033"),
            yaxis_title=selected_column,
            margin=dict(l=20, r=20, t=40, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # ---------------------------------------------
        # DETECTION RESULT
        # ---------------------------------------------

        st.markdown("### Detection Result")

        if anomalies.empty:

            st.success(
                f"No statistical anomalies were detected in "
                f"**{selected_column}** using the IQR method."
            )

        else:

            st.warning(
                f"DataShadow detected **{anomaly_count} potential anomalies** "
                f"in **{selected_column}**, representing "
                f"**{anomaly_percentage:.2f}%** of the dataset."
            )

            st.markdown("### Unusual Records")

            st.dataframe(
                anomalies,
                use_container_width=True,
                hide_index=True
            )
# =================================================
# VISUAL EXPLORER
# =================================================

elif page == "Visual Explorer":

    st.markdown("## Visual Explorer")
    st.caption("Interactively explore your dataset")

    available_charts = []

    if numeric_columns:
        available_charts.extend([
            "Histogram",
            "Box Plot"
        ])

    if len(numeric_columns) >= 2:
        available_charts.append("Scatter Plot")

    if categorical_columns:
        available_charts.append("Bar Chart")

    if not available_charts:

        st.warning(
            "No suitable columns are available for visualization."
        )

    else:

        chart_type = st.selectbox(
            "Visualization Type",
            available_charts
        )

        if chart_type == "Histogram":

            column = st.selectbox(
                "Select Feature",
                numeric_columns
            )

            fig = px.histogram(
                df,
                x=column
            )

        elif chart_type == "Scatter Plot":

            col1, col2 = st.columns(2)

            with col1:

                x_axis = st.selectbox(
                    "X Axis",
                    numeric_columns
                )

            with col2:

                y_axis = st.selectbox(
                    "Y Axis",
                    numeric_columns,
                    index=1
                )

            fig = px.scatter(
                df,
                x=x_axis,
                y=y_axis
            )

        elif chart_type == "Box Plot":

            column = st.selectbox(
                "Select Feature",
                numeric_columns
            )

            fig = px.box(
                df,
                y=column,
                points="outliers"
            )

        elif chart_type == "Bar Chart":

            column = st.selectbox(
                "Select Category",
                categorical_columns
            )

            counts = (
                df[column]
                .value_counts()
                .reset_index()
            )

            counts.columns = [
                column,
                "Count"
            ]

            fig = px.bar(
                counts,
                x=column,
                y="Count"
            )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="#172033"),
            margin=dict(l=20, r=20, t=40, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )