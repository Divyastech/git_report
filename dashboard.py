import streamlit as st
import pandas as pd
import os

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="IBVAP - Border Surveillance",
    page_icon="🛡️",
    layout="wide"
)

# =====================================
# TITLE
# =====================================

st.title("🛡️ IBVAP")
st.subheader("Intelligent Border Video Analytics Platform")

st.markdown("---")

# =====================================
# LOAD ALERT DATA
# =====================================

if os.path.exists("alerts.csv"):

    alerts = pd.read_csv("alerts.csv")

else:

    alerts = pd.DataFrame(
        columns=[
            "Date",
            "Time",
            "Camera",
            "Object",
            "Event",
            "Status"
        ]
    )

# =====================================
# STATISTICS
# =====================================

total_alerts = len(alerts)

# =====================================
# TOP METRICS
# =====================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📹 Live Cameras",
        "01"
    )

with col2:
    st.metric(
        "👤 Persons Detected",
        "04"
    )

with col3:
    st.metric(
        "🚗 Vehicles Detected",
        "03"
    )

with col4:
    st.metric(
        "🚨 Intrusions",
        total_alerts
    )

st.markdown("---")

# =====================================
# CAMERA SECTION
# =====================================

st.header("📹 Live Surveillance")

col1, col2 = st.columns([2, 1])

with col1:

    st.video("CCTV.mp4")

with col2:

    st.success("🟢 SYSTEM ONLINE")

    st.write("**Camera:** BOP-01")
    st.write("**Location:** Border Outpost")
    st.write("**Status:** Live")
    st.write("**AI Engine:** YOLO")
    st.write("**Tracking:** ByteTrack")

# =====================================
# ALERT SECTION
# =====================================

st.markdown("---")

st.header("🚨 Security Event Log")

if len(alerts) > 0:

    st.dataframe(
        alerts,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No security events detected.")

# =====================================
# SYSTEM INFORMATION
# =====================================

st.markdown("---")

st.header("⚙️ AI Analytics")

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        "👤 Human Detection\n\n"
        "YOLO-based real-time detection"
    )

with col2:

    st.info(
        "🎯 Object Tracking\n\n"
        "ByteTrack-based tracking IDs"
    )

with col3:

    st.info(
        "🚨 Intrusion Detection\n\n"
        "Virtual fence monitoring"
    )

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "IBVAP | Intelligent Border Video Analytics Platform | Prototype"
)