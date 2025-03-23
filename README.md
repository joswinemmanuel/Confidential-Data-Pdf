# Fake Confidential Data PDF Generator

This Python script generates a PDF file containing fake confidential data, such as website URLs, usernames, and passwords. It uses the `reportlab` library to create the PDF.

## Prerequisites

* Python 3.x
* `reportlab` library (install with `pip install reportlab`)

## How to Use

1.  **Save the script:** Save the Python code as a `.py` file (e.g., `pdf_generator.py`).
2.  **Install dependencies:** If you don't have `reportlab` installed, run:

    ```bash
    pip install reportlab
    ```

3.  **Run the script:** Execute the Python script from your terminal:

    ```bash
    python pdf_generator.py
    ```

4.  **Output:** A PDF file named `confidential_data.pdf` will be created in the same directory as the script.

## Functionality

* The script generates a PDF with fake website, username, and password data.
* The PDF's file size is checked to ensure it remains under 500 KB.
* The script handles page breaks to accommodate varying amounts of generated data.
* The output is formatted to be readable.

## Code Explanation

* **`generate_fake_data()`:** Generates a list of tuples, each containing a fake website, username, and password.
* **`create_pdf()`:** Creates the PDF file using `reportlab`. It iterates through the generated data and adds it to the PDF. It also handles page breaks to ensure the content fits.
* **`check_pdf_size()`:** Checks the size of the generated PDF and prints the size in bytes to the console, and then confirms if it is under the 500kb limit.

## Example Output

The generated PDF will contain data similar to this:

```
Confidential Data

Website: abcdefg.com
Username: aB1cDe2fG3
Password: aB1c!@#$dE2fG3hI4jK

Website: hijklmno.com
Username: pQ5rSt6uV7
Password: lM8n%^&*oP9qRs0tU

... and so on ...
```

## Notes

* This script is intended for generating *fake* data for testing or demonstration purposes.
* Do not use the generated data for any real-world confidential information.
* The number of generated entries can be easily modified by changing the `num_entries` variable within the `generate_fake_data` function.
