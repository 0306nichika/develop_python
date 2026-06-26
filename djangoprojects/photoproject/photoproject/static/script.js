
function likePost(postId) {
  const userId = USER_ID;

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

  // ★ここを追加した
  if (data.status === "fail") {
    return;
  }

  //  成功のときだけ更新
  document.getElementById("like-count-" + postId).innerText = data.likeCount;
});

}

