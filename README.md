# 🚀 QR Code Generator – Turn Your URLs Into Pixel Art!

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

1. Make sure Playwright is installed:
   ```bash
   pip install playwright
   playwright install
   ```
2. Start the app (`python main.py`) – it should run in the background.
3. Run the Playwright tests from the `tests` directory:
   ```bash
   pytest tests/
   ```

The tests check that:
- The application is reachable.
- A QR code can be generated from a URL.
- The results are correctly displayed in the UI.

> If you want to add your own tests, check out [`tests/test_app.py`](./tests/test_app.py) for inspiration.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details. Free to use, modify, and distribute as needed.



