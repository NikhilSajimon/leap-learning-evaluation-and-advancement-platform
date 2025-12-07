
import streamlit as st
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
QUESTIONS_FILE = DATA_DIR / "questions" / "questions.csv"

st.set_page_config(
    page_title="LEAP - Learning Evaluation & Advancement Platform",
    layout="centered"
)

st.title("LEAP")
st.subheader("Learning Evaluation & Advancement Platform")
st.caption("Start ahead. Stay ahead.")

st.markdown("---")

# Initialize session state
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "responses" not in st.session_state:
    st.session_state.responses = []

def load_questions():
    if QUESTIONS_FILE.exists():
        df = pd.read_csv(QUESTIONS_FILE)
        return df
    else:
        st.warning("Question bank not found yet. Please add data/questions/questions.csv")
        return pd.DataFrame()

questions_df = load_questions()

if questions_df.empty:
    st.info("Once the question bank is added, a quiz interface will appear here.")
else:
    total_questions = len(questions_df)

    if st.session_state.current_index < total_questions:
        row = questions_df.iloc[st.session_state.current_index]

        st.markdown(
            f"**Question {st.session_state.current_index + 1} of {total_questions}**"
        )
        st.write(row["question"])

        options = []
        for i in range(1, 5):
            col_name = f"option_{i}"
            if col_name in row and pd.notna(row[col_name]):
                options.append(row[col_name])

        user_answer = st.radio(
            "Select your answer:",
            options,
            index=None,
            key=f"q_{st.session_state.current_index}"
        )

        if st.button("Next"):
            if user_answer is None:
                st.warning("Please select an answer.")
            else:
                st.session_state.responses.append({
                    "question_id": row["id"],
                    "skill": row["skill"],
                    "correct_answer": row["answer"],
                    "user_answer": user_answer
                })
                st.session_state.current_index += 1
                st.experimental_rerun()
    else:
        st.success("You have completed the quiz!")

        responses_df = pd.DataFrame(st.session_state.responses)

        if not responses_df.empty:
            responses_df["is_correct"] = (
                responses_df["user_answer"] == responses_df["correct_answer"]
            )
            skill_summary = (
                responses_df
                .groupby("skill")["is_correct"]
                .mean()
                .reset_index()
            )
            skill_summary.rename(columns={"is_correct": "accuracy"}, inplace=True)

            st.subheader("Your Skill-wise Performance (simple Week 1 version)")
            st.dataframe(skill_summary)

            st.write(
                "In Week 2, this will become a mastery model "
                "with adaptive logic and personalized plans."
            )

        if st.button("Restart"):
            st.session_state.current_index = 0
            st.session_state.responses = []
            st.experimental_rerun()
