import pandas as pd


def is_spam(message, model, words):
    """
    Predicts whether a given message or list of messages is spam or not.

    Parameters:
    - message (str or list of str): The message or list of messages to be classified. If a single message is provided,
      it should be a string. If multiple messages are provided, they should be contained within a list of strings.

    Returns:
    - pred (array-like): An array-like object containing the predicted labels for each input message. A value of 1
      indicates that the message is classified as spam, while a value of 0 indicates that the message is not spam.
    """

    def count_uppercase(strings):
        uppercase_counts = []
        for string in strings:
            uppercase_count = sum(1 for char in string if char.isupper())
            uppercase_counts.append(uppercase_count)
        return sum(uppercase_counts)

    def message_to_words(message_):
        """
        The message_to_words(message) function accepts a string as input.
        It splits the input string into individual words,
        converts each word to lowercase, and returns a list of these lowercase words.
        """
        return message_.lower().split()

    def make_rows(messages, words=words):
        """
        The make_rows(messages, words) function accepts a list of messages and a list of words.
        It generates a list of dictionaries where each dictionary represents a message and
        indicates the presence of each word from the specified word list.
        """
        result = []
        symbols_to_check = set(".,!@#$%^&*()-+_=:;?/\\1234567890><😊😂😍👍🔥💯🎉❤️😎🙌👏✨🚀🌟💥🎊💪")
        for message in messages:
            words_dict = {word: 1 if word in message else 0 for word in words}
            words_dict["words_count"] = len(message)
            words_dict["big_letter_count"] = count_uppercase(message)
            for word in message:
                for letter in word:
                    if letter in symbols_to_check:
                        words_dict[letter] = 1
                new_word = ''.join(char for char in word if char not in symbols_to_check)
                if new_word in words:
                    words_dict[new_word] = 1
            result.append(words_dict)
        return result

    if isinstance(message, list):
        messages_as_words = [message_to_words(msg) for msg in message]
    elif isinstance(message, str):
        if not message:
            raise ValueError("Input message cannot be empty.")
        messages_as_words = [message_to_words(message)]
    else:
        raise TypeError("Invalid input format. Please provide either a string or a list of strings.")

    rows = make_rows(messages_as_words)
    df_test = pd.DataFrame(rows, columns=words)
    df_test = df_test.dropna()
    if df_test.empty:
        raise ValueError("Input data is empty after processing.")

    pred = model.predict(df_test)
    return pred.astype(int)
