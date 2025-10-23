from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LocalLLM:
    def __init__(self, model_name="microsoft/phi-2", device=None):
        print(f"Loading model: {model_name} (this may take a while on first run)...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate_review(self, code_text: str) -> str:
        """Generate a basic code review suggestion using local model"""
        prompt = f"Review this code for readability, modularity, and potential bugs:\n\n{code_text}\n\nSuggestions:"
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True,
            top_p=0.9
        )
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Trim output after 'Suggestions:' to avoid echo
        return result.split("Suggestions:")[-1].strip()
