
function likePost(postId) {
  const userId = localStorage.getItem("userId") || "user1";

  fetch("/like/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      postId: postId,
      userId: userId
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("like-count-" + postId).innerText = data.likeCount;
  });
}

