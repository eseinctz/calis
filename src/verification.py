from pysmt.shortcuts import Symbol, And, Implies, Not, Bool, Solver, Or
from pysmt.typing import BOOL
import matplotlib.pyplot as plt
import numpy as np

# Define symbols for protocol states and actions
controller_sends_key = Symbol("controller_sends_key", BOOL)
edge_receives_key = Symbol("edge_receives_key", BOOL)
intruder_intercepts_key = Symbol("intruder_intercepts_key", BOOL)
intruder_knows_receiver_priv_key = Symbol("intruder_knows_receiver_priv_key", BOOL)
intruder_knows_shared_key = Symbol("intruder_knows_shared_key", BOOL)
intruder_knows_aes_key = Symbol("intruder_knows_aes_key", BOOL)
edge_sends_message = Symbol("edge_sends_message", BOOL)
server_receives_message = Symbol("server_receives_message", BOOL)
intruder_intercepts_message = Symbol("intruder_intercepts_message", BOOL)
intruder_knows_message = Symbol("intruder_knows_message", BOOL)
intruder_knows_nonce = Symbol("intruder_knows_nonce", BOOL)
edge_authenticates = Symbol("edge_authenticates", BOOL)
server_authenticates = Symbol("server_authenticates", BOOL)
secure_channel = Symbol("secure_channel", BOOL)
message_encrypted = Symbol("message_encrypted", BOOL)
message_valid = Symbol("message_valid", BOOL)

# Define the protocol as a conjunction of logical constraints
protocol = And(
    Implies(controller_sends_key, And(secure_channel, Or(edge_receives_key, intruder_intercepts_key))),
    Implies(intruder_knows_shared_key, intruder_knows_receiver_priv_key),
    Implies(intruder_knows_aes_key, And(intruder_knows_shared_key, intruder_intercepts_key)),
    Implies(edge_sends_message, And(message_encrypted, secure_channel, Or(server_receives_message, intruder_intercepts_message))),
    Implies(server_receives_message, And(message_valid, server_authenticates)),
    Implies(message_valid, edge_sends_message),
    Implies(intruder_knows_message, And(intruder_intercepts_message, intruder_knows_aes_key, intruder_knows_nonce)),
    Implies(edge_receives_key, edge_authenticates),
    Not(intruder_knows_shared_key),
    Not(intruder_knows_aes_key),
    Not(intruder_knows_message),
    secure_channel,
    message_encrypted
)

# Define threat models
threat_models = [
    {"name": "ECC Key Secure, Nonce Secure", "assertion": And(Not(intruder_knows_receiver_priv_key), Not(intruder_knows_nonce))},
    {"name": "ECC Key Compromised", "assertion": intruder_knows_receiver_priv_key},
    {"name": "Nonce Compromised", "assertion": intruder_knows_nonce}
]

# Verify protocol under each threat model and collect results
results = []
for tm in threat_models:
    with Solver(name="z3") as solver:
        solver.add_assertion(protocol)
        solver.add_assertion(tm["assertion"])
        # Check secrecy: intruder does not know the message
        secrecy_holds = not solver.solve([intruder_knows_message])
        # Check authentication: if server receives message, then edge sent it
        auth_holds = not solver.solve([server_receives_message, Not(edge_sends_message)])
        results.append({
            "threat_model": tm["name"],
            "secrecy": 1 if secrecy_holds else 0,
            "authentication": 1 if auth_holds else 0
        })
        print(f"Verification for {tm['name']}:")
        print(f"  Secrecy: {'Holds' if secrecy_holds else 'Does not hold'}")
        print(f"  Authentication: {'Holds' if auth_holds else 'Does not hold'}")
