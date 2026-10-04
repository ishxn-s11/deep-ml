def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    """

    def evaluate(coeffs):
        res=0
        p=len(coeffs)-1

        for i in coeffs:
            res+=i*(x**p)
            p-=1

        return res

    def derivative_coeffs(coeffs):
        res=[]
        p=len(coeffs)-1

        for i in coeffs[:-1]:
            res.append(i*p)
            p-=1

        return res

    g=evaluate(g_coeffs)
    h=evaluate(h_coeffs)

    g_prime=evaluate(derivative_coeffs(g_coeffs))
    h_prime=evaluate(derivative_coeffs(h_coeffs))

    return (g_prime*h-g*h_prime)/(h**2)