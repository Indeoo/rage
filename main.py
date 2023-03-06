from web3 import Web3
import requests
from termcolor import cprint
import time
import json
import random

gasLimit = 4000000


RPC = {
        # '1': '',
        # '3': '',
        '10': 'https://mainnet.optimism.io',
        '56': 'https://bsc-dataseed.binance.org',
        '137': 'https://polygon-rpc.com',
        '42161': 'https://arb1.arbitrum.io/rpc',
        # '43114': '',  # https://support.avax.network/en/articles/4626956-how-do-i-set-up-metamask-on-avalanche
    }


def approveToken():
    global address
    # gasPrice = intToDecimal(0.0000000001, 18)
    nonce = web3.eth.get_transaction_count(address_wallet)
    address = web3.toChecksumAddress('0xff970a61a04b1ca14834a43f5de4533ebddb5cc8')
    ABI = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"Blacklisted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"newBlacklister","type":"address"}],"name":"BlacklisterChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"pauser","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousPauser","type":"address"},{"indexed":true,"internalType":"address","name":"newPauser","type":"address"}],"name":"PauserChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"UnBlacklisted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"pauser","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"blacklist","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"blacklister","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"bridgeBurn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Address","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"bridgeInit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"bridgeMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"changeOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"gatewayAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"symbol","type":"string"},{"internalType":"uint8","name":"decimals","type":"uint8"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_gatewayAddress","type":"address"},{"internalType":"address","name":"_l1Address","type":"address"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"symbol","type":"string"},{"internalType":"uint8","name":"decimals","type":"uint8"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isBlacklisted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"l1Address","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pauser","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"setPauser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"transferAndCall","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"unBlacklist","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newBlacklister","type":"address"}],"name":"updateBlacklister","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
    contract = web3.eth.contract(address=address, abi=ABI)

    def intToDecimal(qty, decimal):
        return int(qty * int("".join(["1"] + ["0"] * decimal)))

    gasPrice = intToDecimal(0.0000000001, 18)
    contract_txn = contract.functions.approve('0x4521916972A76D5BFA65Fb539Cf7a0C2592050Ac',
                                              115792089237316195423570985008687907853269984665640564039457584007913129639935).buildTransaction(
        {
            'from': address_wallet,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce
        })
    signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key=privatekey)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    cprint(signed_txn)
    cprint(tx_hash)

