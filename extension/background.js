chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    console.log("hello");
    if (changeInfo.url) {
        checkAirpointsMall(changeInfo.url, tabId);
    }
});

function checkAirpointsMall(url, tabId) {
    const knownDomains = ['www.chemistwarehouse.co.nz', 'example2.com'];  // Add more domains as needed
    const urlObj = new URL(url);
    let iconPath = 'images/icon128.png';  // Default icon
    console.log(urlObj.hostname);
    if (knownDomains.includes(urlObj.hostname)) {
        iconPath = 'images/icon_active.png';  // Icon indicating an Airpoints Mall site
        chrome.action.setIcon({
            path: iconPath,
            tabId: tabId
        });
    } else {
        // Reset to default icon if not a listed site
        chrome.action.setIcon({
            path: iconPath,
            tabId: tabId
        });
    }
}
