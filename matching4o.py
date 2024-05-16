import difflib

def find_best_match(reference, candidates):
    for candidate in candidates:
        s = difflib.SequenceMatcher(None, reference, candidate)
        matching_blocks = s.get_matching_blocks()
        match_info = []
        for block in matching_blocks:
            if block.size > 0:
                match_info.append(f"{reference[block.a:block.a+block.size]} (at index {block.a} in reference and {block.b} in candidate)")
        print(f"Comparing '{reference}' with '{candidate}':")
        print(f"Matching blocks: {match_info}")
        print(f"Similarity ratio: {s.ratio():.2f}\n")

reference_string = "tsudanuma"
candidates = ["tsdanuma", "tsudaenuma", "tsdanema"]

find_best_match(reference_string, candidates)
