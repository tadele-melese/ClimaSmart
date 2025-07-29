import shap

def explain_model_predictions(model, inputs, background=None, model_type="lstm"):
    """
    Explain time-series model predictions using SHAP.
    """
    model.eval()
    if background is None:
        background = inputs[:100]

    explainer = shap.DeepExplainer(model, background)
    shap_values = explainer.shap_values(inputs)

    shap.summary_plot(shap_values, inputs)
    return shap_values
