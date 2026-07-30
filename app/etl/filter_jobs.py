from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parents[2] / "data"
RAW_JOBS_FILE = DATA_FOLDER / "jobs_raw.parquet"
PROCESSED_FOLDER = DATA_FOLDER / "processed"
OUTPUT_FILE = PROCESSED_FOLDER / "software_jobs.parquet"

df = pd.read_parquet(RAW_JOBS_FILE)

print("Original rows:", len(df))

us_values= ["United States", "USA", "US", "U.S.", "U.S.A.", "America", "United States of America"]

df_us= df[df["country"].isin(us_values)].copy()

print("US rows:" , len(df_us))

software_title_keywords = (
    "software engineer|software developer|backend engineer|backend developer|"
    "frontend developer|front end developer|full stack|fullstack|"
    "java developer|java engineer|python developer|python engineer|"
    "data engineer|data analyst|data scientist|business intelligence|bi analyst|"
    "cloud engineer|devops engineer|site reliability engineer|sre|"
    "machine learning engineer|ml engineer|platform engineer|"
    "database developer|database engineer|application developer|"
    "application engineer|systems engineer|network engineer|security engineer|"
    "data platform engineer|analytics engineer"
)

tech_skill_keywords = (
    "python|java|sql|javascript|typescript|react|angular|spring|"
    "aws|azure|gcp|docker|kubernetes|postgresql|mysql|oracle|"
    "snowflake|spark|kafka|tableau|power bi|git|linux|api"
)

exclude_keywords = (
    "physical therapist|occupational therapist|civil engineer|"
    "mechanical engineer|manufacturing engineer|electrical engineer|"
    "project engineer|construction engineer|field engineer|"
    "biomedical engineer|clinical engineer"
)


# ---------------------------------------------------
# 5. CREATE SOFTWARE / IT MASK
# ---------------------------------------------------

title_mask = (
    df_us["title"]
    .fillna("")
    .str.contains(
        software_title_keywords,
        case=False,
        regex=True
    )
)

skill_mask = (
    df_us["skills_required"]
    .fillna("")
    .str.contains(
        tech_skill_keywords,
        case=False,
        regex=True
    )
)

function_mask = (
    df_us["function"]
    .fillna("")
    .str.contains(
        "technology|software|data|engineering|information technology|analytics",
        case=False,
        regex=True
    )
)

exclude_mask = (
    df_us["title"]
    .fillna("")
    .str.contains(
        exclude_keywords,
        case=False,
        regex=True
    )
)


software_mask = (
    title_mask
    | (function_mask & skill_mask)
) & ~exclude_mask


df_software = df_us[software_mask].copy()

print("US Software / IT rows:", len(df_software))


columns_to_keep = [
    "title",
    "normalized_title",
    "company_name",
    "industry",
    "function",
    "employment_type",
    "work_model",
    "experience_level",
    "job_level_normalized",
    "years_experience_numeric",
    "education_level",
    "skills_required",
    "certifications",
    "salary_min",
    "salary_max",
    "salary_currency",
    "salary_rate_unit",
    "city",
    "country",
    "location_resolved",
    "latitude",
    "longitude",
    "visa_sponsorship_available",
    "date_posted",
]

df_software = df_software[columns_to_keep]

PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)


df_software.to_parquet(
    OUTPUT_FILE,
    index=False,
)

print("Final rows:", len(df_software))
print("Final columns:", len(df_software.columns))
print("Saved to:", OUTPUT_FILE)
print("\nSample job titles:")
print(df_software["title"].head(30).to_string(index=False))
print("\nTop 30 job titles:")
print(
    df_software["normalized_title"]
    .value_counts()
    .head(30)
)