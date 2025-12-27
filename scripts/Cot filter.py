import pandas as pd

def cot_filter(path, market_code, columns_needed, show_columns=False, savepath=None):
    import os
    df = pd.read_csv(path, low_memory=False)

    if show_columns:
        print("Available columns:")
        print(df.columns.tolist())

    # === Handle different possible column names across years ===
    market_code_col = None
    for col in df.columns:
        if "CFTC" in col and ("Market Code" in col or "Contract Market Code" in col):
            market_code_col = col
            break

    if market_code_col is None:
        raise KeyError("No CFTC market code column found! Check your CSV.")

    # Clean the market code: convert to string and strip spaces
    df[market_code_col] = df[market_code_col].astype(str).str.strip()

    # Normalize market_code input
    market_code_str = str(market_code).strip()

    # Filter rows for the desired market
    df = df[df[market_code_col] == market_code_str]

    if df.empty:
        print(f"Warning: No data found for market code {market_code_str}")
        print("Available codes in this file:")
        print(sorted(df[market_code_col].unique()))
        return pd.DataFrame()

    # Fix date column name (changes over years)
    date_col = None
    for col in ["As of Date in Form YYYY-MM-DD", "Report Date as YYYY-MM-DD", "As of Date"]:
        if col in df.columns:
            date_col = col
            break

    if date_col is None:
        raise KeyError("No date column found!")

    df["Date"] = pd.to_datetime(df[date_col], errors='coerce',dayfirst= True)
    df = df.set_index("Date").sort_index()

    # Ensure requested columns exist
    missing_cols = [col for col in columns_needed if col not in df.columns]
    if missing_cols:
        print(f"Warning: These columns not found: {missing_cols}")

    # Select only available requested columns
    available_cols = [col for col in columns_needed if col in df.columns]
    result = df[available_cols]

    if savepath:
        if os.path.isdir(savepath):  # if savepath is a folder
            base = os.path.basename(path).replace(".csv", "")
            filename = f"{base}_filtered_{market_code}.csv"
            savepath = os.path.join(savepath, filename)
            print( "   Saved to folder")
        result.to_csv(savepath)

    return result