class CombinationIterator:

    def __init__(self, sequence, length):
        self.sequence = sequence
        self.length = length
        self.answer = self.combination_generator([], self.sequence, 0, [])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.answer):
            answer = self.answer[self.index]
            self.index += 1
            return answer
        else:
            raise StopIteration

    def combination_generator(self, processed, unprocessed, index, answer):
        # base condition
        if (len(processed) == self.length) or (index >= len(unprocessed)):
            answer.append(processed)
            print("answer list", answer)
            return answer

        # accept the unprocessed
        self.combination_generator(processed + [unprocessed[index]], unprocessed, index + 1, answer)

        # reject the unprocessed
        return self.combination_generator(processed, unprocessed, index + 1, answer)
