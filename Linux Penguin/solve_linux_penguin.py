# ECB codebook solver for the Penguin Challenge

words = [
    "biocompatibility", "biodegradability", "characterization", "contraindication",
    "counterbalancing", "counterintuitive", "decentralization", "disproportionate",
    "electrochemistry", "electrochemistry", "environmentalist", "internationality",
    "internationalism", "institutionalize", "microlithography", "microphotography",
    "misappropriation", "mischaracterized", "miscommunication", "misunderstanding",
    "photolithography", "phonocardiograph", "psychophysiology", "rationalizations",
    "representational", "responsibilities", "transcontinental", "unconstitutional"
]

# 🔽 Paste ALL ciphertexts you got when encrypting the words (same order)
oracle_ciphertexts = [
    # Round 1
    "2aab6b4031e72df2d3f5d99800924fd7", "246fc6f5658bec30b841e59b1405ccd1", "91a332e7dccfbc78fba5360eff2161f8", "65f2cfe249b24e0c77686c81219cd841",
    # Round 2
    "21e05bcfe9db448b3c7435427397ff81", "6f694055612c373e924d5597cbd72523", "92d80cb49bcf6248e6e728978b8a9577", "8c776e0815127a7d08767c3445bb8451",
    # Round 3
    "b0a7ed7ddd9ffd525cb5d82c9d796ad7", "dedc5cd0d2e63db05d88d30cc82b6b3a", "96021d5e7ef9881856209b4eb429169c", "30d86c49dd3759ab7924b8c5c7a60184",
    # Round 4
    "8599dc9ff43d51484e7031b4c8ae5661", "713150f28c94ec80926dc47f96fe8e94", "ee3aa702f26bf318203034ec01248916", "f9b6a1bd57ec097ce4f4bace2eb54b23",
    # Round 5
    "0133a7167ffdbc3d982693d348ebe9f4", "ef48da592445b0276677362dba7533e4", "4ea3d4324a57c861be5738d3422cccbf", "f9eeecfc15825cedf8648af8d6e1f9c8",
    # Round 6
    "01dc9512a49aab95230379825257a7b3" ,"dc4bd97a1796855a86a61a5a8dad7042", "2c9a80f98d4bed9545e02a84564ff4e4", "6e7bc7666024dc94a807a814282164d0",
    # Round 7
    "6a4574f041cf9a12a4b5921ecf67c8ba" ,"183f51a87b5a3c7b6e70160cb5f06ac6", "39966d5b3cb733ec6d14a9940312ebd2" ,"66bbc47bbf8b37700d85b6cc75f9d1bd",
]

assert len(words) == len(oracle_ciphertexts)

# Build ECB codebook
codebook = {}
for word, ct in zip(words, oracle_ciphertexts):
    codebook[ct] = word

# 🔽 Paste the final ciphertext shown by the challenge
final_ciphertext = "ee3aa702f26bf318203034ec01248916 246fc6f5658bec30b841e59b1405ccd1 ef48da592445b0276677362dba7533e4 ef48da592445b0276677362dba7533e4 f9b6a1bd57ec097ce4f4bace2eb54b23"

decoded_words = []
for ct in final_ciphertext.split():
    decoded_words.append(codebook[ct])

print("Recovered words:")
for w in decoded_words:
    print("-", w)

print("\nSubmit these words in any order to get the flag.")
