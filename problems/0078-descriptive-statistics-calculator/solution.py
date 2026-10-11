import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    pass

    data=np.asarray(data)

    if data.size==0:

        raise ValueError("Dataset cannot be empty")

    mean=np.mean(data)
    median=np.median(data)
    val,cnt=np.unique(data,return_counts=True)
    mode=val[np.argmax(cnt)]
    var=np.var(data)
    std=np.std(data)

    q1=np.percentile(data,25)
    q2=np.percentile(data,50)
    q3=np.percentile(data,75)
    iqr=q3-q1

    return {
        "mean":float(mean),
        "median":float(median),
        "mode":mode.item(),
        "variance":float(var),
        "standard_deviation":float(std),
        "25th_percentile":float(q1),
        "50th_percentile":float(q2),
        "75th_percentile":float(q3),
        "interquartile_range":float(iqr)
    }