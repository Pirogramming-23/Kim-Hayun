
function loadItems() {
  return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

// given items로 리스트 업데이트 
function displayItems(items) {
  const container = document.querySelector('.items');
  const html = items.map(item => createHTMLString(item));
  container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

//given data item으로 html list item 만들기
 function createHTMLString(item) {
  return `
    <li class="item">
      <img src="${item.image}" alt="${item.type}" class="item_thumbnail" />
      <span class="item_description">${item.gender}, ${item.size}</span>
    </li>
  `;
}

function setEventListeners(items) {
  const logo = document.querySelector('.logo');
  const buttons = document.querySelector('.buttons');

  logo.addEventListener('click', () => displayItems(items));
  buttons.addEventListener('click', event => onButtonClick(event, items));
}

// Handle button 클릭
function onButtonClick(event, items) {
  const target = event.target;
  const key = target.dataset.key;
  const value = target.dataset.value;

  if (key == null || value == null) {
    return;
  }
  const filtered = items.filter(item => item[key] === value);
  displayItems(filtered);
}
loadItems()
    .then(items=>{
        displayItems(items);
        setEventListeners(items)
    })
    .catch(console.log);
