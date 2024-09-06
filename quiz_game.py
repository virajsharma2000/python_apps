from web3 import Web3

account_address = input('Enter your account address: ')

score = 0

questions_and_answers = {
    'question1':'vitalik buterin',
    'question2':'18',
    'question3':'canada'
    'question4':'russia'
    }

print('\n\n')

question1 = input('who created ethereum blockchain?')

if question1 == questions_and_answers.get('question1'):
    score += 1
    
question2 = input('wei has how many zeros?')

if question2 == questions_and_answers.get('question2'):
    score += 1

question3 = input('where does currently vitalik buterin live?')

if question3 == questions_and_answers.get('question3'):
    score += 1

question4 = input('before migrating to canada where did vitalik buterin lived?')

if question4 == questions_and_answers.get('question4'):
    score += 1
    

eth_blockchain = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/mY45HFGBigF0RFWsGjtlBl-lDLqzmbey'))

nounce = eth_blockchain.eth.transaction_count('0x03747De51920F67b0b49ed9b03D48D3173b6e9D3')

tx = {
    'nounce':nounce,
    'from':'0x03747De51920F67b0b49ed9b03D48D3173b6e9D3',
    'to':account_address,
    'value':score
    }

signed_tx = eth_blockchain.eth.sign_transaction(tx,'0xc30b17d5b2014e857941c063ec5adefd754fa9d9da891b16acddff9c9f99c68a')

eth_blockchain.eth.send_raw_transaction(signed_tx.rawTransaction)
