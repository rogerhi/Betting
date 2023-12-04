// screenshot.js

// puppeteer-extra is a drop-in replacement for puppeteer,
// it augments the installed puppeteer with plugin functionality
const puppeteer = require('puppeteer-extra')

// add stealth plugin and use defaults (all evasion techniques)
const StealthPlugin = require('puppeteer-extra-plugin-stealth')
puppeteer.use(StealthPlugin())

// puppeteer usage as normal




async function run() {
    const browser = await puppeteer.launch({
        headless: false
    });
  const page = await browser.newPage();

  await page.goto('https://www.ladbrokes.com.au/sports/australian-rules/afl')
  await page.screenshot({ path: 'screeenshot.png', fullPage: true });

  browser.close();
}

run();