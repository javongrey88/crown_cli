"""
Hair Routines Matrix for Crown AI CLI App
Each key is a tuple: (Hair Type, Goal)
Each value is a dictionary representing the care routine.
"""

# Continuing with routines for 4B, 4A, 3C, and Locs

hair_routines = ({
    # --- 4B ---
    ("4B", "Growth"): {
        "Cleanse": "Co-wash weekly, clarify monthly to prevent buildup.",
        "Condition": "Deep condition weekly with protein and moisture balance.",
        "Moisturize": "Use creamy leave-ins 2–3x/week to maintain softness.",
        "Seal": "Use LOC method with olive or castor oil.",
        "Scalp Care": "Scalp massage 3x/week with rosemary oil.",
        "Style": "Loose twists or mini-braids to protect ends."
    },
    ("4B", "Moisture"): {
        "Cleanse": "Hydrating co-wash weekly, avoid harsh shampoos.",
        "Condition": "Use humectant-based masks (glycerin, aloe) weekly.",
        "Moisturize": "Spritz daily with rose water + leave-in.",
        "Seal": "LCO method with creamy butter and oil.",
        "Scalp Care": "Use jojoba oil to soothe dryness once a week.",
        "Style": "Moisture-retentive styles like bantu knots or updos."
    },
    ("4B", "Strength"): {
        "Cleanse": "Clarify every 2–3 weeks, use strengthening shampoo.",
        "Condition": "Protein treatment bi-weekly (egg, hydrolyzed protein).",
        "Moisturize": "Alternate moisture/protein leave-ins weekly.",
        "Seal": "Use whipped shea butter and protein-rich oil blend.",
        "Scalp Care": "Avoid buildup; exfoliate monthly with clay.",
        "Style": "Braids or cornrows (not too tight)."
    },
    ("4B", "Scalp Health"): {
        "Cleanse": "Tea tree or charcoal shampoo every week.",
        "Condition": "Cooling scalp conditioner with mint or menthol.",
        "Moisturize": "Aloe vera mist to soothe scalp.",
        "Seal": "Massage in oil blend (peppermint, jojoba, tea tree).",
        "Scalp Care": "Scalp detox mask monthly, massage weekly.",
        "Style": "Flat twists or braided crown to leave scalp accessible."
    },
    ("4B", "Damage Repair"): {
        "Cleanse": "Use mild shampoo with bond-repair ingredients.",
        "Condition": "Alternate protein/moisture treatments weekly.",
        "Moisturize": "Daily spritz with strengthening leave-in.",
        "Seal": "Use mango butter and argan oil mix.",
        "Scalp Care": "Avoid scratching/flaking, massage gently weekly.",
        "Style": "Low-stress styles like twist-outs or silk scarves."
    },

    # --- 4A ---
    ("4A", "Growth"): {
        "Cleanse": "Sulfate-free shampoo bi-weekly.",
        "Condition": "Deep condition weekly with heat cap.",
        "Moisturize": "2x/week moisture with aloe-based leave-in.",
        "Seal": "Use LCO method with coconut oil and butter.",
        "Scalp Care": "Light oil massage twice weekly.",
        "Style": "Tension-free braids or updos."
    },
    ("4A", "Moisture"): {
        "Cleanse": "Co-wash weekly, shampoo every 2 weeks.",
        "Condition": "Hydrating deep conditioner weekly.",
        "Moisturize": "Daily spritz with rose water and glycerin.",
        "Seal": "Cream sealant and olive oil.",
        "Scalp Care": "Use jojoba oil to hydrate and soothe.",
        "Style": "Pineapple or twist-out styles."
    },
    ("4A", "Strength"): {
        "Cleanse": "Strengthening shampoo every 2 weeks.",
        "Condition": "Protein mask bi-weekly with moisture follow-up.",
        "Moisturize": "Moisturize 2–3x/week with protein leave-in.",
        "Seal": "Butter + avocado oil combo.",
        "Scalp Care": "Monthly clay rinse for buildup.",
        "Style": "Braided updos or satin wraps."
    },
    ("4A", "Scalp Health"): {
        "Cleanse": "Mint or tea tree shampoo weekly.",
        "Condition": "Scalp-soothing conditioner with neem or eucalyptus.",
        "Moisturize": "Aloe vera gel on scalp and edges.",
        "Seal": "Massage tea tree + jojoba oil mix weekly.",
        "Scalp Care": "Weekly massage, monthly scalp detox.",
        "Style": "Flat twists or mini puffs."
    },
    ("4A", "Damage Repair"): {
        "Cleanse": "Gentle cleansing shampoo weekly.",
        "Condition": "Alternate protein and deep moisture masks.",
        "Moisturize": "Hydrating leave-in every other day.",
        "Seal": "Butter + grapeseed oil for ends.",
        "Scalp Care": "Massage with castor oil for regrowth.",
        "Style": "Wigs or low-tension buns."
    },

    # --- 3C ---
    ("3C", "Growth"): {
        "Cleanse": "Shampoo every 1–2 weeks to remove buildup.",
        "Condition": "Deep condition weekly, rinse with cool water.",
        "Moisturize": "2x/week with curl cream or leave-in.",
        "Seal": "Use jojoba or almond oil lightly.",
        "Scalp Care": "Massage with growth oil 2x/week.",
        "Style": "Defined curls or pinned twists."
    },
    ("3C", "Moisture"): {
        "Cleanse": "Use co-wash midweek, shampoo on weekends.",
        "Condition": "Moisture mask weekly (honey, glycerin).",
        "Moisturize": "Daily curl refresh spray.",
        "Seal": "Light cream sealant.",
        "Scalp Care": "Use aloe mist or light oil.",
        "Style": "Wash n' go or curl set."
    },
    ("3C", "Strength"): {
        "Cleanse": "Clarify every 2 weeks with protein shampoo.",
        "Condition": "Protein-rich conditioner every other week.",
        "Moisturize": "Alternate leave-ins with strengthening properties.",
        "Seal": "Coconut or rice bran oil.",
        "Scalp Care": "Keep scalp clean and massaged weekly.",
        "Style": "Protective curl buns or braids."
    },
    ("3C", "Scalp Health"): {
        "Cleanse": "Anti-dandruff shampoo weekly.",
        "Condition": "Conditioner with peppermint or eucalyptus oils.",
        "Moisturize": "Hydrating aloe-based spritz.",
        "Seal": "Massage tea tree/jojoba oil mix on scalp.",
        "Scalp Care": "Weekly scalp massage, monthly detox.",
        "Style": "Curls or space buns for airflow."
    },
    ("3C", "Damage Repair"): {
        "Cleanse": "Gentle shampoo 1–2x/week.",
        "Condition": "Alternate protein and hydration masks weekly.",
        "Moisturize": "Use leave-in daily with strengthening ingredients.",
        "Seal": "Butter + vitamin E oil.",
        "Scalp Care": "Scalp repair serum or oil mix.",
        "Style": "Loose curls or silk wraps."
    },

    # --- Locs ---
    ("Locs", "Growth"): {
        "Cleanse": "Clarify monthly, shampoo every 2 weeks.",
        "Condition": "Use light conditioner sparingly to prevent buildup.",
        "Moisturize": "Daily spritz with water + aloe vera juice.",
        "Seal": "Light oil mist with rosehip or jojoba.",
        "Scalp Care": "Massage 3x/week with castor oil blend.",
        "Style": "Retwist monthly or palm-roll as needed."
    },
    ("Locs", "Moisture"): {
        "Cleanse": "Shampoo with moisture-focused formula bi-weekly.",
        "Condition": "Use light leave-ins or sprays (avoid buildup).",
        "Moisturize": "Daily mist with water + glycerin mix.",
        "Seal": "Rosewater + jojoba oil spritz.",
        "Scalp Care": "Oil scalp with lightweight oil 2–3x/week.",
        "Style": "Low-maintenance updos or wraps."
    },
    ("Locs", "Strength"): {
        "Cleanse": "Cleanse weekly with strengthening shampoo.",
        "Condition": "Avoid deep conditioners; use protein-infused sprays.",
        "Moisturize": "Light mist every 2 days.",
        "Seal": "Seal with grapeseed or sweet almond oil.",
        "Scalp Care": "Massage bi-weekly to support strong roots.",
        "Style": "Wrap styles that protect from breakage."
    },
    ("Locs", "Scalp Health"): {
        "Cleanse": "Tea tree or charcoal shampoo weekly.",
        "Condition": "Avoid conditioner; focus on scalp treatments.",
        "Moisturize": "Hydrating aloe mist for scalp and roots.",
        "Seal": "Tea tree + jojoba oil blend massage.",
        "Scalp Care": "Exfoliate monthly with clay or brush.",
        "Style": "Loose or semi-freeform to allow air circulation."
    },
    ("Locs", "Damage Repair"): {
        "Cleanse": "Use gentle shampoo weekly to remove buildup.",
        "Condition": "Avoid conditioners; focus on loc-safe treatments.",
        "Moisturize": "Daily mist with strengthening tonic.",
        "Seal": "Light oil blends (avoid heavy waxes).",
        "Scalp Care": "Nourishing oil blend 2x/week to aid regrowth.",
        "Style": "Protective wraps and minimal tension styles."
    },
})
