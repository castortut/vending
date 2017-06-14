import requests

URL = "http://127.0.0.1:8000"


KEY_SUCCESS = 'success'
KEY_ACCOUNT = 'account'
KEY_BALANCE = 'balance'
KEY_MSG1 = 'message'
KEY_MSG2 = 'message2'


class Result:
    """
    Object to save the result of an API call
    """
    success = False
    error   = False
    
    account = None
    balance = None
    
    message1 = None
    message2 = None

    def __init__(self, success=False, account=None, balance=None, message1=None, message2=None, error=False):
        """
        :param success: Was the operation successful
         :type success: bool or None
         
        :param token: Name of the account
         :type token: str or None
        :param balance: Account balance in cents (1.23€ => 123)
         :type balance: int or None
         
        :param message1: Server-sent message row 1
         :type message1: str 
        :param message2: Server-sent message row 2
         :type message2: str
        
        :param error: Did an error occur while parsing the API call result
         :type error: bool
        """
        self.success = success
        
        self.account = account
        self.balance = balance
        
        self.message1 = message1
        self.message2 = message2
        
        self.error = error

    @staticmethod
    def from_object(o):

        try:
            success = o[KEY_SUCCESS]

            if success:
                account = o[KEY_ACCOUNT]
                balance = o[KEY_BALANCE]

                message1 = None
                message2 = None
            else:
                account = None
                balance = None

                message1 = o[KEY_MSG1]
                if KEY_MSG2 in o.keys():
                    message2 = o[KEY_MSG2]
                else:
                    message2 = None

            return Result(success=success, account=account, balance=balance,
                          message1=message1,message2=message2, error=False)
        except ValueError:
            return Result(error=True)


class Bank:
    def __init__(self):
        pass

    def make_transaction(self, token, amount):
        """
        Attempt to make a transaction
        :param token: The token associated with the account to do the transaction against
         :type token: str
        :param amount: Amount of currency to move in cents
         :type amount: int
        :return: Result of the transaction
        :rtype: Result
        """

        req = requests.post(URL + "/api/token/" + token + "/transaction", {'amount': amount})
        return Result.from_object(req.json())


    def get_balance(self, token):
        """
        Attempt to get account balance
        :param token: The token associated with the account to get the balance for
         :type token: str
        :return: Account balance
        :rtype: Result
        """

        req = requests.get(URL + "/api/token/" + token + "/balance")
        return Result.from_object(req.json())

        