from scholarscout_agents import (
    ProfileAgent,
    DiscoveryAgent,
    EligibilityAgent,
    AdvisorAgent,
    PlannerAgent,
    Orchestrator
)

def run_demo():
    print("\n--- ScholarScout Demo Output ---\n")

    # Sample student profile
    user_profile = {
        "gender": "female",
        "year": "2nd year",
        "income": "low",
        "cgpa": 8.7
    }

    orchestrator = Orchestrator()
    result = orchestrator.run(user_profile)

    print(result)

if __name__ == "__main__":
    run_demo()
