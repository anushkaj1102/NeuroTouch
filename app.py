import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(
    page_title="NeuroTouch",
    layout="wide"
)

# ---------------------------
# HEADER
# ---------------------------
st.title("🧤 NeuroTouch")
st.subheader("A compact tactile-feedback system for restoring touch awareness")

st.markdown("### Team Members")
st.markdown("""
- **Ananya Shivarama Bhat**  
- **Anushka Jain**  
- **Devanshi Kalpeshbhai Patel**  
""")

# ---------------------------
# TABS
# ---------------------------
tabs = st.tabs([
    "🏠 Overview",
    "📄 Abstract",
    "💡 Motivation",
    "🧩 Block Diagram",
    "🛠️ System Architecture",
    "📊 Live Sensor Dashboard & Results",
    "🧭 References & Future Work",
    "🎥 Project Demo"
])


# ===========================
# TAB 1 — OVERVIEW
# ===========================
with tabs[0]:
    st.header("Overview")

    col1, col2 = st.columns(2)

    # Left side – text
    with col1:
        st.write("""
        Welcome to NeuroTouch - A Smart Haptic Glove project showcase!  

        This interface presents a full walkthrough of the system, including our design, 
        motivation, architecture, and a demo of how our product works.
        """)

    # Right side – image
    with col2:
        st.image("images/smartgloves_intro.png", width=250)

    # Full-width video below
    st.video("video/intro_robot_and_human.mp4")

    

# ===========================
# TAB 2 — ABSTRACT
# ===========================
with tabs[1]:
    st.header("Abstract")
    st.write("""Individuals with congenital insensitivity to pain or loss of touch sensation lack the sensory feedback needed to safely interact with their environment. This project proposes a Smart Haptic Glove that restores a sense of touch awareness using a compact embedded system built around the ATmega328PB microcontroller. Each glove hand integrates multiple force-sensitive resistors (FSRs) for contact pressure, a precision temperature sensor (MCP9700) for surface heat detection, and ERM haptic motors (P1012 class) that reproduce tactile feedback through vibrations proportional to force or temperature. A low-power OLED display provides real-time sensor data and system status. The system runs on a power bank with on-board power regulation and noise filtering, ensuring full compliance with laboratory safety requirements. The glove’s firmware performs continuous analog sampling, threshold detection, and PWM-based haptic control while employing sleep and duty-cycling techniques for efficient power management. The end goal is a lightweight, wearable assistive device that enables users without tactile sensation to perceive pressure and temperature cues safely and intuitively.
    
    """)

# ===========================
# TAB 3 — MOTIVATION
# ===========================
with tabs[2]:
    st.header("Motivation")
    st.write("""
    People affected by **Congenital Insensitivity to Pain with Anhidrosis (CIPA)** or other neuropathic conditions lack the ability to feel **pain, temperature, or touch**—fundamental sensations that protect the body from harm. Everyday tasks such as holding a hot object, applying pressure, or gripping tools can result in severe injuries without the person realizing it.

Our motivation is to **restore safe sensory awareness** through an assistive wearable device that translates real-world stimuli into **intelligent haptic feedback**. Rather than simply detecting hazards, the glove allows the user to *feel* through controlled vibrations and cues—making safety instinctive again.

The project also serves as a **demonstration of embedded systems integration**, combining analog sensing, PWM motor control, and real-time signal processing on a compact **ATmega328PB** platform. By designing a power-efficient, sensor-rich glove that operates entirely on **a power bank**, we aim to create an accessible, wearable prototype that showcases how embedded technology can bridge the gap between human perception and digital intelligence.

Ultimately, this project is driven by two goals:

1. **Human impact** — improving quality of life for individuals who have lost tactile perception.
2. **Engineering innovation** - proving that low-cost embedded systems can deliver meaningful assistive technology when designed thoughtfully.
    """)
