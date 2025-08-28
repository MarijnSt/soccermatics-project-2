def get_top_players(df, n=10):
    """
    Get the players who score the most xD and danger passes per 90.

    Parameters
    ----------
    df: pd.DataFrame
        A dataframe with player stats. Contains xD per 90 and danger passes per 90.
    n: int
        The number of top players to return for each role.

    Returns
    -------
    df_top_players: pd.DataFrame
        A dataframe with the top n players for each role.
    """
    # Create a copy of the data
    data = df.copy()
    
    # Better approach: vectorized operations
    data['xD_normalized'] = data.groupby('role')['xD_per_90'].transform(
        lambda x: (x - x.min()) / (x.max() - x.min())
    )
    
    data['danger_passes_normalized'] = data.groupby('role')['danger_passes_per_90'].transform(
        lambda x: (x - x.min()) / (x.max() - x.min())
    )
    
    # Create combined danger score
    data['danger_score'] = data['xD_normalized'] + data['danger_passes_normalized']
    
    # Get top n players for each role
    df_top_players = data.groupby('role').apply(
        lambda x: x.nlargest(n, 'danger_score')
    ).reset_index(drop=True)
    
    return df_top_players