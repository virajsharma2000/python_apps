import pysims

token_id = pysims.show_token_id()

sims_client = pysims.SIMS(token_id)

message = sims_client.send_message(
    from_firstname = 'yash',
    from_lastname = 'sharma',
    to_firstname = 'viraj',
    to_lastname = 'sharma',
    your_message = 'hello,calling pysims using python'
    )

print(message)
