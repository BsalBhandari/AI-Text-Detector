class DataHandler:
    def calculate_avg_perplexity(self, data):
        total_perplexity = 0
        total_sentences = 0
        for document in data:
            sentences = document['sentences']
            for sentence in sentences:
                perplexity = sentence['perplexity']
                total_perplexity += perplexity
                total_sentences += 1
        if total_sentences > 0:
            return total_perplexity / total_sentences
        else:
            return 0

    def get_highest_perplexity(self, data):
        perplexities = [sentence['perplexity']
                        for sentence in data[0]['sentences']]
        return max(perplexities)

    def extract_scores(self, data):
        avg_perplexity_score = self.calculate_avg_perplexity(data)
        perplexity_score = self.get_highest_perplexity(data)
        burstiness_score = data[0]['overall_burstiness']
        return avg_perplexity_score, perplexity_score, burstiness_score
