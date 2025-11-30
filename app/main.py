import streamlit as st
from agents.planner import PlannerAgent
from agents.action_agent import ActionAgent
from agents.alert_agent import AlertAgent
from agents.evaluator import EvaluatorAgent

st.set_page_config(page_title="SafeBuddy", page_icon="🛡️", layout="centered")
st.title("🛡️ SafeBuddy – Women Safety Chatbot")

# Input field
user_input = st.text_input("How can I help you?")

if st.button("Ask"):
    if user_input:
        # Simple workflow: Planner -> Action -> Evaluator
        plan = PlannerAgent().create_plan(user_input)
        action_response = ActionAgent().perform_action(plan)
        evaluation = EvaluatorAgent().evaluate(action_response)
        st.success(f"SafeBuddy: {evaluation}")

st.write("---")
st.subheader("🚨 Emergency Support")

if st.button("Send SOS Alert"):
    alert_msg = AlertAgent().send_alert()
    st.warning(alert_msg)
