document.addEventListener('DOMContentLoaded', () => {

    const csrfToken = document.querySelector("meta[name=csrf-token]").content;
    const headers = {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
    };

    // 2. 'like-btn' 클래스를 버튼들 이벤트 리스너 
    const addLikeButtonListeners = () => {
        const likeButtons = document.querySelectorAll('.like-btn');
        
        likeButtons.forEach(button => {
            button.addEventListener('click', event => {
                const clickedButton = event.currentTarget;
                
                const postId = clickedButton.dataset.postId;
                const url = `/posts/${postId}/like/`; 

                // 3. fetch API를 사용해 서버에 비동기 POST 요청 보내기
                fetch(url, {
                    method: 'POST',
                    headers: headers, 
                })
                .then(response => {
                    // 에러 처리
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json(); 
                })
                .then(data => {
                    // 4. 서버로부터 화면 업데이트
                    
                    const likeCountElement = document.getElementById(`like-count-${postId}`);
                    likeCountElement.textContent = data.like_count;

                    clickedButton.classList.toggle('liked', data.liked);
                })
                .catch(error => {
                    console.error('There has been a problem with your fetch operation:', error);
                    alert('좋아요 기능에 문제가 발생했습니다.');
                });
            });

        });

    };

    addLikeButtonListeners();
    document.querySelectorAll('.comment-form').forEach(form => {
        form.addEventListener('submit', event => {
            event.preventDefault();

            const postId = event.currentTarget.dataset.postId;
            const input = event.currentTarget.querySelector('input[name="content"]');
            const content = input.value;

            if (!content.trim()) {
                alert('댓글 내용을 입력하세요.');
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
                    newComment.innerHTML = `<strong>${data.comment.author}</strong>: ${data.comment.content}`;
                    commentList.appendChild(newComment);
                    input.value = '';
                } else {
                    alert(data.message || '댓글 작성에 실패했습니다.');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });

});