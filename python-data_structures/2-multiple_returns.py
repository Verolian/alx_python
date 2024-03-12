def multiple_returns(sentence):
    if not sentence:  # Check if the sentence is empty
        return (0, None)  # Return (0, None) if the sentence is empty
    else:
        return (len(sentence), sentence[0])  # Return tuple with length and first character