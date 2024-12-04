import streamlit as st
from datetime import *

# HRIS Class definition
class HRIS:
    half_day = timedelta(hours=4, minutes=15)  # Time for half-day leave
    full_day = timedelta(hours=8, minutes=30)  # Time for full-day leave
    short_leave = timedelta(minutes=50)  # Time for short leave
    
    def __init__(self, hr, min):
        self.__in_time = time(hr, min)
    
    def full_day_out_time(self):
        # Full day out-time based on in-time + full_day duration
        in_datetime = datetime.combine(datetime.today(), self.__in_time)
        full_out = in_datetime + HRIS.full_day
        return full_out.time()
    
    def short_leave_out_time(self, number):
        # Short leave out-time
        full_out = self.full_day_out_time()
        in_datetime = datetime.combine(datetime.today(), full_out)
        short_out = in_datetime - number * HRIS.short_leave
        return short_out.time()
    
    def half_leave_out_time(self):
        # Half leave out-time
        full_out = self.full_day_out_time()
        in_datetime = datetime.combine(datetime.today(), full_out)
        half_out = in_datetime - HRIS.half_day
        return half_out.time()
    
    def __str__(self):
        return f"In-time: {self.__in_time}"

# Streamlit interface
def main():
    st.title("HRIS - Working Hours and Leave Calculation")
    st.markdown("### Enter your in-time and select your leave type to calculate the out-time.")
    
    # Inputs
    hr = st.number_input("Enter Hour of In-Time", min_value=0, max_value=23, value=9)
    minute = st.number_input("Enter Minute of In-Time", min_value=0, max_value=59, value=0)
    
    leave_type = st.selectbox("Select Leave Type", ["Full Day", "Half Leave", "Short Leave"])
    number_of_short_leaves = 0
    
    if leave_type == "Short Leave":
        number_of_short_leaves = st.number_input("Enter Number of Short Leaves", min_value=1, value=1,max_value=3)
    
    # HRIS instance
    hris = HRIS(hr, minute)
    
    if leave_type == "Full Day":
        out_time = hris.full_day_out_time()
        st.markdown(f"<h2 style='text-align: center; font-weight: bold;'>Out-time for a Full Day: {out_time}</h2>", unsafe_allow_html=True)
    
    elif leave_type == "Half Leave":
        out_time = hris.half_leave_out_time()
        st.markdown(f"<h2 style='text-align: center; font-weight: bold;'>Out-time for Half Leave: {out_time}</h2>", unsafe_allow_html=True)
    
    elif leave_type == "Short Leave":
        out_time = hris.short_leave_out_time(number_of_short_leaves)
        st.markdown(f"<h2 style='text-align: center; font-weight: bold;'>Out-time for Short Leave ({number_of_short_leaves}): {out_time}</h2>", unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
