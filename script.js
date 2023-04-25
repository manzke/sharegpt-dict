  let urls = [];
  let currentIndex = 0; // Current index of the loaded URL
  
  // Function to fetch and render the URL content
  const fetchAndRenderURL = async (url) => {
    try {
      const iframe = document.createElement('iframe');
      iframe.id = 'iframe';
      iframe.src = url;
      iframe.className = 'swipeable-item';
      const swipeableContainer = document.getElementById('swipeableContainer');
      swipeableContainer.appendChild(iframe);
    } catch (error) {
      console.error(`Failed to fetch URL: ${url}`, error);
    }
  };

  async function loadUrlsFromFile(urlFile) {
    try {
      const response = await fetch(urlFile);
      const data = await response.text();
      urls = data.split("\n").filter(url => url.trim() !== ""); // Split URLs by new line and remove empty lines
      //totalUrls = urls.length;
      //totalUrlsElement.textContent = totalUrls;
      updateURLCounter();
      updateIframeSrc();
      updateUrlParam();
    } catch (error) {
      console.error("Failed to load URLs from file:", error);
    }
  }
  
  // Function to update the URL counter
  const updateURLCounter = () => {
    //const urlCounter = document.getElementById('urlCounter');
    //urlCounter.textContent = `URLs loaded: ${currentIndex + 1}/${urls.length} (${urls[currentIndex]})`;
  };
  
  // Function to handle swipe left event
  const swipeLeft = () => {
    if (currentIndex > 0) {
      currentIndex--;
      //const swipeableContainer = document.getElementById('swipeableContainer');
      //swipeableContainer.style.transform = `translateX(${-currentIndex * 100}vw)`;
      updateURLCounter();
      updateIframeSrc();
      updateUrlParam();
    }
  };
  
  // Function to handle swipe right event
  const swipeRight = () => {
    if (currentIndex < urls.length - 1) {
      currentIndex++;
      //const swipeableContainer = document.getElementById('swipeableContainer');
      //swipeableContainer.style.transform = `translateX(${-currentIndex * 100}vw)`;
      updateURLCounter();
      updateIframeSrc();
      updateUrlParam();
    }
  };

  function updateIframeSrc() {
    var iframe = document.getElementById("iframe");
    var currentUrl = urls[currentIndex]; // Subtract 1 from currentIndex to get the correct array index
    iframe.src = currentUrl; 
  }
  
  // Fetch and render the first URL
  fetchAndRenderURL(urls[currentIndex]);
  updateURLCounter();
  
  // Add event listeners for swipe gestures
  document.addEventListener('keydown', (event) => {
    if (event.keyCode === 37) { // Left arrow key
      swipeLeft();
    } else if (event.keyCode === 39) { // Right arrow key
      swipeRight();
    }
  });

  function updateUrlParam() {
    window.history.replaceState({}, document.title, `?index=${currentIndex}`);
  }  
  
document.getElementById("prevBtn").addEventListener("click", swipeLeft);
document.getElementById("nextBtn").addEventListener("click", swipeRight);

// Load the first URL on page load
window.addEventListener("load", () => {
  loadUrlsFromFile("sitemap.txt");

  // Check if URL parameter exists for current index
  const urlParams = new URLSearchParams(window.location.search);
  const indexFromURL = urlParams.get("index");
  if (indexFromURL !== null) {
    currentIndex = parseInt(indexFromURL);
  }

  updateURLCounter();
  updateIframeSrc();
});
