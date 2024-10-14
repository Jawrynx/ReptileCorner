document.addEventListener('DOMContentLoaded', () => {
    const postsList = document.querySelector('.posts-list');
    const posts = postsList.querySelectorAll('.post');
    /**Desktop Screensizes. Will adjust and centre posts if there are 4 or less posts avaialable */
    function centerPosts() {
      if (posts.length <= 4 && window.innerWidth >= 1280) {
        postsList.style.setProperty('display', 'flex', 'important');
        postsList.style.justifyContent = 'center';
        console.log("Display style:", postsList.style.display);
      } else {
        // Reset the styles for smaller screens
        postsList.style.display = '';
        postsList.style.justifyContent = '';
      }
    }

    centerPosts(); 
    window.addEventListener('resize', centerPosts); 
});