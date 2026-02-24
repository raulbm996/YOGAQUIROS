const https = require('https');
const url = 'https://yogaquiros.com/';

function fetch(u) {
    https.get(u, (res) => {
        if ([301, 302, 307, 308].includes(res.statusCode)) {
            console.log('Redirecting to:', res.headers.location);
            fetch(res.headers.location);
            return;
        }
        let data = '';
        res.on('data', c => data += c);
        res.on('end', () => {
            const urls = data.match(/src="([^"]+?\.(jpg|jpeg|png|webp))"/gi) || [];
            const bgUrls = data.match(/url\(['"]?([^'"]+?\.(jpg|jpeg|png|webp))['"]?\)/gi) || [];
            console.log([...new Set(urls.concat(bgUrls))].join('\n'));
        });
    }).on('error', console.error);
}
fetch(url);
