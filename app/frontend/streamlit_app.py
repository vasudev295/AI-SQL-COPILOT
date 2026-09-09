import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from app.agents.orchestrator import QueryOrchestrator
from app.visualization.charts import make_chart

st.set_page_config(page_title="QueryPilot AI",page_icon="🤖",layout="wide")
st.title("🤖 QueryPilot AI")
st.caption("Enterprise Text-to-SQL & Data Analyst Copilot")

if "history" not in st.session_state:
    st.session_state.history=[]

question=st.chat_input("Ask your database a question...")

if question:
    with st.spinner("Generating, validating and executing SQL..."):
        try:
            history_text="\n".join(
                f"User: {x['question']}\nAssistant: {x.get('explanation','')}"
                for x in st.session_state.history[-5:]
            )
            result=QueryOrchestrator().run(question,history_text)
            st.session_state.history.append({"question":question,**result})
        except Exception as e:
            st.error(str(e))

for item in reversed(st.session_state.history):
    with st.chat_message("user"):
        st.write(item["question"])
    with st.chat_message("assistant"):
        if item["error"]:
            st.error(f"Failed after {item['attempts']} attempts: {item['error']}")
            continue
        st.success(item["explanation"])
        with st.expander("🔍 Generated SQL"):
            st.code(item["sql"],language="sql")
        if item["rows"]:
            st.dataframe(item["rows"],use_container_width=True)
            chart=make_chart(item["rows"])
            if chart:
                st.plotly_chart(chart,use_container_width=True)
        else:
            st.info("No rows returned.")

with st.sidebar:
    st.header("💡 Try these")
    for q in [
        "What are the top 5 products by revenue?",
        "Which region generated the most revenue?",
        "Show monthly revenue for 2025.",
        "Compare revenue between North and South."
    ]:
        st.write("• "+q)
    if st.button("Clear history"):
        st.session_state.history=[]
        st.rerun()
