import re

import pandas as pd
import streamlit as st

import database


st.set_page_config(
    page_title="StudentHub | Management",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Keep styling lightweight; avoid animations and expensive visual effects.
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #172554);
        color: #f8fafc;
    }
    .block-container {
        padding: 1.5rem 2rem;
        max-width: 1500px;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827, #1e1b4b);
        border-right: 1px solid #3730a3;
    }
    [data-testid="stSidebar"] * {
        color: #e2e8f0;
    }
    h1, h2, h3, h4 {
        color: #f8fafc !important;
        font-weight: 700 !important;
    }
    p, label, .stMarkdown {
        color: #cbd5e1;
    }
    .brand {
        font-size: 27px;
        font-weight: 800;
        color: #a78bfa;
        padding: 10px 0;
    }
    .brand-subtitle {
        color: #94a3b8;
        font-size: 13px;
    }
    .section-title {
        font-size: 25px;
        font-weight: 750;
        color: #f8fafc;
        margin-bottom: 18px;
    }
    .metric-card {
        background: linear-gradient(145deg, #1e293b, #312e81);
        border: 1px solid #4f46e5;
        border-radius: 16px;
        padding: 20px;
        min-height: 135px;
    }
    .metric-icon {
        font-size: 28px;
        margin-bottom: 10px;
    }
    .metric-label {
        font-size: 14px;
        color: #cbd5e1;
    }
    .metric-value {
        font-size: 30px;
        font-weight: 800;
        color: #ffffff;
        margin-top: 5px;
    }
    .panel {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 15px;
        padding: 24px;
        margin: 12px 0;
    }
    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1e293b !important;
        color: white !important;
        border-radius: 9px !important;
    }
    .stTextInput label,
    .stNumberInput label,
    .stSelectbox label {
        color: #cbd5e1 !important;
        font-weight: 600;
    }
    .stButton button,
    .stDownloadButton button,
    .stFormSubmitButton button {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white !important;
        border: none;
        border-radius: 9px;
        font-weight: 700;
        padding: 9px 20px;
    }
    .stButton button:hover,
    .stDownloadButton button:hover,
    .stFormSubmitButton button:hover {
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
        border: none;
    }
    [data-testid="stDataFrame"] {
        border: 1px solid #475569;
        border-radius: 10px;
        overflow: hidden;
    }
    [data-testid="stSidebar"] .stRadio label {
        background: #1e293b;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 5px;
    }
    hr {
        border-color: #334155;
    }
    [data-testid="stAlert"] {
        border-radius: 10px;
    }
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        padding: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


COURSES = [
    "Information Science",
    "Computer Science",
    "Artificial Intelligence",
    "Data Science",
    "Electronics",
    "Mechanical",
    "Civil",
    "Other",
]
DATA_COLUMNS = ["ID", "Name", "Email", "Phone", "Course", "Marks"]


@st.cache_data(ttl=30, show_spinner=False)
def get_data():
    """Load student records once and reuse them briefly across reruns."""
    records = database.get_students()
    return pd.DataFrame(records, columns=DATA_COLUMNS)


def refresh_data():
    """Invalidate cached records after a successful database mutation."""
    get_data.clear()


def valid_email(email):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))


def valid_phone(phone):
    return not phone or bool(re.fullmatch(r"\d{10}", phone))


def metric_card(title, value, icon):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-label">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with st.sidebar:
    st.markdown(
        '<div class="brand">🎓 StudentHub</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="brand-subtitle">Student Management System</div>',
        unsafe_allow_html=True,
    )
    st.divider()
    st.caption("MAIN MENU")

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Add Student",
            "View Students",
            "Update Student",
            "Delete Student",
            "Analytics",
            "Export Data",
        ],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("**🚀 Python Developer Internship**")
    st.caption("Week 5 | Deployment & Production")
    st.divider()
    st.caption("Built with Python and Streamlit")


