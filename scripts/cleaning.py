import pandas as pd
import numpy as np


# 1. CLEANING FUNCTIONS


def clean_rate_column(df):
    """Extract numeric rating from text like '4.1/5', '3.9', 'NEW', '-'."""
    df["rate"] = df["rate"].astype(str).str.extract(r"(\d+\.\d+)")
    df["rate"] = pd.to_numeric(df["rate"], errors="coerce")
    return df


def clean_cost_column(df):
    """Remove commas from cost column and convert to numeric."""
    col = "approx_cost(for two people)"
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def clean_cuisines_column(df):
    """Standardize cuisines and extract primary cuisine."""
    if "cuisines" in df.columns:
        df["cuisines"] = df["cuisines"].astype(str).str.strip()
        df["primary_cuisine"] = df["cuisines"].str.split(",").str[0]
    return df


def handle_missing_values(df):
    """Fill or drop missing values appropriately."""
    if "rate" in df.columns:
        df["rate"] = df["rate"].fillna(df["rate"].median())

    if "approx_cost(for two people)" in df.columns:
        df["approx_cost(for two people)"] = df["approx_cost(for two people)"].fillna(
            df["approx_cost(for two people)"].median()
        )

    if "votes" in df.columns:
        df["votes"] = df["votes"].fillna(0)

    return df


def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates()


def drop_irrelevant_columns(df):
    """Drop columns not useful for EDA."""
    cols_to_drop = [
        "url",
        "phone",
        "dish_liked",
        "reviews_list",
        "menu_item"
    ]
    existing = [c for c in cols_to_drop if c in df.columns]
    return df.drop(columns=existing)


# 2. FEATURE ENGINEERING


def create_cost_category(df):
    """Create cost category: Low, Medium, High."""
    col = "approx_cost(for two people)"
    if col in df.columns:
        df["cost_category"] = pd.cut(
            df[col],
            bins=[0, 300, 700, np.inf],
            labels=["Low", "Medium", "High"]
        )
    return df


def create_rating_category(df):
    """Create rating quality category."""
    if "rate" in df.columns:
        df["rating_category"] = pd.cut(
            df["rate"],
            bins=[0, 2.5, 3.5, 4.5, 5.1],
            labels=["Poor", "Average", "Good", "Excellent"]
        )
    return df

# 3. MASTER CLEANING FUNCTION
def clean_dataset(df):
    """Runs all cleaning steps in correct order."""
    df = remove_duplicates(df)
    df = drop_irrelevant_columns(df)
    df = clean_rate_column(df)
    df = clean_cost_column(df)
    df = clean_cuisines_column(df)
    df = handle_missing_values(df)
    df = create_cost_category(df)
    df = create_rating_category(df)
    df.reset_index(drop=True, inplace=True)
    return df