# ===========================
# TAB 4 — BLOCK DIAGRAM
# ===========================
with tabs[3]:
    st.header("Block Diagram")

    # Center the image using CSS
    st.markdown(
        """
        <style>
        .centered-image {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Wrap the st.image inside a div that uses the centering style
    st.markdown("<div class='centered-image'>", unsafe_allow_html=True)
    st.image("images/Block_diagram.png", caption="Block Diagram", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("""
    The block diagram illustrates the overall workflow of the Smart Haptic Glove system.
    Sensor data is captured by the FSRs and temperature sensor, processed by the ATmega328PB,
    and translated into haptic feedback for the user. Wireless communication enables data
    streaming to external dashboards for monitoring or analysis.
    """)

# ===========================
# TAB 5 — SYSTEM ARCHITECTURE
# ===========================
with tabs[4]:
    st.header("System Architecture")

    # -------------------------------
    # TOP TWO-COLUMN LAYOUT
    # -------------------------------
    col1, col2 = st.columns([1.2, 1])

    # LEFT SIDE — REQUIREMENTS
    with col1:
        st.subheader("Hardware Requirement Specifications")
        st.write("""
        - ATmega328PB Microcontroller
        - 4× Force Sensitive Resistors (FSRs)
        - ST7735 LCD screen
        - Lilypad temperature sensor
        - APDS9960 proximity sensor  
        - Haptic vibrator driver 
        - HC-05 Bluetooth module  
        - 5V power supply - Power Bank
        """)

        st.subheader("Software Requirement Specifications")
        st.write("""
        - Embedded C firmware for ATmega328PB  
        - ADC-based sensor acquisition and filtering  
        - PWM motor control logic  
        - I²C communication for ST7735 LCD  
        - UART communication with HC-05 Bluetooth module  
        - Real-time data processing and threshold detection  
        - Python/Streamlit dashboard for live sensor monitoring  
        """)

    # RIGHT SIDE — INITIAL DESIGN
    with col2:
        st.subheader("System Block Placement")
        st.image("images/Design_Sketch.png", caption="Initial Design Sketch", use_container_width=True)

    st.markdown("---")

    # -------------------------------
    # THREE IMAGES — NICE LAYOUT
    # -------------------------------
    st.subheader("Prototype & Actual Build")

    img_col1, img_col2 = st.columns(2)

    with img_col1:
        st.image("images/glove_imageI.png", caption="Completed Glove – View 1", use_container_width=True)

    with img_col2:
        st.image("images/glove_imageII.png", caption="Completed Glove – View 2", use_container_width=True)


# ===========================
# TAB 6 — LIVE SENSOR DASHBOARD 
# ===========================
with tabs[5]:

    import streamlit as st
    import pandas as pd
    from serial_reader import read_serial_line
    from streamlit_autorefresh import st_autorefresh
    import altair as alt

    st.header("📊 Live Sensor Dashboard")

    # Auto refresh
    st_autorefresh(interval=500, key="refresh")

    # -------------------------------
    # Initialize session state
    # -------------------------------
    if "stream_data" not in st.session_state:
        st.session_state.stream_data = []

    if "stream_active" not in st.session_state:
        st.session_state.stream_active = False

    if "stream_gen" not in st.session_state:
        st.session_state.stream_gen = None

    # -------------------------------
    # Start / Stop buttons
    # -------------------------------
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start Streaming"):
            st.session_state.stream_active = True
            if st.session_state.stream_gen is None:
                st.session_state.stream_gen = read_serial_line("/dev/tty.HC-05", 9600)
            st.success("Streaming started...")

    with col2:
        if st.button("Stop Streaming"):
            st.session_state.stream_active = False
            st.warning("Streaming stopped.")

    # -------------------------------
    # Friendly names
    # -------------------------------
    friendly_names = {
        "FSR": "Force (N)",
        "T": "Temperature (°C)",
        "PROX": "Proximity (ADC converted)",
        "BURN": "Burn (0 or 1)",
        "NEAR": "Near (0 or 1)"
    }

    # -------------------------------
    # Sensor selection checkboxes
    # -------------------------------
    st.subheader("Select sensors to plot")
    col_fsr, col_t, col_prox = st.columns(3)

    fsr_sel = col_fsr.checkbox(friendly_names["FSR"], value=True)
    t_sel = col_t.checkbox(friendly_names["T"], value=True)
    prox_sel = col_prox.checkbox(friendly_names["PROX"], value=True)

    selected_sensors = []
    if fsr_sel:
        selected_sensors.append("FSR")
    if t_sel:
        selected_sensors.append("T")
    if prox_sel:
        selected_sensors.append("PROX")

    # -------------------------------
    # Read new serial data
    # -------------------------------
    if st.session_state.stream_active and st.session_state.stream_gen is not None:
        try:
            for _ in range(5):
                new_sample = next(st.session_state.stream_gen)
                st.session_state.stream_data.append(new_sample)
        except Exception as e:
            st.error(f"Error reading serial: {e}")
            st.session_state.stream_active = False

    # -------------------------------
    # Plot + Table
    # -------------------------------
    if st.session_state.stream_data:

        df_live = pd.DataFrame(st.session_state.stream_data)

        if "Index" not in df_live.columns:
            df_live["Index"] = df_live.index

        st.subheader("Live Sensor Chart")

        if selected_sensors:

            cols_for_plot = ["Index"] + selected_sensors
            df_plot = df_live[cols_for_plot].copy()

            df_melted = df_plot.melt(
                id_vars="Index",
                var_name="Sensor",
                value_name="Value"
            )

            df_melted["Sensor"] = df_melted["Sensor"].map(friendly_names)

            chart = (
                alt.Chart(df_melted)
                .mark_line(strokeWidth=3)
                .encode(
                    x=alt.X("Index", title="Time"),
                    y=alt.Y("Value", title="Sensor Value"),
                    color="Sensor:N"
                )
                .properties(width=900, height=400)
            )

            st.altair_chart(chart, use_container_width=True)

        else:
            st.info("Select at least one sensor to plot.")

        st.subheader("Latest Sensor Data")

        table_cols = ["T", "FSR", "PROX", "BURN", "NEAR"]
        table_cols = [c for c in table_cols if c in df_live.columns]

        df_table = df_live[table_cols].copy()
        st.dataframe(df_table.tail(10))

    else:
        st.info("No data yet. Click 'Start Streaming'.")

    st.image("images/Live_Sensor_Chart.png", caption="Reference Plot (as received when Nick tested the glove on Demo Day)")

# ===========================
# TAB 7 — References & Future Work
# ===========================
with tabs[6]:
    st.header("📚 References & Future Work")

    # ---------------------------
    # LIBRARIES USED
    # ---------------------------
    st.subheader("Libraries Used")
    st.write("""
    - **uart.h** handles the configuration and operation of UART serial communication on the microcontroller, enabling reliable data transmission and reception. It supports communication with external devices such as Bluetooth modules or a PC, making it essential for wireless telemetry and real-time monitoring.
    
    - **LCD_GFX.h** provides graphics utility functions for drawing shapes, text, and UI components on the TFT screen. It simplifies low-level pixel manipulation and supports rendering the emoji-based interface, indicators, and other visual elements.
    
    - **ASCII_LUT.h** contains a lookup table of ASCII character bitmaps that map characters to pixel patterns. This enables the system to convert text into drawable graphics on the LCD, allowing readable on-screen messages and labels.
    
    - **ST7735.h** is the driver library for the ST7735 TFT display controller, managing low-level SPI communication and screen initialization. It handles pixel updates, color formatting, and communication protocols, forming the foundation on which LCD_GFX functions operate.
    """)

    # ---------------------------
    # FUTURE WORK
    # ---------------------------
    st.subheader("Future Work")
    st.write("""
    Future improvements include developing a fully wireless dashboard using optimized HC-05 telemetry, expanding sensing to all fingers, and integrating distributed temperature and force measurement. Creating a custom PCB would significantly enhance comfort and reliability. Additional advancements could include machine-learning-based safety detection, improved power management, and a compact integrated housing. Together, these enhancements would move the glove closer to becoming a practical and robust assistive device.
    """)

# ===========================
# TAB 8 — PROJECT DEMO VIDEO
# ===========================
with tabs[7]:
    st.header("🎥 Project Demo Video")

    st.write("""
    Here is a short walkthrough of our Smart Haptic Glove in action —
    demonstrating live sensing, haptic feedback, and system behavior in real-time.
    """)

    # YouTube video embed
    st.video("https://youtu.be/Nd8sG4NLBmw")


