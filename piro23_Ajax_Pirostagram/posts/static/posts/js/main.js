document.addEventListener('DOMContentLoaded', () => {
    const csrfToken = document.querySelector("meta[name=csrf-token]").content;
    const headers = {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
    };

    document.querySelectorAll('.like-btn').forEach(button => {
        button.addEventListener('click', event => {
            const postId = event.currentTarget.dataset.postId;
            const url = `/posts/${postId}/like/`;

            fetch(url, {
                method: 'POST',
                headers: headers,
            })
            .then(response => response.json())
            .then(data => {
                const likeCountElement = document.getElementById(`like-count-${postId}`);
                likeCountElement.textContent = data.like_count;
                event.currentTarget.classList.toggle('liked', data.liked);
            })
            .catch(error => console.error('Error:', error));
        });
    });

    document.querySelectorAll('.comment-form').forEach(form => {
        form.addEventListener('submit', event => {
            event.preventDefault();

            const postId = event.currentTarget.dataset.postId;
            const input = event.currentTarget.querySelector('input[name="content"]');
            const content = input.value;

            if (!content.trim()) {
                return;
            }

            const url = `/posts/${postId}/comment/`;

            fetch(url, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify({ content: content }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'ok') {
                    const commentList = document.getElementById(`comment-list-${postId}`);
                    const newComment = document.createElement('li');
                    newComment.id = `comment-${data.comment.id}`;
                    newComment.innerHTML = `
                        <strong>${data.comment.author}</strong>: ${data.comment.content}
                        <button class="delete-comment-btn" data-comment-id="${data.comment.id}">삭제</button>
                    `;
                    commentList.appendChild(newComment);
                    input.value = '';
                } else {
                    alert(data.message || '댓글 작성에 실패했습니다.');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });

    document.querySelectorAll('.comment-list').forEach(commentList => {
        commentList.addEventListener('click', event => {
            if (event.target.matches('.delete-comment-btn')) {
                if (!confirm('정말로 삭제하시겠습니까?')) {
                    return;
                }

                const commentId = event.target.dataset.commentId;
                const url = `/posts/comment/${commentId}/delete/`;

                fetch(url, {
                    method: 'POST',
                    headers: headers,
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'ok') {
                        document.getElementById(`comment-${commentId}`).remove();
                    } else {
                        alert(data.message || '댓글 삭제에 실패했습니다.');
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        });
    });
});