# scholar_tools.py
"""
ScholarScout - Custom Tools
These tools simulate external actions like searching scholarships,
checking eligibility, and planning application steps.
"""

class ScholarshipSearchTool:
    """Simulates searching an external database for scholarships."""
    
    def search(self, profile):
        gender = profile.get("gender")
        cgpa = profile.get("cgpa", 0)

        results = []

        # Scholarship 1
        if gender == "female" and cgpa >= 8.0:
            results.append({
                "name": "Women in Technology Award",
                "criteria": {"gender": "female", "cgpa": 8.0},
                "deadline": "2025-03-10",
            })

        # Scholarship 2
        if cgpa >= 7.5:
            results.append({
                "name": "General Merit Support",
                "criteria": {"cgpa": 7.5},
                "deadline": "2025-02-01",
            })

        return results


class EligibilityTool:
    """Checks if a student satisfies scholarship requirements."""

    def evaluate(self, profile, scholarships):
        evaluations = []

        for s in scholarships:
            eligible = True
            reasons = []

            for key, value in s["criteria"].items():
                if profile.get(key) != value and profile.get(key, 0) < value:
                    eligible = False
                    reasons.append(f"Failed {key} requirement")

            evaluations.append({
                "scholarship": s["name"],
                "eligible": eligible,
                "reasons": reasons
            })

        return evaluations


class ApplicationPlanTool:
    """Generates a simple application checklist for each scholarship."""

    def plan(self, scholarships):
        plans = []
        default_steps = [
            "Prepare transcripts",
            "Prepare ID and income certificate",
            "Write a short application statement",
            "Submit before deadline"
        ]

        for s in scholarships:
            plans.append({
                "scholarship": s["name"],
                "steps": default_steps
            })

        return plans
