let urls = [];
let currentIndex = 0; // Current index of the loaded URL

async function loadUrlsFromFile(urlFile) {
  try {
    const response = await fetch(urlFile);
    const data = await response.text();
    urls = data
    .split("\n")
    .filter(url => url.trim() !== "")
    .sort(); // Split URLs by new line, remove empty lines, and sort alphabetically
  

    // Check if URL parameter exists for current index
    const urlParams = new URLSearchParams(window.location.search);
    const indexFromURL = urlParams.get("index");
    if (indexFromURL !== null) {
      currentIndex = parseInt(indexFromURL);
    }
    
    updateIframeSrc();
    updateUrlParam();
  } catch (error) {
    console.error("Failed to load URLs from file:", error);
  }
}

// Function to handle swipe left event
const swipeLeft = () => {
  if (currentIndex > 0) {
    currentIndex--;

    updateIframeSrc();
    updateUrlParam();
  }
};

// Function to handle swipe right event
const swipeRight = () => {
  if (currentIndex < urls.length - 1) {
    currentIndex++;

    updateIframeSrc();
    updateUrlParam();
  }
};

function updateIframeSrc() {
  var url = urls[currentIndex];
  var iframe = document.getElementById("iframe");
  if (!iframe) {
    iframe = document.createElement('iframe');
    iframe.id = 'iframe';
    iframe.src = url;
    iframe.className = 'swipeable-item';
    const swipeableContainer = document.getElementById('swipeableContainer');
    swipeableContainer.appendChild(iframe);
  }

  iframe.src = url; 
}

function updateUrlParam() {
  window.history.replaceState({}, document.title, `?index=${currentIndex}`);
  document.getElementById("footer").focus();
}  
  
// Load the first URL on page load
window.addEventListener("load", () => {
  loadUrlsFromFile("sitemap.txt");
});

document.getElementById("prevBtn").addEventListener("click", swipeLeft);
document.getElementById("nextBtn").addEventListener("click", swipeRight);

// Add event listeners for swipe gestures
document.getElementById("footer").addEventListener('keydown', (event) => {
  if (event.keyCode === 37) { // Left arrow key
    swipeLeft();
  } else if (event.keyCode === 39) { // Right arrow key
    swipeRight();
  }
});
