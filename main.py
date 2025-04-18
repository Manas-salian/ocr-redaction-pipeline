import ocr_redaction, model

filename = "Profile.pdf"

# Extract text from the PDF
ocr_redaction.print_contents(f"{filename}", "extracted.txt")

# Analyze the extracted text and get the list of PII terms
ocr_redaction.PII_TERMS = model.analyze_single_file()

# Perform redaction
ocr_redaction.legal_redact_pdf(f"{filename}", "legal_redacted.pdf", pii_terms=ocr_redaction.PII_TERMS, method="full_redact")

# 2. Obfuscation with black boxes
ocr_redaction.legal_redact_pdf(f"{filename}", "blackout.pdf", pii_terms=ocr_redaction.PII_TERMS, method="obfuscate")

# 3. Replacement with custom text
ocr_redaction.legal_redact_pdf(f"{filename}", "replaced.pdf", pii_terms=ocr_redaction.PII_TERMS, method="replace", replace_text="CONFIDENTIAL")
