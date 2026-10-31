def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    # Your code here
    pass

    totalx=0
    countxy=0

    for i,j in data:

      if i==x:
        totalx+=1

        if j==y:
          countxy+=1
    
    if totalx==0:

      return 0.0
    
    return round(countxy/totalx,4)