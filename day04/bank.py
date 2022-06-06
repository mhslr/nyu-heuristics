from typing import Dict
from dataclasses import dataclass

BTC_RATE = 29693.56
GAS_FEE = 0.05


@dataclass
class Account:
    name: str
    usd_balance: float
    btc_balance: float


@dataclass
class Bank:
    accounts: Dict[str, Account]

    def get_account(self, name):
        return self.accounts[name]

    def open_account(self, name, usd, btc):
        """
        open an account
        provision it
        add it to self.accounts
        """
        ...  # TODO

    def transfer_usd(self, acc_from, acc_to, amount_usd):
        """
        if from has enough balance:
            transfer amount from -> to
            return True
        otherwise:
            return False
        """
        return False

    def transfer_btc(self, acc_from, acc_to, amount_btc):
        """
        same as usd,
        except that "the blockchain" will take a GAS_FEE cut,
        proportional to initial amount transfered.
        round after 5 digits the amount received
        """
        amount_to = round(0.12312312, 5)
        return False

    def invest(self, acc, amount_usd):
        """
        if enough balance
            BUY crypto at BTC_RATE, 0 fees, round btc at 5
            return True
        """
        return False

    def panic(self, acc, amount_btc):
        """
        if enough balance
            SELL crypto at BTC_RATE, 0 fees, round usd at 3
            return True
        """
        return False
