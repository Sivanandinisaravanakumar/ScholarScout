class ProfileAgent:
    def store_profile(self, profile):
        return {"stored_profile": profile}


class DiscoveryAgent:
    def discover(self, profile):
        sample = [
            {
                "name": "Women in Technology Award",
                "criteria": {"gender": "female", "cgpa": 8.0},
                "deadline": "2025-03-10"
            },
            {
                "name": "General Merit Support",
                "criteria": {"cgpa": 7.5},
                "deadline": "2025-02-01"
            }
        ]
        return {"scholarships": sample}


class EligibilityAgent:
    def evaluate(self, profile, scholarships):
        evaluated = []

        for s in scholarships:
            required_cgpa = s["criteria"].get("cgpa", 0)
            required_gender = s["criteria"].get("gender", None)

            eligible = True
            reasons = []

            if profile["cgpa"] < required_cgpa:
                eligible = False
                reasons.append("CGPA below requirement")

            if required_gender and profile["gender"] != required_gender:
                eligible = False
                reasons.append("Gender requirement not met")

            evaluated.append({
                "scholarship": s["name"],
                "eligible": eligible,
                "reasons": reasons
            })

        return {"evaluated": evaluated}


class AdvisorAgent:
    def explain(self, evaluated):
        explanations = []
        for e in evaluated:
            if e["eligible"]:
                msg = f"You are eligible for {e['scholarship']}."
            else:
                msg = f"You are not eligible for {e['scholarship']} because: {', '.join(e['reasons'])}"

            explanations.append(msg)

        return {"advice": explanations}


class PlannerAgent:
    def create_plan(self, evaluated):
        plans = []
        for e in evaluated:
            if e["eligible"]:
                plans.append({
                    "scholarship": e["scholarship"],
                    "steps": [
                        "Prepare transcripts",
                        "Prepare ID and income certificate",
                        "Write a short application statement",
                        "Submit before deadline"
                    ]
                })
        return {"plans": plans}


class Orchestrator:
    def __init__(self):
        self.profile_agent = ProfileAgent()
        self.discovery_agent = DiscoveryAgent()
        self.eligibility_agent = EligibilityAgent()
        self.advisor_agent = AdvisorAgent()
        self.planner_agent = PlannerAgent()

    def run(self, profile):
        p = self.profile_agent.store_profile(profile)
        d = self.discovery_agent.discover(profile)

        e = self.eligibility_agent.evaluate(
            profile,
            d["scholarships"]
        )

        a = self.advisor_agent.explain(e["evaluated"])
        plan = self.planner_agent.create_plan(e["evaluated"])

        return {
            "profile": p,
            "discovered": d,
            "eligibility": e,
            "advice": a,
            "plans": plan
        }
