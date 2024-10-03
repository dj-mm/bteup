const crypto = require('crypto');
const fetch = require('node-fetch');
const { JSDOM } = require('jsdom');

async function getWebsiteHash(url) {
    try {
        const response = await fetch(url);
        const text = await response.text();
        const dom = new JSDOM(text);
        const bodyText = dom.window.document.body.textContent.trim();
        return crypto.createHash('sha256').update(bodyText, 'utf8').digest('hex');
    } catch (error) {
        console.error(`Error fetching ${url}: ${error}`);
        return null;
    }
}

const url = 'https://bteup.ac.in/webapp/home.aspx';
let previousHash = null;
const checkInterval = 30000; // 30 seconds

async function checkForUpdate() {
    const currentHash = await getWebsiteHash(url);
    if (currentHash && currentHash !== previousHash) {
        console.log(`Update on ${url} at ${new Date().toLocaleTimeString()}`);
        previousHash = currentHash;
    }
}

(async function() {
    previousHash = await getWebsiteHash(url); // Get initial hash
    setInterval(checkForUpdate, checkInterval);
})();
