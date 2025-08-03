// Download functionality for Strong No Recoil
const GITHUB_REPO = 'YOUR_USERNAME/strong-no-recoil'; // Replace with your username

function downloadFromGitHub(releaseType = 'latest') {
    const baseUrl = `https://github.com/${GITHUB_REPO}/releases/${releaseType}`;
    
    // Create download links based on release type
    const downloads = {
        'full': `${baseUrl}/download/strong-no-recoil-full.zip`,
        'basic': `${baseUrl}/download/strong-no-recoil-basic.zip`,
        'advanced': `${baseUrl}/download/strong-no-recoil-advanced.zip`
    };
    
    return downloads;
}

// Direct download functions that work immediately
function downloadPackage() {
    // For now, redirect to GitHub repository
    window.open('https://github.com/YOUR_USERNAME/strong-no-recoil', '_blank');
}

function downloadBasic() {
    // Direct download of basic version
    window.open('https://raw.githubusercontent.com/YOUR_USERNAME/strong-no-recoil/main/no_recoil_app.py', '_blank');
}

function downloadAdvanced() {
    // Direct download of advanced version
    window.open('https://raw.githubusercontent.com/YOUR_USERNAME/strong-no-recoil/main/advanced_no_recoil.py', '_blank');
}

function downloadPackage() {
    const downloads = downloadFromGitHub();
    window.open(downloads.full, '_blank');
}

function downloadBasic() {
    const downloads = downloadFromGitHub();
    window.open(downloads.basic, '_blank');
}

function downloadAdvanced() {
    const downloads = downloadFromGitHub();
    window.open(downloads.advanced, '_blank');
}

// Alternative: Direct file download from repository
function downloadDirectFile(filename) {
    const fileUrl = `https://raw.githubusercontent.com/${GITHUB_REPO}/main/${filename}`;
    window.open(fileUrl, '_blank');
}

// Show download options
function showDownloadOptions() {
    const options = `
        <div style="background: rgba(0,0,0,0.8); padding: 20px; border-radius: 10px; margin: 10px 0;">
            <h3>Download Options:</h3>
            <p><strong>Option 1:</strong> Download from GitHub Releases (recommended)</p>
            <p><strong>Option 2:</strong> Clone the repository</p>
            <p><strong>Option 3:</strong> Download individual files</p>
            <br>
            <p><small>Note: Replace 'YOUR_USERNAME' in the code with your actual GitHub username</small></p>
        </div>
    `;
    
    // You can inject this into the page or show as alert
    console.log(options);
} 