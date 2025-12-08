# Presentation Outline: ML Interpretability for Heart Failure Prediction
## CS667 Project 4 - Non-Technical Stakeholder Presentation

**Target Audience**: Hospital administrators, clinicians, healthcare decision-makers (non-technical)

**Duration**: ~10-15 minutes

---

## Slide 1: Title Slide

**Title**: Predicting Heart Failure Outcomes with Interpretable Machine Learning

**Subtitle**: Understanding Not Just What the Model Predicts, But Why

- Team members
- Course: CS667 Practical Data Science
- Date

---

## Slide 2: The Problem

**Key Points to Cover**:
- Heart failure affects millions of patients worldwide
- Early identification of high-risk patients can improve outcomes
- Traditional "black box" AI models make predictions but don't explain themselves
- **The Challenge**: Clinicians need to UNDERSTAND why a patient is flagged as high-risk

**Suggested Visual**: Simple infographic showing the gap between prediction and understanding

---

## Slide 3: Our Dataset

**Key Points to Cover**:
- 299 patients with heart failure from clinical records
- 12 health indicators measured during follow-up
- Tracked whether patients survived or deceased

**Suggested Visual**:
- Simple table showing 3-4 example patient profiles (anonymized)
- Or icons representing the key health factors

**Keep It Simple**: Avoid medical jargon, use plain language descriptions

---

## Slide 4: Our Approach

**Key Points to Cover**:
- Built 4 different prediction models
- Each model "thinks" differently about the data
- Most importantly: Made each model EXPLAIN its reasoning

**Suggested Visual**:
- 4 boxes representing the models (LR, DT, RF, XGBoost)
- Arrow pointing to "Interpretability Tools"

**Analogy to Use**: "Like getting a second opinion from 4 different specialists, and asking each to explain their reasoning"

---

## Slide 5: Which Factors Matter Most?

**Key Points to Cover**:
- Present the top 3-5 most important features
- Explain in plain language what they mean clinically
- Example: "Patients with lower ejection fraction (heart pumping less blood) are at higher risk"

**Suggested Visual**:
- Horizontal bar chart of feature importance
- Use clinical terms with plain-language explanations

**Questions to Prompt in Notes**:
- Which features would clinicians expect to matter?
- Any surprising findings?

---

## Slide 6: How Accurate Are Our Models?

**Key Points to Cover**:
- All 4 models perform well (X-Y% accuracy)
- Compare using simple metrics (correct predictions out of total)
- Highlight the best performer

**Suggested Visual**:
- Simple bar chart comparing model accuracy
- Use green checkmarks for correct, red X for incorrect

**Keep It Simple**: Avoid AUC-ROC unless you can explain it simply (e.g., "how well the model distinguishes high-risk from low-risk patients")

---

## Slide 7: Understanding Individual Predictions

**Key Points to Cover**:
- Show a real example (anonymized)
- Patient A: Predicted high-risk - explain WHY
- Patient B: Predicted low-risk - explain WHY

**Suggested Visual**:
- Simplified SHAP/LIME explanation
- Use arrows or colors to show "factors pushing toward risk" vs "factors reducing risk"

**Key Message**: The model doesn't just say "high risk" - it says "high risk BECAUSE..."

---

## Slide 8: What This Means for Clinicians

**Key Points to Cover**:
- Doctors can see WHY a prediction was made
- Builds trust in AI recommendations
- Helps identify which patients need immediate attention
- Supports (doesn't replace) clinical judgment

**Suggested Visual**:
- Workflow diagram: Patient Data → Model → Explanation → Clinical Decision

**Questions to Address**:
- How would this fit into existing workflows?
- What actions could clinicians take based on explanations?

---

## Slide 9: Limitations & Next Steps

**Key Points to Cover**:
- Small dataset (299 patients) - need validation on larger populations
- Single hospital/region - may not generalize everywhere
- Models trained on historical data - medical practice evolves

**Future Directions**:
- Validate on larger, more diverse patient populations
- Real-time integration with hospital systems
- Continuous monitoring and updating

**Be Honest**: Acknowledge limitations to build credibility

---

## Slide 10: Questions & Discussion

**Key Points to Cover**:
- Recap: We can predict AND explain
- Open floor for questions

**Suggested Discussion Questions**:
- What other clinical decisions could benefit from interpretable AI?
- What concerns do you have about using AI in clinical settings?

---

## Presentation Tips

1. **Avoid Jargon**: No "hyperparameters", "AUC-ROC", "gradient boosting" unless you explain simply
2. **Use Analogies**: Compare ML concepts to familiar ideas
3. **Focus on Impact**: Always tie back to patient outcomes and clinical value
4. **Visual Over Text**: Each slide should have more visuals than bullet points
5. **Tell a Story**: Patient → Problem → Solution → Impact

## Backup Slides (If Asked Technical Questions)

- Model comparison table with detailed metrics
- Hyperparameter details
- Technical methodology summary
