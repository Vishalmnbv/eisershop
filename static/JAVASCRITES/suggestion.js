const searchBox = document.getElementById("searchBox");
const suggestions = document.getElementById("searchSuggestions");

searchBox.addEventListener("keyup", function () {

    const query = this.value.trim();

    if (query.length < 2) {
        suggestions.innerHTML = "";
        suggestions.style.display = "none";
        return;
    }

    fetch(`/live-search/?q=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(data => {

            let html = "";

            data.products.forEach(product => {

                html += `
                    <a href="${product.url}" class="text-decoration-none text-dark">
                        <div class="d-flex align-items-center p-2 border-bottom">

                            <img src="${product.image}"
                                 width="55"
                                 height="60"
                                 class="me-2 rounded">

                            <span>${product.title}</span>

                        </div>
                    </a>
                `;

            });

            suggestions.innerHTML = html;
            suggestions.style.display = "block";

        });
});

document.addEventListener("click", function(e){

    if(!searchBox.contains(e.target) && !suggestions.contains(e.target)){
        suggestions.style.display="none";
    }

});