
def transform_data(df):
    df['word_count'] = df['clean_message'].apply(lambda x: len(x.split()))
    return df
