import requests
import pandas as pd

api_url = "https://remoteok.com/api"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    jobs_data = response.json()
else:
    print("Failed to fetch data:", response.status_code)
    exit()

jobs_list = []
for job in jobs_data[1:]:
    company = job.get("company", "N/A")
    role = job.get("position", "N/A")
    location = job.get("location", "Remote") if job.get("location") else "Remote"
    tags = job.get("tags", [])
    job_type = job.get("job_type", [])
    team = job.get("team", [])
    features = list(set(tags + job_type + team))
    features_str = ", ".join(features)
    jobs_list.append({
        "Company Name": company,
        "Job Role": role,
        "Location": location,
        "Features/Tags": features_str
    })

df = pd.DataFrame(jobs_list)
df.to_csv("remoteok_jobs.csv", index=False)

print("Data successfully saved to remoteok_jobs.csv")


