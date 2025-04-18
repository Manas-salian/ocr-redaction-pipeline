import test, model

filename = "Profile.pdf"

# Extract text from the PDF
test.print_contents(f"{filename}", "extracted.txt")

# Analyze the extracted text and get the list of PII terms
test.PII_TERMS = model.analyze_single_file()

# Perform redaction
test.legal_redact_pdf(f"{filename}", "legal_redacted.pdf", pii_terms=test.PII_TERMS, method="full_redact")

# 2. Obfuscation with black boxes
test.legal_redact_pdf(f"{filename}", "blackout.pdf", pii_terms=test.PII_TERMS, method="obfuscate")

# 3. Replacement with custom text
test.legal_redact_pdf(f"{filename}", "replaced.pdf", pii_terms=test.PII_TERMS, method="replace", replace_text="CONFIDENTIAL")
