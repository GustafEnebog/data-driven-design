import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_airplane_feature_visualizer import page_airplane_feature_visualizer_body
from app_pages.page_domain_specific_analysis import page_domain_specific_analysis_body
from app_pages.page_piper_vs_cessna import page_piper_vs_cessna_body
from app_pages.page_engine_type_airplane_study import page_engine_type_airplane_study_body
from app_pages.page_predict_engine_type import page_predict_engine_type_body
from app_pages.page_multi_engine_airplane_study import page_multi_engine_airplane_study_body
from app_pages.page_predict_multi_engine import page_predict_multi_engine_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_predict_engine_type import page_ml_predict_engine_type_body
from app_pages.page_ml_predict_multi_engine import page_ml_predict_multi_engine_body
from app_pages.page_ml_predict_wing_span import page_ml_predict_wing_span_body
from app_pages.page_ml_cluster import page_ml_cluster_body

app = MultiPage(app_name= "General Aviation Performance Analysis and Predictor tool") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Airplane Feature Visualizer", page_airplane_feature_visualizer_body)
app.add_page("Domain Specific Analysis", page_domain_specific_analysis_body)
app.add_page("Piper_vs_Cessna", page_piper_vs_cessna_body)
app.add_page("Engine Type Airplane Study", page_engine_type_airplane_study_body)
app.add_page("Predict Engine Type", page_predict_engine_type_body)
app.add_page("Multi Engine Airplane Study", page_multi_engine_airplane_study_body)
app.add_page("Predict Multi Engine", page_predict_multi_engine_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Predict Engine Type", page_ml_predict_engine_type_body)
app.add_page("ML: Predict Multi Engine", page_ml_predict_multi_engine_body)
app.add_page("ML: Predict Wing Span", page_ml_predict_wing_span_body)
app.add_page("ML: Cluster Analysis", page_ml_cluster_body)

app.run() # Run the app
