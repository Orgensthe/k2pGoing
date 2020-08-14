def factorial(n):

    def tailFactorial(n,result):
        if n == 1:
            return result

        return tailFactorial(n-1,result*n)

    return tailFactorial(n,1)