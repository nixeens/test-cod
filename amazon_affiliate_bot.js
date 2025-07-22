const puppeteer = require('puppeteer');
require('dotenv').config();

async function fetchProductInfo(query) {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.goto('https://www.amazon.com');

  await page.type('#twotabsearchtextbox', query);
  await Promise.all([
    page.waitForNavigation({ waitUntil: 'networkidle2' }),
    page.keyboard.press('Enter')
  ]);

  await page.waitForSelector('div[data-component-type="s-search-result"] h2 a');
  const firstLink = await page.$('div[data-component-type="s-search-result"] h2 a');
  const source = await page.evaluate(el => el.href, firstLink);

  await Promise.all([
    page.waitForNavigation({ waitUntil: 'networkidle2' }),
    firstLink.click()
  ]);

  await page.waitForSelector('#productTitle');
  const title = await page.$eval('#productTitle', el => el.textContent.trim());

  let price = null;
  if (await page.$('#priceblock_ourprice')) {
    price = await page.$eval('#priceblock_ourprice', el => el.textContent.trim());
  } else if (await page.$('#priceblock_dealprice')) {
    price = await page.$eval('#priceblock_dealprice', el => el.textContent.trim());
  } else if (await page.$('span.a-price.a-text-price')) {
    price = await page.$eval('span.a-price.a-text-price', el => el.textContent.trim());
  }

  let affiliateLink = null;
  try {
    affiliateLink = await page.$eval('#amzn-ss-text-shortlink-text', el => el.value || el.textContent.trim());
  } catch (e) {
    affiliateLink = page.url();
  }

  await browser.close();
  return { title, price, affiliate_link: affiliateLink, source };
}

async function main() {
  const query = process.argv.slice(2).join(' ');
  if (!query) {
    console.error('Usage: node amazon_affiliate_bot.js <product description>');
    process.exit(1);
  }

  try {
    const data = await fetchProductInfo(query);
    console.log(JSON.stringify(data, null, 2));
  } catch (err) {
    console.error('Error:', err);
    process.exit(1);
  }
}

main();
