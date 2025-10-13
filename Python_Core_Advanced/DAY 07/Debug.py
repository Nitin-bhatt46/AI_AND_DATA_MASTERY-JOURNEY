shift_amount = shift_amount % 26
if encode_or_decode == "decode":
    shift_amount = -shift_amount

output_text = ""
for letter in original_text:
    # leave non-letters unchanged
    if not letter.isalpha():
        output_text += letter
        continue
