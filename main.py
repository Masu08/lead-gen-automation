from scraper import fetch_leads
from scoring import score_lead
from dm import generate_dm
from sheets import save_to_sheets

def main():
    leads = fetch_leads("fitnesscoach")

    filtered = [
        l for l in leads
        if l["followers"] and 200 < l["followers"] < 10000 and l["engagement"] and l["engagement"] > 0.02
    ]

    final_leads = []

    for lead in filtered:
        result = score_lead(lead)

        try:
            score = int(result.get("score", 0))
        except:
            score = 0

        if score > 70:
            dm = generate_dm(lead)
            lead["dm"] = dm
            final_leads.append(lead)

            print(f"\nDM to {lead['username']}:\n{dm}")

    if final_leads:
        save_to_sheets(final_leads)

if __name__ == "__main__":
    main()
