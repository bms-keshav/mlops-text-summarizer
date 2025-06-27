def ingest_data():
    input_path = "Data/raw/news_summary.csv"
    output_path = "Data/processed/"

    df = pd.read_csv(input_path, encoding='iso-8859-1')

    # Use 'ctext' as full text, 'headlines' as summary
    df = df[["ctext", "headlines"]].rename(columns={"ctext": "text", "headlines": "summary"})
    df = df.dropna()

    # Save full cleaned dataset
    df.to_csv(os.path.join(output_path, "cleaned_data.csv"), index=False)

    # Optional: split into train/test for future training use
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    train_df.to_csv(os.path.join(output_path, "train.csv"), index=False)
    test_df.to_csv(os.path.join(output_path, "test.csv"), index=False)

    print("✅ Data ingestion complete. Files saved to:", output_path)
