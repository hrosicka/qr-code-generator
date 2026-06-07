# 🚀 QR Code Generator – Turn Your URLs Into Pixel Art!


[![Python Version](https://img.shields.io/badge/Python-3.8_--_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Framework: Flask](https://img.shields.io/badge/Framework-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![E2E Tests: Playwright](https://img.shields.io/badge/E2E_Tests-Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev)
[![GitHub Stars](https://img.shields.io/github/stars/hrosicka/qr-code-generator?style=for-the-badge&logo=github&color=ffee55&logoColor=white)](https://github.com/hrosicka/qr-code-generator/stargazers)
[![Author: Hanka](https://img.shields.io/badge/Author-Hanka%20%F0%9F%91%A9%E2%80%8D%F0%9F%94%AC-deeppink?style=for-the-badge)](https://github.com/hrosicka)
[![GitHub License](https://img.shields.io/github/license/hrosicka/qr-code-generator?style=for-the-badge&color=yellow)](./LICENSE)


Welcome to the digital wizardry workshop, where boring URLs are transformed into mysterious QR glyphs.  
Just type in your link, press the button, and voilà – your very own QR code is born!  
This is QR Code Generator, powered by Python, Flask, and a pinch of magic. ✨

---

## How to Use?
1. Launch the app:  
   ```bash
   python main.py
   ```
2. Open your browser at [localhost:5000](http://localhost:5000).
3. Paste any URL into the form.  
4. Behold your QR code! Download it, share it, or show it off to your grandma. 🖼️

---

## Why Should You Use This?
- Because typing endless URLs is boring, but showing off a QR code is classy! 😎
- Works faster than your morning coffee. ☕
- Friendly UI – so simple, even your cat could use it. 🐾

---

## How Does It Work?
- Powered by Flask – no complicated stuff, just pure Python bliss.
- QR code magic by the `qrcode` library.
- Output is beamed directly to your browser as an image, ready to scan.

---

## Testing
Application quality is checked with automated tests.  
You’ll find test files in the [`tests/`](./tests) directory.

### End-to-End UI Tests with Playwright

To make sure the user interface works and QR codes are generated correctly, we use [Playwright](https://playwright.dev/) for end-to-end testing.

#### How to run Playwright tests

To run the test suite successfully, follow these exact steps:

##### Step 1: Install Dependencies
Make sure you have both `pytest` and `playwright` installed, along with the required browser binaries:
```bash
pip install playwright pytest
playwright install
```

##### Step 2: Start the Application
The web application must be running in the background for the UI tests to connect to it. Start the app in your terminal:
```bash
python main.py
```
*(Leave this terminal window open so the server keeps running!)*

##### Step 3: Run the Tests
Open a **new, separate terminal window/tab**, navigate back to your project root directory, and run the tests:
```bash
pytest tests/
```

The tests check that:
- The application is reachable.
- A QR code can be generated from a URL.
- The results are correctly displayed in the UI.

> If you want to add your own tests, check out [`tests/test_app.py`](./tests/test_app.py) for inspiration.

---

## Author

Lovingly crafted by [Hanka Robovska](https://github.com/hrosicka)

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details. Free to use, modify, and distribute as needed.