class SheetAnalyzer:
    def __init__(self):
        self.urgent_keywords = ["error", "critical", "down", "crash", "urgent"]
        self.normal_keywords = ["warning", "low", "minor"]

    def classify(self, text, labels=["urgent", "normal", "low"]):
        text_lower = text.lower()

        # ⬇️ تشخیص با کلمات کلیدی
        if any(kw in text_lower for kw in self.urgent_keywords):
            return {"text": text, "label": "urgent", "score": 0.9}
        elif any(kw in text_lower for kw in self.normal_keywords):
            return {"text": text, "label": "normal", "score": 0.7}
        else:
            return {"text": text, "label": "low", "score": 0.5}