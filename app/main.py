import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from agents.planner import PlannerAgent
from agents.action_agent import ActionAgent
from agents.evaluator import EvaluatorAgent
from agents.alert_agent import AlertAgent

st.set_page_config(page_title="SafeBuddy", page_icon="🛡️", layout="centered")
st.title("🛡️ SafeBuddy – Women Safety Chatbot")

# Initialize agents
planner = PlannerAgent()
action_agent = ActionAgent()
evaluator = EvaluatorAgent()
alert_agent = AlertAgent()

# Chat Section
st.subheader("🗨️ Chat with SafeBuddy")
user_text = st.text_input("You:", "")

if st.button("Send", key="send_chat"):
    if user_text.strip():
        # Workflow: Planner -> Action -> Evaluator
        plan = planner.plan(user_text)
        action_response = action_agent.perform_action(plan)
        evaluation = evaluator.evaluate(action_response)
        st.write("**SafeBuddy:**", evaluation)
    else:
        st.warning("Please type a message.")

# Emergency Alert Section
st.subheader("🚨 Emergency Support")
if st.button("Send SOS Alert", key="send_sos"):
    user_location = "https://maps.google.com/?q=12.9716,77.5946"  # optional: you can get real location later
    alert_msg = alert_agent.send_alert(user_location=user_location)
    st.warning(alert_msg)
