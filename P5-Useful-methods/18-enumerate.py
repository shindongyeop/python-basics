def solution(s):
    answer = []
    words = s.split(" ") # Split the string into words (preserving spaces)
    for word in words:
        formatted_word = []
        for idx, char in enumerate(word):
            if idx % 2 == 0:
                formatted_word.append(char.upper())
            else:
                formatted_word.append(char.lower())
        answer.append("".join(formatted_word))
        # Join the formatted word and add to answer
        
    return " ".join(answer)  # Rejoin words with spaces

# Test case
print(solution("try hello world"))