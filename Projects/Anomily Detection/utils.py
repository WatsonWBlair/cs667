import pandas as pd

def targetEncode(data: pd.DataFrame, targetFeature: str, encodeFeatures: list[str]):
    """
    Performs target encoding using the median of the targetFeature.

    Args:
        data (pd.DataFrame): Dataframe to perform target encoding in.
        targetFeature str: The target feature to encode features to.
        encodeFeatures (list[str]): Features to encode.

    Returs:
        pd.DataFrame: Data Frame with target encoded features
    """
    result = data.copy(deep=True)
    for feature in encodeFeatures:
        categories = result[feature].unique()
        grouped = result.groupby(feature)
        for category in categories:
            encodedValue = grouped[targetFeature].median()[category]
            result.loc[result[feature] == category, feature] = encodedValue
    return result

def labelEncode(data: pd.DataFrame, encodeFeatures: list[str]):
    """
    Performs label encoding using an integer for each unique value of the featue being encoded.

    Args:
        data (pd.DataFrame): Dataframe to perform label encoding in.
        encodeFeatures (list[str]): Features to encode.

    Returs:
        pd.DataFrame: Data Frame with label encoded features
    """
    result = data.copy()

    for feature in encodeFeatures:
        categories = result[feature].unique()
        for i, category in enumerate(categories):
            result.loc[result[feature] == category, feature] = i

    return result

def oneHotEnocde(data: pd.DataFrame, encodeFeatures: list[str]):
    """
    Performs integer One Hot Encoding on the provided features.

    Args:
        data (pd.DataFrame): Dataframe to perform One Hot encoding on.
        encodeFeatures (list[str]): Features to encode.

    Returs:
        pd.DataFrame: Data Frame with label encoded features
    """
    result = data.copy()
    
    result = pd.get_dummies(result, columns=encodeFeatures, dtype=int, drop_first=True)

    return result