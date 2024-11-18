document.addEventListener('DOMContentLoaded', () => {
    const postsList = document.querySelector('.posts-list');
    const posts = postsList.querySelectorAll('.post');
  
    function adjustPostLayout() {
      if (posts.length <= 4 && window.innerWidth >= 1280) {
        posts.forEach(post => {
          post.classList.remove('col-xl-3');
          post.classList.add('col-xl-4');
        });
      } else {
        posts.forEach(post => {
          post.classList.remove('col-xl-4');
          post.classList.add('col-xl-3');
        });
      }
    }
  
    adjustPostLayout();
    window.addEventListener('resize', adjustPostLayout);
});