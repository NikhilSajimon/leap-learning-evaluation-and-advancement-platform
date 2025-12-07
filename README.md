# LEAP — Learning Evaluation & Advancement Platform

LEAP is an intelligent platform that evaluates a student's prerequisite knowledge for a course,
identifies their specific gaps, and generates a personalized "bridge" learning path. It also
runs periodic micro-assessments during the course to track mastery and prevent students from
falling behind.

## Goals

- Diagnose prerequisite knowledge **before** a course starts.
- Identify micro-skill gaps (e.g., `SQL:JOINs`, `Stats:P-value`).
- Recommend a **personalized bridge curriculum**.
- Run **periodic checks** during the course to track learning and catch new gaps early.

## High-Level Architecture

- **Frontend:** Streamlit web app for students and instructors.
- **Backend:** Python modules for skill trees, question management, and mastery logic.
- **Data Layer:** CSV / database storing skills, questions, and responses.
- **(Later)** ML models for adaptive testing and predictive analytics.

##  Repository Structure

```text
app/            # Streamlit UI
backend/        # Skill tree, question bank, mastery logic
data/           # Skill tree & question bank files
notebooks/      # DS/ML experiments
docs/           # Design docs & architecture notes
tests/          # Unit tests