st.markdown(
    """
    <div style="
        background:linear-gradient(100deg,#312e81,#4338ca,#7c3aed);
        padding:25px;
        border-radius:16px;
        margin-bottom:25px;
        border:1px solid #6366f1;
    ">
        <div style="font-size:14px;color:#ddd6fe;">
            STUDENT MANAGEMENT PLATFORM
        </div>
        <div style="
            font-size:32px;
            font-weight:800;
            color:white;
            margin-top:5px;
        ">
            🎓 StudentHub
        </div>
        <div style="color:#e0e7ff;font-size:14px;">
            Manage student records and academic performance.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Cached data is reused on normal Streamlit reruns. Database changes below
# explicitly invalidate this cache so users see the latest records.
df = get_data()


if page == "Dashboard":
    st.markdown(
        '<div class="section-title">📊 Dashboard Overview</div>',
        unsafe_allow_html=True,
    )

    total = len(df)
    average = float(df["Marks"].mean()) if total else 0.0
    passed = int((df["Marks"] >= 40).sum()) if total else 0
    courses_count = int(df["Course"].nunique()) if total else 0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card("Total Students", total, "👨‍🎓")
    with col2:
        metric_card("Average Marks", f"{average:.1f}", "📈")
    with col3:
        metric_card("Passed Students", passed, "✅")
    with col4:
        metric_card("Total Courses", courses_count, "📚")

    left, right = st.columns([1.5, 1])
    with left:
        st.markdown(
            '<div class="section-title">👥 Recent Students</div>',
            unsafe_allow_html=True,
        )
        if not df.empty:
            st.dataframe(
                df.head(5),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info("No students registered yet.")

    with right:
        st.markdown(
            '<div class="section-title">📌 Quick Summary</div>',
            unsafe_allow_html=True,
        )
        if not df.empty:
            st.metric("Highest Marks", f"{df['Marks'].max():.1f}")
            st.metric("Lowest Marks", f"{df['Marks'].min():.1f}")
            st.metric("Pass Percentage", f"{(passed / total) * 100:.1f}%")
        else:
            st.info("Add students to see statistics.")


elif page == "Add Student":
    st.markdown(
        '<div class="section-title">➕ Register New Student</div>',
        unsafe_allow_html=True,
    )

    with st.form("add_student", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name *")
            email = st.text_input("Email Address *")
            phone = st.text_input("Phone Number")

        with col2:
            course = st.selectbox("Select Course", COURSES)
            marks = st.number_input(
                "Academic Marks",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=1.0,
            )

        submitted = st.form_submit_button(
            "➕ Register Student",
            use_container_width=True,
        )

    if submitted:
        name = name.strip()
        email = email.strip().lower()
        phone = phone.strip()

        if not name or not email:
            st.error("Please enter the student's name and email.")
        elif not valid_email(email):
            st.error("Please enter a valid email address.")
        elif not valid_phone(phone):
            st.error("Phone number must contain exactly 10 digits.")
        else:
            result = database.add_student(name, email, phone, course, marks)
            if result:
                refresh_data()
                st.success("Student registered successfully!")
                st.rerun()
            else:
                st.error("Student could not be added. Check for duplicate email.")


elif page == "View Students":
    st.markdown(
        '<div class="section-title">👥 Student Records</div>',
        unsafe_allow_html=True,
    )

    if not df.empty:
        search = st.text_input(
            "🔍 Search students",
            placeholder="Search by name, email, course or ID...",
        )

        if search.strip():
            search_value = search.strip()
            searchable = df[DATA_COLUMNS].astype(str)
            mask = searchable.apply(
                lambda column: column.str.contains(
                    search_value,
                    case=False,
                    regex=False,
                    na=False,
                )
            ).any(axis=1)
            filtered = df.loc[mask]
        else:
            filtered = df

        st.caption(f"Showing {len(filtered)} of {len(df)} students")
        st.dataframe(
            filtered,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No student records available.")


elif page == "Update Student":
    st.markdown(
        '<div class="section-title">✏️ Update Student Details</div>',
        unsafe_allow_html=True,
    )

    if not df.empty:
        student_options = {
            int(row["ID"]): f"{int(row['ID'])} - {row['Name']}"
            for _, row in df.iterrows()
        }
        student_id = st.selectbox(
            "Select Student",
            options=list(student_options),
            format_func=lambda value: student_options[value],
        )
        student = df.loc[df["ID"] == student_id].iloc[0]

        with st.form("update_student"):
            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input("Full Name", value=str(student["Name"]))
                email = st.text_input("Email", value=str(student["Email"]))
                phone = st.text_input(
                    "Phone",
                    value="" if pd.isna(student["Phone"]) else str(student["Phone"]),
                )

            with col2:
                current_course = str(student["Course"])
                courses = COURSES.copy()
                if current_course not in courses:
                    courses.append(current_course)

                course = st.selectbox(
                    "Course",
                    courses,
                    index=courses.index(current_course),
                )
                current_marks = (
                    0.0 if pd.isna(student["Marks"]) else float(student["Marks"])
                )
                marks = st.number_input(
                    "Marks",
                    min_value=0.0,
                    max_value=100.0,
                    value=min(100.0, max(0.0, current_marks)),
                    step=1.0,
                )

            submitted = st.form_submit_button(
                "💾 Save Changes",
                use_container_width=True,
            )

        if submitted:
            name = name.strip()
            email = email.strip().lower()
            phone = phone.strip()

            if not name or not email:
                st.error("Name and email are required.")
            elif not valid_email(email):
                st.error("Enter a valid email address.")
            elif not valid_phone(phone):
                st.error("Phone number must contain exactly 10 digits.")
            else:
                result = database.update_student(
                    int(student_id), name, email, phone, course, marks
                )
                if result:
                    refresh_data()
                    st.success("Student details updated successfully!")
                    st.rerun()
                else:
                    st.error(
                        "Student could not be updated. Check for a duplicate email "
                        "or confirm that the record still exists."
                    )
    else:
        st.info("No students available to update.")


elif page == "Delete Student":
    st.markdown(
        '<div class="section-title">🗑️ Delete Student</div>',
        unsafe_allow_html=True,
    )

    if not df.empty:
        student_options = {
            int(row["ID"]): f"{int(row['ID'])} - {row['Name']}"
            for _, row in df.iterrows()
        }
        student_id = st.selectbox(
            "Select Student",
            options=list(student_options),
            format_func=lambda value: student_options[value],
        )
        student = df.loc[df["ID"] == student_id].iloc[0]

        st.warning(
            f"You selected {student['Name']} ({student['Email']})."
        )
        confirm = st.checkbox("I confirm that I want to delete this student.")

        if st.button("🗑️ Delete Student", disabled=not confirm):
            result = database.delete_student(int(student_id))
            if result:
                refresh_data()
                st.success("Student deleted successfully!")
                st.rerun()
            else:
                st.error("Could not delete student. The record may no longer exist.")
    else:
        st.info("No students available to delete.")


elif page == "Analytics":
    st.markdown(
        '<div class="section-title">📈 Academic Analytics</div>',
        unsafe_allow_html=True,
    )

    if not df.empty:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Students by Course")
            st.bar_chart(df["Course"].value_counts())

        with col2:
            st.subheader("Marks Distribution")
            bins = pd.cut(
                df["Marks"],
                bins=[-1, 39, 59, 79, 100],
                labels=["Below 40", "40–59", "60–79", "80–100"],
            )
            st.bar_chart(bins.value_counts().sort_index())

        passed = int((df["Marks"] >= 40).sum())
        failed = int((df["Marks"] < 40).sum())
        pass_rate = (passed / len(df)) * 100

        st.subheader("Performance Summary")
        col1, col2, col3 = st.columns(3)
        col1.metric("Passed", passed)
        col2.metric("Failed", failed)
        col3.metric("Pass Rate", f"{pass_rate:.1f}%")
    else:
        st.info("Register students to view analytics.")


elif page == "Export Data":
    st.markdown(
        '<div class="section-title">📥 Export Student Data</div>',
        unsafe_allow_html=True,
    )

    if not df.empty:
        st.success(f"{len(df)} student records available.")
        csv_data = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download CSV",
            data=csv_data,
            file_name="student_records.csv",
            mime="text/csv",
            use_container_width=True,
        )

        st.subheader("Data Preview")
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No records available for export.")


st.markdown(
    """
    <div class="footer">
        StudentHub © 2026 |
        Python Developer Internship |
        Built with Streamlit, Pandas and SQLite
    </div>
    """,
    unsafe_allow_html=True,
)
