import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class DeterministicRuleEngine:
    """
    Acts as the first line of defense before hitting the expensive LLM.
    Uses O(1) hash map lookups to flag known toxic ingredients and hidden sugars.
    """
    def __init__(self):
        # Master dictionaries for deterministic mapping
        self.hidden_sugars = {"maltodextrin", "dextrose", "corn syrup", "high fructose corn syrup", "sucralose"}
        self.banned_or_restricted = {"e319", "tbhq", "titanium dioxide", "e171", "brominated vegetable oil", "bvo"}
        self.healthy_indicators = {"whole wheat", "oat", "millet", "ragi", "almond"}

    def evaluate_baseline_risk(self, normalized_ingredients: List[str]) -> Dict[str, List[str]]:
        """
        Scans the ingredient list against hardcoded regulatory red flags.
        """
        logger.info("Running deterministic baseline evaluation...")
        
        evaluation = {
            "critical_flags": [],
            "hidden_sugars": [],
            "safe_flags": []
        }

        # Convert everything to lowercase for case-insensitive matching
        ing_lower = [ing.lower().strip() for ing in normalized_ingredients]

        for ing in ing_lower:
            if any(sugar in ing for sugar in self.hidden_sugars):
                evaluation["hidden_sugars"].append(ing)
            
            if any(toxic in ing for toxic in self.banned_or_restricted):
                evaluation["critical_flags"].append(ing)

            if any(healthy in ing for healthy in self.healthy_indicators):
                evaluation["safe_flags"].append(ing)

        return evaluation

# Singleton instance
baseline_rules = DeterministicRuleEngine()
