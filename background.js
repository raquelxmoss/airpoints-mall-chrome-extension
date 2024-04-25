chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    if (changeInfo.url) {
        checkAirpointsMall(changeInfo.url);
    }
});

function checkAirpointsMall(url) {
    const knownDomains = ['chemistwarehouse.co.nz', 'example2.com'];  // Add more domains as needed
    const urlObj = new URL(url);
    if (knownDomains.includes(urlObj.hostname)) {
        chrome.notifications.create({
            type: 'basic',
            iconUrl: 'images/icon128.png',
            title: 'Airpoints Mall Site!',
            message: 'You are visiting a site that is part of the Air NZ Airpoints Mall.',
            priority: 2
        });
    }
}