def deposit():
    global address
    # gasPrice = intToDecimal(0.0000000001, 18)
    nonce = web3.eth.get_transaction_count(address_wallet)
    address = web3.toChecksumAddress('0x4521916972a76d5bfa65fb539cf7a0c2592050ac')
    ABI = '[{"inputs":[{"internalType":"address","name":"senderAddress","type":"address"}],"name":"AccessDenied","type":"error"},{"inputs":[],"name":"CannotPauseIfUnpauseInProgress","type":"error"},{"inputs":[],"name":"CannotUnpauseIfPauseInProgress","type":"error"},{"inputs":[{"internalType":"uint32","name":"collateralId","type":"uint32"}],"name":"CollateralDoesNotExist","type":"error"},{"inputs":[{"internalType":"uint32","name":"collateralId","type":"uint32"}],"name":"CollateralNotAllowedForUse","type":"error"},{"inputs":[{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"}],"name":"IllegalSqrtPrice","type":"error"},{"inputs":[{"internalType":"contract IERC20","name":"incorrectAddress","type":"address"},{"internalType":"contract IERC20","name":"correctAddress","type":"address"}],"name":"IncorrectCollateralAddress","type":"error"},{"inputs":[{"internalType":"address","name":"invalidAddress","type":"address"}],"name":"InvalidCollateralAddress","type":"error"},{"inputs":[{"internalType":"enum IClearingHouseEnums.MulticallOperationType","name":"multicallOperationType","type":"uint8"}],"name":"InvalidMulticallOperationType","type":"error"},{"inputs":[{"internalType":"uint256","name":"errorCode","type":"uint256"}],"name":"InvalidSetting","type":"error"},{"inputs":[],"name":"InvalidTokenLiquidationParameters","type":"error"},{"inputs":[{"internalType":"int256","name":"keeperFee","type":"int256"}],"name":"KeeperFeeNotPositive","type":"error"},{"inputs":[{"internalType":"uint256","name":"notionalValue","type":"uint256"}],"name":"LowNotionalValue","type":"error"},{"inputs":[],"name":"NotRageTradeFactory","type":"error"},{"inputs":[{"internalType":"uint32","name":"poolId","type":"uint32"}],"name":"PoolDoesNotExist","type":"error"},{"inputs":[{"internalType":"uint32","name":"poolId","type":"uint32"}],"name":"PoolNotAllowedForTrade","type":"error"},{"inputs":[{"internalType":"uint256","name":"value","type":"uint256"}],"name":"SafeCast_UInt224Overflow","type":"error"},{"inputs":[],"name":"SlippageBeyondTolerance","type":"error"},{"inputs":[],"name":"T","type":"error"},{"inputs":[],"name":"Unauthorised","type":"error"},{"inputs":[],"name":"ZeroAddress","type":"error"},{"inputs":[],"name":"ZeroAmount","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"ownerAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"accountId","type":"uint256"}],"name":"AccountCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"contract IERC20","name":"cToken","type":"address"},{"components":[{"internalType":"contract IOracle","name":"oracle","type":"address"},{"internalType":"uint32","name":"twapDuration","type":"uint32"},{"internalType":"bool","name":"isAllowedForDeposit","type":"bool"}],"indexed":false,"internalType":"struct IClearingHouseStructures.CollateralSettings","name":"cTokenInfo","type":"tuple"}],"name":"CollateralSettingsUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousGovernancePending","type":"address"},{"indexed":true,"internalType":"address","name":"newGovernancePending","type":"address"}],"name":"GovernancePending","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousGovernance","type":"address"},{"indexed":true,"internalType":"address","name":"newGovernance","type":"address"}],"name":"GovernanceTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"paused","type":"bool"}],"name":"PausedUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint32","name":"poolId","type":"uint32"},{"components":[{"internalType":"uint16","name":"initialMarginRatioBps","type":"uint16"},{"internalType":"uint16","name":"maintainanceMarginRatioBps","type":"uint16"},{"internalType":"uint16","name":"maxVirtualPriceDeviationRatioBps","type":"uint16"},{"internalType":"uint32","name":"twapDuration","type":"uint32"},{"internalType":"bool","name":"isAllowedForTrade","type":"bool"},{"internalType":"bool","name":"isCrossMargined","type":"bool"},{"internalType":"contract IOracle","name":"oracle","type":"address"}],"indexed":false,"internalType":"struct IClearingHouseStructures.PoolSettings","name":"settings","type":"tuple"}],"name":"PoolSettingsUpdated","type":"event"},{"anonymous":false,"inputs":[{"components":[{"internalType":"uint16","name":"rangeLiquidationFeeFraction","type":"uint16"},{"internalType":"uint16","name":"tokenLiquidationFeeFraction","type":"uint16"},{"internalType":"uint16","name":"closeFactorMMThresholdBps","type":"uint16"},{"internalType":"uint16","name":"partialLiquidationCloseFactorBps","type":"uint16"},{"internalType":"uint16","name":"insuranceFundFeeShareBps","type":"uint16"},{"internalType":"uint16","name":"liquidationSlippageSqrtToleranceBps","type":"uint16"},{"internalType":"uint64","name":"maxRangeLiquidationFees","type":"uint64"},{"internalType":"uint64","name":"minNotionalLiquidatable","type":"uint64"}],"indexed":false,"internalType":"struct IClearingHouseStructures.LiquidationParams","name":"liquidationParams","type":"tuple"},{"indexed":false,"internalType":"uint256","name":"removeLimitOrderFee","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"minimumOrderNotional","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"minRequiredMargin","type":"uint256"}],"name":"ProtocolSettingsUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousTeamMultisigPending","type":"address"},{"indexed":true,"internalType":"address","name":"newTeamMultisigPending","type":"address"}],"name":"TeamMultisigPending","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousTeamMultisig","type":"address"},{"indexed":true,"internalType":"address","name":"newTeamMultisig","type":"address"}],"name":"TeamMultisigTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"acceptGovernanceTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"acceptTeamMultisigTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"createAccount","outputs":[{"internalType":"uint256","name":"newAccountId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"collateralId","type":"uint32"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"createAccountAndAddMargin","outputs":[{"internalType":"uint256","name":"newAccountId","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"slot","type":"bytes32"}],"name":"extsload","outputs":[{"internalType":"bytes32","name":"val","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32[]","name":"slots","type":"bytes32[]"}],"name":"extsload","outputs":[{"internalType":"bytes32[]","name":"","type":"bytes32[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"},{"internalType":"bool","name":"isInitialMargin","type":"bool"}],"name":"getAccountMarketValueAndRequiredMargin","outputs":[{"internalType":"int256","name":"marketValue","type":"int256"},{"internalType":"int256","name":"requiredMargin","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"}],"name":"getAccountNetProfit","outputs":[{"internalType":"int256","name":"accountNetProfit","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"},{"internalType":"uint32","name":"poolId","type":"uint32"}],"name":"getAccountNetTokenPosition","outputs":[{"internalType":"int256","name":"netPosition","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32","name":"poolId","type":"uint32"}],"name":"getRealTwapPriceX128","outputs":[{"internalType":"uint256","name":"realPriceX128","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32","name":"poolId","type":"uint32"}],"name":"getVirtualTwapPriceX128","outputs":[{"internalType":"uint256","name":"virtualPriceX128","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"governance","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"governancePending","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_rageTradeFactoryAddress","type":"address"},{"internalType":"address","name":"initialGovernance","type":"address"},{"internalType":"address","name":"initialTeamMultisig","type":"address"},{"internalType":"contract IERC20","name":"_defaultCollateralToken","type":"address"},{"internalType":"contract IOracle","name":"_defaultCollateralTokenOracle","type":"address"},{"internalType":"contract IInsuranceFund","name":"_insuranceFund","type":"address"},{"internalType":"contract IVQuote","name":"_vQuote","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newGovernancePending","type":"address"}],"name":"initiateGovernanceTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newTeamMultisigPending","type":"address"}],"name":"initiateTeamMultisigTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"insuranceFund","outputs":[{"internalType":"contract IInsuranceFund","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"}],"name":"liquidateLiquidityPositions","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"targetAccountId","type":"uint256"},{"internalType":"uint32","name":"poolId","type":"uint32"}],"name":"liquidateTokenPosition","outputs":[{"internalType":"int256","name":"keeperFee","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"},{"components":[{"internalType":"enum IClearingHouseEnums.MulticallOperationType","name":"operationType","type":"uint8"},{"internalType":"bytes","name":"data","type":"bytes"}],"internalType":"struct IClearingHouseStructures.MulticallOperation[]","name":"operations","type":"tuple[]"}],"name":"multicallWithSingleMarginCheck","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"numAccounts","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfPoolsToUpdateInThisTx","type":"uint256"}],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rageTradeFactoryAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"contract IVToken","name":"vToken","type":"address"},{"internalType":"contract IUniswapV3Pool","name":"vPool","type":"address"},{"internalType":"contract IVPoolWrapper","name":"vPoolWrapper","type":"address"},{"components":[{"internalType":"uint16","name":"initialMarginRatioBps","type":"uint16"},{"internalType":"uint16","name":"maintainanceMarginRatioBps","type":"uint16"},{"internalType":"uint16","name":"maxVirtualPriceDeviationRatioBps","type":"uint16"},{"internalType":"uint32","name":"twapDuration","type":"uint32"},{"internalType":"bool","name":"isAllowedForTrade","type":"bool"},{"internalType":"bool","name":"isCrossMargined","type":"bool"},{"internalType":"contract IOracle","name":"oracle","type":"address"}],"internalType":"struct IClearingHouseStructures.PoolSettings","name":"settings","type":"tuple"}],"internalType":"struct IClearingHouseStructures.Pool","name":"poolInfo","type":"tuple"}],"name":"registerPool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"},{"internalType":"uint32","name":"poolId","type":"uint32"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"}],"name":"removeLimitOrder","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"}],"name":"settleProfit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"},{"internalType":"uint32","name":"poolId","type":"uint32"},{"components":[{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"uint160","name":"sqrtPriceLimit","type":"uint160"},{"internalType":"bool","name":"isNotional","type":"bool"},{"internalType":"bool","name":"isPartialAllowed","type":"bool"},{"internalType":"bool","name":"settleProfit","type":"bool"}],"internalType":"struct IClearingHouseStructures.SwapParams","name":"swapParams","type":"tuple"}],"name":"swapToken","outputs":[{"internalType":"int256","name":"vTokenAmountOut","type":"int256"},{"internalType":"int256","name":"vQuoteAmountOut","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"teamMultisig","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"teamMultisigPending","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfPoolsToUpdateInThisTx","type":"uint256"}],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"cToken","type":"address"},{"components":[{"internalType":"contract IOracle","name":"oracle","type":"address"},{"internalType":"uint32","name":"twapDuration","type":"uint32"},{"internalType":"bool","name":"isAllowedForDeposit","type":"bool"}],"internalType":"struct IClearingHouseStructures.CollateralSettings","name":"collateralSettings","type":"tuple"}],"name":"updateCollateralSettings","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"},{"internalType":"uint32","name":"collateralId","type":"uint32"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"updateMargin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"poolId","type":"uint32"},{"components":[{"internalType":"uint16","name":"initialMarginRatioBps","type":"uint16"},{"internalType":"uint16","name":"maintainanceMarginRatioBps","type":"uint16"},{"internalType":"uint16","name":"maxVirtualPriceDeviationRatioBps","type":"uint16"},{"internalType":"uint32","name":"twapDuration","type":"uint32"},{"internalType":"bool","name":"isAllowedForTrade","type":"bool"},{"internalType":"bool","name":"isCrossMargined","type":"bool"},{"internalType":"contract IOracle","name":"oracle","type":"address"}],"internalType":"struct IClearingHouseStructures.PoolSettings","name":"newSettings","type":"tuple"}],"name":"updatePoolSettings","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"},{"internalType":"int256","name":"amount","type":"int256"}],"name":"updateProfit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint16","name":"rangeLiquidationFeeFraction","type":"uint16"},{"internalType":"uint16","name":"tokenLiquidationFeeFraction","type":"uint16"},{"internalType":"uint16","name":"closeFactorMMThresholdBps","type":"uint16"},{"internalType":"uint16","name":"partialLiquidationCloseFactorBps","type":"uint16"},{"internalType":"uint16","name":"insuranceFundFeeShareBps","type":"uint16"},{"internalType":"uint16","name":"liquidationSlippageSqrtToleranceBps","type":"uint16"},{"internalType":"uint64","name":"maxRangeLiquidationFees","type":"uint64"},{"internalType":"uint64","name":"minNotionalLiquidatable","type":"uint64"}],"internalType":"struct IClearingHouseStructures.LiquidationParams","name":"_liquidationParams","type":"tuple"},{"internalType":"uint256","name":"_removeLimitOrderFee","type":"uint256"},{"internalType":"uint256","name":"_minimumOrderNotional","type":"uint256"},{"internalType":"uint256","name":"_minRequiredMargin","type":"uint256"}],"name":"updateProtocolSettings","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountId","type":"uint256"},{"internalType":"uint32","name":"poolId","type":"uint32"},{"components":[{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"int128","name":"liquidityDelta","type":"int128"},{"internalType":"uint160","name":"sqrtPriceCurrent","type":"uint160"},{"internalType":"uint16","name":"slippageToleranceBps","type":"uint16"},{"internalType":"bool","name":"closeTokenPosition","type":"bool"},{"internalType":"enum IClearingHouseEnums.LimitOrderType","name":"limitOrderType","type":"uint8"},{"internalType":"bool","name":"settleProfit","type":"bool"}],"internalType":"struct IClearingHouseStructures.LiquidityChangeParams","name":"liquidityChangeParams","type":"tuple"}],"name":"updateRangeOrder","outputs":[{"internalType":"int256","name":"vTokenAmountOut","type":"int256"},{"internalType":"int256","name":"vQuoteAmountOut","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfPoolsToUpdateInThisTx","type":"uint256"}],"name":"withdrawProtocolFee","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

    contract = web3.eth.contract(address=address, abi=ABI)

    def intToDecimal(qty, decimal):
        return int(qty * int("".join(["1"] + ["0"] * decimal)))

    gasPrice = intToDecimal(0.0000000001, 18)
    contract_txn = contract.functions.createAccountAndAddMargin(3185269960,
                                              20000000).buildTransaction(
        {
            'from': address_wallet,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce
        })
    signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key=privatekey)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

if __name__ == "__main__":

    cprint(f'\n============================================= hodlmod.eth =============================================',
           'cyan')

    cprint(f'\nsubscribe to us : https://t.me/hodlmodeth', 'magenta')

    with open("private_keys.txt", "r") as f:
        keys_list = [row.strip() for row in f]


    for privatekey in keys_list:

        cprint(f'\n=============== start : {privatekey} ===============', 'white')

        ChainUrl = "https://arb1.arbitrum.io/rpc"
        web3 = Web3(Web3.HTTPProvider(ChainUrl))
        account = web3.eth.account.from_key(privatekey)
        address_wallet = account.address

        approveToken()
        deposit()

        tx_cost = []


