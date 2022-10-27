from loguru import logger

"""I fucked DRY"""


def module_5_a(address, private_key):
    """
    @ Swapping & Stablecoins (Polygon)
    @ https://beta.layer3.xyz/bounties/get-started-on-polygon
    @ swap matic -> usdc
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module5

    # setup
    web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
        )

        abi = abi_module5

        contract = web3.eth.contract(address=contract_address, abi=abi)

        wmatic = Web3.toChecksumAddress("0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270")
        pos_usdc = Web3.toChecksumAddress("0x2791bca1f2de4661ed88a30c99a7a9449aa84174")
        who_swap = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        value = 100000000000000

        data = contract.encodeABI(
            fn_name="exactInputSingle",
            args=[(wmatic, pos_usdc, 500, who_swap, value, 64, 0)],
        )

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        multicall_function = contract.get_function_by_selector("0x5ae401dc")

        try:
            transaction = multicall_function(deadline, [data]).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_10_a(address, private_key):
    """
    @ Sending Crypto (Polygon)
    @ https://beta.layer3.xyz/bounties/sending-crypto-polygon
    """
    # imports
    import secrets
    from web3 import Web3
    from abis import abi_module10
    from eth_account import Account

    # setup
    web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic

    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
        )
        abi = abi_module10

        contract = web3.eth.contract(address=contract_address, abi=abi)

        recipient_private_key = "0x" + secrets.token_hex(32)
        account = Account.from_key(recipient_private_key)
        recipient_address = account.address

        amount = 80

        transfer_function = contract.get_function_by_selector("0xa9059cbb")
        try:
            transaction = transfer_function(recipient_address, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )
            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )
            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_11_a(address, private_key):
    """
    @ Swapping & Stablecoins (Polygon)
    @ https://beta.layer3.xyz/bounties/swap-into-stablecoins-polygon
    @ swap matic -> usdt
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module11_a

    # setup
    web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
        )

        abi = abi_module11_a

        contract = web3.eth.contract(address=contract_address, abi=abi)

        abi = json.loads(abi)

        wmatic = Web3.toChecksumAddress("0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270")
        pos_usdt = Web3.toChecksumAddress("0xc2132d05d31c914a87c6611c10748aeb04b58e8f")
        who_swap = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        value = 10000000000000

        data = contract.encodeABI(
            fn_name="exactInputSingle",
            args=[(wmatic, pos_usdt, 500, who_swap, value, 7, 0)],
        )

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        multicall_function = contract.get_function_by_selector("0x5ae401dc")

        try:
            transaction = multicall_function(deadline, [data]).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            print(f"TX hash: {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_11_b(address, private_key):
    """
    @ Swapping & Stablecoins (Polygon)
    @ https://beta.layer3.xyz/bounties/swap-into-stablecoins-polygon
    @ swap matic -> dai
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module11_b

    # setup
    web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
        )

        abi = abi_module11_b

        contract = web3.eth.contract(address=contract_address, abi=abi)

        abi = json.loads(abi)

        wmatic = Web3.toChecksumAddress("0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270")
        dai = Web3.toChecksumAddress("0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063")
        who_swap = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        value = 10000000000000

        data = contract.encodeABI(
            fn_name="exactInputSingle",
            args=[(wmatic, dai, 500, who_swap, value, 7, 0)],
        )

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        multicall_function = contract.get_function_by_selector("0x5ae401dc")
        try:
            transaction = multicall_function(deadline, [data]).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_11_c(address, private_key):
    """
    @ Swapping & Stablecoins (Polygon)
    @ https://beta.layer3.xyz/bounties/swap-into-stablecoins-polygon
    @ swap matic -> frax
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module11_c

    # setup
    web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x9bc2152fd37b196c0ff3c16f5533767c9a983971"
        )

        abi = abi_module11_c

        contract = web3.eth.contract(address=contract_address, abi=abi)

        abi = json.loads(abi)

        amountOutMin = 7978967234872144
        path_wmatic = Web3.toChecksumAddress(
            "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270"
        )
        path_frax = Web3.toChecksumAddress("0x45c32fA6DF82ead1e2EF74d17b76547EDdFaFF89")
        path = [path_wmatic, path_frax]

        address_to = Web3.toChecksumAddress(address)
        value = 10000000000000000

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        try:
            transaction = contract.functions.swapExactETHForTokens(
                amountOutMin, path, address_to, deadline
            ).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_13_a(address, private_key):
    """
    @ wBTC on Polygon: Curve
    @ https://beta.layer3.xyz/bounties/for-the-love-of-btc-ii-curve
    @ swap matic -> wbtc
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module11_a

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
        )

        abi = abi_module11_a

        contract = web3.eth.contract(address=contract_address, abi=abi)

        abi = json.loads(abi)

        wmatic = Web3.toChecksumAddress("0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270")
        wbtc_usdt = Web3.toChecksumAddress("0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6")
        who_swap = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        value = 10000000000000000  # 0.01 matic

        data = contract.encodeABI(
            fn_name="exactInputSingle",
            args=[(wmatic, wbtc_usdt, 500, who_swap, value, 41, 0)],
        )

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        multicall_function = contract.get_function_by_selector("0x5ae401dc")

        try:
            transaction = multicall_function(deadline, [data]).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_13_b(address, private_key):
    """
    @ wBTC on Polygon: Curve
    @ https://beta.layer3.xyz/bounties/for-the-love-of-btc-ii-curve
    @ swap matic -> usdt
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module11_a

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
        )

        abi = abi_module11_a

        contract = web3.eth.contract(address=contract_address, abi=abi)

        abi = json.loads(abi)

        wmatic = Web3.toChecksumAddress("0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270")
        pos_usdt = Web3.toChecksumAddress("0xc2132d05d31c914a87c6611c10748aeb04b58e8f")
        who_swap = Web3.toChecksumAddress("0x81289035b2a56028ad488618b2fee7d17f1cd2f1")
        value = 100000000000000000  # 0.1 matic

        data = contract.encodeABI(
            fn_name="exactInputSingle",
            args=[(wmatic, pos_usdt, 500, who_swap, value, 93099, 0)],
        )

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        multicall_function = contract.get_function_by_selector("0x5ae401dc")

        try:
            transaction = multicall_function(deadline, [data]).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_13_c(address, private_key):
    """
    @ wBTC on Polygon: Curve
    @ https://beta.layer3.xyz/bounties/for-the-love-of-btc-ii-curve
    @ approve
    """
    # imports
    from web3 import Web3
    from abis import abi_module13_c

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xc2132d05d31c914a87c6611c10748aeb04b58e8f"
        )

        abi = abi_module13_c

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0x1d8b86e3D88cDb2d34688e87E72F388Cb541B7C8"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_13_d(address, private_key):
    """
    @ wBTC on Polygon: Curve
    @ https://beta.layer3.xyz/bounties/for-the-love-of-btc-ii-curve
    @ usdt -> wBTC
    """
    # imports
    from web3 import Web3
    from abis import abi_module13_d

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x1d8b86e3d88cdb2d34688e87e72f388cb541b7c8"
        )

        abi = abi_module13_d

        contract = web3.eth.contract(address=contract_address, abi=abi)

        i = 2
        j = 3
        _dx = 50000
        _min_dy = 238

        exchange_underlying_function = contract.get_function_by_selector("0x65b2489b")

        try:
            transaction = exchange_underlying_function(
                i, j, _dx, _min_dy
            ).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_13_e(address, private_key):
    """
    @ wBTC on Polygon: Curve
    @ https://beta.layer3.xyz/bounties/for-the-love-of-btc-ii-curve
    @ approve
    """
    # imports
    from web3 import Web3
    from abis import abi_module13_c

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6"
        )

        abi = abi_module13_c

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0x1d8b86e3D88cDb2d34688e87E72F388Cb541B7C8"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")
        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_13_f(address, private_key):
    """
    @ wBTC on Polygon: Curve
    @ https://beta.layer3.xyz/bounties/for-the-love-of-btc-ii-curve
    @ lp wBTC
    """
    # imports
    from web3 import Web3
    from abis import abi_module13_d

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x1d8b86e3d88cdb2d34688e87e72f388cb541b7c8"
        )

        abi = abi_module13_d

        contract = web3.eth.contract(address=contract_address, abi=abi)

        _amounts = (0, 0, 0, 4, 0)
        _min_mint_amount = 83393963343

        add_liquidity_function = contract.get_function_by_selector("0x84738499")

        try:
            transaction = add_liquidity_function(
                _amounts, _min_mint_amount
            ).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_13_g(address, private_key):
    """
    @ wBTC on Polygon: Curve
    @ https://beta.layer3.xyz/bounties/for-the-love-of-btc-ii-curve
    @ approve
    """
    # imports
    from web3 import Web3
    from abis import abi_module13_c

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xdad97f7713ae9437fa9249920ec8507e5fbb23d3"
        )

        abi = abi_module13_c

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0xBb1B19495B8FE7C402427479B9aC14886cbbaaeE"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_13_h(address, private_key):
    """
    @ wBTC on Polygon: Curve
    @ https://beta.layer3.xyz/bounties/for-the-love-of-btc-ii-curve
    @ stake wBTC
    """
    # imports
    from web3 import Web3
    from abis import abi_module13_h

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xbb1b19495b8fe7c402427479b9ac14886cbbaaee"
        )

        abi = abi_module13_h

        contract = web3.eth.contract(address=contract_address, abi=abi)

        _value = 338441969609

        deposit_function = contract.get_function_by_selector("0xb6b55f25")

        try:
            transaction = deposit_function(_value).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_16_a(address, private_key):
    """
    Explore Avalanche: Intro to AVAX Staking
    https://beta.layer3.xyz/bounties/explore-avalanche-intro-to-avax-staking-1
    """
    # imports
    from web3 import Web3
    from abis import abi_module16_a

    # setup
    web3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    value = 400000000000000  # add random

    if web3.isConnected:

        # logic
        contract_address = Web3.toChecksumAddress(
            "0x2b2C81e08f1Af8835a78Bb2A90AE924ACE0eA4bE"
        )
        abi = abi_module16_a

        contract = web3.eth.contract(address=contract_address, abi=abi)

        try:
            transaction = contract.functions.submit().buildTransaction(
                {
                    "chainId": 43114,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_16_b(address, private_key):
    """
    Explore Avalanche: Intro to AVAX Staking
    https://beta.layer3.xyz/bounties/explore-avalanche-intro-to-avax-staking-1
    """
    # imports
    from web3 import Web3
    from abis import abi_module16_b

    # setup
    web3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    value = 400000000000000

    if web3.isConnected:

        # logic
        contract_address = Web3.toChecksumAddress(
            "0x2b2C81e08f1Af8835a78Bb2A90AE924ACE0eA4bE"
        )
        abi = abi_module16_b

        contract = web3.eth.contract(address=contract_address, abi=abi)

        sender = "0xF362feA9659cf036792c9cb02f8ff8198E21B4cB"

        try:
            transaction = contract.functions.approve(sender, value).buildTransaction(
                {
                    "chainId": 43114,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_16_c(address, private_key):
    """
    Explore Avalanche: Intro to AVAX Staking
    https://beta.layer3.xyz/bounties/explore-avalanche-intro-to-avax-staking-1
    """
    # imports
    from web3 import Web3
    from abis import abi_module16_c

    # setup
    web3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    value = int(0.0001 * (10**18))

    if web3.isConnected:

        # logic
        contract_address = Web3.toChecksumAddress(
            "0xf362fea9659cf036792c9cb02f8ff8198e21b4cb"
        )
        abi = abi_module16_c

        contract = web3.eth.contract(address=contract_address, abi=abi)

        try:
            transaction = contract.functions.mint(value).buildTransaction(
                {
                    "chainId": 43114,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_a(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ swap matic -> wETH
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module17_a

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
        )

        abi = abi_module17_a

        contract = web3.eth.contract(address=contract_address, abi=abi)

        wmatic = Web3.toChecksumAddress("0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270")
        pos_weth = Web3.toChecksumAddress("0x7ceb23fd6bc0add59e62ac25578270cff1b9f619")
        who_swap = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        value = 10000000000000000

        data = contract.encodeABI(
            fn_name="exactInputSingle",
            args=[(wmatic, pos_weth, 500, who_swap, value, 5762642572749, 0)],
        )

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        multicall_function = contract.get_function_by_selector("0x5ae401dc")

        try:
            transaction = multicall_function(deadline, [data]).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_b(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ swap matic -> usdt
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module17_a

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
        )

        abi = abi_module17_a

        contract = web3.eth.contract(address=contract_address, abi=abi)

        wmatic = Web3.toChecksumAddress("0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270")
        pos_usdt = Web3.toChecksumAddress("0xc2132d05d31c914a87c6611c10748aeb04b58e8f")
        who_swap = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        value = 1500000000000000000

        data = contract.encodeABI(
            fn_name="exactInputSingle",
            args=[(wmatic, pos_usdt, 500, who_swap, value, 1215807, 0)],
        )

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        multicall_function = contract.get_function_by_selector("0x5ae401dc")

        try:
            transaction = multicall_function(deadline, [data]).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_c(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ swap matic -> usdc
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module17_a

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
        )

        abi = abi_module17_a

        contract = web3.eth.contract(address=contract_address, abi=abi)

        wmatic = Web3.toChecksumAddress("0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270")
        pos_usdc = Web3.toChecksumAddress("0x2791bca1f2de4661ed88a30c99a7a9449aa84174")
        who_swap = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        value = 1500000000000000000

        data = contract.encodeABI(
            fn_name="exactInputSingle",
            args=[(wmatic, pos_usdc, 500, who_swap, value, 1215807, 0)],
        )

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        multicall_function = contract.get_function_by_selector("0x5ae401dc")

        try:
            transaction = multicall_function(deadline, [data]).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_d_1(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ approve usdc
    """
    # imports
    from web3 import Web3
    from abis import abi_module17_d_1

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
        )

        abi = abi_module17_d_1

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")
        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_d_2(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ approve usdt
    """
    # imports
    from web3 import Web3
    from abis import abi_module17_d_2

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xc2132d05d31c914a87c6611c10748aeb04b58e8f"
        )

        abi = abi_module17_d_2

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_e(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ mint
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module17_e

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xc36442b4a4522e871399cd717abdd847ab11fe88"
        )

        abi = abi_module17_e

        contract = web3.eth.contract(address=contract_address, abi=abi)

        token0 = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
        token1 = "0xc2132D05D31c914a87C6611C10748AEb04B58e8F"
        fee = 100
        tickLower = -3
        tickUpper = 13
        amount0Desired = 1099996
        amount1Desired = 223329
        amount0Min = 0
        amount1Min = 0
        recipient = address

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        params = (
            token0,
            token1,
            fee,
            tickLower,
            tickUpper,
            amount0Desired,
            amount1Desired,
            amount0Min,
            amount1Min,
            recipient,
            deadline,
        )

        mint_function = contract.get_function_by_selector("0x88316456")
        try:
            transaction = mint_function(params).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_f(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ approve dai
    """
    # imports
    from web3 import Web3
    from abis import abi_module17_f

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063"
        )

        abi = abi_module17_f

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0x445FE580eF8d70FF569aB36e80c647af338db351"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_g(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ add liquidity
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module17_g

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x445fe580ef8d70ff569ab36e80c647af338db351"
        )

        abi = abi_module17_g

        contract = web3.eth.contract(address=contract_address, abi=abi)

        _amounts = [100000000000, 0, 0]
        _min_mint_amount = 94057346311
        _use_underlying = True

        add_liquidity_function = contract.get_function_by_selector("0x2b6e993a")

        try:
            transaction = add_liquidity_function(
                _amounts, _min_mint_amount, _use_underlying
            ).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_h_1(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ approve usdc
    """
    # imports
    from web3 import Web3
    from abis import abi_module17_h_1

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
        )

        abi = abi_module17_h_1

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0x546C79662E028B661dFB4767664d0273184E4dD1"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_h_2(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ approve usdt
    """
    # imports
    from web3 import Web3
    from abis import abi_module17_h_1

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xc2132d05d31c914a87c6611c10748aeb04b58e8f"
        )

        abi = abi_module17_h_1

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0x546C79662E028B661dFB4767664d0273184E4dD1"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_i(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ addLiquidity
    """
    # imports
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module17_i

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x546c79662e028b661dfb4767664d0273184e4dd1"
        )

        abi = abi_module17_i

        contract = web3.eth.contract(address=contract_address, abi=abi)

        tokenA = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
        tokenB = "0xc2132D05D31c914a87C6611C10748AEb04B58e8F"
        pool = "0x38766867c0Ee0BD530777F5F19b0D0D28d270AB8"
        amountADesired = 10000
        amountBDesired = 9203
        amountAMin = 9950
        amountBMin = 9156
        vReserveRatioBounds = [
            5166349655479536086022716356821061,
            5218272767594908307992793908145895,
        ]
        to = address

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        addLiquidity_function = contract.get_function_by_selector("0x24341934")

        try:
            transaction = addLiquidity_function(
                tokenA,
                tokenB,
                pool,
                amountADesired,
                amountBDesired,
                amountAMin,
                amountBMin,
                vReserveRatioBounds,
                to,
                deadline,
            ).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_j_1(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ approve usdc
    """
    # imports
    from web3 import Web3
    from abis import abi_module17_j_1

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
        )

        abi = abi_module17_j_1

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_j_2(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ approve dai
    """
    # imports
    from web3 import Web3
    from abis import abi_module17_j_2

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063"
        )

        abi = abi_module17_j_2

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_17_k(address, private_key):
    """
    @ Bear Market Stablecoin Mastery: Polygon
    @ https://beta.layer3.xyz/bounties/bear-market-stablecoin-mastery-polygon
    @ addLiquidity
    """
    # imports
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module17_k

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xa5e0829caced8ffdd4de3c43696c57f7d7a678ff"
        )

        abi = abi_module17_k

        contract = web3.eth.contract(address=contract_address, abi=abi)

        tokenA = "0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063"
        tokenB = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
        amountADesired = 1000000000000
        amountBDesired = 1
        amountAMin = 995000000000
        amountBMin = 0
        to = address

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        addLiquidity_function = contract.get_function_by_selector("0xe8e33700")

        try:
            transaction = addLiquidity_function(
                tokenA,
                tokenB,
                amountADesired,
                amountBDesired,
                amountAMin,
                amountBMin,
                to,
                deadline,
            ).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_18_a(address, private_key):
    """
    @ Uniswap Pro: Swapping & LPing
    @ https://beta.layer3.xyz/bounties/uniswap-pro-swapping-and-lping
    @ approve
    """
    # imports
    from web3 import Web3
    from abis import abi_module17_j_2

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063"
        )

        abi = abi_module17_j_2

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_18_b(address, private_key):
    """
    @ Uniswap Pro: Swapping & LPing
    @ https://beta.layer3.xyz/bounties/uniswap-pro-swapping-and-lping
    @ mint
    """
    # imports
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module17_e

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://polygon-mainnet.g.alchemy.com/v2/4qjJEkBRDCW70NIZmTr1WnmG0c6qWux2"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xc36442b4a4522e871399cd717abdd847ab11fe88"
        )

        abi = abi_module17_e

        contract = web3.eth.contract(address=contract_address, abi=abi)

        token0 = "0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063"
        token1 = "0xc2132D05D31c914a87C6611C10748AEb04B58e8F"
        fee = 100
        tickLower = -276335
        tickUpper = -276315
        amount0Desired = 9969499723380
        amount1Desired = 12
        amount0Min = 0
        amount1Min = 0
        recipient = address

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        params = (
            token0,
            token1,
            fee,
            tickLower,
            tickUpper,
            amount0Desired,
            amount1Desired,
            amount0Min,
            amount1Min,
            recipient,
            deadline,
        )

        mint_function = contract.get_function_by_selector("0x88316456")
        try:
            transaction = mint_function(params).buildTransaction(
                {
                    "chainId": 137,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_18_c(address, private_key):
    """
    @ Uniswap Pro: Swapping & LPing
    @ https://beta.layer3.xyz/bounties/uniswap-pro-swapping-and-lping
    @ eth -> usdt
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module5

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://opt-mainnet.g.alchemy.com/v2/ukR1HPHHIAyYzHSeDTeDXH0exUUHLOg4"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
        )

        abi = abi_module5

        contract = web3.eth.contract(address=contract_address, abi=abi)

        weth = Web3.toChecksumAddress("0x4200000000000000000000000000000000000006")
        usdt = Web3.toChecksumAddress("0x94b008aa00579c1307b0ef2c499ad98a8ce58e58")
        who_swap = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        value = 1000000000000

        data = contract.encodeABI(
            fn_name="exactInputSingle",
            args=[(weth, usdt, 500, who_swap, value, 1455, 0)],
        )

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        multicall_function = contract.get_function_by_selector("0x5ae401dc")

        try:
            transaction = multicall_function(deadline, [data]).buildTransaction(
                {
                    "chainId": 10,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_18_d(address, private_key):
    """
    @ Uniswap Pro: Swapping & LPing
    @ https://beta.layer3.xyz/bounties/uniswap-pro-swapping-and-lping
    @ approve
    """
    # imports
    from web3 import Web3
    from abis import abi_module17_j_2

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://opt-mainnet.g.alchemy.com/v2/ukR1HPHHIAyYzHSeDTeDXH0exUUHLOg4"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58"
        )

        abi = abi_module17_j_2

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 10,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_18_e(address, private_key):
    """
    @ Uniswap Pro: Swapping & LPing
    @ https://beta.layer3.xyz/bounties/uniswap-pro-swapping-and-lping
    @ lp
    """
    # imports
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module18_e

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://opt-mainnet.g.alchemy.com/v2/ukR1HPHHIAyYzHSeDTeDXH0exUUHLOg4"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
        )

        abi = abi_module18_e

        contract = web3.eth.contract(address=contract_address, abi=abi)

        mint_function = contract.get_function_by_name("mint")

        token0 = Web3.toChecksumAddress("0x4200000000000000000000000000000000000006")
        token1 = Web3.toChecksumAddress("0x94b008aa00579c1307b0ef2c499ad98a8ce58e58")
        amount0Desired = 27781989455
        amount1Desired = 100
        amount0Min = 0
        amount1Min = 0
        recipient = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        mint_params = (
            token0,
            token1,
            500,
            -203490,
            -203480,
            amount0Desired,
            amount1Desired,
            amount0Min,
            amount1Min,
            recipient,
            deadline,
        )

        mint_data = contract.encodeABI(fn_name="mint", args=[mint_params])

        refundETH_data = contract.encodeABI(
            fn_name="refundETH",
            args=[],
        )

        data = [mint_data, refundETH_data]

        value = 27781989455

        try:
            multicall_function = contract.get_function_by_selector("0xac9650d8")
            transaction = multicall_function(data).buildTransaction(
                {
                    "chainId": 10,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_18_f(address, private_key):
    """
    @ Uniswap Pro: Swapping & LPing
    @ https://beta.layer3.xyz/bounties/uniswap-pro-swapping-and-lping
    @ eth -> usdt
    """
    # imports
    import json
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module5

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://arb-mainnet.g.alchemy.com/v2/yghHGnv19p9tYMjNfVN7__V2u8iQhVNm"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45"
        )

        abi = abi_module5

        contract = web3.eth.contract(address=contract_address, abi=abi)

        weth = Web3.toChecksumAddress("0x82af49447d8a07e3bd95bd0d56f35241523fbab1")
        usdt = Web3.toChecksumAddress("0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9")
        who_swap = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        value = 1000000000000

        data = contract.encodeABI(
            fn_name="exactInputSingle",
            args=[(weth, usdt, 500, who_swap, value, 1455, 0)],
        )

        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        multicall_function = contract.get_function_by_selector("0x5ae401dc")

        try:
            transaction = multicall_function(deadline, [data]).buildTransaction(
                {
                    "chainId": 42161,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_18_g(address, private_key):
    """
    @ Uniswap Pro: Swapping & LPing
    @ https://beta.layer3.xyz/bounties/uniswap-pro-swapping-and-lping
    @ approve
    """
    # imports
    from web3 import Web3
    from abis import abi_module17_j_2

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://arb-mainnet.g.alchemy.com/v2/yghHGnv19p9tYMjNfVN7__V2u8iQhVNm"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9"
        )

        abi = abi_module17_j_2

        contract = web3.eth.contract(address=contract_address, abi=abi)

        spender = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935

        approve_function = contract.get_function_by_selector("0x095ea7b3")

        try:
            transaction = approve_function(spender, amount).buildTransaction(
                {
                    "chainId": 42161,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_18_h(address, private_key):
    """
    @ Uniswap Pro: Swapping & LPing
    @ https://beta.layer3.xyz/bounties/uniswap-pro-swapping-and-lping
    @ lp
    """
    # imports
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module18_h

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://arb-mainnet.g.alchemy.com/v2/yghHGnv19p9tYMjNfVN7__V2u8iQhVNm"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0xc36442b4a4522e871399cd717abdd847ab11fe88"
        )

        abi = abi_module18_h

        contract = web3.eth.contract(address=contract_address, abi=abi)

        token0 = Web3.toChecksumAddress("0x82aF49447D8a07e3bd95BD0d56f35241523fBab1")
        token1 = Web3.toChecksumAddress("0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9")
        fee = 500
        tickLower = -887270
        tickUpper = 887270
        amount0Desired = 64233193914
        amount1Desired = 100
        amount0Min = 64073210617
        amount1Min = 100
        recipient = Web3.toChecksumAddress("0x81289035b2A56028ad488618B2FEe7d17f1cd2f1")
        now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        deadline = int(
            time.mktime(
                datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timetuple()
            )
            + 60 * 3
        )

        mint_params = (
            token0,
            token1,
            fee,
            tickLower,
            tickUpper,
            amount0Desired,
            amount1Desired,
            amount0Min,
            amount1Min,
            recipient,
            deadline,
        )

        mint_data = contract.encodeABI(fn_name="mint", args=[mint_params])

        refundETH_data = contract.encodeABI(
            fn_name="refundETH",
            args=[],
        )

        data = [mint_data, refundETH_data]

        value = 68569066716

        try:
            multicall_function = contract.get_function_by_selector("0xac9650d8")
            transaction = multicall_function(data).buildTransaction(
                {
                    "chainId": 42161,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_21_a(address, private_key):
    """
    @ Lending & Borrowing (Optimism)
    @ https://beta.layer3.xyz/bounties/lending-and-borrowing-optimism
    @ lend
    """
    # imports
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module21_a

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://opt-mainnet.g.alchemy.com/v2/ukR1HPHHIAyYzHSeDTeDXH0exUUHLOg4"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x76d3030728e52deb8848d5613abade88441cbc59"
        )

        abi = abi_module21_a

        contract = web3.eth.contract(address=contract_address, abi=abi)

        undefined = "0x794a61358D6845594F94dc1DB02A252b5b4814aD"
        onBehalfOf = "0x81289035b2A56028ad488618B2FEe7d17f1cd2f1"
        referralCode = 0

        value = 1000000000000

        try:
            depositETH_function = contract.get_function_by_selector("0x474cf53d")
            transaction = depositETH_function(
                undefined, onBehalfOf, referralCode
            ).buildTransaction(
                {
                    "chainId": 10,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "value": value,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)


def module_21_b(address, private_key):
    """
    @ Lending & Borrowing (Optimism)
    @ https://beta.layer3.xyz/bounties/lending-and-borrowing-optimism
    @ borrow
    """
    # imports
    import time
    import datetime
    from web3 import Web3
    from abis import abi_module21_b

    # setup
    web3 = Web3(
        Web3.HTTPProvider(
            "https://opt-mainnet.g.alchemy.com/v2/ukR1HPHHIAyYzHSeDTeDXH0exUUHLOg4"
        )
    )

    address = address
    private_key = private_key
    nonce = web3.eth.getTransactionCount(address)

    # logic
    if web3.isConnected:

        contract_address = Web3.toChecksumAddress(
            "0x794a61358d6845594f94dc1db02a252b5b4814ad"
        )

        abi = abi_module21_b

        contract = web3.eth.contract(address=contract_address, abi=abi)

        args = '0x0000000000000000000000000002000000000000000000000000000003e80002'

        try:
            borrow_function = contract.get_function_by_selector("0xd5eed868")
            transaction = borrow_function(args).buildTransaction(
                {
                    "chainId": 10,
                    "gasPrice": web3.eth.gas_price,
                    "from": address,
                    "nonce": nonce,
                }
            )

            signed_txn = web3.eth.account.sign_transaction(
                transaction, private_key=private_key
            )

            raw_tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_hash = web3.toHex(raw_tx_hash)
            logger.success(f"Wallet {address[:9]}, transaction hash - {tx_hash}")
        except Exception as e:
            logger.error(e)
