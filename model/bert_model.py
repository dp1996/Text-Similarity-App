import torch
from transformers import BertModel, BertTokenizer
class BertSimilarity:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def encode(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', max_length=512, truncation=True, padding='max_length')
        outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1)

    def compute_similarity(self, text1, text2):
        embedding1 = self.encode(text1)
        embedding2 = self.encode(text2)
        cosine_sim = torch.nn.functional.cosine_similarity(embedding1, embedding2)
        return cosine_sim.item()
